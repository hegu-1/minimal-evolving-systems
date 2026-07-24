# 03 · Axioms

STATUS: **no statement in this file has AXIOM status yet.** Under
`AI_PROTOCOL.md`, AXIOM is reserved for assumptions we explicitly failed to
delete; no deletion attempt has yet been recorded as failed.

## Current candidate representation

**CANDIDATE (2026-07-24).** An evolving system is described by a triple

> **(X, Φ, A)**

| Symbol | Name |
|---|---|
| X | Configuration Space |
| Φ | Evolution Flow |
| A | Admissibility Structure |

This is not final and is expected to **shrink**:

- **OP-2** — if Φ is derivable from a Generator G, the candidate becomes (X, G, A).
- **OP-1** — if X is itself derivable, it is not primitive and the candidate shrinks further.

Promotion of any component to AXIOM requires a recorded, failed deletion
attempt (see `AI_PROTOCOL.md`, Minimality Test).
