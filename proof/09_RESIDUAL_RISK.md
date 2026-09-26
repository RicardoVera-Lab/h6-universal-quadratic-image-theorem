# 09 — RESIDUAL RISK

## Mathematical status within scope

`CONFIRMED_WITHIN_SCOPE`.

No unresolved internal bridge remains in the frozen proof of `h(6)>=25` under the stated definition of coordinatewise quadratic maps.

## Residual risks that remain

### 1. External theorem trust boundary

The large sum-free theorem is source-verified and its statement matches the required application, but it is not reproved or formally verified inside this capsule.

**Class:** `EXTERNAL_THEOREM` residual dependency.

### 2. Shared witness data

Both internal verifiers use the same 45 witness truth-table pairs. They validate those data independently, but they do not independently rediscover a second witness corpus.

**Effect:** limits independence level; does not create an unchecked mathematical step because each witness is fully verified.

### 3. Shared Delsarte certificate coefficients

The second verifier independently checks the exact rational coefficients with a different Krawtchouk implementation, but the coefficients themselves are shared with the primary certificate.

**Effect:** strong certificate checking, but not independent certificate discovery in this mission.

### 4. No formal proof assistant

The human proof text and Python exact checkers are not a Lean/Coq/Isabelle formalization. A transcription error in prose remains possible even when the computational claims are correct; the expert-review brief therefore targets the proof bridges explicitly.

### 5. No external competent reproduction yet

The capsule has internal clean-room reconstruction plus a second internal checker, not a third-party independent audit.

**Effect:** the result should remain an internal R4-style computer-assisted theorem candidate until external mathematical review/reproduction.

## Explicit non-risks after hardening

The following previously plausible failure modes are closed in the current capsule:

- 24-versus-23/22 off-by-one;
- output-translation normalization;
- zero/repeated target columns;
- even-subcode dimension;
- active-length lower bound;
- exact-kernel versus merely contained-kernel confusion;
- profile completeness;
- exceptional all-one profile;
- rational Delsarte arithmetic;
- strict 640 threshold;
- coset-to-hyperplane inference;
- MacWilliams integer feasibility;
- hidden dependence on `h(6)>=26`;
- hidden novelty assumption.

## Boundary of the verdict

This verdict says only that the supplied proof/certificate chain establishes the frozen lower bound internally and is ready for destructive expert review. It does not assert novelty, priority, importance, `h(6)=25`, or any stronger lower bound.