# v1.0.0 — H6 Lower-Bound Public Research Release

**Release date:** 2026-09-26  
**Author:** Ricardo Vera  
**Affiliation:** CIEC LAB  
**Status:** preprint / public reproducibility release

## Frozen mathematical claim

For every set \(H\subseteq \mathbb F_2^{12}\) with \(|H|\le 24\), there exists a coordinatewise algebraic-degree-\(\le 2\) map

\[
q:\mathbb F_2^6\to \mathbb F_2^{12}
\]

whose image contains \(H\). Consequently,

\[
h(6)\ge 25.
\]

This release does **not** claim \(h(6)=25\), \(h(6)\ge 26\), a general formula for \(h(n)\), journal peer review, external third-party reproduction, or absolute historical priority.

## Included in this release

- Preprint v1.0 PDF.
- Human-readable proof architecture.
- Public clean-room exact verifier.
- Exact-kernel witness corpus.
- 46-profile dangerous-weight census.
- 45 exact-kernel witness pairs.
- Nine exact rational Delsarte/Krawtchouk certificate checks.
- Exact MacWilliams feasibility closure.
- All-one exceptional branch.
- Reproducibility instructions and public CI workflow.

## Reproduction

```bash
python certificate/verify_h6_lower25_cleanroom.py certificate/h6_exact_profile_witnesses.txt
```

The repository also documents a second internal checker used during publication hardening. Internal redundancy is not presented as external independent reproduction.

## Prior-art boundary

A targeted search did not locate an equivalent published theorem for the universal <=24 containment claim. This is not an exhaustive historical-priority certification.

## Public paper

`paper/Vera_2026_Universal_Quadratic_Image_Containment_h6_ge25_Preprint_v1.pdf`

## Citation

Use `CITATION.cff` for repository citation. A Zenodo DOI will be added after the first archival deposit is published.
