# 05 · Propositions

STATUS: normative — each entry carries a complete proof in `proofs/`.

## P-1 · Bounded absorption under dominant dissipation

If dissipation uniformly dominates internal amplification (α > β) and the
input pairing is bounded, then the balance functional B = ½‖δ‖² enters and
remains in a finite absorbing region:

  limsup_{t→∞} B(t) ≤ γ / (2(α − β)).

Full statement, hypotheses, proof, and remarks (including the Writer's
variant P-1′ with an honest input hypothesis):
`proofs/p001_bounded_absorption.md`.

First mathematical statement of the project. Attribution: classical result,
recorded for calibration — no novelty claimed (OP-16). The live question it
opens is OP-14: when does the absorbing region *not* collapse to a single
equilibrium?

Placement under v2: P-1 is a **static-class** result (U ≡ 0, B-method). Its
evolving-class analogue is P-4's two-layer balance criterion: balance bounds
must survive both the moving state and the moving law.

## P-2 · Local well-posedness of the coupled layers

If the law space 𝓖 embeds continuously into the Lipschitz vector fields on X
(evaluation bounds E1–E2) and the law update U is locally Lipschitz, then the
two-layer system dδ/dt = F(δ), dF/dt = U(F, δ) has a unique local C¹
solution for every initial pair (δ₀, F₀); along the realized law trajectory
the propagation Φ_{t,s} is globally defined on the existence interval and
satisfies the process property.

Full statement and proof: `proofs/p002_local_wellposedness.md`. Settles the
ambient-space local half of OP-18. Its remark R2 formalizes the suspension
objection: the product presentation is canonical and autonomous; the evolving
presentation is trajectory-relative (OP-17). Classical technique; no novelty
claimed (OP-16).

## P-3 · The absorbing region always contains an equilibrium (finite dim.)

A compact convex positively invariant set of a locally Lipschitz flow in ℝⁿ
contains a rest point (Brouwer-limit argument); under P-1's hypotheses every
ball {B ≤ c}, c > γ/(2(α−β)), is such a set. Hence in finite dimension the
absorbing region can never be equilibrium-free.

Full statement and proof: `proofs/p003_equilibrium_in_absorbing_region.md`.
**Consequence: OP-14 is reframed** — the gate to persistent complexity is
equilibrium *instability* coexisting with an attracting non-trivial set, not
equilibrium absence. Infinite-dimensional extension (Schauder, compact
semiflows) recorded as open. Classical; no novelty claimed (OP-16).

## P-4 · K-invariance and global existence for the coupled layers

If K ⊂ 𝓖 is nonempty, closed, and convex, and the law update satisfies the
Nagumo tangency condition U(F, δ) ∈ T_K(F) for every F ∈ K, then the local
solution of P-2 stays in X × K. If, in addition, the state and law layers admit
coercive balance functionals B_X and B_𝓖 whose derivatives close by a
two-layer Grönwall estimate, then no finite-time blow-up occurs and the
coupled system is globally well-posed in X × K.

Full statement and proof: `proofs/p004_k_invariance_global_existence.md`.
This settles the remaining formal half of OP-18 under explicit Nagumo and
balance hypotheses. Classical; no novelty claimed (OP-16).

## P-5 · The complexity gate requires non-gradient structure

On a compact positively invariant region C ⊂ ℝⁿ, if the flow admits a strict
Lyapunov function (a C¹ function decreasing off the equilibria), then every
ω-limit set lies in the equilibrium set (LaSalle) and no non-trivial attracting
set exists — the reframed OP-14 gate is closed. Contrapositive: **an open gate
requires that no strict Lyapunov function exist on C, i.e. F is non-gradient.**

Full statement and proof: `proofs/p005_gate_requires_nongradient.md`. Sharpens
OP-14 with P-3: the gate lives only in the non-gradient regime, in every finite
dimension. Classical (LaSalle); no novelty claimed (OP-16).

## P-6 · In two dimensions, all-repelling equilibria open the gate

For n = 2, if a P-1 absorbing disk contains finitely many equilibria all of
which are sources (Jacobian spectrum in the open right half-plane), then the
disk contains a periodic orbit (Lyapunov-equation collars + Poincaré–Bendixson),
so the reframed OP-14 gate is open.

Full statement and proof: `proofs/p006_two_dimensional_gate.md`. Promotes
OP-14's own witness (unstable focus + trapping region) to a proposition. In the
plane it gives the strong conclusion — a *periodic orbit*. Classical; no novelty
claimed (OP-16).

## P-7 · All-source equilibria open the gate in every finite dimension

If every equilibrium in a P-1 absorbing region is a source, then every
non-equilibrium trajectory has a non-trivial ω-limit set (ω(x) ⊄ E), so the
gate is open **in every finite dimension** — no Poincaré–Bendixson or Conley
index required, only connectedness of ω-limit sets and the empty stable set of a
source. The global attractor strictly contains the equilibria.

Full statement and proof: `proofs/p007_all_source_gate_every_dimension.md`.
**Corrects the P-6/07-29 "n ≥ 3 is the hard core" framing:** opening the gate is
not dimension-hard. Classical; no novelty claimed (OP-16).

## P-8 · Unstable hyperbolic equilibria open the gate almost everywhere

If every equilibrium in a P-1 absorbing region is hyperbolic and unstable
(d_s < n each), then ⋃_p W^s(p) is Lebesgue-null, so a full-measure set of
initial conditions has non-trivial ω-limit (ω(x) ⊄ E): the gate is open for
almost every initial condition, in every finite dimension. Subsumes P-7 (sources
= d_s ≡ 0).

Full statement and proof: `proofs/p008_unstable_gate_almost_everywhere.md`.
**Resolves OP-14 residue (i):** OP-14's own condition "every equilibrium
unstable" already opens the gate — the source hypothesis was unnecessary. The
engine is the null stable manifold ("gradient descent avoids saddles a.e." in
absorbing-region form). Classical; no novelty claimed (OP-16).

## P-9 · A linear escape direction opens the gate almost everywhere

Drops P-8's hyperbolicity: if each of finitely many equilibria has at least one
eigenvalue with Re > 0 (a linear escape direction; centre directions allowed),
the centre-stable manifold has dimension n − d_u < n, so ⋃(W^s(p) ∩ C) is
Lebesgue-null and the gate opens for a.e. initial condition, every dimension.
Uses the forward-map nullity technique (no global backward completeness).

Full statement and proof: `proofs/p009_linear_instability_gate.md`. **Narrows
OP-14 residue (a) to its sharp core:** the gate can only close on a
positive-measure set at an equilibrium with **d_u = 0** (linearly neutral,
nonlinearly unstable — non-generic), or at non-isolated equilibrium continua.
Classical (centre-manifold theorem); no novelty claimed (OP-16).
