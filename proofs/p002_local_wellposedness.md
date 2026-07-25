# P-2 · Local well-posedness of the coupled layers

STATUS: PROPOSITION — complete proof below. Writer, 2026-07-25 (sixth step).
Settles the ambient-space half of OP-18.

## Setting

Let X be a Banach space (differences) and 𝓖 a Banach space of evolution
laws, linearly embedded into the vector fields on X via evaluation, with a
constant C ≥ 0 such that for all F ∈ 𝓖 and δ, δ′ ∈ X:

- (E1) ‖F(δ) − F(δ′)‖_X ≤ C ‖F‖_𝓖 ‖δ − δ′‖_X   (Lipschitz evaluation)
- (E2) ‖F(δ)‖_X ≤ C ‖F‖_𝓖 (1 + ‖δ‖_X)          (linear growth)

Let U : 𝓖 × X → 𝓖 be locally Lipschitz: for each R > 0 there is L_R with
‖U(F, δ) − U(F′, δ′)‖_𝓖 ≤ L_R (‖F − F′‖_𝓖 + ‖δ − δ′‖_X) whenever all norms
are ≤ R. The coupled system is

  dδ/dt = F(δ),  dF/dt = U(F, δ),  (δ(0), F(0)) = (δ₀, F₀).

## Statement

**(a)** For every (δ₀, F₀) ∈ X × 𝓖 there exist T > 0 and a unique
(δ, F) ∈ C¹([0, T]; X × 𝓖) solving the coupled system.

**(b)** Along the realized law trajectory t ↦ F_t of that solution, for every
s ∈ [0, T] and η ∈ X the non-autonomous equation dη/dt = F_t(η), η(s) = η
has a unique solution on [s, T]; the resulting operators
Φ_{t,s} : X → X satisfy Φ_{s,s} = Id, the process property
Φ_{t,r} = Φ_{t,s} ∘ Φ_{s,r} (r ≤ s ≤ t), and δ_t = Φ_{t,0}(δ₀).

## Proof

**(a)** Work on Z = X × 𝓖 with norm ‖(δ, F)‖_Z = ‖δ‖_X + ‖F‖_𝓖, and define
G : Z → Z by G(δ, F) = (F(δ), U(F, δ)).

*Step 1: G is locally Lipschitz.* Fix z₀ = (δ₀, F₀), let R = ‖z₀‖_Z + 1, and
take z = (δ, F), z′ = (δ′, F′) in the closed ball B̄(z₀, 1) (so all norms
≤ R). First component: since F − F′ ∈ 𝓖, (E1) applied to F and (E2) applied
to F − F′ give

  ‖F(δ) − F′(δ′)‖_X ≤ ‖F(δ) − F(δ′)‖_X + ‖(F − F′)(δ′)‖_X
    ≤ C R ‖δ − δ′‖_X + C (1 + R) ‖F − F′‖_𝓖
    ≤ C (1 + R) ‖z − z′‖_Z.

Second component: ‖U(F, δ) − U(F′, δ′)‖_𝓖 ≤ L_R ‖z − z′‖_Z. Hence G is
Lipschitz on B̄(z₀, 1) with constant Λ = C(1 + R) + L_R, and bounded there by
M := ‖G(z₀)‖_Z + Λ < ∞.

*Step 2: Picard contraction.* Let T = min(1/M, 1/(2Λ)) and let

  𝒮 = { w ∈ C([0, T]; Z) : w(0) = z₀, sup_{t} ‖w(t) − z₀‖_Z ≤ 1 },

a complete metric space under the sup metric. Define
(𝒫w)(t) = z₀ + ∫₀ᵗ G(w(s)) ds (Bochner integral of a continuous integrand).
For w ∈ 𝒮: ‖(𝒫w)(t) − z₀‖_Z ≤ T M ≤ 1, so 𝒫 maps 𝒮 into 𝒮. For w, w′ ∈ 𝒮:

  ‖𝒫w − 𝒫w′‖_sup ≤ T Λ ‖w − w′‖_sup ≤ ½ ‖w − w′‖_sup.

By the Banach fixed-point theorem 𝒫 has a unique fixed point z(·) in 𝒮.
Since G ∘ z is continuous, the integral equation gives z ∈ C¹ and
z′(t) = G(z(t)): a solution.

*Step 3: uniqueness among all C¹ solutions.* If z̃ is another solution on
[0, T′], both trajectories are compact, hence contained in a common ball on
which G is Lipschitz with some constant Λ′; then
‖z(t) − z̃(t)‖_Z ≤ Λ′ ∫₀ᵗ ‖z(s) − z̃(s)‖_Z ds, and Grönwall gives
z ≡ z̃ on the common interval. ∎(a)

**(b)** Along the solution, t ↦ F_t is continuous, so
S := sup_{[0,T]} ‖F_t‖_𝓖 < ∞. The time-dependent field f(t, η) = F_t(η) is
continuous in t and, by (E1), Lipschitz in η with the uniform constant C S;
by (E2) it has linear growth uniformly in t. The standard non-autonomous
Picard argument (identical in form to Step 2) gives a unique local solution
through every (s, η), and linear growth plus Grönwall
(‖η(t)‖ ≤ (‖η(s)‖ + C S (t − s)) e^{C S (t − s)}) excludes blow-up before T,
so solutions extend to all of [s, T]. Define Φ_{t,s}(η) as the value at time
t of the solution through (s, η). Then Φ_{s,s} = Id by construction, and for
r ≤ s ≤ t the curves t ↦ Φ_{t,r}(η) and t ↦ Φ_{t,s}(Φ_{s,r}(η)) both solve
the same equation with the same value at time s, hence coincide by
uniqueness: the process property. Finally δ_t solves this equation with
δ(0) = δ₀, so δ_t = Φ_{t,0}(δ₀). ∎(b)

## Remarks

- **R1 (K not yet addressed — the remaining half of OP-18).** P-2 solves in
  the ambient space 𝓖. Keeping F_t ∈ K for a closed K ⊊ 𝓖 requires a
  tangency condition on U at the boundary of K (Nagumo-type invariance);
  not proved here.
- **R2 (the suspension objection acquires formal teeth — feeds OP-17).**
  Step 1–2 construct an autonomous local semiflow on the *product* X × 𝓖.
  The evolving-presentation operators Φ_{t,s} of part (b) exist only
  *relative to a realized law trajectory*: change δ₀ and the law curve F_t
  changes too, so {Φ_{t,s}} is not intrinsic to the system, only to the
  trajectory. The static presentation (product) is canonical; the evolving
  presentation is trajectory-relative. Any canonical-split proposal (OP-17)
  must live with this asymmetry.
- **R3 (global existence — open).** Beyond [0, T] one needs a priori bounds
  on both layers; the natural route is a two-layer balance estimate
  (P-1-style on the δ-layer plus a growth bound on ‖F_t‖_𝓖). Future work.
- **R4 (non-vacuity).** The space of bounded Lipschitz vector fields with
  norm ‖F‖ = ‖F(0)‖ + Lip(F) satisfies (E1)–(E2); the hypotheses describe a
  real class.
- **R5 (attribution).** Entirely classical technique (Picard–Lindelöf /
  Banach fixed point in Banach spaces); recorded for the framework, no
  novelty claimed (OP-16).
