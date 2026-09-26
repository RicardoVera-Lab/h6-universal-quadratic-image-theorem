# 01 — RM(2,6) EVALUATION EQUIVALENCE

## 1. Evaluation embedding

Let `P_2` be the 22-dimensional `F_2`-space of Boolean polynomials in six variables of algebraic degree at most 2. Fix the ordered monomial basis

`M_2 = {1, x_1,...,x_6, x_i x_j : 1<=i<j<=6}`.

Define

`phi_2 : F_2^6 -> F_2^22`

by

`phi_2(x) = (m(x))_{m in M_2}`.

The first coordinate is always 1, and the six linear coordinates recover `x`, so `phi_2` is injective.

The 64 columns `phi_2(x)` span `F_2^22`: if a coefficient vector is orthogonal to all 64 columns, the corresponding degree-<=2 Boolean polynomial vanishes on all of `F_2^6`; uniqueness of algebraic normal form forces all coefficients to be zero.

**Dependency class:** `HUMAN_PROOF`, with rank 22 also checked by both verifiers.

## 2. Every quadratic map factors through `phi_2`

Let

`q=(q_1,...,q_12):F_2^6 -> F_2^12`

with every `q_j` of degree at most 2. Write the coefficient row of `q_j` in the basis `M_2` as `a_j in F_2^22`. Let `T` be the `12 x 22` matrix with rows `a_j`. Then, for every `x`,

`q(x)=T phi_2(x)`.

Conversely, any linear map `T:F_2^22 -> F_2^12` defines a coordinatewise degree-<=2 map `q(x)=T phi_2(x)`.

Thus quadratic maps are exactly linear images of the evaluation configuration `phi_2(F_2^6)`.

**Dependency class:** `HUMAN_PROOF`.

## 3. Adaptive projection/interpolation property

For `t<=24`, define `AP(t)` as follows.

For every injective ordered target list

`Y=(y_1,...,y_t)`, `y_i in F_2^12`,

there exist distinct domain points

`X=(x_1,...,x_t)`, `x_i in F_2^6`,

and a linear map `T:F_2^22 -> F_2^12` such that

`T phi_2(x_i)=y_i` for every `i`.

This is adaptive: both the selected subset of the 64 evaluation points and the linear map may depend on the target set.

Let

`V_X = [phi_2(x_1) ... phi_2(x_t)]`, a `22 x t` matrix,

and

`M_Y = [y_1 ... y_t]`, a `12 x t` matrix.

Then `AP(t)` is equivalent to the kernel condition

`ker(V_X) subset ker(M_Y)`.

### Proof of the kernel criterion

The interpolation equations are

`M_Y = T V_X`.

Such a `T` exists iff every row of `M_Y` belongs to the row space of `V_X`, i.e.

`row(M_Y) subset row(V_X)`.

For a matrix over `F_2`, the right kernel is the orthogonal complement of its row space. Therefore

`row(M_Y) subset row(V_X)`

iff

`row(V_X)^perp subset row(M_Y)^perp`

iff

`ker(V_X) subset ker(M_Y)`.

**Dependency class:** `HUMAN_PROOF`.

## 4. Equivalence A <=> B

### A

Every `H subset F_2^12` with `|H|<=24` is contained in `im(q)` for some coordinatewise degree-<=2 map `q:F_2^6 -> F_2^12`.

### B

`AP(t)` holds for every `t<=24`; equivalently, for every injective target matrix `M_Y` with `t<=24` columns, one can choose `t` distinct evaluation points so that

`ker(V_X) subset ker(M_Y)`.

### A => B

Fix distinct targets `y_1,...,y_t`. By A there is a quadratic map `q` whose image contains them. Choose `x_i` with `q(x_i)=y_i`. Because the `y_i` are distinct, the `x_i` are distinct. By the factorization lemma, `q=T phi_2` for some linear `T`. Hence

`T phi_2(x_i)=y_i`

for all `i`, which is B.

### B => A

Fix `H={y_1,...,y_t}`. B supplies distinct `x_i` and linear `T` with `T phi_2(x_i)=y_i`. Define

`q(x)=T phi_2(x)`.

By construction every coordinate of `q` has algebraic degree at most 2 and every `y_i` lies in its image. Hence A.

Therefore A and B are exactly equivalent; no one-way relaxation is used.

**Dependency class:** `HUMAN_PROOF`.

## 5. Why 22 points are trivial and 23/24 are not

Because the 64 evaluation columns have rank 22, one can choose a 22-point information set. For any `t<=22`, choose `t` independent columns. Then `ker(V_X)=0`, so the kernel criterion is automatic for every target matrix.

For 23 points, every `V_X` has a nonzero kernel. For 24 points, every `V_X` has kernel dimension at least 2. Thus the issue beyond 22 is not lack of coefficients alone; it is whether the unavoidable evaluation dependencies can be made to lie inside the target dependency space.

The proof of `h(6)>=25` shows that for every 24-point target set one can adapt the preimages so that an exact 2-dimensional evaluation kernel is contained in the target kernel.