# Roadmap

## Long-term goal

Version 0.1 of **"A Minimal Axiomatic Theory of Evolving Systems"**.

The first objective is **not** correctness. It is **clarity, minimality, and
falsifiability** — a document any mathematician can read and criticize.

## Phase 0.1 — from framework to mathematics (current)

**Concept invention is over for now. The work is formalization.**
(Reframed 2026-07-24 per the maintainer's five-point program, third intake;
structure updated to 𝓜 after the fourth.)

Work items:

1. Rigorously define **𝓜 = (X, K, U)** (v2, two-layer structure) with no
   domain vocabulary — no "cognition", "AI", "fluid". Upstream blockers:
   OP-17 (canonical state/law split), OP-18 (well-posedness of the coupled
   layers), OP-10 (time), plus OP-3 (minimality order / ambient class 𝒞,
   which C-001 v2 quantifies over). K's final name: OP-13 (maintainer call,
   non-blocking).
2. Prove Navier–Stokes is representable as the quadruple (`mappings/navier_stokes.md`).
3. Prove a Transformer is representable (`mappings/transformer.md`).
4. Prove a cognitive update model — predictive coding, Bayesian update, or
   reinforcement learning — is representable (`mappings/cognition.md`, `mappings/rl.md`).
5. Prove **at least one non-trivial theorem**. Status: P-1 (bounded
   absorption, `proofs/p001_bounded_absorption.md`) delivers the first proved
   proposition — but it is a classical calibration result, not the novelty
   payload. The live theorem target is **OP-14**: minimal conditions under
   which the absorbing region sustains persistent complex structure rather
   than collapsing to equilibrium.

Gates:
- Items 2–4: conjecture C-001 must first be strengthened to a falsifiable
  statement (see its attack log), and OP-15 (which B?) settled; otherwise
  representation proofs are vacuous.
- Any external claim: OP-16 (novelty gate) — read the classical dissipative
  dynamical systems literature (`references/bibliography.md`) and state the
  delta explicitly.

**Exit criterion:** at least one external mathematician reads `book/` and
produces a substantive objection. An objection is success; silence is failure.

## Phase 0.2 — the attack loop

Falsify, delete, shrink. Promote only survivors. Nothing else.
