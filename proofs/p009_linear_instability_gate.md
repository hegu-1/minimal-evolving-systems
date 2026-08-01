# P-9 · A linear escape direction opens the gate almost everywhere

STATUS: PROPOSITION — complete proof below. Writer, 2026-08-01. Removes P-8's
hyperbolicity assumption: a single eigenvalue with Re > 0 at each equilibrium
already opens the gate (a.e.), non-hyperbolic centre directions allowed. Uses
the forward-map nullity technique of the P-8 Formalizer repair (no global
backward completeness). Narrows OP-14 residue (a) to its genuine core.

## Setting

Let X = ℝⁿ (n ≥ 1) and dδ/dt = F(δ) with F of class C². Let C = C_c be a P-1
absorbing ball — compact, positively invariant (P-3(b)); in particular the
forward flow is complete on C. Let E = {δ ∈ C : F(δ) = 0}. Gate terminology as
in P-5.

For an equilibrium p, write d_u(p) = #{eigenvalues of DF(p) with Re > 0}. By
the centre-manifold theorem (F ∈ C²), p has a local **centre-stable manifold**
W^{cs}_loc(p): an embedded C¹ submanifold tangent to E^s(p) ⊕ E^c(p), of
dimension n − d_u(p), locally invariant, and characterised (on a neighbourhood
U ∋ p) by

  W^{cs}_loc(p) ⊇ {x ∈ U : Φ_t(x) ∈ U for all t ≥ 0}.

Every forward orbit that stays near p — in particular every orbit converging to
p — lies in W^{cs}_loc(p) from some time on.

## Hypothesis

- **(U′) A linear escape direction at each equilibrium.** E is finite, and
  every p ∈ E has d_u(p) ≥ 1 (at least one eigenvalue with Re > 0). Hyperbolicity
  is **not** assumed: eigenvalues with Re = 0 (centre directions) are allowed.
  (P-8's hypothesis (U) is the special case with no centre directions.)

## Statement

Under (U′), ⋃_{p∈E} (W^s(p) ∩ C) is Lebesgue-null; hence a full-measure set of
initial conditions in C has ω(x) ⊄ E, and the gate is open for
Lebesgue-almost-every initial condition, in every finite dimension. The global
attractor A satisfies A ⊋ E and attracts C.

## Proof

**(1) The trapped stable set is null.** Fix p ∈ E. By (U′), d_u(p) ≥ 1, so
dim W^{cs}_loc(p) = n − d_u(p) ≤ n − 1; an embedded C¹ submanifold of dimension
< n is Lebesgue-null in ℝⁿ.

For m ∈ ℕ let D_m = {x : the solution through x exists on [0, m]}; C ⊆ D_m for
all m by forward completeness on C. The time-m map Φ_m : D_m → ℝⁿ is a local
C¹ diffeomorphism (its derivative is the fundamental matrix of the variational
equation, invertible), so

  S_m(p) := {x ∈ D_m : Φ_m(x) ∈ W^{cs}_loc(p)}

is, locally, the Φ_m-preimage of an embedded submanifold of dimension < n under
a diffeomorphism — an embedded C¹ submanifold of the same dimension
n − d_u(p) < n, hence null. If x ∈ W^s(p) ∩ C then Φ_t(x) → p while staying in
the compact C, so Φ_m(x) ∈ W^{cs}_loc(p) for all large integers m; thus

  W^s(p) ∩ C ⊆ ⋃_{m∈ℕ} S_m(p),

a countable union of null sets, hence null. As E is finite,
⋃_{p∈E} (W^s(p) ∩ C) is null in C. (This is the P-8 forward-map argument with
the stable manifold replaced by the centre-stable manifold; global backward
completeness of Φ is not used.)

**(2)–(3)** Verbatim as in P-8: with S := C ∖ ⋃_p W^s(p) of full measure, any
x ∈ S has Φ_t(x) ↛ any equilibrium, so its ω-limit set (nonempty, compact,
invariant, connected) is not a single point, hence — being connected and E
finite — satisfies ω(x) ⊄ E. The global attractor A = ⋂_{t≥0} Φ_t(C) contains
E and, containing some such ω(x), strictly contains E. ∎

## Remarks

- **R1 (what P-9 buys over P-8).** P-8 needed every equilibrium hyperbolic.
  P-9 needs only *one strictly unstable eigenvalue* per equilibrium — the rest
  of the spectrum may sit on the imaginary axis. The engine is unchanged: a
  proper (< n-dimensional) centre-stable manifold cannot trap a positive-measure
  set. So the gate opens a.e. as soon as every equilibrium has a **linear escape
  direction**, hyperbolic or not.
- **R2 (the genuine residue (a), now sharp).** The measure-zero argument uses
  d_u(p) ≥ 1 essentially. It fails exactly when some equilibrium is unstable
  with **d_u = 0** — all eigenvalues in Re ≤ 0, instability carried by the
  nonlinear centre dynamics (model: ẋ = x² at 0, whose stable set {x ≤ 0} has
  positive measure). There the centre-stable manifold is the whole space and a
  positive-measure set can converge to E, closing the gate on that set. This
  linearly-neutral / nonlinearly-unstable case is the honest, and thin
  (non-generic, by Kupka–Smale hyperbolicity density), residue (a) of OP-14.
- **R3 (the other residue: non-isolated equilibria).** (U′) keeps E finite.
  Dropping it — a continuum of equilibria — reintroduces an *uncountable* union
  of null centre-stable manifolds, which may fail to be null; a normally-
  hyperbolic-repelling hypothesis on the equilibrium set would be the natural
  replacement. Recorded, not proved.
- **R4 (net OP-14 picture).** P-5 (necessary: non-gradient) and P-9 (sufficient:
  a linear escape direction at each of finitely many equilibria) bracket the
  gate. In the hyperbolic regime the bracket is tight (P-8: open a.e. ⟺ no
  sink). The residue is now precisely two thin cases: **d_u = 0 nonlinear
  instability** (R2) and **non-isolated equilibria** (R3). Neither is the
  "n ≥ 3 is hard" object once feared; both are degeneracy/genericity questions.
- **R5 (attribution).** Centre-manifold theorem, Lebesgue-nullity of proper
  C¹ submanifolds, and the forward-map preimage technique (the last from the
  P-8 Formalizer repair) are classical. **No novelty claimed (OP-16).**
