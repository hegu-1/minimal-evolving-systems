# 04 · Definitions

STATUS: entries CANDIDATE unless marked. Tables reflect v2 (2026-07-25),
𝓜 = (X, K, U).

## Candidate primitives — three objects

| Term | Symbol | Status | Notes |
|---|---|---|---|
| Difference Space | X | CANDIDATE — formalizing | space of evolvable difference configurations; symbol recycled from the rejected Configuration Space — different object |
| Admissibility Kernel | K | CANDIDATE | K ⊆ 𝓕(X): which laws may exist and within which the law may move; the hard constraint on self-modification. Naming: OP-13 |
| Law Update | U | CANDIDATE (v2 — **now housed**) | U : K × X → TK, K-preserving; U ≡ 0 allowed. Resolves OP-9 |

The current law F ∈ K and the difference configuration δ ∈ X are *variables*
(initial data), not primitives.

## Derived objects

| Term | Definition | Source |
|---|---|---|
| Propagation Φ | the solution operator Φ_{t,s} obtained by integrating the coupled layers; process/cocycle in general, semigroup iff U ≡ 0 | v2 (completes OP-2's direction: the generator is fundamental) |
| Object | a structure of the derived Φ retaining identifiability: invariant set (Φ maps O to O), attractor, or metastable set (τ_internal ≪ τ_lifetime) | D1, rigorized fourth intake |
| Observation | the coupling that maps a difference into a propagation | D2 |
| Learning | non-trivial action of U on the law — now *inside* the structure | A4 → v2 |
| Static / Evolving | D3: given a declared (X, K) split, static ⟺ U ≡ 0 along the trajectory; evolving ⟺ U non-trivial. Presentation-relative — see OP-17 | v2 |
| Cognition | an instance, not a foundation | `mappings/cognition.md` |

## Instruments (method, not structure)

| Term | Definition | Notes |
|---|---|---|
| Balance Functional B | any B : X → ℝ≥0 with the decomposition dB/dt = J_in + J_amp + J_redist − J_diss (J_redist B-neutral) | demoted from v1 component to instrument — resolves OP-15; P-1 is a B-method result on the static class |

## Deleted primitives

- **Invariant (I)** — deleted by counterexample (fourth intake); its
  successor B was then moved out of the structure entirely (v2).
- **Propagation-as-primitive (P / Φ)** — derived in v2 from (K, U) + initial
  data.
- **State / Configuration Space** — questioned from the first intake (OP-1);
  rejected by A1 (third intake).
- Memory, Intelligence, Complexity — still expected to be derived; unplaced.
