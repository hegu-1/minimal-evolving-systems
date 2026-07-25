# P-3 · The absorbing region always contains an equilibrium (finite dimension)

STATUS: PROPOSITION — complete proof below. Writer, 2026-07-25 (seventh
step). Confirms the OP-14 lead and reframes the gate.

## Statement

**(a) Rest-point theorem.** Let C ⊂ ℝⁿ be nonempty, compact, convex, and
positively invariant under the semiflow Φ of dδ/dt = F(δ), where F is
locally Lipschitz. Then C contains an equilibrium: some δ* ∈ C with
F(δ*) = 0.

**(b) Application to P-1.** Let X = ℝⁿ and suppose H1–H3 of P-1 hold
(⟨Aδ, δ⟩ ≤ −α‖δ‖², ⟨N(δ), δ⟩ ≤ β‖δ‖², ⟨f, δ⟩ ≤ γ) with α > β, and
F := A + N(·) + f locally Lipschitz. Then for every c > γ / (2(α − β)) the
ball C_c = {δ : B(δ) ≤ c}, B = ½‖δ‖², contains an equilibrium:

  ∃ δ* with Aδ* + N(δ*) + f = 0, ½‖δ*‖² ≤ c.

*Consequence for OP-14: in finite dimension, the absorbing region can never
be equilibrium-free. Persistent complexity, if it exists, must coexist with
an equilibrium — the gate is equilibrium **instability**, not equilibrium
absence.*

## Proof

**(a)** Trajectories starting in C stay in the compact set C, so they cannot
blow up and Φ_t : C → C is defined for all t ≥ 0; by local Lipschitz
continuity of F, solutions are unique and the map (t, x) ↦ Φ_t(x) is
continuous on [0, ∞) × C, hence uniformly continuous on [0, 1] × C.

For each t > 0 the map Φ_t : C → C is continuous on a nonempty compact
convex subset of ℝⁿ, so by **Brouwer's fixed-point theorem** it has a fixed
point. Choose t_n ↓ 0 and fixed points x_n = Φ_{t_n}(x_n) ∈ C. By
compactness pass to a subsequence with x_n → x* ∈ C.

Fix t > 0. Write t = k_n t_n + r_n with k_n ∈ ℕ and 0 ≤ r_n < t_n. Iterating
the fixed-point relation gives Φ_{k_n t_n}(x_n) = x_n, so by the semiflow
property

  Φ_t(x_n) = Φ_{r_n}(Φ_{k_n t_n}(x_n)) = Φ_{r_n}(x_n).

Let n → ∞. The left side tends to Φ_t(x*) by continuity of Φ_t. For the
right side,

  ‖Φ_{r_n}(x_n) − x*‖ ≤ ‖Φ_{r_n}(x_n) − Φ_{r_n}(x*)‖ + ‖Φ_{r_n}(x*) − x*‖;

the first term → 0 by uniform continuity of Φ on [0, 1] × C (since
x_n → x*, uniformly over r_n), and the second → 0 by continuity of
t ↦ Φ_t(x*) at t = 0. Hence Φ_t(x*) = x* for every t > 0. The constant curve
δ(t) ≡ x* is then the solution through x*, and differentiating at t = 0
gives F(x*) = 0. ∎(a)

**(b)** It suffices to show C_c is positively invariant; C_c is nonempty
(0 ∈ C_c), compact and convex (a closed ball), and (a) applies.

Let ε := 2(α − β)c − γ > 0. Along any solution, P-1's computation gives
dB/dt ≤ −2(α − β)B + γ, so whenever B(δ(t)) = c:

  dB/dt ≤ −2(α − β)c + γ = −ε < 0.   (★)

Suppose a solution with B(δ(0)) ≤ c exits C_c, and let
t₀ = inf{t ≥ 0 : B(δ(t)) > c}. On [0, t₀] we have B ≤ c (definition of the
infimum, plus continuity at t₀), and in particular B(δ(t₀)) = c: it cannot
be < c, since then continuity would keep B < c on a neighborhood of t₀,
contradicting the existence — again by definition of the infimum — of times
t_k ↓ t₀ with B(δ(t_k)) > c. Now B(δ(·)) is C¹ near t₀ with derivative at
t₀ bounded by (★): dB/dt ≤ −ε < 0. Hence B(δ(t)) < c on some interval
(t₀, t₀ + h), h > 0, which contradicts t_k ↓ t₀ with B(δ(t_k)) > c. No exit
occurs, and C_c is positively invariant. ∎(b)

## Remarks

- **R1 (OP-14 reframed).** The maintainer-boxed question "when does the
  absorbing region not collapse to a single equilibrium?" cannot be answered
  by exhibiting equilibrium-free absorbing dynamics — no such thing exists
  in finite dimension. The sharpened question: *under what minimal
  conditions on F (equivalently on the layers of 𝓜) is every equilibrium in
  C_c unstable, while a non-trivial invariant set attracts?* Classical
  examples (Lorenz system; limit cycles via unstable focus + trapping
  region) show the reframed gate is non-empty.
- **R2 (infinite dimension — open).** Brouwer fails in infinite dimensions;
  for semiflows whose time-t maps are compact (dissipative parabolic PDEs,
  Navier–Stokes in 2D), Schauder's fixed-point theorem yields the same
  conclusion. Not proved here; extension recorded as a Formalizer task.
- **R3 (nonconstructivity).** The proof locates no equilibrium; it only
  forbids their absence. Consistent with its role: it prunes the OP-14
  search space rather than solving OP-14.
- **R4 (attribution).** The rest-point theorem for compact convex positively
  invariant sets is classical (a standard Brouwer-limit argument); no
  novelty claimed (OP-16).
