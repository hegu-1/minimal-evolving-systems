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

## Current state (2026-07-24, fourth intake)

Candidate structure: **𝓜 = (X, Φ, K, B)** — Difference Space, Propagation
(flow / semigroup), Admissibility Kernel, Balance Functional. The former
Invariant component was deleted by counterexample (dissipative systems have
none) and replaced by B with the balance decomposition
dB/dt = injection + redistribution − dissipation. First proved result:
**P-1** (bounded absorption under dominant dissipation, `proofs/`). The
Navier–Stokes balance layer maps exactly (`mappings/navier_stokes.md`).

Live front: **OP-14** — when does the absorbing region *not* collapse to a
single equilibrium but sustain persistent complex structure? — and **OP-9** —
self-modification (A4) is still outside 𝓜, whose semigroup assumption
expresses persistence, not evolution. Novelty scoping is gated by OP-16.

See `book/03_axioms.md` and `book/08_open_problems.md`.

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
