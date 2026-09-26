# 06 — INDEPENDENT VERIFICATION

## Primary rerun

The earlier clean-room verifier was rerun against the frozen 45-witness dataset.

Observed environment:

- Python `3.13.5`;
- Linux `6.18.44`, x86_64, glibc 2.41;
- Python standard library only for the proof-authoritative primary checker.

Observed result:

`INTERNAL_COMPUTATIONAL_VERDICT=PASS`.

The run reconfirmed:

- full evaluation rank 22;
- 46 profiles;
- 45 valid exact-kernel witnesses;
- unique missing profile `(12,12,24)`;
- all nine Delsarte bounds above 640;
- zero MacWilliams survivors;
- all-one complement bound and exceptional closure;
- adversarial self-tests reject tampering.

## Second checker

A new checker was written without importing the primary code.

Observed result:

`INDEPENDENT_CHECK_VERDICT=PASS`.

It reconfirmed the same finite claims using several different mathematical implementations:

| Component | Primary | Second checker | Independence note |
|---|---|---|---|
| Evaluation matrix | row bitsets | 22-bit column vectors | implementation-independent representation |
| Degree <=3 witness test | Möbius/ANF transform | fourth finite differences | conceptually distinct criterion |
| GF(2) rank | row elimination | column-pivot elimination | separate code path |
| Krawtchouk | binomial alternating sum | generating-polynomial coefficient | conceptually distinct calculation |
| Dangerous profiles | direct enumeration | independent direct enumeration | separate code path |
| MacWilliams candidates | exact Krawtchouk routine | independent polynomial-coefficient routine | separate code path |
| Witness data | shared | shared | not independent data |
| Delsarte dual coefficients | shared | shared | checker independence only |

## Independence classification

This capsule supports a mixed `I1/I2` internal independence claim:

- `I2`-like conceptual independence for several local calculations (degree test and Krawtchouk implementation);
- `I1` reimplementation for the overall proof architecture because both checkers use the same high-level reduction, the same 45 witness data, and the same exact Delsarte dual coefficients.

It is **not** `I4` external independence. No third party, formal proof assistant, or separately generated witness corpus has reproduced the theorem in this mission.

## Result

No discrepancy between the two implementations was found.