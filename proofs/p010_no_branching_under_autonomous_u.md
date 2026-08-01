# P-10 · A law layer that reads only its own attractor cannot diversify

STATUS: PROPOSITION — complete proof below. Writer, 2026-08-01. Refutes
**C-003 as originally stated**: clauses (a) and (c) of C-003 are mutually
inconsistent, so the branching prediction is empty under C-003(a)'s own
hypothesis. The refutation is constructive — it states exactly what the U layer
must gain for the prediction to have content (see C-003 (v2)).

## Setting

A two-layer 𝓜 with a slow law layer, in the regime of C-003:

- fast layer dδ/dt = F_φ(δ) on X, with attractor A(φ) for each frozen law φ;
- slow layer ε dφ/dt = U(φ) on law space 𝒢 = ℝ^m, ε ≪ 1;
- Ψ : 𝒢 → ℝ of class C², a scalar functional *read off the frozen-law
  attractor*: Ψ(φ) is determined by A(φ).

**Hypothesis (A) — autonomous fitness.** U = ∇Ψ, and the fitness of a variant
law φ′ is the same functional value Ψ(φ′), independently of the resident law
against which it is evaluated. This is exactly the hypothesis of C-003(a):
"U the gradient of a fast-attractor functional, U(φ) = ∇_φ Ψ(φ), Ψ(φ) a scalar
read off A(φ)". Resident-independence is not an extra assumption — it is forced
by Ψ being a function of one argument.

At a *singular point* φ\* (i.e. U(φ\*) = 0, equivalently ∇Ψ(φ\*) = 0) define,
following adaptive dynamics:

- **(D1) convergence stability** — φ\* is linearly asymptotically stable for the
  slow flow φ̇ = ∇Ψ(φ);
- **(D2) uninvadability (ESS)** — φ\* is a strict local maximum of variant
  fitness: there is a neighbourhood N with Ψ(φ′) < Ψ(φ\*) for all φ′ ∈ N∖{φ\*};
- **(D3) branching point** — φ\* is convergence-stable **and** invadable
  (i.e. (D1) holds and (D2) fails).

(D3) is the class C-003(c) predicts to be non-empty and to force the slow layer
to split.

## Statement

Assume (A). Then for every C² functional Ψ and every dimension m:

- **(a)** Hess Ψ(φ\*) ≺ 0 ⟹ φ\* is convergence-stable *and* uninvadable.
- **(b)** Hess Ψ(φ\*) has an eigenvalue > 0 ⟹ φ\* is invadable *and* not
  convergence-stable.
- **(c)** Hence no φ\* is linearly classified as a branching point: (D3) is
  empty apart from the degenerate set where Hess Ψ(φ\*) is negative semidefinite
  and singular, on which neither (D1) nor (D2) is decided at second order.

**Consequently: no 𝓜 whose law layer satisfies (A) exhibits evolutionary
branching — for any Ψ, in any dimension.** C-003(c) has no instances inside
C-003(a).

## Proof

Under (A), (D1) and (D2) are conditions on the *same function at the same
point*.

(D1). φ\* is an equilibrium of the gradient-ascent flow φ̇ = ∇Ψ(φ), whose
linearisation is φ̇ = Hess Ψ(φ\*) φ. Since Hess Ψ(φ\*) is symmetric, it is
diagonalisable with real spectrum, and the equilibrium is linearly
asymptotically stable iff every eigenvalue is negative, i.e. Hess Ψ(φ\*) ≺ 0;
it is unstable as soon as some eigenvalue is positive.

(D2). By the second-derivative test, Hess Ψ(φ\*) ≺ 0 implies φ\* is a strict
local maximum of Ψ, hence uninvadable; if some eigenvalue is positive then Ψ
strictly increases along the corresponding eigendirection, exhibiting invaders,
hence φ\* is invadable.

(a) and (b) follow immediately, and (c) is their contrapositive on the
non-degenerate set: convergence stability forces Hess Ψ(φ\*) ≺ 0, which forces
uninvadability, so (D1) ∧ ¬(D2) is contradictory. ∎

*Sign conventions are immaterial.* If the slow layer descends a loss instead of
ascending a fitness, replace "local maximum" by "local minimum" throughout;
(D1) and (D2) again coincide.

## Remark R1 — the obstruction is *not* gradient-ness

It is tempting to read P-10 as "gradient flows cannot branch". That is false,
and the distinction matters.

In dimension one **every** vector field D(φ) is a gradient: D = V′ for
V(φ) = ∫D. So "the canonical equation of adaptive dynamics is a gradient flow"
holds vacuously in 1-D — and yet adaptive dynamics does exhibit branching in
1-D. Gradient structure of the slow drift is therefore not the obstruction.

The obstruction in (A) is the **identification of the drift potential with the
fitness functional**. In adaptive dynamics the invasion fitness s(φ, φ′) — the
growth rate of a rare variant φ′ against resident φ — genuinely has two
arguments, with s(φ, φ) = 0. The selection gradient is D(φ) = ∂₂s(φ, φ), and at
a singular point φ\*:

- convergence stability ⟺ D′(φ\*) = (∂₁∂₂s + ∂₂²s)(φ\*, φ\*) < 0,
- uninvadability ⟺ ∂₂²s(φ\*, φ\*) < 0.

The two conditions differ **exactly by ∂₁∂₂s**, the frequency-dependence term:
how a variant's fitness depends on the resident. The 1-D drift potential V does
exist, but V″ = ∂₁∂₂s + ∂₂²s ≠ ∂₂²s. A branching point requires

  ∂₂²s > 0 and ∂₁∂₂s < −∂₂²s < 0, in particular ∂₁∂₂s ≠ 0.

Under (A), fitness is resident-independent — equivalently s(φ, φ′) = Ψ(φ′) −
Ψ(φ) — so ∂₁∂₂s ≡ 0, the two second-order conditions collapse onto one, and the
branching class is emptied. P-10 is that collapse.

## Remark R2 — what this demands of the U layer (OP-9)

Under (A) the law layer computes its update from the attractor of its *own*
law. P-10 says such a layer cannot diversify. To have a non-empty branching
class, U must be built from a **two-argument** functional

  U(φ) = ∇_{φ′} Ψ(φ, φ′) |_{φ′=φ},

where Ψ(φ, φ′) is read off the fast-layer attractor **of the resident law φ
with a variant law φ′ evaluated against it**. The law layer must evaluate
counterfactual laws, not merely its own.

This is a structural requirement on U, and it is OP-9's self-modification
question in checkable form. It is also the repair that produces C-003 (v2).

## Remark R3 — the same shape at the state layer (→ OP-19)

P-5 (state layer): if a single scalar decreases monotonically along the flow on
the absorbing region — a strict Lyapunov function — the OP-14 gate is closed;
no persistent non-equilibrium structure.

P-10 (law layer): if a single scalar governs both the drift and the fitness,
branching is impossible; no persistent diversity.

Both have the form *a one-functional description of a layer forbids that
layer's interesting behaviour*. Whether this is more than an analogy — whether
one statement about 𝓜 specialises to both — is recorded as **OP-19**. Note the
parallel is not exact: P-5's single functional is monotone along the flow,
while P-10's is monotone *and* doubles as the invadability criterion, which is
the stronger demand. Any unification must account for that gap.

## What this proposition does NOT establish

It does not show that branching *occurs* in any two-layer 𝓜; it only removes
the case where C-003 placed it. Instances require the two-argument U of R2 —
see P-11 for one built from machine-learning primitives. No OP-16 novelty is
claimed: the adaptive-dynamics second-order conditions used in R1 are textbook
(Metz–Geritz–Nisbet, Geritz et al. 1998, Dieckmann–Law).
