# v1.0.1 - Public distribution maintenance

**Release date:** 2026-10-28

**Author:** Ricardo Vera

**Affiliation:** CIEC LAB

**Scientific status:** preprint; external mathematical reproduction and journal peer review remain open.

## Scope

This release updates the public distribution and documentation. The preprint remains **v1.0 (2026-09-26)**. The PDF, proof files, public certificate verifier and witness corpus are unchanged from v1.0.0. The frozen claim remains **h(6) ≥ 25**; no stronger bound or new validation status is asserted.

## Changes

- Replace the historical internal-package manifest with `reproducibility/PUBLIC_MANIFEST_SHA256.txt`, covering the actual public distribution except the manifest itself.
- Verify those hashes in CI before running the exact certificate checker.
- Exclude internal role names from the current distribution and document the limits of historical cleanup.
- Repair the Spanish README and add direct links to the current release and public manifest.
- Update repository citation metadata to distribution version 1.0.1.

## Files and reproduction

The release attaches the unchanged preprint v1.0 PDF, the public manifest and a source archive containing the current snapshot without Git history.

After extracting the source archive, run from its root:

```bash
sha256sum --strict --check reproducibility/PUBLIC_MANIFEST_SHA256.txt
python certificate/verify_h6_lower25_cleanroom.py certificate/h6_exact_profile_witnesses.txt
```

Every manifest entry must report `OK`; the verifier must emit `INTERNAL_COMPUTATIONAL_VERDICT=PASS`. The verifier also reports the external mathematical dependency required by the proof. Hash consistency and a successful rerun are not journal peer review or external mathematical reproduction.

## Earlier publication states

v1.0.1 supersedes v1.0.0 for the current public distribution. Earlier tags, release archives and Git history remain accessible and can contain earlier disclosures. This maintenance release does not retract the mathematical claim or erase historical copies.

A Zenodo DOI remains pending; none is asserted by this release.
