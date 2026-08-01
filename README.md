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

## Current state (2026-08-01, v2)

Candidate structure: **𝓜 = (X, K, U)** — Difference Space, Admissibility
Kernel, Law Update — a **two-layer system**: the current law F ∈ K
propagates the difference (dδ/dt = F(δ)) while the law itself is updated
within K (dF/dt = U(F, δ)). Propagation Φ is now *derived* (a process;
semigroup iff U ≡ 0), and the Balance Functional B is an *instrument* of the
method, not a component. **D3** defines the split: static (U ≡ 0 — where the
proved P-1 lives) vs evolving (U non-trivial) — presentation-relative, see
the suspension objection (OP-17). C-001 restated in falsifiable-leaning form
(v2, `proofs/conjectures.md`).

Live front: **OP-17** (can the state/law split be made canonical?) and
**OP-14** (now bracketed by P-5/P-8: in the hyperbolic regime the gate is
open a.e. iff no equilibrium is a sink; the residue is non-hyperbolic
equilibria plus classification of the forced non-trivial set).
**OP-18** is resolved modulo maintainer promotion: P-2 proves local
well-posedness, and P-4 proves K-invariance plus global existence under
two-layer balance estimates. Novelty scoping remains gated by OP-16.

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
Created by naze. Licensed under CC BY 4.0 (`LICENSE`).
