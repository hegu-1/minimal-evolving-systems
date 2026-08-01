# P-5 · The complexity gate requires non-gradient structure

STATUS: PROPOSITION — complete proof below. Writer, 2026-07-29. Sharpens
OP-14 (with P-3): prunes the gate to the non-gradient regime in every finite
dimension.

## Setting

Let X = ℝⁿ and dδ/dt = F(δ) with F locally Lipschitz. Let C ⊂ ℝⁿ be
nonempty, compact, and positively invariant under the semiflow Φ — for
instance an absorbing ball C_c = {δ : ½‖δ‖² ≤ c}, c > γ/(2(α−β)), of P-1
(P-3(b)). Write

  E := {δ ∈ C : F(δ) = 0}

for the equilibrium set, nonempty by P-3(a).

**Terminology (recurrence, not mere non-equilibrium content).** The gate must
be stated via ω-limit sets, *not* via "the attractor contains a non-equilibrium
point": a gradient flow's global attractor is the equilibria together with
their heteroclinic connections, which does contain non-equilibrium points, yet
the flow is dynamically trivial (every trajectory converges to a single
equilibrium). What "persistent complexity" excludes is such convergence. So:
the reframed OP-14 gate is *open* on C iff some δ₀ ∈ C has an ω-limit set
ω(δ₀) ⊄ E — a recurrent non-equilibrium structure (limit cycle, strange
attractor); *closed* iff ω(δ₀) ⊆ E for every δ₀ ∈ C.

## Hypothesis

- **(G) Gradient-likeness.** There exists L ∈ C¹(C; ℝ) whose derivative along
  the flow, L̇(δ) := ⟨∇L(δ), F(δ)⟩, satisfies L̇ ≤ 0 on C and

    {δ ∈ C : L̇(δ) = 0} ⊆ E.

  (L strictly decreases off the equilibria; L is a strict Lyapunov function
  for the flow restricted to C. Gradient systems δ̇ = −∇V are the model case,
  with L = V.)

## Statement

Under (G), every ω-limit set satisfies ω(δ₀) ⊆ E for all δ₀ ∈ C — so the
reframed OP-14 gate is **closed** on C (no trajectory has a recurrent
non-equilibrium ω-limit).

Contrapositive (the sharpening): if the gate is open on C, then no function
satisfying (G) exists — F admits no strict Lyapunov function on C, i.e. **F is
not gradient-like on C**. Non-gradient structure is *necessary* for persistent
complexity.

## Proof

Fix δ₀ ∈ C. Since C is compact and positively invariant, the forward orbit
{Φ_t(δ₀) : t ≥ 0} is precompact, so ω(δ₀) is nonempty, compact, invariant,
and contained in C (standard properties of ω-limit sets of precompact
orbits).

Along the solution, d/dt L(δ(t)) = ⟨∇L(δ(t)), F(δ(t))⟩ = L̇(δ(t)) ≤ 0 by (G),
so t ↦ L(δ(t)) is nonincreasing; it is bounded below because L is continuous
on the compact set C. Hence L(δ(t)) ↓ ℓ for some ℓ ∈ ℝ.

Let p ∈ ω(δ₀). Take t_k → ∞ with Φ_{t_k}(δ₀) → p; by continuity of L,
L(p) = lim_k L(Φ_{t_k}(δ₀)) = ℓ. As p ∈ ω(δ₀) was arbitrary, L ≡ ℓ on
ω(δ₀). Now ω(δ₀) is invariant, so for q ∈ ω(δ₀) the whole trajectory
Φ_t(q) stays in ω(δ₀), where L is constant; differentiating L(Φ_t(q)) ≡ ℓ at
t = 0 gives L̇(q) = 0. Thus ω(δ₀) ⊆ {L̇ = 0} ⊆ E by (G). This is LaSalle's
invariance principle in the present setting.

Therefore ω(δ₀) ⊆ E for every δ₀ ∈ C: no trajectory has an ω-limit set
containing a non-equilibrium point, so no recurrent non-equilibrium structure
attracts and the gate is closed. The contrapositive is the logical converse of
this implication. ∎

(Regularity: L is taken C¹ on an open neighborhood of C, so ∇L is defined at
every point of ω(δ₀) ⊆ C, including boundary points; the derivative
d/dt L(Φ_t(q)) at t = 0 is one-sided where needed and equals ⟨∇L(q), F(q)⟩.)

## Remarks

- **R1 (why B does not close the gate itself).** P-1's balance functional
  B = ½‖δ‖² satisfies Ḃ ≤ −2(α−β)B + γ, which is negative only *outside* the
  absorbing ball; **inside** C_c the sign of Ḃ is unconstrained. So B drives
  trajectories *into* C_c but is not a Lyapunov function *within* it. P-5 says
  precisely: if the gate is open on C_c, then **no** C¹ function — B or any
  other — is a strict Lyapunov function there. The complexity question is thus
  not "does energy decrease?" but "does *some* observable decrease
  monotonically?"
- **R2 (relation to P-3).** P-3 removed *equilibrium absence* as the gate
  mechanism (finite dim). P-5 removes *gradient dynamics* as a place the gate
  could open. Together they confine OP-14 to: finite-dimensional,
  equilibrium-containing, non-gradient flows on a compact absorbing region.
- **R3 (attribution).** LaSalle's invariance principle (LaSalle 1960;
  see also Hale, *Asymptotic Behavior of Dissipative Systems*) — classical.
  Recorded to prune the OP-14 search space; **no novelty claimed (OP-16)**.
- **R4 (necessary, not sufficient).** (G)'s failure does not *produce* a
  non-trivial attractor; P-5 forbids the gate in the gradient regime but does
  not open it off that regime. P-7/P-8/P-9 give sufficient hypotheses by
  progressively deleting assumptions: sources, then hyperbolic unstable
  equilibria, then any finite equilibrium set with a linear escape direction.
