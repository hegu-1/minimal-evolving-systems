# Mapping: Cognition

STATUS: DISCUSSION — anchor definition added (fifth intake, 2026-07-28,
relayed by the maintainer); symbols propagated v1 → v2 (consistency fix per
the supersession chain of 2026-07-25). The representation proof is ROADMAP
item 4 and has not begun.

## Anchor definition (neutral restatement)

**Cognitive state (CANDIDATE).** For the observed process of a cognitive
agent — inputs u_t and behavior y_t — a *state representation* is a process
C_t such that the conditional law of future behavior given (C_t, future
inputs) equals the conditional law given the full history H_t and future
inputs: C_t is a **predictively sufficient statistic** of H_t. A *cognitive
state* is such a C_t that is in addition (i) **bounded**, (ii) **minimal** —
no proper reduction of C_t retains sufficiency — and (iii) **stable** under
time translation.

As received, the definition read: "the minimal internal representation
sufficient to predict the agent's future cognitive evolution and decisions
without access to its full history." The restatement makes conditions
(i)–(iii) explicit because without them the definition cannot fail (see
below).

## Classical lineage (OP-16 — read before claiming anything)

This is the standard state concept of several mature fields; no novelty
lives at this layer:

- **Minimal realization** (Kalman): which input–output behaviors admit
  finite-dimensional state realizations; minimal realizations are unique up
  to isomorphism.
- **Causal states / ε-machine** (computational mechanics,
  Crutchfield–Shalizi): "which histories compress, and what is retained"
  answered exactly — histories are equivalent iff their conditional futures
  coincide; the ε-machine is provably the minimal maximally predictive
  model; statistical complexity measures its size.
- **Predictive state representations** (reinforcement learning): state as a
  vector of verifiable predictions about future tests.
- **Mori–Zwanzig**: the exact cost of under-compression — projection onto an
  insufficient state produces a memory kernel plus a fluctuation term;
  "must consult history" = non-decaying kernel, a computable property.

## Falsifiability, sharpened

The naive criterion — "if every C must consult the full history, the
definition fails" — never triggers: C_t = H_t is always sufficient. The
falsifiable form quantifies only over *bounded, minimal, stable* C.
Processes with divergent statistical complexity exist (no finite predictively
sufficient statistic); whether a given agent's observed process admits a
bounded C is therefore measurable in principle, not rhetorical.

## Correspondence (v2)

| 𝓜 | Cognition candidate |
|---|---|
| δ ∈ X | current content state: prediction error / belief state (itself the classical compression of the observation history) |
| F ∈ K | the agent's current update law: inference style, dispositional structure |
| U | drift of the law itself: model revision, learning-to-learn, habit formation |
| Φ (derived) | the realized belief-update process along the law trajectory |
| B (instrument) | prediction-error magnitude / free-energy candidates (unexamined) |

Three consequences of reading the anchor definition inside 𝓜:

1. **Sufficiency becomes a theorem consequence, not a definition.** P-2 +
   P-4 (OP-18) state: under (E1)–(E2), locally Lipschitz U, Nagumo tangency
   and two-layer balance, the pair (δ, F) is a complete state — prediction
   needs no history. In 𝓜 the anchor definition's content is delivered by
   well-posedness.
2. **The unplowed face is the law layer.** The entire lineage above lives in
   U ≡ 0 (fixed dynamics). The question with actual room: does the *law's*
   history compress into a law-state — a sufficient statistic for F_t under
   non-trivial U? This is the same locus OP-16 already flags as candidate
   delta (ii).
3. **OP-17 translates.** Splitting C_t into "content" (δ) and "rule" (F) is
   presentation-relative: what counts as belief versus style is a declared
   split unless a canonical one exists (typing-asymmetry lead). The anchor
   definition treats C_t unsplit — it sits one level above OP-17 and
   inherits its unresolved status.

## Candidate instantiation for the proof (ROADMAP item 4)

Bayesian filtering with model revision: δ = posterior belief (content
layer), F = likelihood/dynamics model, U = hierarchical model revision.
Verify (E1)–(E2) for a concrete function-space choice; then P-2 applies, and
P-4's tangency condition asks which model revisions preserve admissibility.
A recursion worth exploiting: the belief state is already the classical
sufficient statistic at the content layer; the proof would ask whether model
revision admits the same at the law layer. Not begun.

## What this mapping does NOT establish

- No evidence for any promotion; DISCUSSION throughout (AI_PROTOCOL).
- Not established: that human or artificial cognition admits a bounded,
  minimal, stable C_t (empirical; open).
- Not established: a canonical content/law split (OP-17 open).
- Not established: novelty (OP-16 open; every result named above predates
  this file).
- Not established: that 𝓜 is the unique or preferred frame for cognition —
  C-001 v2 territory; see the ledger's predictive-minimality attack entry
  (2026-07-28), which this mapping motivated.
