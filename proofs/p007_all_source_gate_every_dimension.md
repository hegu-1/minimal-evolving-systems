# P-7 · All-source equilibria open the gate in every finite dimension

STATUS: PROPOSITION — complete proof below. Writer, 2026-08-01. Settles the
reframed OP-14 gate (open/closed) under hypothesis (R) in every finite
dimension, and **corrects the "n ≥ 3 is the hard core" framing of P-6/notebook
2026-07-29**: opening the gate is not dimension-hard; only the *structure* of
the attracting set is.

## Setting

Let X = ℝⁿ (n ≥ 1) and dδ/dt = F(δ) with F of class C¹. Let C = C_c =
{½‖δ‖² ≤ c}, c > γ/(2(α−β)), be an absorbing ball of P-1 — compact, convex,
positively invariant (P-3(b)). Write E = {δ ∈ C : F(δ) = 0} (nonempty by
P-3(a)). Gate terminology is that of P-5: the reframed OP-14 gate is *open* on
C iff some x ∈ C has ω(x) ⊄ E.

## Hypothesis

- **(R) All equilibria repel.** Every p ∈ E is a source:
  spec(DF(p)) ⊂ {Re > 0}. (As in P-6; each such p is hyperbolic, hence
  isolated, so E = {p₁, …, p_m} is finite.)

## Statement

Under (R):

1. For every x ∈ C \ E, the ω-limit set ω(x) is a **non-trivial** compact
   connected invariant set with ω(x) ⊄ E. Hence the gate is **open** on C in
   every finite dimension n ≥ 1.
2. Consequently the global attractor A := ⋂_{t≥0} Φ_t(C) satisfies A ⊋ E and
   attracts the neighbourhood C — a non-trivial invariant set attracts.

The Poincaré–Bendixson machinery of P-6 is therefore not needed to *open* the
gate; it is needed only for the stronger planar conclusion that the attracting
set is a *periodic orbit*.

## Proof

**Lemma (a source has trivial stable set).** For p ∈ E under (R), the stable
set W^s(p) := {x ∈ C : Φ_t(x) → p as t → ∞} equals {p}.

*Proof.* As in P-6 Step 1: −DF(p) is Hurwitz, so B_pᵀ P + P B_p = I
(B_p := DF(p)) has a unique P = Pᵀ ≻ 0, and V(δ) := (δ−p)ᵀ P (δ−p) satisfies
V̇ = ∇V·F > 0 on a punctured ellipse 0 < V ≤ ρ. Suppose x ≠ p and Φ_t(x) → p.
By uniqueness of solutions Φ_t(x) ≠ p for all finite t (the constant curve p is
the solution through p). For t large enough Φ_t(x) lies in {V ≤ ρ} \ {p}, where
t ↦ V(Φ_t(x)) is strictly increasing; hence V(Φ_t(x)) ≥ V(Φ_T(x)) > 0 for
t ≥ T, contradicting V(Φ_t(x)) → V(p) = 0. So no x ≠ p converges to p. ∎

**Main argument.** Fix x ∈ C \ E. Since C is compact and positively invariant,
the forward orbit is precompact, so ω(x) is nonempty, compact, invariant, and
**connected** (the standard ω-limit theorem for precompact orbits of a
continuous flow).

Suppose ω(x) = {q} is a single point. Invariance gives Φ_s({q}) = {q} for all
s, i.e. F(q) = 0, so q ∈ E; by (R), q is a source. But ω(x) = {q} means
Φ_t(x) → q, so x ∈ W^s(q) = {q} by the Lemma, forcing x = q ∈ E — contradicting
x ∈ C \ E. Hence ω(x) is not a single point.

A connected set with at least two points in ℝⁿ is infinite (uncountable); E is
finite; therefore ω(x) ⊄ E, and ω(x) contains non-equilibrium points. This is
statement 1, and the gate is open by the P-5 definition.

For statement 2: A = ⋂_{t≥0} Φ_t(C) is the global attractor (nonempty, compact,
invariant, attracts C, since C is compact positively invariant). Each p ∈ E is
a fixed point in C, hence p ∈ Φ_t(C) for all t, so E ⊆ A. Pick any x ∈ C \ E;
ω(x) ⊆ A and ω(x) ⊄ E by statement 1, so A ⊋ E. Thus A is a non-trivial
invariant set attracting the neighbourhood C. ∎

## Remarks

- **R1 (correction of the 2026-07-29 framing).** P-6 and that day's notebook
  called n ≥ 3 "the remaining hard core," suggesting a topological/Conley-index
  argument was needed to open the gate. That was an over-statement. Opening the
  gate under (R) needs only two classical facts — connectedness of ω-limit sets
  and the empty stable set of a source — and holds verbatim in every dimension.
  The genuinely hard, still-open questions are narrower (R2, R3).
- **R2 (what remains open — classification).** P-7 shows a non-trivial invariant
  set is forced but says **nothing about its type**. In n = 2, P-6 upgrades it
  to a periodic orbit; in n ≥ 3 it may be a periodic orbit, a torus, or a
  strange attractor (Lorenz-type), and deciding which for a given F is the hard
  (and, in full generality, effectively unbounded) problem of dynamical systems.
  OP-14's *gate* is settled under (R); the *classification* is not, and is
  arguably outside OP-14's minimal-conditions scope.
- **R3 (what remains open — the source/unstable gap).** OP-14 asked about
  *unstable* equilibria; (R) assumes the stronger *source*. For an unstable but
  non-source equilibrium (a saddle, with a nonempty stable manifold) the Lemma
  fails — trajectories can converge to it along W^s — and the gate can be
  **closed**: a gradient flow with saddle equilibria has every ω-limit in E.
  So (R) cannot be weakened to "unstable" without a further condition
  controlling how the stable manifolds of the non-source equilibria meet C.
  This gap — minimal conditions on the stable-manifold geometry — is the honest
  residue of OP-14.
- **R4 (relation to P-5).** P-5 (necessary): open gate ⇒ non-gradient. P-7
  (sufficient): all-source ⇒ open gate, every n. Together they bracket the gate
  from both sides; the open middle is exactly R3's saddle regime.
- **R5 (attribution).** Connectedness of ω-limit sets (Birkhoff) and the empty
  stable set of a hyperbolic source (stable-manifold theorem / Lyapunov collar)
  are classical. Recorded to settle the gate and relocate the genuine
  difficulty; **no novelty claimed (OP-16)**.
- **R6 (generalized by P-8, 2026-08-01).** P-7's source hypothesis (R) is the
  special case d_s ≡ 0 of P-8's condition (U) "all equilibria hyperbolic and
  unstable" (d_s < n). P-8 opens the gate for a.e. initial condition under (U)
  in every dimension, resolving the source/unstable gap (residue (i)) that R3
  flagged. See `proofs/p008_unstable_gate_almost_everywhere.md`.
