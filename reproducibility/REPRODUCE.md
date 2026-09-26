# Reproduce H6

## Requirements

- Python 3.11+ recommended
- Python standard library only for the public proof-authoritative verifier

## Run

From the repository root:

```bash
python certificate/verify_h6_lower25_cleanroom.py certificate/h6_exact_profile_witnesses.txt
```

Expected final line:

```text
INTERNAL_COMPUTATIONAL_VERDICT=PASS
```

The checker independently performs the finite proof-authoritative tasks embedded in the public certificate path, including:

- full RM(2,6) evaluation rank check;
- dangerous 2D profile enumeration;
- exact-kernel witness validation;
- exact rational Delsarte checks;
- exact MacWilliams closure;
- all-one exceptional-branch closure;
- adversarial self-tests.

## Public and internal verification

The publication-hardening capsule records two internal implementations returning PASS.

The public repository includes the clean-room verifier and the frozen witness corpus. The second internal implementation used different representations for several calculations and is documented in [proof/06_INDEPENDENT_VERIFICATION.md](../proof/06_INDEPENDENT_VERIFICATION.md).

The two implementations shared the witness dataset and Delsarte coefficient data; this is internal reimplementation, not a claim of external independence.

## Integrity

The original publication-hardening capsule hashes are preserved in [ORIGINAL_MANIFEST_SHA256.txt](ORIGINAL_MANIFEST_SHA256.txt).
