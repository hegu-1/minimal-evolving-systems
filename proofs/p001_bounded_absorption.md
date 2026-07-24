# P-1 · Bounded absorption under dominant dissipation

STATUS: PROPOSITION — complete proof below. Received fourth intake,
2026-07-24; formal write-up and remarks by the Writer.

## Setting

Let X be a real Hilbert space and let δ : [0, ∞) → X solve

  dδ/dt = Aδ + N(δ) + f,

where A is the dissipative part, N the nonlinear amplification /
redistribution, and f the external input. Standing assumption: solutions are
regular enough that t ↦ ½‖δ(t)‖² is differentiable with the chain rule
(see Remark R3). Define the balance functional

  B(δ) = ½‖δ‖².

## Hypotheses

- (H1) Dissipativity: ⟨Aδ, δ⟩ ≤ −α‖δ‖² for some α > 0.
- (H2) Bounded amplification: ⟨N(δ), δ⟩ ≤ β‖δ‖² for some β ≥ 0.
- (H3) Bounded input pairing: ⟨f, δ⟩ ≤ γ for some γ ≥ 0.

## Statement

If α > β, then for all t ≥ 0

  B(t) ≤ B(0) e^{−2(α−β)t} + (γ / (2(α−β))) (1 − e^{−2(α−β)t}),

and in particular

  limsup_{t→∞} B(t) ≤ γ / (2(α−β)).

*Dissipation dominating amplification confines the difference to a finite
absorbing region: no blow-up, no requirement of a conserved invariant.*

## Proof

Along a solution,

  dB/dt = ⟨dδ/dt, δ⟩ = ⟨Aδ, δ⟩ + ⟨N(δ), δ⟩ + ⟨f, δ⟩
        ≤ −α‖δ‖² + β‖δ‖² + γ           (H1)–(H3)
        = −(α−β)‖δ‖² + γ
        = −2(α−β)B + γ.

Set λ = 2(α−β) > 0. The scalar comparison y′ = −λy + γ with y(0) = B(0) has
solution y(t) = B(0)e^{−λt} + (γ/λ)(1 − e^{−λt}), and Grönwall's inequality
gives B(t) ≤ y(t) for all t ≥ 0. Letting t → ∞ yields
limsup B(t) ≤ γ/λ = γ / (2(α−β)). ∎

## Remarks

- **R1 (on H3 — Writer's variant P-1′).** For a fixed f ∈ X, Cauchy–Schwarz
  gives ⟨f, δ⟩ ≤ ‖f‖‖δ‖, which is *not* uniformly bounded in δ; H3 as stated
  is a strong assumption. The standard repair is Young's inequality:
  ⟨f, δ⟩ ≤ (ε/2)‖δ‖² + ‖f‖²/(2ε) = εB + ‖f‖²/(2ε) for any ε > 0. Then
  dB/dt ≤ −(2(α−β) − ε)B + ‖f‖²/(2ε), and for ε < 2(α−β) the same
  comparison argument gives limsup B(t) ≤ ‖f‖² / (2ε(2(α−β) − ε)); taking
  ε = α−β yields the absorbing-ball bound limsup B ≤ ‖f‖² / (2(α−β)²).
  Conclusion unchanged, constants adjusted, hypothesis honest.
- **R2 (attribution).** This is the classical energy / absorbing-set estimate
  of dissipative dynamical systems theory (cf. Temam; Robinson —
  `references/bibliography.md`). It is recorded to calibrate the framework;
  **no novelty is claimed** (OP-16).
- **R3 (regularity).** For weak formulations the chain-rule step needs care;
  for 3D Navier–Stokes only an energy *inequality* is available for weak
  solutions — which still suffices for this argument's direction. See
  `mappings/navier_stokes.md`.
- **R4 (regimes — DISCUSSION).** The same inequality suggests three regimes:
  dissipative (α > β, this proposition), critical (α ≈ β), amplifying
  (α < β — no conclusion; a *necessary direction* for instability, not a
  proof of it, as the intake itself notes).
