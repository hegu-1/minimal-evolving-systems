# 03 · Axioms

STATUS: CANDIDATE structure, working name **NEPM-0** (v2, 2026-07-25;
maintainer-directed step). No entry has final AXIOM status
(`AI_PROTOCOL.md`). Supersession chain: (X, Φ, A) → (S, O, T, C, I) →
(Δ, P, K, I) → (X, Φ, K, B) → **current**; the path is preserved in git
history and `notebook/`.

## Candidate structure v2 — the two-layer system

> **𝓜 = (X, K, U)** — three objects.

Let 𝓕(X) be a space of admissible generators (evolution laws) on X, and
K ⊆ 𝓕(X). A configuration of the full system is a pair

  (δ, F) ∈ X × K.

**Two coupled layers:**

- *Difference layer:* dδ/dt = F(δ) — the current law propagates the
  difference configuration.
- *Law layer:* dF/dt = U(F, δ) — the law itself is updated in response to
  the difference configuration, with U **K-preserving**: the law never
  leaves admissibility. K is the hard constraint on self-modification.

| Component | Name | Role |
|---|---|---|
| X | Difference Space | space of evolvable difference configurations, δ ∈ X (typically infinite-dimensional) |
| K | Admissibility Kernel | K ⊆ 𝓕(X): which laws may exist, and within which the law may move |
| U | Law Update | U : K × X → TK, the self-modification field; U ≡ 0 is allowed |

**Φ is derived, not primitive.** Integrating the coupled layers yields the
solution operator Φ_{t,s} : X → X (evolve from time s to t along the
*realized* law trajectory — see P-2, remark R2: Φ is trajectory-relative,
not intrinsic), satisfying Φ_{s,s} = Id and the process (cocycle) property
Φ_{t,r} = Φ_{t,s} ∘ Φ_{s,r}. If U ≡ 0, then F_t ≡ F₀ and Φ_{t,s} = Φ_{t−s}:
the semigroup — v1's Φ — is recovered exactly. This completes the direction
of OP-2: the generator, not the flow, is fundamental. Well-posedness under
Lipschitz hypotheses: P-2 (`proofs/`).

**B is an instrument, not a component.** For any chosen balance functional
B : X → ℝ≥0, the balance decomposition
dB/dt = J_in + J_amp + J_redist − J_diss (J_redist B-neutral) and results
like P-1 apply to the difference layer. Since one system admits many such
functionals, B belongs to the *method*, not the structure. (Resolves OP-15
in the instrument direction; removes the non-canonicity of v1.)

## D3 — Static and evolving *(definition, not axiom)*

Given a declared split (X, K) of a system's description into difference and
law:

- the system is **static** if U ≡ 0 along its trajectory — the law never
  changes; classical (autonomous, dissipative) dynamics; where P-1 lives;
- the system is **evolving** if U is non-trivial — the law itself moves,
  within K.

This is the candidate resolution of OP-4 via OP-12: *evolving* is defined by
self-modification of the law, not by any property of the difference layer.

⚠ **The suspension objection (OP-17).** Any evolving system can be
repackaged as a static one on the enlarged space X × K with state (δ, F) and
constant law F′(δ, F) = (F(δ), U(F, δ)). D3 is therefore
*presentation-relative*: it classifies a system **given** a declared
state/law split. Whether a canonical split exists — note the intrinsic
typing asymmetry: the second factor consists of maps acting on the first —
is OP-17, currently the deepest open problem of the definition layer. The
working stance is the methodological one (consistent with the fourth
intake's retreat): declare the split, then classify.

**Scope note.** Second-order self-modification — K itself changing
("institutions", "revolutions" from the second-intake meta-tower) — is
deliberately excluded at this stage: first-order U suffices for the learning
class. Revisit only if a concrete theorem demands it.

## Requirements (v2)

1. **Distinguishability** — δ ∈ X. Methodological: without
   distinguishability, no dynamical description can be built.
2. **Admissibility** — F ∈ K at all times; U is K-preserving.
3. **Self-modification** — the law layer dF/dt = U(F, δ) is part of the
   structure; U ≡ 0 is the static specialization.
4. **Balance (method)** — B-analysis applies to the difference layer;
   see `proofs/p001_bounded_absorption.md`.
5. **Objecthood** — an Object is an invariant, attracting, or metastable
   structure of the derived Φ (see `04_definitions.md`).
6. **Complexity candidate condition** — complex behavior tends to arise
   near Amplification ∼ Dissipation (see OP-14; DISCUSSION until precise).

## v1 as specialization

v1's 𝓜 = (X, Φ, K, B) is not discarded: it is the **static specialization**
(U ≡ 0, Φ a semigroup) together with one chosen instrument B. Everything
proved there (P-1) transfers to v2's static class unchanged.

## Open gaps of v2

- **OP-17** — the suspension objection: can the state/law split be made
  canonical?
- **OP-18** — well-posedness of the coupled layers: conditions on K and U
  for existence / uniqueness of (δ_t, F_t). Prerequisite to any theorem
  about the evolving class.
- **OP-10** — time remains an explicit primitive parameter (unchanged by
  v2).
