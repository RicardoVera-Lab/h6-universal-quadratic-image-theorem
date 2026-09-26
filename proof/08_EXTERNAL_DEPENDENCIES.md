# 08 — EXTERNAL DEPENDENCIES

## 1. Non-elementary external theorem actually used

The proof uses the following theorem for sum-free subsets of binary vector spaces.

**Leo Versteegen**, *The Structure of Large SUM-Free Sets in F_p^n*, **The Quarterly Journal of Mathematics** 75(3) (2024), 1057–1071, Theorem 1.2, DOI `10.1093/qmath/haae042`.

The theorem states, for the binary case:

If `A subset F_2^n` is sum-free and

`|A| > 5*2^(n-4)`,

then there is a proper subspace `V < F_2^n` such that `A` is contained in a coset of `V`.

The paper attributes the binary result to Davydov–Tombak and independently to Clark–Pedersen.

For this mission `n=11`, so the strict threshold is exactly

`5*2^7=640`.

**Dependency class:** `EXTERNAL_THEOREM`.

## 2. Original binary reference

**W. Edwin Clark and John Pedersen**, *Sum-free sets in vector spaces over GF(2)*, **Journal of Combinatorial Theory, Series A** 61(2) (1992), 222–229, DOI `10.1016/0097-3165(92)90019-Q`.

The publication-hardening proof relies on the direct arbitrary-set formulation quoted in Versteegen Theorem 1.2, avoiding any need to reconstruct the result indirectly from maximal sum-free sets.

## 3. What is not treated as an opaque external theorem

The following ingredients are included at proof level in the capsule and are not hidden behind citations:

- factorization of quadratic maps through `phi_2`;
- row-space/right-kernel equivalence;
- Hamming-bound arithmetic used for active lengths;
- 2-dimensional profile coordinate counts;
- the Delsarte linear inequalities used in the certificate;
- the MacWilliams/Krawtchouk coefficient formula needed for feasibility;
- the separation of a nontrivial coset by a hyperplane;
- the all-one complement-pair argument.

Standard names such as "Delsarte" and "MacWilliams" identify the framework, but the exact equations needed here are stated and machine-checked in the capsule.

## 4. No novelty research

This mission performs no literature search for whether `h(6)>=25`, the parameter `h`, the exact-kernel profile construction, or the two-point excess mechanism is new. Priority and originality remain outside scope and are not mathematical dependencies.