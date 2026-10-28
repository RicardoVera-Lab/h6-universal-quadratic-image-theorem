# Reproduce H6

## Requirements

- Python 3.11+ recommended
- Python standard library only for the public proof-authoritative verifier

## Run

From the repository root:

```bash
python certificate/verify_h6_lower25_cleanroom.py certificate/h6_exact_profile_witnesses.txt
```

Expected verdict (followed by the external-dependency notice):

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

The [public SHA-256 manifest](PUBLIC_MANIFEST_SHA256.txt) covers every tracked file in this distribution except the manifest itself. Paths are relative to the repository root. It describes the public files actually supplied, not a separate internal research package.

From the repository root, verify the downloaded files before running the certificate:

```bash
sha256sum --strict --check reproducibility/PUBLIC_MANIFEST_SHA256.txt
```

Every entry must report `OK`. GitHub Actions runs this integrity check as well as the exact certificate verifier. Matching hashes establish file consistency, not independent mathematical validation.

Maintainers must regenerate the manifest after changing public files. Stage the intended distribution first, then run from the repository root:

```bash
git ls-files -z -- ':!:reproducibility/PUBLIC_MANIFEST_SHA256.txt' | LC_ALL=C sort -z | xargs -0 sha256sum > reproducibility/PUBLIC_MANIFEST_SHA256.txt
git add reproducibility/PUBLIC_MANIFEST_SHA256.txt
```

Use the manifest from the same commit or release as the files being checked. Older releases and Git history preserve earlier publication states; a new manifest does not remove those historical copies.
