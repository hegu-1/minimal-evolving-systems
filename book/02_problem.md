# 02 · Problem Statement

STATUS: DISCUSSION — hardening toward a formal statement. This chapter is the
core deliverable of Phase 0.1.

## The question

> What is the minimal set of mathematical objects required to describe any
> system capable of sustained evolution?

We are not inventing a new theory. We are deriving the minimum structure that
any description of an evolving system must already contain.

## Two sub-problems that make the question well-posed

As stated, the question is not yet mathematically well-posed. Making it
well-posed **is** the current work — these are open problems (OP-3, OP-4), not
footnotes.

**P1 — Non-circularity.** "Capable of sustained evolution" must be defined
without smuggling in the candidate primitives. If "evolving" is defined in
terms of a space and a flow, then (space, flow) is minimal by construction and
the result is empty. The definition of the *explanandum* must be independent of
the *explanans*.

*Status update (fourth intake, 2026-07-24): this warning is now live. The
fourth-intake candidate (X, Φ, K, B) is precisely a space plus a flow (plus
constraints and bookkeeping). Unless "evolving" is defined independently —
the candidate route is OP-12: evolving :⟺ the propagation law is
non-trivially self-modifying — C-001 risks being true by construction for the
*persisting* class while remaining silent about the *evolving* one (see
OP-9).*

*Second update (v2, 2026-07-25): the route was taken — D3 now defines
static / evolving via the law-update U in the two-layer structure
𝓜 = (X, K, U). The residual obstruction is the suspension objection: the
definition is relative to a declared state/law split (OP-17).*

**P2 — The minimality order.** "Minimal" is only meaningful relative to
(a) an ambient class of admissible formalizations, and
(b) an order on that class — number of primitives? number of axioms?
interpretability of one formalization inside another?
A minimality claim without a declared order is rhetoric, not mathematics.

**M1 — Meta-risk.** The ambient class in P2 is itself a modeling choice. Any
minimality result is relative to that choice and must say so explicitly.

## Non-goals

- Taking memory, intelligence, cognition, learning, objects, complexity, or
  observation as primitives — all rejected; see `book/04_definitions.md`. They
  are expected to *emerge* from a smaller structure, or be shown not to.
- Correctness of a grand theory. Phase 0.1's only deliverable is a problem
  statement a mathematician considers precise enough to attack.
