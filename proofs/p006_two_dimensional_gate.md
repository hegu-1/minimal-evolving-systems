# P-6 · In two dimensions, all-repelling equilibria open the gate

STATUS: PROPOSITION — complete proof below. Writer, 2026-07-29. Settles the
reframed OP-14 gate for n = 2 under an explicit minimal condition; isolates
n ≥ 3 as the open core.

## Setting

Let X = ℝ² and dδ/dt = F(δ) with F of class C¹. Let C = C_c = {½‖δ‖² ≤ c},
c > γ/(2(α−β)), be an absorbing disk of P-1 — compact, convex, positively
invariant (P-3(b)). Write E = {δ ∈ C : F(δ) = 0} for the equilibrium set
(nonempty by P-3(a)).

## Hypothesis

- **(R) All equilibria repel.** For each p ∈ E, spec(DF(p)) ⊂ {λ ∈ ℂ : Re λ > 0}
  — both eigenvalues of the Jacobian at p have positive real part (p is an
  unstable node or focus, i.e. a *source*; no equilibrium has a stable
  direction). *(Finiteness is automatic: each such p is hyperbolic, hence
  isolated, and E ⊆ C is compact, so E = {p₁, …, p_m} is finite.)*

## Statement

Under (R), C contains a periodic orbit Γ. Γ is a non-trivial compact
invariant set (Γ ⊄ E), so the reframed OP-14 gate is **open** on C in
dimension two.

## Proof

**Step 1 — a repelling collar around each source.** Fix i. Set B_i := DF(pᵢ);
by (R), spec(B_i) ⊂ {Re > 0}, so −B_i is Hurwitz. The Lyapunov equation for the
Hurwitz matrix −B_i with right-hand side −I,

  (−B_i)ᵀ P_i + P_i(−B_i) = −I,  equivalently  B_iᵀ P_i + P_i B_i = I,

has a unique solution P_i = P_iᵀ ≻ 0 (standard; P_i = ∫₀^∞ e^{−B_iᵀ s} e^{−B_i s} ds).
Put V_i(δ) := (δ − pᵢ)ᵀ P_i (δ − pᵢ), whose sublevel sets are ellipses centred
at pᵢ. For the linearised field ẋ = B_i x (x = δ − pᵢ),

  V̇_i = xᵀ(B_iᵀ P_i + P_i B_i) x = xᵀ x = ‖x‖² > 0  (x ≠ 0).

Since F(δ) = B_i(δ−pᵢ) + o(‖δ−pᵢ‖), there is ρᵢ > 0 with
∇V_i(δ)·F(δ) > 0 on the punctured ellipse 0 < V_i(δ) ≤ ρᵢ. Shrink the ρᵢ so
that the closed ellipses D_i := {V_i ≤ ρᵢ} are pairwise disjoint and contained
in int C. On each boundary ellipse ∂D_i = {V_i = ρᵢ}, ∇V_i is the outward
normal (V_i is a positive-definite quadratic, hence convex), and V̇_i > 0 means
F points strictly outward; so no forward trajectory enters D_i°.

**Step 2 — an equilibrium-free trapping region.** Let C′ := C \ ⋃_i D_i°.
Then C′ is compact, and C′ ∩ E = ∅ (every equilibrium pᵢ lies in D_i°). C′ is
positively invariant: a forward trajectory from C′ cannot leave C (P-1 positive
invariance of C) and cannot enter any D_i° (Step 1: outward flux on ∂D_i), so
it remains in C′ for all t ≥ 0.

**Step 3 — Poincaré–Bendixson.** C′ is a nonempty compact positively
invariant subset of ℝ² containing no equilibrium. Pick δ₀ ∈ C′; its
ω-limit set ω(δ₀) ⊆ C′ is nonempty, compact, invariant, and equilibrium-free.
By the **Poincaré–Bendixson theorem**, an ω-limit set in the plane that
contains no equilibrium is a periodic orbit. Hence Γ := ω(δ₀) is a periodic
orbit contained in C, and Γ ⊄ E. ∎

## Remarks

- **R1 (this is OP-14's own witness, promoted).** The reframing remark of P-3
  named "limit cycles via unstable focus + trapping region" as evidence the
  gate is non-empty. P-6 turns that witness into a proposition with an
  explicit sufficient condition (R).
- **R2 (n ≥ 3 is the open core).** The proof uses Poincaré–Bendixson, which is
  false in ℝ³ and above, where a non-trivial invariant set can be a **strange
  attractor** rather than a periodic orbit. The Lorenz flow witnesses that the
  n ≥ 3 gate opens onto chaos — a bounded absorbing region with a non-trivial
  attracting set that is neither an equilibrium nor a cycle — and thereby that
  no planar-style "the ω-limit is a cycle" conclusion can hold in general.
  (Caveat: Lorenz's equilibria are *saddles*, not sources, so it does **not**
  satisfy hypothesis (R); it motivates the difficulty, it is not an instance of
  the (R)-question.) **The remaining hard core of OP-14, now isolated:** for
  n ≥ 3, non-gradient (P-5), with every equilibrium in a P-1 trapping region a
  source (R) — is a non-trivial invariant set forced to attract? Poincaré–
  Bendixson gives no leverage; a topological argument (degree / Conley index)
  would be needed. Open.
  *(Framing correction, 2026-08-01: P-7 shows the gate **opens** under (R) in
  every dimension by a short ω-limit-connectedness argument — no Conley index
  needed. What is hard in n ≥ 3 is not opening the gate but **classifying** the
  forced non-trivial set, and the saddle/unstable gap. See
  `proofs/p007_all_source_gate_every_dimension.md`.)*
- **R3 (sufficient, not necessary).** (R) is not necessary for the gate to
  open even in n = 2: a trapping region with saddle equilibria can carry a
  periodic orbit or a heteroclinic graphic. P-6 gives one clean minimal
  *sufficient* condition, not a characterization.
- **R4 (attribution).** Poincaré–Bendixson theorem and the Lyapunov-equation
  collar are classical (see Hirsch–Smale–Devaney; Perko). Recorded to settle
  the planar case and locate the open core; **no novelty claimed (OP-16)**.
