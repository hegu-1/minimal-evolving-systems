# P-8 · Unstable hyperbolic equilibria open the gate almost everywhere

STATUS: PROPOSITION — complete proof below. Writer, 2026-08-01. Resolves
OP-14 residue (i): the source hypothesis (R) of P-6/P-7 is not needed —
OP-14's original condition, "every equilibrium unstable," already opens the
gate (for a.e. initial condition), once hyperbolicity is assumed. Subsumes P-7.

## Setting

Let X = ℝⁿ (n ≥ 1) and dδ/dt = F(δ) with F of class C¹. Let C = C_c =
{½‖δ‖² ≤ c}, c > γ/(2(α−β)), be an absorbing ball of P-1 — compact, positively
invariant (P-3(b)) — and E = {δ ∈ C : F(δ) = 0}. Gate terminology as in P-5:
the gate is *open* on C iff some x ∈ C has ω(x) ⊄ E.

For a hyperbolic equilibrium p, W^s(p) := {x : Φ_t(x) → p} is its global stable
manifold; by the stable-manifold theorem the local stable manifold W^s_loc(p)
is an embedded C¹ disk of dimension d_s(p) = #{eigenvalues of DF(p) with
Re < 0}, and W^s(p) = ⋃_{m∈ℕ} Φ_{−m}(W^s_loc(p)).

## Hypothesis

- **(U) All equilibria are hyperbolic and unstable.** Every p ∈ E has
  spec(DF(p)) ∩ iℝ = ∅ (hyperbolic) and at least one eigenvalue with Re > 0
  (unstable). Equivalently d_s(p) < n for every p. (Hyperbolicity ⇒ each p
  isolated ⇒ E = {p₁, …, p_m} finite. Sources — hypothesis (R) — are the case
  d_s = 0.)

## Statement

Under (U):

1. ⋃_{p∈E} W^s(p) has Lebesgue measure zero in ℝⁿ.
2. Hence C ∖ ⋃_p W^s(p) has full measure in C, and for **every** x in it
   ω(x) ⊄ E. The gate is open — for Lebesgue-almost-every initial condition —
   in every finite dimension.
3. The global attractor A = ⋂_{t≥0} Φ_t(C) satisfies A ⊋ E and attracts C.

## Proof

**(1) Stable manifolds are null.** Fix p ∈ E. By (U), d_s(p) < n, so W^s_loc(p)
is an embedded C¹ submanifold of dimension < n, hence Lebesgue-null in ℝⁿ (a
C¹ image of an open subset of ℝ^{d_s}, d_s < n, is null). Each Φ_{−m} is a
diffeomorphism of ℝⁿ, so Φ_{−m}(W^s_loc(p)) is again an embedded C¹
submanifold of dimension d_s(p) < n, hence null. Therefore

  W^s(p) = ⋃_{m∈ℕ} Φ_{−m}(W^s_loc(p))

is a countable union of null sets, hence null; and ⋃_{p∈E} W^s(p) is a finite
union of null sets, hence null.

**(2) A full-measure set has non-trivial ω-limit.** Let
S := C ∖ ⋃_p W^s(p); by (1) and Leb(C) > 0, S has full measure in C (in
particular S ≠ ∅). Fix x ∈ S. Since C is compact positively invariant, ω(x) is
nonempty, compact, invariant, and connected. If ω(x) were a single point it
would be an equilibrium q ∈ E (invariance), and ω(x) = {q} means Φ_t(x) → q,
i.e. x ∈ W^s(q) — contradicting x ∈ S. So ω(x) has at least two points;
being connected it is infinite, while E is finite, so ω(x) ⊄ E. As S has full
measure, this holds for a.e. x ∈ C; the gate is open.

**(3) Attractor.** As in P-7: A = ⋂_{t≥0} Φ_t(C) is nonempty, compact,
invariant, and attracts C; E ⊆ A (equilibria are fixed points in C); and
picking any x ∈ S gives ω(x) ⊆ A with ω(x) ⊄ E, so A ⊋ E. ∎

## Remarks

- **R1 (OP-14's original hypothesis was right).** OP-14 asked for conditions
  making "every equilibrium unstable while a non-trivial invariant set
  attracts." P-8 shows the two clauses are not independent goals to be
  engineered: **"every equilibrium hyperbolic and unstable" already forces the
  second**, in every dimension, for a.e. initial condition. The stronger source
  hypothesis (R) of P-6/P-7 is unnecessary; P-7 is the special case d_s ≡ 0.
- **R2 (the mechanism, and its classical lineage).** The engine is: a proper
  (< n-dimensional) stable manifold cannot trap a positive-measure set, so
  almost every trajectory escapes the equilibria and — having nowhere in the
  finite E to land — must accumulate on a non-trivial invariant set. This is
  the continuous-time, absorbing-region form of the "gradient descent avoids
  saddles almost surely" phenomenon (center-stable manifolds are null; cf.
  Lee–Simchowitz–Jordan–Recht 2016 for the discrete map, and the classical
  Kupka–Smale / Morse–Smale genericity theory). **No novelty claimed (OP-16).**
- **R3 (measure-zero, not everywhere).** The gate can still be closed on the
  null set ⋃W^s(p): individual trajectories may converge to saddles along their
  stable manifolds. "Open a.e." is the honest and sharp statement; a
  literally-everywhere gate requires ⋃W^s(p) ∩ C to be empty (the all-source
  case, P-7). Gate globally *closed* requires the opposite extreme,
  C ⊆ ⋃W^s(p) — possible only if some equilibrium is a sink (d_s = n), i.e. (U)
  fails; the gradient flow with a sink is the model.
- **R4 (residue of OP-14 after P-8).** The gate (open/closed) is now settled in
  the hyperbolic regime: **open for a.e. x ⟺ no equilibrium is a sink ⟺ (U)**.
  What remains: **(a)** non-hyperbolic equilibria (centre directions — the
  stable *set* may fail to be null; needs a centre-manifold argument or a
  transversality/genericity hypothesis); **(b)** the *classification* of the
  forced non-trivial set (cycle / torus / strange attractor), the genuinely
  hard and arguably unbounded n ≥ 3 problem, outside OP-14's minimal-conditions
  remit. With P-5 (necessary: non-gradient) and P-8 (sufficient: (U)) the gate
  itself is bracketed tightly; only (a) and (b) remain.
