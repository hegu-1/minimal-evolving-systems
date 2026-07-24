# Roadmap

## Long-term goal

Version 0.1 of **"A Minimal Axiomatic Theory of Evolving Systems"**.

The first objective is **not** correctness. It is **clarity, minimality, and
falsifiability** — a document any mathematician can read and criticize.

## Phase 0.1 — from framework to mathematics (current)

**Concept invention is over for now. The work is formalization.**
(Reframed 2026-07-24, third intake, per the maintainer's five-point program.)

Work items:

1. Rigorously define **(Δ, P, K, I)** with no domain vocabulary — no
   "cognition", "AI", "fluid". Upstream blockers: OP-9 (where U lives),
   OP-10 (time), OP-13 (naming of K), plus OP-3/OP-4 (minimality order,
   non-circular "evolving"; OP-12 is a candidate route).
2. Prove Navier–Stokes is representable as the quadruple (`mappings/navier_stokes.md`).
3. Prove a Transformer is representable (`mappings/transformer.md`).
4. Prove a cognitive update model — predictive coding, Bayesian update, or
   reinforcement learning — is representable (`mappings/cognition.md`, `mappings/rl.md`).
5. Prove **at least one non-trivial theorem**: e.g., under conditions on P
   and K, stable propagation structures (Objects) necessarily form; or a
   scale cascade necessarily occurs; or an invariant necessarily exists
   (which would derive I — OP-11).

Gate on items 2–4: conjecture C-001 must first be strengthened to a
falsifiable statement (see its attack log in `proofs/conjectures.md`);
otherwise representation proofs are vacuous.

**Exit criterion:** at least one external mathematician reads `book/` and
produces a substantive objection. An objection is success; silence is failure.

## Phase 0.2 — the attack loop

Falsify, delete, shrink. Promote only survivors. Nothing else.
