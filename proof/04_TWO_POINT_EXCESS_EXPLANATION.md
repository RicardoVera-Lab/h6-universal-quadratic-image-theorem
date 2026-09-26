# 04 — WHY THE PROOF GAINS TWO POINTS BEYOND DIMENSION 22

The gain from 22 to 24 is not extra polynomial freedom. The scalar quadratic space still has dimension exactly 22.

The mechanism is **adaptive matching of dependency spaces**.

## 1. Fixed preimages stop at 22

For an ordered preimage set `X` of size `t`, interpolation of arbitrary scalar values is possible exactly when the `22 x t` evaluation matrix `V_X` has trivial kernel.

That can happen for `t<=22` by choosing an information set. It cannot happen for `t>22`.

Thus ordinary interpolation with preimages fixed in advance has a hard dimension barrier at 22.

## 2. The preimages are not fixed

For vector-valued interpolation the target data form a `12 x t` matrix `M`. We do not need `ker(V_X)=0`. We only need

`ker(V_X) subset ker(M)`.

The preimage set `X` may be chosen after seeing `M`.

For 24 targets, an evaluation matrix of full possible rank 22 has exactly two unavoidable relations. The target matrix, by contrast, has

`dim ker(M) >= 24-12 = 12`.

After translation removes zero target columns and repeated targets are already excluded, this target kernel has minimum distance at least 3. Intersecting with the even-weight hyperplane leaves an 11-dimensional even code `E` of minimum distance at least 4.

So the target data have a large reservoir of legal relations. The problem becomes:

> Can we find a 2-dimensional subspace `L <= ker(M)` which is itself the exact dependency space of 24 points of the quadratic evaluation configuration?

The proof answers yes.

## 3. Where the two relations come from

The 45 witness families show that almost every dangerous 2-dimensional weight profile can occur as an exact kernel of 24 selected points of `phi_2(F_2^6)`. The only missing profile is `(12,12,24)`, which is precisely the all-one exceptional geometry and is handled separately.

If the target kernel contained no realizable dangerous 2-plane, then the dangerous words in its 11-dimensional even subcode would have to be sum-free.

That avoidance condition is too strong:

1. exact Delsarte bounds force more than 640 dangerous words;
2. the large sum-free theorem forces such a set into a coset of a proper subspace;
3. a separating hyperplane then contains only the safe weights `{4,6,10}`;
4. exact MacWilliams constraints show that no such dimension-10 binary code exists.

Therefore the target kernel must contain a realizable 2-plane `L` (or the exceptional all-one branch leads to the same contradiction).

Choose 24 evaluation points with

`ker(V_X)=L`.

Since `L<=ker(M)`, the kernel criterion gives a quadratic interpolant.

## 4. Conceptual summary

The two-point excess is therefore:

`22 coefficients`

plus

`2 unavoidable evaluation relations`

matched adaptively to

`>=12 target relations`.

No coefficients are created. Instead, the proof uses the freedom to choose the 24 preimages so that the two relations forced by the 22-dimensional evaluation space are relations the 24 target vectors already satisfy.

This is the mathematical mechanism behind the gain from 22 to 24.

## 5. Why this is stronger than "the program checked it"

The computation only certifies two finite structural ingredients:

- which 2-dimensional dangerous dependency types are realizable as exact evaluation kernels;
- that Delsarte/MacWilliams finite feasibility regions contain no escape route.

The explanatory mechanism is human-readable and independent of the implementation:

**adaptive kernel placement inside a surplus target-kernel space, forced by additive-combinatorial and coding-theoretic structure.**