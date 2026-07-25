# 08 · Open Problems

STATUS: normative ledger. IDs are append-only. Closing an OP requires either a
proof in `proofs/` or a recorded argument in `notebook/` promoted by the
maintainer. "RESOLVED" = closure argument recorded, maintainer promotion
pending.

| ID | Problem | Status |
|---|---|---|
| OP-1 | Can Configuration Space X be derived? | RESOLVED (third intake): X-as-state is not primitive — Difference is prior (A1). Pending promotion. (Symbol note: "X" here is the former Configuration Space; 𝓜's X is the Difference Space — recycled symbol, see `03`/`04`.) |
| OP-2 | Can Evolution Flow Φ be derived from a Generator G? | SUPERSEDED: the generator role is filled by F (fourth intake) and the update U (A4). Residual absorbed into OP-9. |
| OP-3 | State the minimality order: relative to which ambient class of formalizations, ordered how? (P2) | OPEN — blocks any minimality claim; now includes the minimality of the time primitive (see OP-10) |
| OP-4 | Define "evolving system" non-circularly. (P1) | OPEN — candidate route via OP-12 |
| OP-5 | Is Difference primitive? | RESOLVED (A1): reinstated as the base primitive, in methodological form (fourth intake, item 9). Pending promotion. |
| OP-6 | Is Observation first-class? | RESOLVED (D2): defined as coupling, not primitive. Pending promotion. |
| OP-7 | Is Invariant primitive, or derivable? | RESOLVED (fourth intake), in an unexpected direction: I deleted by counterexample — dissipative / driven systems have no strict invariant — and replaced by the Balance Functional B. Pending promotion. |
| OP-8 | Define A as "the space of admissible transformations". | ABSORBED into A3/K: the Admissibility Kernel is that space. |
| OP-9 | **Self-modification is not in the structure.** | RESOLVED (v2, 2026-07-25): U housed as a first-class component — 𝓜 = (X, K, U), two coupled layers, Φ derived as a process (semigroup iff U ≡ 0). Pending promotion. Residual formal work → OP-18. |
| OP-10 | **Time.** | PARTIALLY RESOLVED: the fourth intake commits to continuous time as a primitive parameter (flow / semigroup), and retracts the ontological "no difference → no time" argument. Whether time could instead emerge from propagation order remains unexplored; the minimality of the time primitive folds into OP-3. |
| OP-11 | Would theorem target 5 derive I? | CLOSED as obsolete: I is no longer in the candidate (OP-7). Its successor question is OP-15. |
| OP-12 | Is A4 an axiom about all systems, or the *definition* of the evolving class? | RESOLVED (v2): the latter — D3 defines static / evolving via U. Candidate resolution of OP-4, conditional on OP-17. Pending promotion. |
| OP-13 | Naming of K. | OPEN, softened: fourth intake names it "Admissibility Kernel", reducing collision risk (null space / integral kernel / RKHS). Final naming = maintainer. |
| OP-14 | **The stability → complexity gate** (maintainer-boxed, fourth intake): under what minimal conditions does the bounded absorbing region guaranteed by P-1 *not* collapse to a single equilibrium, but sustain persistent complex structure? | OPEN — current focus |
| OP-15 | **Is B structure or instrument?** | RESOLVED (v2): instrument — B moved out of the structure into the method; non-canonicity of v1 removed; C-001 restated (v2 in `proofs/conjectures.md`). Pending promotion. |
| OP-16 | **Novelty gate.** As written, the static class + P-1 reconstruct classical dissipative dynamical systems theory (see `references/bibliography.md`). Locate the delta: candidate loci are (i) K as a first-class object, (ii) the U-layer / two-layer coupling (v2's core; compare against adaptive-dynamics, meta-learning, and non-autonomous systems literature before claiming it), (iii) the cross-domain representation discipline (C-001 v2). No external novelty claim before this is answered. | OPEN — blocks any public claim |
| OP-17 | **The suspension objection.** Any evolving system repackages as a static one on X × K with state (δ, F). D3 is therefore presentation-relative. Does a *canonical* state/law split exist (candidate lead: the typing asymmetry — the law factor consists of maps acting on the state factor), or must "evolving" remain relative to a declared split? | OPEN — deepest problem of the definition layer |
| OP-18 | **Well-posedness of the coupled layers.** Conditions on K and U under which (δ_t, F_t) exists and is unique (and Φ_{t,s} is well-defined). Prerequisite to any theorem about the evolving class. | OPEN |
