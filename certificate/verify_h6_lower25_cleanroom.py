#!/usr/bin/env python3
"""Clean-room verifier for the internal claim h(6) >= 25.

This implementation does NOT use the unavailable original verifier or log.
It independently checks the supplied RM(3,6) witness table, derives the 46
algebraically possible dangerous 2D profiles, verifies exact-kernel extension,
checks exact rational Delsarte dual certificates (and matching primal LP points),
and exhausts MacWilliams-compatible [N,10] enumerators for the closure step.

The external large-sum-free theorem is NOT reproved here; it is an explicitly
external dependency audited in CLEANROOM_REPORT.md.
"""
from __future__ import annotations

import argparse
import hashlib
import math
import platform
import sys
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple

M = 6
DOMAIN_SIZE = 1 << M
D2 = 1 + M + math.comb(M, 2)  # 22 squarefree monomials of degree <=2
DANGEROUS = {8, 12, 14, 16, 18, 20, 22, 24}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def gf2_rank(rows: Iterable[int]) -> int:
    """Rank of binary row vectors encoded as Python integers."""
    pivots: Dict[int, int] = {}
    rank = 0
    for value in rows:
        x = int(value)
        while x:
            p = x.bit_length() - 1
            if p in pivots:
                x ^= pivots[p]
            else:
                pivots[p] = x
                rank += 1
                break
    return rank


def monomial_masks_deg_le_2() -> List[Tuple[int, ...]]:
    mons: List[Tuple[int, ...]] = [()]
    mons += [(i,) for i in range(M)]
    mons += [(i, j) for i in range(M) for j in range(i + 1, M)]
    assert len(mons) == D2
    return mons

MONOMIALS = monomial_masks_deg_le_2()


def eval_monomial(x: int, mon: Tuple[int, ...]) -> int:
    if not mon:
        return 1
    out = 1
    for bit in mon:
        out &= (x >> bit) & 1
    return out


def eval_rows(points: Sequence[int]) -> List[int]:
    """Rows of the RM(2,6) evaluation matrix on the given distinct points."""
    assert len(points) == len(set(points))
    rows: List[int] = []
    for mon in MONOMIALS:
        row = 0
        for col, x in enumerate(points):
            row |= eval_monomial(x, mon) << col
        rows.append(row)
    return rows


def eval_rank(points: Sequence[int]) -> int:
    return gf2_rank(eval_rows(points))


def truth_table_from_hex(h: str) -> List[int]:
    """64 truth values; bit x of the integer is the value at x in F_2^6."""
    if len(h) != 16:
        raise ValueError(f"expected 16 hex digits, got {len(h)}")
    v = int(h, 16)
    return [(v >> x) & 1 for x in range(DOMAIN_SIZE)]


def anf_degree(tt: Sequence[int]) -> int:
    """Algebraic degree from the Boolean Möbius transform."""
    if len(tt) != DOMAIN_SIZE:
        raise ValueError("truth table must have 64 entries")
    a = list(map(int, tt))
    for bit in range(M):
        for mask in range(DOMAIN_SIZE):
            if (mask >> bit) & 1:
                a[mask] ^= a[mask ^ (1 << bit)]
    deg = -1
    for mask, coeff in enumerate(a):
        if coeff:
            deg = max(deg, mask.bit_count())
    return deg


def dot_parity(tt: Sequence[int], mon: Tuple[int, ...]) -> int:
    return sum((tt[x] & eval_monomial(x, mon)) for x in range(DOMAIN_SIZE)) & 1


def rm2_orthogonal(tt: Sequence[int]) -> bool:
    return all(dot_parity(tt, mon) == 0 for mon in MONOMIALS)


def vector_on_points(tt: Sequence[int], points: Sequence[int]) -> int:
    out = 0
    for j, x in enumerate(points):
        out |= (tt[x] & 1) << j
    return out


def weight_int(v: int) -> int:
    return v.bit_count()


def profile_coordinate_counts(profile: Tuple[int, int, int]) -> Tuple[int, int, int, int]:
    """For nonzero codewords u,v,u+v with sorted weights a,b,c.

    Returns three nonzero coordinate-type counts (up to relabeling) and union size.
    Nonnegativity/integrality is exactly the algebraic feasibility test for a 2D code.
    """
    a, b, c = profile
    nums = (a + b - c, a + c - b, b + c - a)
    if any(x < 0 or x % 2 for x in nums):
        raise ValueError("infeasible profile")
    counts = tuple(x // 2 for x in nums)
    union = (a + b + c) // 2
    return counts[0], counts[1], counts[2], union


def enumerate_dangerous_profiles() -> List[Tuple[int, int, int]]:
    out: List[Tuple[int, int, int]] = []
    for a in sorted(DANGEROUS):
        for b in sorted(DANGEROUS):
            for c in sorted(DANGEROUS):
                if not (a <= b <= c):
                    continue
                if (a + b + c) % 2:
                    continue
                try:
                    *_, union = profile_coordinate_counts((a, b, c))
                except ValueError:
                    continue
                if union <= 24:
                    out.append((a, b, c))
    return out


def extend_to_24_with_rank22(active: Sequence[int]) -> List[int]:
    """Greedily extend active points until the RM(2,6) rank is 22.

    If rank(active)=|active|-2, exactly 24-|active| independent columns are needed.
    The full 64-point evaluation matrix has rank 22, so such an extension must exist.
    """
    selected = list(active)
    current_rank = eval_rank(selected)
    target_add = 24 - len(selected)
    added = 0
    for x in range(DOMAIN_SIZE):
        if x in selected:
            continue
        new_rank = eval_rank(selected + [x])
        if new_rank == current_rank + 1:
            selected.append(x)
            current_rank = new_rank
            added += 1
            if len(selected) == 24:
                break
    assert added == target_add, (len(active), added, target_add)
    assert len(selected) == 24 and len(set(selected)) == 24
    assert current_rank == D2
    return selected


@dataclass(frozen=True)
class WitnessResult:
    advertised: Tuple[int, int, int]
    actual: Tuple[int, int, int]
    degrees: Tuple[int, int, int]
    union_size: int
    rank_union: int
    rank_extended: int


def verify_witness_line(line: str) -> WitnessResult:
    parts = line.split()
    if len(parts) != 5:
        raise ValueError("witness line must have 5 fields")
    advertised = tuple(map(int, parts[:3]))
    h1, h2 = parts[3], parts[4]
    f = truth_table_from_hex(h1)
    g = truth_table_from_hex(h2)
    s = [a ^ b for a, b in zip(f, g)]
    actual = tuple(sorted((sum(f), sum(g), sum(s))))
    if actual != advertised:
        raise AssertionError(("profile mismatch", advertised, actual))
    degrees = (anf_degree(f), anf_degree(g), anf_degree(s))
    if max(degrees) > 3:
        raise AssertionError(("degree >3", advertised, degrees))
    # Do not trust RM duality as a black box: check orthogonality directly.
    if not (rm2_orthogonal(f) and rm2_orthogonal(g) and rm2_orthogonal(s)):
        raise AssertionError(("not orthogonal to RM(2,6)", advertised))

    active = [x for x, (a, b) in enumerate(zip(f, g)) if a or b]
    union_size = len(active)
    _, _, _, expected_union = profile_coordinate_counts(advertised)
    if union_size != expected_union or union_size > 24:
        raise AssertionError(("union mismatch", advertised, union_size, expected_union))

    rank_u = eval_rank(active)
    if rank_u != union_size - 2:
        raise AssertionError(("kernel not exactly 2D on union", advertised, union_size, rank_u))

    fv = vector_on_points(f, active)
    gv = vector_on_points(g, active)
    if fv == 0 or gv == 0 or fv == gv:
        raise AssertionError(("dependent witness generators", advertised))
    # Both supplied dependency vectors must lie in the kernel.
    for v in (fv, gv, fv ^ gv):
        for row in eval_rows(active):
            if (v & row).bit_count() & 1:
                raise AssertionError(("dependency not in kernel", advertised))

    extended = extend_to_24_with_rank22(active)
    rank_e = eval_rank(extended)
    if rank_e != 22 or 24 - rank_e != 2:
        raise AssertionError(("extension kernel dimension", advertised, rank_e))
    # f,g vanish outside active support, so their 24-coordinate extensions remain dependencies.
    fext = vector_on_points(f, extended)
    gext = vector_on_points(g, extended)
    for v in (fext, gext, fext ^ gext):
        for row in eval_rows(extended):
            if (v & row).bit_count() & 1:
                raise AssertionError(("extended dependency lost", advertised))
    if gf2_rank([fext, gext]) != 2:
        raise AssertionError(("extended generators dependent", advertised))

    return WitnessResult(advertised, actual, degrees, union_size, rank_u, rank_e)


def verify_profiles_and_witnesses(path: Path) -> Tuple[List[Tuple[int, int, int]], List[WitnessResult]]:
    profiles = enumerate_dangerous_profiles()
    assert len(profiles) == 46, len(profiles)
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    assert len(lines) == 45, len(lines)
    results = [verify_witness_line(ln) for ln in lines]
    advertised = [r.advertised for r in results]
    assert len(set(advertised)) == 45
    assert set(advertised).issubset(set(profiles))
    missing = set(profiles) - set(advertised)
    assert missing == {(12, 12, 24)}, missing
    # In that sole profile, union size is 24 and the weight-24 word is the all-ones word.
    *_, union = profile_coordinate_counts((12, 12, 24))
    assert union == 24
    return profiles, results


def krawtchouk(n: int, j: int, i: int) -> int:
    lo = max(0, j - (n - i))
    hi = min(j, i)
    return sum(((-1) ** t) * math.comb(i, t) * math.comb(n - i, j - t) for t in range(lo, hi + 1))


# Exact dual certificates independently reconstructed in the clean-room.
# Interpretation: F(i)=alpha+beta*K_1(i)+sum_j lambda_j*K_j(i) <= 1_D(i)
# on every allowed even weight i>=4, with lambda_j>=0.  Therefore
# |D| >= 2047*alpha - n*beta - sum_j lambda_j*C(n,j).
DELSARTE_CERTS = {
    16: (Fraction(165, 256), Fraction(0), {2: Fraction(385, 4096), 3: Fraction(143, 2048), 4: Fraction(53, 1024), 5: Fraction(53, 2048), 6: Fraction(25, 4096), 15: Fraction(119, 1024)}),
    17: (Fraction(67, 128), Fraction(0), {2: Fraction(5, 256), 3: Fraction(5, 256), 4: Fraction(7, 512), 5: Fraction(7, 512), 16: Fraction(3, 128)}),
    18: (Fraction(1, 2), Fraction(-27, 2048), {5: Fraction(13, 2048), 9: Fraction(5, 4096)}),
    19: (Fraction(377, 704), Fraction(-29, 1408), {2: Fraction(53, 5632), 4: Fraction(3, 2816), 5: Fraction(95, 22528), 6: Fraction(57, 22528), 9: Fraction(13, 11264)}),
    20: (Fraction(73, 128), Fraction(-7931, 262144), {2: Fraction(179, 16384), 3: Fraction(325, 262144), 5: Fraction(693, 262144), 6: Fraction(43, 16384), 7: Fraction(213, 262144), 9: Fraction(165, 262144), 10: Fraction(19, 32768)}),
    21: (Fraction(3131, 5120), Fraction(-143, 3840), {2: Fraction(253, 24576), 3: Fraction(27, 8192), 5: Fraction(23, 15360), 6: Fraction(11, 5120), 7: Fraction(13, 12288), 10: Fraction(59, 122880)}),
    22: (Fraction(8389, 14336), Fraction(-209, 3584), {2: Fraction(11, 3584), 3: Fraction(2145, 458752), 6: Fraction(11, 14336), 7: Fraction(55, 65536), 11: Fraction(23, 131072)}),
    23: (Fraction(196473, 434176), Fraction(-279, 3392), {3: Fraction(939, 217088), 4: Fraction(13, 217088), 7: Fraction(101, 434176), 8: Fraction(23, 434176)}),
    24: (Fraction(50299, 95488), Fraction(-27111, 381952), {3: Fraction(1, 256), 6: Fraction(7, 59680), 7: Fraction(1441, 5729280), 8: Fraction(133, 1432320)}),
}

# Matching exact feasible points of the Delsarte LP.  They are not claimed to be
# realizable code weight enumerators; they only independently certify that each
# dual lower bound is the exact optimum of this LP relaxation.
DELSARTE_PRIMAL = {
    16: {4: Fraction(140), 6: Fraction(448), 8: Fraction(870), 10: Fraction(448), 12: Fraction(140), 16: Fraction(1)},
    17: {4: Fraction(79), 6: Fraction(394), 8: Fraction(735), 10: Fraction(636), 12: Fraction(177), 14: Fraction(26)},
    18: {4: Fraction(151, 3), 6: Fraction(308), 8: Fraction(1841, 3), 10: Fraction(2336, 3), 12: Fraction(231), 14: Fraction(196, 3)},
    19: {4: Fraction(235, 11), 6: Fraction(3059, 11), 8: Fraction(4809, 11), 10: Fraction(881), 12: Fraction(3393, 11), 14: Fraction(1329, 11), 18: Fraction(1, 11)},
    20: {4: Fraction(5), 6: Fraction(240), 8: Fraction(250), 10: Fraction(1056), 12: Fraction(250), 14: Fraction(240), 16: Fraction(5), 20: Fraction(1)},
    21: {6: Fraction(987, 5), 8: Fraction(651, 5), 10: Fraction(1043), 12: Fraction(1757, 5), 14: Fraction(1457, 5), 16: Fraction(28), 18: Fraction(21, 5), 20: Fraction(7, 5)},
    22: {4: Fraction(211, 8), 6: Fraction(831, 7), 10: Fraction(7244, 7), 12: Fraction(13493, 28), 14: Fraction(2379, 7), 18: Fraction(298, 7), 20: Fraction(153, 56)},
    23: {4: Fraction(23, 53), 6: Fraction(44367, 424), 10: Fraction(468487, 424), 14: Fraction(337341, 424), 16: Fraction(276, 53), 18: Fraction(15341, 424)},
    24: {4: Fraction(26036, 373), 6: Fraction(54762, 373), 10: Fraction(1733414, 1865), 14: Fraction(801654, 1865), 16: Fraction(350691, 1865), 18: Fraction(527906, 1865)},
}


def verify_delsarte_certificate(n: int) -> Fraction:
    alpha, beta, lambdas = DELSARTE_CERTS[n]
    if any(lam < 0 for lam in lambdas.values()):
        raise AssertionError("dual lambda must be nonnegative")
    allowed = list(range(4, n + 1, 2))
    for i in allowed:
        rhs = Fraction(1 if i in DANGEROUS else 0)
        f = alpha + beta * krawtchouk(n, 1, i)
        f += sum(lam * krawtchouk(n, j, i) for j, lam in lambdas.items())
        if f > rhs:
            raise AssertionError(("dual pointwise inequality failed", n, i, f, rhs))
    bound = 2047 * alpha - n * beta
    bound -= sum(lam * math.comb(n, j) for j, lam in lambdas.items())
    if bound <= 640:
        raise AssertionError(("bound does not cross threshold", n, bound))

    # Independent exact primal feasibility check, establishing matching LP optimum.
    x = {i: DELSARTE_PRIMAL[n].get(i, Fraction(0)) for i in allowed}
    if any(v < 0 for v in x.values()):
        raise AssertionError("negative primal variable")
    assert sum(x.values()) == 2047
    assert sum(x[i] * krawtchouk(n, 1, i) for i in allowed) == -n
    for j in range(2, n + 1):
        lhs = math.comb(n, j) + sum(x[i] * krawtchouk(n, j, i) for i in allowed)
        if lhs < 0:
            raise AssertionError(("primal Delsarte inequality failed", n, j, lhs))
    primal_obj = sum(x[i] for i in allowed if i in DANGEROUS)
    assert primal_obj == bound, (n, primal_obj, bound)
    return bound


def macwilliams_dual_counts(n: int, A: Dict[int, int], dim: int) -> Tuple[bool, str, List[int]]:
    size = 1 << dim
    B: List[int] = []
    for j in range(n + 1):
        numerator = sum(count * krawtchouk(n, j, i) for i, count in A.items())
        if numerator % size:
            return False, f"B_{j} nonintegral numerator={numerator}/{size}", []
        bj = numerator // size
        if bj < 0:
            return False, f"B_{j} negative={bj}", []
        B.append(bj)
    return True, "OK", B


def enumerate_safe_weight_enumerators(n: int, exceptional_allones: bool = False) -> Tuple[int, int, Dict[str, int]]:
    """Enumerate candidates after size+B1, then enforce exact MacWilliams integrality/nonnegativity."""
    if exceptional_allones and n != 24:
        raise ValueError("all-ones exceptional branch only has n=24")
    aN = 1 if exceptional_allones else 0
    remaining = (1 << 10) - 1 - aN  # exclude zero word and optional all-ones word
    initial = 0
    survivors = 0
    first_fail: Dict[str, int] = {}
    for a4 in range(remaining + 1):
        # a6+a10 = remaining-a4.  Solve B1=0 exactly for a6.
        s = remaining - a4
        const = n + (n - 8) * a4 + (n - 20) * s + ((n - 2 * n) * aN)
        # coefficient of a6 after substituting a10=s-a6 is 8.
        if (-const) % 8:
            continue
        a6 = (-const) // 8
        a10 = s - a6
        if a6 < 0 or a10 < 0:
            continue
        initial += 1
        A = {0: 1, 4: a4, 6: a6, 10: a10}
        if aN:
            A[n] = aN
        ok, reason, _ = macwilliams_dual_counts(n, A, dim=10)
        if ok:
            survivors += 1
        else:
            key = reason.split()[0]
            first_fail[key] = first_fail.get(key, 0) + 1
    return initial, survivors, first_fail


def verify_macwilliams_closure() -> Dict[int, Tuple[int, int]]:
    summary: Dict[int, Tuple[int, int]] = {}
    for n in range(14, 25):
        initial, survivors, _ = enumerate_safe_weight_enumerators(n, exceptional_allones=False)
        if survivors != 0:
            raise AssertionError(("MacWilliams survivor exists", n, survivors))
        summary[n] = (initial, survivors)
    initial, survivors, _ = enumerate_safe_weight_enumerators(24, exceptional_allones=True)
    if survivors != 0:
        raise AssertionError(("exceptional all-ones MacWilliams survivor", survivors))

    # Conceptually independent one-line check for the exceptional case:
    # in length 24, K1(0)=+24 and K1(24)=-24 cancel; K1(4),K1(6),K1(10)
    # are +16,+12,+4.  B1=0 cannot hold for 1022 remaining nonzero words.
    assert krawtchouk(24, 1, 0) + krawtchouk(24, 1, 24) == 0
    assert all(krawtchouk(24, 1, w) > 0 for w in (4, 6, 10))
    return summary


def verify_allones_complement_bound() -> None:
    possible = [0, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
    for w in possible:
        wc = 24 - w
        if not (w in DANGEROUS or wc in DANGEROUS):
            raise AssertionError(("complement pair without dangerous member", w, wc))
    # 2^11 words / 2 per complement pair = 1024 pairs; at least one D-word per pair.
    assert (1 << 11) // 2 == 1024
    assert 1024 - 1 == 1023 and 1023 > 640


def adversarial_self_tests(witness_path: Path) -> None:
    lines = [ln.strip() for ln in witness_path.read_text(encoding="utf-8").splitlines() if ln.strip()]
    first = lines[0].split()

    # 1) Tamper one truth-table bit: verifier must reject.
    h = int(first[3], 16) ^ 1
    tampered = " ".join(first[:3] + [f"{h:016x}", first[4]])
    rejected = False
    try:
        verify_witness_line(tampered)
    except Exception:
        rejected = True
    assert rejected, "tampered witness was incorrectly accepted"

    # 2) Duplicate generators: exact-kernel witness must reject.
    dup = " ".join(first[:3] + [first[3], first[3]])
    rejected = False
    try:
        verify_witness_line(dup)
    except Exception:
        rejected = True
    assert rejected, "dependent witness generators were incorrectly accepted"

    # 3) Algebraically impossible near-profile must not enter the 46-profile universe.
    assert (8, 8, 24) not in enumerate_dangerous_profiles()

    # 4) Tamper a Delsarte certificate upward: pointwise feasibility must fail.
    n = 18
    alpha, beta, lambdas = DELSARTE_CERTS[n]
    bad_alpha = alpha + 1
    bad_feasible = True
    for i in range(4, n + 1, 2):
        rhs = Fraction(1 if i in DANGEROUS else 0)
        f = bad_alpha + beta * krawtchouk(n, 1, i)
        f += sum(lam * krawtchouk(n, j, i) for j, lam in lambdas.items())
        if f > rhs:
            bad_feasible = False
            break
    assert not bad_feasible, "tampered dual certificate was incorrectly accepted"

    # 5) A candidate satisfying size+B1 but with nonintegral MacWilliams coefficient must reject.
    A_fake = {0: 1, 4: 1, 6: 764, 10: 258}  # length 14 candidate after size+B1
    assert sum(A_fake.values()) == 1024
    assert sum(v * krawtchouk(14, 1, i) for i, v in A_fake.items()) == 0
    ok, _, _ = macwilliams_dual_counts(14, A_fake, dim=10)
    assert not ok, "fake MacWilliams enumerator was incorrectly accepted"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("witness", nargs="?", default="h6_exact_profile_witnesses.txt")
    args = parser.parse_args()
    witness_path = Path(args.witness).resolve()
    source_path = Path(__file__).resolve()

    print("H6-LOWER25 CLEAN-ROOM VERIFIER")
    print(f"python={sys.version.split()[0]} platform={platform.platform()}")
    print(f"source_sha256={sha256(source_path)}")
    print(f"witness_sha256={sha256(witness_path)}")

    # Core ambient RM(2,6) sanity check.
    full_rank = eval_rank(list(range(DOMAIN_SIZE)))
    assert full_rank == D2 == 22
    print(f"[PASS] RM(2,6) full evaluation rank = {full_rank}")

    profiles, witness_results = verify_profiles_and_witnesses(witness_path)
    print(f"[PASS] dangerous 2D profiles independently enumerated = {len(profiles)}")
    print(f"[PASS] witness profiles verified = {len(witness_results)} distinct")
    print("[PASS] unique missing profile = (12,12,24), necessarily all-ones exceptional")
    print("[PASS] every supplied witness: degree<=3, direct RM(2,6) orthogonality, exact 2D kernel, extension to 24/rank22")

    bounds: Dict[int, Fraction] = {}
    for n in range(16, 25):
        bounds[n] = verify_delsarte_certificate(n)
        print(f"[PASS] Delsarte N={n}: |D| >= {bounds[n]} > 640")

    mw = verify_macwilliams_closure()
    for n in range(14, 25):
        initial, survivors = mw[n]
        print(f"[PASS] MacWilliams N={n}: size+B1 candidates={initial}, exact survivors={survivors}")
    print("[PASS] exceptional [24,10] weights {4,6,10,24} with A24=1 impossible (B1 and exhaustive exact check)")

    verify_allones_complement_bound()
    print("[PASS] all-ones complement-pair bound: |D(E)|>=1024; |D(E)\\{1}|>=1023>640")

    adversarial_self_tests(witness_path)
    print("[PASS] adversarial self-tests reject tampered/rank-deficient/fake certificates")

    print("INTERNAL_COMPUTATIONAL_VERDICT=PASS")
    print("EXTERNAL_DEPENDENCY_REQUIRED=large sum-free theorem (Davydov-Tombak / Clark-Pedersen)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())