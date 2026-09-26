# 05 — CERTIFICATE ARCHITECTURE

## Capsule contents used as proof certificates

`certificate/verify_h6_lower25_cleanroom.py`  
Primary exact verifier reconstructed in the earlier clean-room hardening.

`certificate/verify_h6_publication_independent.py`  
Second checker written for this publication-hardening mission with different internal representations for several core calculations.

`certificate/h6_exact_profile_witnesses.txt`  
45 exact-kernel witness pairs. Each line has

`a b c f_hex g_hex`

where `(a,b,c)` is the sorted dangerous weight profile and the two hex strings encode 64-bit Boolean truth tables.

`certificate/PRIMARY_RUN.log`  
Observed exact rerun of the primary verifier.

`certificate/INDEPENDENT_RUN.log`  
Observed exact run of the second verifier.

## What the primary verifier certifies

1. rank 22 of the full `RM(2,6)` evaluation matrix;
2. exact enumeration of 46 dangerous profiles;
3. validation of all 45 supplied witness profiles;
4. direct orthogonality of witness dependencies to all degree-<=2 monomials;
5. exact-kernel rank `|U|-2` on each witness union support;
6. extension to 24 distinct evaluation points of rank 22;
7. nine exact rational Delsarte dual certificates;
8. matching exact feasible primal LP points;
9. exhaustive exact MacWilliams closure for the safe-weight dimension-10 branch;
10. exact closure of the all-one branch;
11. negative self-tests that reject corrupted witnesses/certificates.

## What the second verifier changes

The second verifier does not import the primary checker.

- It represents `phi_2(x)` as a 22-bit **column vector**, whereas the primary verifier is row-oriented.
- It checks witness degree <=3 by vanishing of all fourth coordinate finite differences, rather than by a Boolean Möbius transform.
- It computes Krawtchouk coefficients as coefficients of `(1+z)^(n-i)(1-z)^i`, rather than by the primary binomial-sum formula.
- It performs a separate column-rank basis extension to 24 points.
- It independently re-enumerates dangerous profiles and safe-weight MacWilliams candidates.
- It explicitly checks the Hamming-bound off-by-one points `N_E>=16` and `N_C>=15`.

The exact Delsarte coefficient data and witness dataset are shared, so this is not external independence and is not claimed as such.

## Exactness

All proof-authoritative arithmetic in both checkers is integer or rational arithmetic. No timeout, random search, absence of a model, or floating-point comparison is used as a proof of impossibility.

## Delsarte certificate form

For each active length `N`, the certificate supplies rational

`alpha`, `beta`, and `lambda_j>=0`

such that for every allowed even weight `i`,

`alpha + beta K_1(i) + sum_j lambda_j K_j(i) <= 1_D(i)`.

The checker then derives the exact lower bound

`|D| >= 2047 alpha - N beta - sum_j lambda_j C(N,j)`

and verifies that it is greater than 640.

## MacWilliams closure

For the generic hyperplane code, the checker exhausts nonnegative integers

`A_4,A_6,A_10`

with total 1023 and `B_1=0`, then requires every dual coefficient

`B_j=2^(-10) sum_i A_i K_j(i)`

to be a nonnegative integer. No candidate survives.

The exceptional length-24 branch additionally has `A_24=1`; it is already impossible from `B_1=0` and is also checked exhaustively.

## Reproduction

From the ZIP root:

```bash
python certificate/verify_h6_lower25_cleanroom.py certificate/h6_exact_profile_witnesses.txt
python certificate/verify_h6_publication_independent.py certificate/h6_exact_profile_witnesses.txt
```

Expected terminal verdicts:

`INTERNAL_COMPUTATIONAL_VERDICT=PASS`

and

`INDEPENDENT_CHECK_VERDICT=PASS`.