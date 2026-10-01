# H6 — Universal Quadratic Image Theorem

> **CIEC LAB mathematical discovery — a computer-assisted theorem that pushes guaranteed quadratic image containment beyond the apparent 22-dimensional interpolation ceiling.**

## Preprint v1.0

**Ricardo Vera — CIEC LAB**

**Universal Quadratic Image Containment over F₂: A Computer-Assisted Proof that h(6) ≥ 25**

[Read the preprint PDF](paper/Vera_2026_Universal_Quadratic_Image_Containment_h6_ge25_Preprint_v1.pdf)

Publication status: **preprint**. The result has passed internal clean-room hardening and a second internal checker. External third-party mathematical reproduction and journal peer review are still open.

---

## 22 apparent degrees of freedom. 24 universally guaranteed targets.

Let

**q : F₂⁶ → F₂¹²**

range over maps whose 12 coordinate functions have algebraic degree at most 2.

H6 proves:

> **Every subset H ⊆ F₂¹² with |H| ≤ 24 is contained in the image of at least one such quadratic map.**

Equivalently,

**h(6) ≥ 25.**

This is a **positive computer-assisted theorem**, not a failed search, heuristic signal or numerical guess.

---

## Why this result is surprising

The scalar space of Boolean polynomials of degree at most 2 in six variables has dimension

**1 + 6 + C(6,2) = 22.**

If preimages are fixed in advance, 22 is the natural interpolation barrier.

H6 gets to **24 arbitrary targets** without creating two new coefficients.

The mechanism is different:

> **adaptive placement of unavoidable dependency relations inside dependency relations the target set already possesses.**

For 24 selected evaluation points, two relations are unavoidable because the evaluation space has rank 22.  
For 24 targets in F₂¹², the target kernel has dimension at least 12.

The proof shows that the preimages can be chosen so that the two unavoidable evaluation relations are legal target relations.

**The barrier is not broken by adding capacity. It is beaten by placing dependencies where they do not hurt.**

See [Why 22 becomes 24](proof/04_TWO_POINT_EXCESS_EXPLANATION.md).

---

## Executive signal

This repository is not valuable to CIEC LAB because every executive needs a theorem about F₂.

It is valuable because it demonstrates a harder capability:

> **CIEC LAB can enter an unresolved technical problem, build new mathematical representations, construct a proof architecture, generate exact certificates, attack its own result adversarially and exit with an auditable positive result.**

That capability transfers to high-consequence work such as:

- frontier R&D;
- technical due diligence;
- algorithm and model validation;
- formal and computational verification;
- scientific hypothesis attack;
- evidence architecture;
- decision intelligence under technical uncertainty.

**The commercial product is not “more analysis.” It is decision-grade knowledge when a confident technical error is expensive.**

See [Executive Signal](report/EXECUTIVE_SIGNAL.md).

---

## What was actually proved

The theorem is equivalent to an adaptive evaluation-geometry statement.

Define the degree-≤2 evaluation embedding

**φ₂ : F₂⁶ → F₂²².**

For every **t ≤ 24** and every injective target matrix **M ∈ F₂^(12×t)**, there exist **t** distinct points **X ⊂ F₂⁶** such that, for the evaluation matrix **V_X**,

**ker(V_X) ⊆ ker(M).**

Equivalently, there exists a linear map **T : F₂²² → F₂¹²** satisfying

**M = T V_X.**

Full statement: [proof/02_THEOREM_STATEMENT.md](proof/02_THEOREM_STATEMENT.md)  
Full proof: [proof/03_PROOF_FROM_FIRST_PRINCIPLES.md](proof/03_PROOF_FROM_FIRST_PRINCIPLES.md)

---

## Proof architecture

The proof combines human mathematics with finite exact certification:

| Layer | Public result |
|---|---|
| Boolean polynomial / evaluation equivalence | Human proof |
| Target-kernel reduction | Human proof |
| Dangerous 2D dependency profiles | **46 exact profiles** |
| Exact-kernel realizations | **45 certified witness profiles** |
| Unique exceptional profile | **(12,12,24)** |
| Delsarte/Krawtchouk closure | **9 exact rational certificates**, all **>640** |
| Large sum-free structure | Published theorem |
| Safe-weight code escape route | **0 MacWilliams survivors** |
| All-one exceptional branch | Closed separately |
| Adversarial attack suite | No internal counterexample found |

The proof-authoritative arithmetic is integer or rational. No timeout, random search, missing model or floating-point comparison is used as proof of impossibility.

---

## Reproduce the public certificate

The public clean-room verifier uses the Python standard library.

```bash
python certificate/verify_h6_lower25_cleanroom.py certificate/h6_exact_profile_witnesses.txt
```

Expected terminal verdict:

```text
INTERNAL_COMPUTATIONAL_VERDICT=PASS
```

GitHub Actions runs the same verification on repository changes.

See [Reproduction](reproducibility/REPRODUCE.md).

---

## Adversarial validation

The frozen proof was attacked for:

- off-by-one errors;
- invalid target translation;
- rank and minimum-distance assumptions;
- missing 2D profiles;
- contained-kernel vs exact-kernel confusion;
- coordinate-equivalence mistakes;
- Delsarte sign/arithmetic errors;
- misuse of the strict sum-free threshold;
- invalid coset-to-hyperplane inference;
- MacWilliams escape routes;
- all-one exceptional cases;
- circular use of the theorem itself.

No attack produced a counterexample or unresolved bridge within the frozen scope.

See [Adversarial Attacks](proof/07_ADVERSARIAL_ATTACKS.md).

---

## Research status

**Mathematical status:** `CONFIRMED_WITHIN_SCOPE` inside the frozen proof/certificate chain.

**Targeted prior-art status:** no equivalent statement for **h(6) ≥ 25** was located in the dedicated search across quadratic maps, vectorial Boolean functions, Reed–Muller/interpolation language and related formulations.

This repository therefore presents H6 as a **CIEC LAB mathematical discovery and computer-assisted theorem**.

It does **not** claim:

- an exhaustive first-in-history priority certification;
- **h(6) = 25**;
- **h(6) ≥ 26**;
- a general theorem for every **n**;
- an immediate engineering application.

See [Prior-Art & Claim Boundary](docs/PRIOR_ART_STATUS.md) and [Status](STATUS.md).

---

## Why the next question matters

For general **n**, the scalar quadratic space has dimension

**Dₙ = 1 + n + C(n,2).**

For **n = 6**, **D₆ = 22**, yet universal containment reaches at least **24 = D₆ + 2**.

The next research program is not “run the same brute force at larger n.”

It is:

> **Is adaptive dependency matching a general phenomenon, and when can universal interpolation exceed the raw evaluation dimension?**

That investigation is deliberately separated from this repository so the H6 theorem remains frozen and auditable.

---

## Public evidence. Private machinery.

This repository exposes enough material to inspect the theorem, proof, certificate structure, witness corpus, public verifier, limitations and claim boundary.

CIEC LAB's internal research operating architecture remains proprietary.

> **Public evidence. Private machinery.**

See [Public Disclosure Boundary](PUBLIC_DISCLOSURE_BOUNDARY.md).

---

## Repository map

- [Preprint v1.0 PDF](paper/Vera_2026_Universal_Quadratic_Image_Containment_h6_ge25_Preprint_v1.pdf)
- [Release notes v1.0.0](RELEASE_NOTES_v1.0.0.md)
- [Zenodo deposit metadata](ZENODO_DEPOSIT_METADATA.md)
- [Plain-language explanation](docs/PLAIN_LANGUAGE.md)
- [Theorem statement](proof/02_THEOREM_STATEMENT.md)
- [Evaluation equivalence](proof/01_RM2_EVALUATION_EQUIVALENCE.md)
- [Proof from first principles](proof/03_PROOF_FROM_FIRST_PRINCIPLES.md)
- [Why 22 becomes 24](proof/04_TWO_POINT_EXCESS_EXPLANATION.md)
- [Certificate architecture](proof/05_CERTIFICATE_ARCHITECTURE.md)
- [Independent internal verification](proof/06_INDEPENDENT_VERIFICATION.md)
- [Adversarial attacks](proof/07_ADVERSARIAL_ATTACKS.md)
- [External mathematical dependency](proof/08_EXTERNAL_DEPENDENCIES.md)
- [Residual risk](proof/09_RESIDUAL_RISK.md)
- [Public verifier](certificate/verify_h6_lower25_cleanroom.py)
- [45 exact-kernel witnesses](certificate/h6_exact_profile_witnesses.txt)
- [Reproduction instructions](reproducibility/REPRODUCE.md)

---

## From public evidence to a real decision

If your organization has a technical claim, model, R&D hypothesis, vendor assertion or high-consequence decision that should survive adversarial review before commitment, start with one bounded object.

[**CIEC LAB — Decision Audit Sprint →**](https://github.com/RicardoVera-Lab/RicardoVera-Lab/blob/main/DECISION_AUDIT_SPRINT.md)

**Contact:** richardvera084@gmail.com  
**Suggested subject:** CIEC LAB — Decision Audit

> **Bring the claim before you bet capital, architecture or reputation on it.**

# CIEC LAB

### Strategic Research · Decision Intelligence · High-Consequence R&D

> **We attack uncertainty before it becomes capital loss.**

**Research. Break. Prove. Verify. Decide.**
