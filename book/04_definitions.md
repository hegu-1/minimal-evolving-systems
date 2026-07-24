# 04 · Definitions

STATUS: all entries CANDIDATE unless marked; a formal definition is added one
section per term only after passing the Definition Test. The tables reflect
the third intake (NEPM-0), 2026-07-24.

## Candidate primitives — (Δ, P, K, I)

| Term | Symbol | Status | Notes |
|---|---|---|---|
| Difference | Δ | CANDIDATE — base primitive (A1) | prior to State: without Δ, no information, no change, no time |
| Propagation | P | CANDIDATE (A2) | acts on differences, not on states |
| Kernel | K | CANDIDATE (A3) | the space of admissible propagations, P ∈ K. ⚠ name collides with standard mathematical usage (null space, integral kernel, RKHS) — OP-13 |
| Invariant | I | CANDIDATE — primitivity doubted | possibly derivable from conditions on P, K (OP-7, OP-11) |
| Operator update | U | CANDIDATE (A4) — **not in the quadruple** | P ↦ U(P, Δ); placement unresolved (OP-9); possibly the definitional boundary of "evolving" (OP-12) |

## Defined (derived) objects

Former rejected-primitives are being recovered as *definitions* — the theory
working as intended.

| Term | Definition | Source |
|---|---|---|
| Object | a stable propagation pattern — a vortex is not water; a person is not their cells; an LLM is not its weights | D1 |
| Observation | the coupling that maps a difference into a propagation; not input — coupling | D2 (resolves OP-6) |
| Learning | update of propagation: U acting on P | A4 |
| Cognition | an instance, not a foundation: Δ = prediction error, P = belief update, K = long-term dispositional structure | `mappings/cognition.md` |

## Rejected as primitive

- **State / Configuration Space (X)** — rejected by A1: Difference is prior
  (settles OP-1's question against X's primitivity).
- Memory, Intelligence, Complexity — still expected to be derived; unplaced.
- **Difference** — *reinstated* as the base primitive (A1; resolves OP-5).

## Superseded candidates

- **(X, Φ, A)** — first intake; superseded by NEPM-0 (third intake).
- **(S, O, T, C, I)** — second intake; S, O, T, C absorbed as Δ-structure,
  coupling (D2), P, and K respectively; I carried forward under doubt (OP-7).
