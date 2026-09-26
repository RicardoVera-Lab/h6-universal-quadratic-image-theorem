# 02 — THEOREM STATEMENT

## Main theorem

Let `q:F_2^6 -> F_2^12` range over maps whose 12 coordinate functions have algebraic degree at most 2. Then every subset `H subset F_2^12` of cardinality at most 24 is contained in the image of at least one such `q`.

Hence

`h(6) >= 25`.

## Equivalent evaluation-geometry statement

Let

`phi_2:F_2^6 -> F_2^22`

be the degree-<=2 evaluation embedding. For every `t<=24` and every injective target matrix `M in F_2^(12 x t)`, there exists an ordered set `X` of `t` distinct points of `F_2^6` such that, with

`V_X=[phi_2(x)]_{x in X}`,

one has

`ker(V_X) subset ker(M)`.

Equivalently, there is a linear `T:F_2^22 -> F_2^12` with

`M=T V_X`.

## Proof dependencies

The theorem is established in this capsule from:

1. elementary linear algebra and Boolean polynomial interpolation — `HUMAN_PROOF`;
2. an exact finite classification of dangerous 2-dimensional dependency profiles — `FINITE_EXHAUSTION`;
3. 45 exact-kernel witness pairs, each checked by exact arithmetic/rank — `CERTIFICATE_CHECK`;
4. exact rational Delsarte/Krawtchouk certificates for active lengths 16 through 24 — `CERTIFICATE_CHECK`;
5. the published large sum-free theorem for `F_2^11` at threshold `5*2^(11-4)=640` — `EXTERNAL_THEOREM`;
6. an exhaustive exact MacWilliams feasibility check for the resulting safe-weight dimension-10 subcode — `FINITE_EXHAUSTION` + `CERTIFICATE_CHECK`;
7. a separate all-one exceptional branch — `HUMAN_PROOF` + `CERTIFICATE_CHECK`.

No novelty premise and no stronger lower-bound premise enters the proof.