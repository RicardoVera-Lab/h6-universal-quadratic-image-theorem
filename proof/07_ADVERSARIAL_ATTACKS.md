# 07 — ADVERSARIAL ATTACKS

The following attacks were executed against the frozen claim and proof chain.

| Attack | Question | Result |
|---|---|---|
| Off-by-one at `|H|<=24` | Does proving exactly 24 really cover smaller sets? | **PASS.** Enlarge any smaller set to 24 distinct codomain points. |
| Distinct preimages | Could two target points use the same preimage? | **PASS.** Distinct target values force distinct preimages. |
| Translation normalization | Does translating the target preserve the class of maps and badness? | **PASS.** Output translation is addition of a constant vector. Choose translator outside `H` to avoid zero. |
| Kernel rank | Is `dim ker(M)>=12` always valid? | **PASS.** `M` is `12 x 24`; rank may be smaller, which only increases the kernel. |
| Minimum distance | Can `ker(M)` contain weight 1 or 2? | **PASS.** Weight 1 means a zero target column; weight 2 means two equal target columns. Both are excluded after normalization/distinctness. |
| Even subcode | Is an 11D even subcode guaranteed? | **PASS.** Intersect a `>=12`-dimensional kernel with the codimension-1 even hyperplane. |
| Zero coordinates | Does deleting coordinates zero on `E` alter dimension or weights? | **PASS.** It removes positions identically zero on every codeword. |
| Active-length lower bound | Is `N_E>=16` correct? | **PASS.** Hamming bound after one puncture: fail at 15, equality at 16. |
| Safe-subcode lower bound | Was range 14 used incorrectly? | **PASS WITH PRESENTATION FIX.** A full-support dimension-10 safe code actually has `N_C>=15`; the primary verifier's inclusion of `N=14` is harmless overcoverage. |
| Profile completeness | Are there really 46 dangerous sorted profiles? | **PASS.** Both checkers regenerate exactly 46 from the coordinate-type formulas. |
| Missing profile | Is the only missing witness `(12,12,24)`? | **PASS.** Set difference is exactly that singleton. |
| Exact-kernel bridge | Do witnesses give merely contained dependencies rather than exact kernels? | **PASS.** On union support the rank is `|U|-2`; after basis extension to 24 points the rank is 22, so kernel dimension is exactly 2. |
| Coordinate equivalence | Can a witness of the same weight triple be transferred to the actual 2-plane in `K`? | **PASS.** Sorted nonzero weights determine the three nonzero coordinate-type multiplicities up to `GL(2,2)` and coordinate permutation. |
| Basis-extension circularity | Does extension to 24 use `h(6)>=25`? | **PASS.** It uses only full rank 22 of the complete evaluation configuration. |
| Sum-free bridge | Could a dangerous triple fail to yield interpolation? | **PASS.** Exact kernel `L<=ker(M)` gives `row(M)<=row(V_X)` and therefore a quadratic interpolant. |
| All-one exception | Could `(12,12,24)` create an unhandled triple? | **PASS.** Removing the all-one word eliminates that profile from any sum-free violation; size is recovered by complement pairing. |
| Delsarte arithmetic | Are bounds floating or approximate? | **PASS.** Every inequality and final bound is exact rational arithmetic. |
| Delsarte sign convention | Could the dual inequality be reversed? | **PASS.** The pointwise inequality is multiplied by nonnegative `A_i`; `B_j>=0` enters with nonnegative multipliers and yields the stated lower bound. |
| External theorem threshold | Is the threshold 640 inclusive or strict? | **PASS.** The theorem requires `>5*2^(n-4)`; every certified bound is strictly greater than 640, and exceptional size is at least 1023 after removal. |
| Coset-to-hyperplane inference | Does the theorem itself give a disjoint hyperplane? | **PASS.** The proof derives it: the containing coset is nontrivial because a sum-free subset of a proper subspace has size at most 512; then a linear functional separates the coset. |
| MacWilliams feasibility | Could a real safe code evade the enumerator search? | **PASS.** Any such code must have integer counts totaling 1023, full-support `B_1=0`, and all dual counts nonnegative integers. The finite search exhausts these necessary conditions. |
| Exceptional `1 in C` | Could a `{4,6,10,24}` code survive? | **PASS.** `B_1=0` is impossible because the 0/24 contributions cancel and every remaining permitted weight contributes positively. |
| Hidden use of frozen claim | Is any lemma proved by assuming the conclusion? | **PASS.** No step invokes `h(6)>=25`, `h(6)>=26`, or an equivalent interpolation assertion as an input. |
| Novelty contamination | Is priority or originality used as evidence? | **PASS.** No novelty premise appears anywhere in the mathematical chain. |

## Adversarial tamper tests

The primary checker also rejects:

- a one-bit-corrupted witness;
- dependent duplicate witness generators;
- the algebraically impossible near-profile `(8,8,24)`;
- an inflated invalid Delsarte dual certificate;
- a fake `[14,10]` weight enumerator satisfying size and `B_1` but failing exact MacWilliams integrality.

No attack produced a counterexample or an unresolved bridge within the frozen scope.