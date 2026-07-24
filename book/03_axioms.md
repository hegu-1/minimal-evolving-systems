# 03 · Axioms

STATUS: CANDIDATE axiom system, working name **NEPM-0** (third intake,
2026-07-24; name introduced by the maintainer). No entry has final AXIOM
status — under `AI_PROTOCOL.md` that requires a recorded, failed deletion
attempt. This set supersedes the earlier candidate (X, Φ, A); the path is
preserved in git history and `notebook/2026-07-24.md`.

**Discipline:** write as if in 1850 — after Newton, before Einstein, no modern
theory available, only axioms. An axiom that derives nothing is deleted.

## A1 — Distinguishability

There exist at least two distinguishable states: a ≠ b.

Not "there exists a State": **Difference is prior to State.** Without
difference there is no information, no change, and no time.

## A2 — Propagation

Difference propagates: there is a propagation operator P acting on
differences, Δ ↦ P(Δ). This is difference-update, not state-update. Motion
begins here.

⚠ OP-10: the received form Δ(t+1) = P(Δ(t)) indexes by a global discrete t,
which presupposes time — in tension with A1's own justification. The
t-notation is therefore not part of the axiom as recorded here.

## A3 — Constrainedness

Propagation is constrained: there exists K with P ∈ K. Unconstrained
propagation diverges immediately. K is not a rule set, not memory, not an
object: **K is the space of admissible propagations.** (Absorbs OP-8.)

## A4 — Self-modification

Propagation can change propagation: P ↦ U(P, Δ) — an operator update, not a
state update. Learning lives here: gradients update parameters, and
parameters define the operator.

WRITER'S NOTE (consistency): A4 may not be an axiom about all systems but the
*definitional boundary of the evolving class* — see OP-12, which would make it
a candidate resolution of OP-4.

## D1 — Object *(definition, not axiom)*

**Object := a stable propagation pattern.** A vortex is not water; a person is
not their cells; an LLM is not its weights.

## D2 — Observation *(definition, not axiom)*

**Observation := the coupling that maps a difference into a propagation.**
Not input — coupling. (Resolves OP-6: Observation is defined, not primitive.)

*Writer's reclassification note: the third intake presented six axioms; items
5–6 introduce no assumptions and are recorded here as definitions, reducing
the axiom count to four. Reversible; flagged for maintainer review.*

## Candidate primitive set

> **(Δ, P, K, I)** — Difference, Propagation, Kernel, Invariant

Conjecture C-001 (`proofs/conjectures.md`): every system capable of long-term
persistence and sustained evolution is representable as such a quadruple —
currently not falsifiable as stated; see its attack log.

Known gaps in the compression itself:
- **OP-9** — U appears in A4 but in no component of the quadruple.
- **OP-11** — theorem target 5 (`ROADMAP.md`) would, if proved, *derive* I,
  shrinking the candidate to (Δ, P, K).
