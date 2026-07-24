# 03 · Axioms

STATUS: CANDIDATE structure, working name **NEPM-0** (fourth intake,
2026-07-24). No entry has final AXIOM status (`AI_PROTOCOL.md`). Supersession
chain: (X, Φ, A) → (S, O, T, C, I) → (Δ, P, K, I) → current; the path is
preserved in git history and `notebook/`.

## Current candidate structure

> **𝓜 = (X, Φ, K, B)**

| Component | Name | Formal shape |
|---|---|---|
| X | Difference Space | the space of evolvable difference configurations, δ(t) ∈ X; typically infinite-dimensional (function spaces, probability-distribution spaces, graph state spaces). ⚠ Symbol recycled: X previously denoted the *rejected* Configuration Space — this is a different object. |
| Φ | Propagation | a flow: dδ/dt = F(δ, t) generating Φ_t : X → X with Φ_0 = Id; when the law is time-independent, the semigroup property Φ_{t+s} = Φ_t ∘ Φ_s. |
| K | Admissibility Kernel | K ⊆ 𝓕(X), the set of admissible evolution operators; the realized F must satisfy F ∈ K. May encode boundary conditions, conservation constraints, causality, locality, symmetry, maximal propagation speed, forbidden regions, and the allowed range of rule modification. F ∉ K ⟹ the evolution is rejected. A restriction on evolution *possibilities*, not a description of current state. |
| B | Balance Functional | B : X → ℝ≥0, the size of the current difference configuration (energy, variance, information, error, free energy, …), with the balance decomposition dB/dt = J_in + J_amp − J_diss. |

**Replacement of I.** The former component I (Invariant) was deleted by
counterexample: dissipative and driven systems — viscous fluids, cognition —
possess no strictly conserved invariant. B generalizes it: not *what is
conserved* but *how a quantity is produced, transferred, and dissipated*.
(Resolves OP-7; obsoletes OP-11. First deletion of a primitive by the
Counterexample Test.)

## Requirements (received first-version skeleton)

1. **Distinguishability** — δ ∈ X. Methodological, not ontological: *without
   distinguishability, no dynamical description can be built.* The stronger
   claim "Difference is ontologically prior to matter / energy / relation" is
   explicitly retracted (fourth intake, item 9), as is the earlier
   "Propagation is the world's first-class citizen" claim.
2. **Evolution** — Φ_t : X → X.
3. **Admissibility** — Φ ∈ K.
4. **Balance** — dB/dt = Injection + Redistribution − Dissipation.
5. **Objecthood** — an Object is an invariant, attracting, or metastable
   structure of Φ (see `04_definitions.md`).
6. **Complexity candidate condition** — complex behavior tends to arise near
   Amplification ∼ Dissipation, given nonlinearity, local coupling, multiple
   scales, sustained input, and finite constraints. (DISCUSSION until made
   precise; see OP-14.)

## WRITER'S NOTE — the missing fourth axiom (OP-9, sharpened)

NEPM-0's A4 (self-modification, P ↦ U(P, Δ)) appears nowhere in 𝓜. Worse:
the semigroup property assumed for Φ is *precisely* the statement that the
law does not change — it excludes self-modification by construction. As
written, 𝓜 is a classical dissipative dynamical system: it can express
**persisting**, not yet **evolving** (OP-12). Restoring U turns Φ_t into a
two-parameter process / cocycle (non-autonomous dynamics), and is a prime
candidate for where this framework's novelty must live (OP-16). The entry
"allowed range of rule modification" in K's list is the likely door.
