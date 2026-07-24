# Roadmap

## Long-term goal

Version 0.1 of **"A Minimal Axiomatic Theory of Evolving Systems"**.

The first objective is **not** correctness. It is **clarity, minimality, and
falsifiability** — a document any mathematician can read and criticize.

## Phase 0.1 — a criticizable problem statement (current)

**Do NOT add concepts. Derive the smallest possible set of primitives.**

Work items:

1. **OP-1** — can Configuration Space X be derived? If yes, X is not primitive. *(current focus)*
2. **OP-2** — can Evolution Flow Φ be derived from a Generator G? Candidate reduction (X, Φ, A) → (X, G, A) or smaller.
3. **OP-4 / P1 (well-posedness)** — define "evolving system" without presupposing the candidate primitives. See `book/02_problem.md`.
4. **OP-3 / P2 (the order)** — state the ordering in which "minimal" is measured: primitives counted how, relative to which ambient class of formalizations.
5. Populate `mappings/` far enough to run the Mapping Test on X, Φ, A.

**Exit criterion:** at least one external mathematician reads `book/` and
produces a substantive objection. An objection is success; silence is failure.

## Phase 0.2 — the attack loop

Falsify, delete, shrink. Promote only survivors. Nothing else.
