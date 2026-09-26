# 00 — FROZEN CLAIM

**MISSION_ID:** H6-LOWER25-PUBLICATION-HARDENING-01  
**Mode:** clean-room mathematical hardening  
**Scope:** only the lower bound `h(6) >= 25`  
**Final status in this capsule:** `CONFIRMED_WITHIN_SCOPE`

## Definition

For `n >= 1`, let

`h(n) = min{|H| : H subset F_2^(2n) and for every coordinatewise algebraic-degree-<=2 map q:F_2^n -> F_2^(2n), H is not a subset of im(q)}.`

Here a coordinate of `q` is a Boolean polynomial in algebraic normal form of degree at most 2.

For `n=6`, the codomain is `F_2^12`.

## Frozen claim

> **Theorem candidate.** Every set `H subset F_2^12` with `|H| <= 24` is contained in the image of some coordinatewise quadratic map `q:F_2^6 -> F_2^12`.

Equivalently,

`h(6) >= 25`.

No assertion is made about `h(6)>=26`, `h(6)=25`, novelty, priority, or publication precedence.

## Reduction to exactly 24 targets

It is enough to prove the statement for `|H|=24`. If `|H|=t<24`, enlarge `H` to a 24-element set `H' subset F_2^12`; the codomain has 4096 points, so this is always possible. A map whose image contains `H'` also contains `H`.

**Dependency class:** `HUMAN_PROOF`.

## Frozen interpretation of "quadratic"

The proof uses the 22-dimensional space of Boolean functions spanned by the squarefree monomials of degree at most 2:

`1`, `x_1,...,x_6`, and `x_i x_j` for `1<=i<j<=6`.

Dimension:

`1 + 6 + C(6,2) = 22`.

**Dependency class:** `ASSUMPTION` only in the sense that this is the mission's fixed definition of coordinatewise algebraic degree. No stronger notion of polynomial map is used.