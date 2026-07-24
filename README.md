# Minimal Evolving Systems

> What is the minimal set of mathematical objects required to describe any evolving system?

**Working title of the theory:** *A Minimal Axiomatic Theory of Evolving Systems*
**Status:** v0.0 — pre-axiomatic. Nothing in this repository is established.

## The one rule

> Delete assumptions before adding concepts.

We are not trying to invent a new theory. We are trying to derive the minimum
mathematical structure that any description of an evolving system must already
contain. Every concept must survive the four tests in `AI_PROTOCOL.md` or it
does not enter the theory.

## Current state (2026-07-24)

Candidate minimal representation: **(X, Φ, A)** — Configuration Space,
Evolution Flow, Admissibility Structure. The candidate is under active attack
and is expected to shrink, not grow:

- **OP-1** — can Configuration Space X itself be derived? (current focus)
- **OP-2** — can Φ be derived from a Generator G, reducing the triple to (X, G, A) or smaller?

See `book/08_open_problems.md`.

## How to read this repository

If you are an AI (or a human) entering this project for the first time, read in
this order — nothing else is required to start working:

1. `README.md` — this file
2. `AI_PROTOCOL.md` — the epistemic contract; nothing may be written without it
3. `ROADMAP.md` — current phase and its exit criterion
4. `book/02_problem.md` — the problem statement

**The repository is the project's memory.** No conversation with any AI is
authoritative; only what is committed here counts. If a chat and the repository
disagree, the repository wins.

## Layout

| Path | Contents |
|---|---|
| `book/` | The white paper, chapter by chapter, with epistemic status labels |
| `notebook/` | Daily research log (append-only, dated) |
| `proofs/` | Formal proofs and the conjecture ledger |
| `mappings/` | Interpretations into other domains (Navier–Stokes, Transformer, RL, …) |
| `references/` | Literature to compare against before claiming novelty |

---
Created by naze.
