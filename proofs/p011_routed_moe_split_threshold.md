# P-11 · A frequency-dependent learning layer splits, with a closed-form threshold

STATUS: PROPOSITION — complete proof below. Writer, 2026-08-01. Companion to
P-10: P-10 shows a resident-independent law layer *cannot* diversify; P-11
exhibits a system built from machine-learning primitives only, whose per-type
fitness *is* resident-dependent, in which the unspecialised configuration loses
stability at an explicitly computed threshold.

## The system

Machine-learning primitives only — no ecological vocabulary.

- **tokens** y ~ N(0, σ²), σ > 0;
- **experts** m = 2 constants φ₁, φ₂ ∈ ℝ; expert i predicts the value φ_i;
- **routing** g_i(y) = softmax_i( −(y − φ_i)² / (2τ) ), routing temperature τ > 0;
- **loss** L(φ₁, φ₂) = E_y[ Σ_i g_i(y) (y − φ_i)² ];
- **slow layer** gradient flow on L. This is U.

Write φ₁ = u + v, φ₂ = u − v; v is the **split coordinate** and v = 0 is the
unspecialised (collapsed) configuration in which both experts predict the same
value.

The routing makes expert i's contribution depend on where the *other* expert
sits: the per-expert fitness is resident-dependent. This is the two-argument U
demanded by P-10 R2, realised without importing anything from population
biology.

## Statement

Let σ > 0 and τ > 0. Then:

- **(i)** L is even in u and in v; (u, v) = (0, 0) is a critical point, and the
  Hessian there is diagonal in (u, v).
- **(ii)** On the slice u = 0,
    L(v) = σ² + v² − 2v · E_y[ y · tanh(v y / τ) ],
  a C^∞ even function of v.
- **(iii)** L(v) = σ² + (1 − 2σ²/τ) v² + (2σ⁴/τ³) v⁴ + O(v⁶); in particular
    ∂²L/∂v² |₀ = 2 (1 − 2σ²/τ),   ∂²L/∂u² |₀ = 2.
- **(iv)** Hence the collapsed configuration is a strict local minimum of L iff
  **τ > 2σ²**, and is a saddle — stable in u, unstable in the split direction —
  iff **τ < 2σ²**. The bifurcation at τ = 2σ² is a **supercritical pitchfork**
  (the quartic coefficient 2σ⁴/τ³ is strictly positive), so v = 0 remains a
  minimum at threshold and the emerging split is continuous, with
    v\* = τ^{3/2} (2σ²/τ − 1)^{1/2} / (2σ²) + o( (2σ²/τ − 1)^{1/2} )
  as τ ↑ 2σ².
- **(v) (control arm — P-10 in this system.)** Replace the routing by any
  position-independent assignment g_i ≡ 1/m. Then L = σ² + u² + v² for m = 2,
  whose unique critical point is the collapsed configuration, a strict global
  minimum for every τ. No split occurs at any temperature.

## Proof

**(i).** The token law is symmetric about 0, so L(−u, v) = L(u, v) via y ↦ −y,
and L(u, −v) = L(u, v) by relabelling the two experts. Both symmetries force
the odd first derivatives and the mixed second derivative to vanish at the
origin.

**(ii).** With φ₁ = u + v, φ₂ = u − v,
  (y − φ₂)² − (y − φ₁)² = 4 v (y − u),
so g₁(y) = ς( 4v(y−u) / (2τ) ) = ς( 2v(y−u)/τ ) with ς the logistic function,
and g₂ = 1 − g₁. At u = 0, g₁(y) = ς(2vy/τ). Then
  L = E[ g₁ (y−v)² + (1−g₁)(y+v)² ]
    = E[ y² + v² ] + E[ (g₁ − (1 − g₁)) · (−2yv) ]
    = σ² + v² − 2v · E[ y (2g₁ − 1) ].
Since 2ς(z) − 1 = tanh(z/2) and z = 2vy/τ, we get 2g₁ − 1 = tanh(vy/τ), which
is the stated formula. Smoothness in v follows from differentiation under the
integral sign: |∂_v^k ( y tanh(vy/τ) )| ≤ C_k |y|^{k+1}, Gaussian-integrable
for every k, uniformly for v in compacts.

**(iii).** By the same domination, the Taylor coefficients of
F(v) = E[y tanh(vy/τ)] at 0 are obtained term by term from
tanh(w) = w − w³/3 + O(w⁵) with w = vy/τ:
  F(v) = (v/τ) E[y²] − (v³ / 3τ³) E[y⁴] + O(v⁵)
       = v σ²/τ − v³ σ⁴/τ³ + O(v⁵),
using E[y²] = σ², E[y⁴] = 3σ⁴. Therefore
  L(v) = σ² + v² − 2v F(v) = σ² + v²(1 − 2σ²/τ) + 2v⁴ σ⁴/τ³ + O(v⁶).
For the u-direction, setting v = 0 collapses both experts to u and gives
L(u, 0) = E[(y − u)²] = σ² + u², so ∂²_u L|₀ = 2.

**(iv).** Immediate from (iii) and (i): the origin is a strict local minimum iff
both diagonal second derivatives are positive, i.e. iff 1 − 2σ²/τ > 0. Since
the quartic coefficient is strictly positive for all τ > 0, the normal form on
the slice is the supercritical pitchfork a v² + b v⁴ with b > 0; minimising
gives v\*² = (2σ²/τ − 1) τ³ / (4σ⁴) to leading order.

**(v).** With g_i ≡ 1/2, L = ½E[(y−φ₁)²] + ½E[(y−φ₂)²] = σ² + u² + v². ∎

## Numerical confirmation

The predictions of (iii)–(v) were checked against the model **definition** —
loss and gradient computed by quadrature from the integral, never from the
expansion — with σ = 1, so the predicted threshold is τ\* = 2.
Script: `tools/c003_branching_check.py`.

Curvature at the collapsed configuration, analytic 2(1 − 2σ²/τ) vs numerical:

| τ | analytic | numerical | rel. err |
|---|---|---|---|
| 0.50 | −6.000000 | −5.999968 | 5.3e−06 |
| 1.00 | −2.000000 | −1.999996 | 2.0e−06 |
| 1.50 | −0.666667 | −0.666665 | 1.8e−06 |
| 1.90 | −0.105263 | −0.105263 | 5.5e−06 |
| 2.00 | 0 | 0.000000 | — |
| 2.10 | +0.095238 | +0.095239 | 4.5e−06 |
| 3.00 | +0.666667 | +0.666667 | 2.2e−07 |
| 5.00 | +1.200000 | +1.200000 | 2.2e−08 |

Minimiser of L over the split coordinate: |v| > 0 for every τ < 2 tested
(0.4 … 1.95) and |v| = 0 for every τ ≥ 2 tested (2.0 … 5.0) — the sign change
occurs exactly at the predicted τ\* = 2, not at a fitted value.

Pitchfork amplitude just below threshold, numerical |v| vs the quartic
prediction v\*, ratio → 1 as τ ↑ 2 (higher-order terms account for the drift):
1.0019 (τ = 1.995), 1.0038 (1.99), 1.0076 (1.98), 1.0152 (1.96), 1.0230 (1.94),
1.0390 (1.90), 1.0812 (1.80).

Control arm (v): position-independent routing gives |v| = 0 at every τ tested.

Exploratory, m = 4, gradient descent from a near-symmetric start (not part of
the proposition; the m ≥ 3 thresholds are not computed here): 4 distinct
positions at τ = 0.15–0.6, a doubly-occupied centre plus two outer positions at
τ = 1.0–1.5, and full collapse at τ = 3.

## Remark R1 — a joint potential is not a resident-independent fitness

The joint dynamics here *is* a gradient flow: both experts descend the single
scalar L. MoE routing has recently been analysed exactly this way — as a
congestion/potential game with softmax as the equilibrium (Mouzouni,
arXiv:2604.04230). This does **not** contradict P-10, and the distinction is
the same one P-10 R1 makes.

P-10's hypothesis (A) is that the fitness of a *variant law* is a function of
that variant alone. Here the loss share felt by an expert at position φ depends
on where the other expert sits — that is resident-dependence — even though the
*joint* objective is a single scalar on ℝ². A potential in the joint variable
and a resident-independent fitness in the single-law variable are different
conditions; only the latter is what P-10 forbids.

## What this proposition does NOT establish

- It does **not** verify the adaptive-dynamics singular-point classification.
  The Hessian computed here is that of the joint loss, not of an invasion
  fitness; the system has a fixed number of coexisting types and no rarity
  parameter, so the monomorphic-resident / rare-mutant construction does not
  literally apply. What is established is the *necessity* direction (P-10) plus
  a frequency-dependent instance with a closed-form threshold.
- The constant in τ\* = 2σ² is **model-specific**. It has the same *form* as the
  adaptive-dynamics condition "competition scale below resource scale" but is
  not obtained by matching kernel widths: identifying the routing kernel width
  with a competition width gives a different constant. The transfer supplies the
  structure (a second-order condition producing a supercritical pitchfork), not
  a universal number. Claiming otherwise would repeat the C-002 error.
- No OP-16 novelty is claimed for the pitchfork itself. That low routing
  temperature yields expert specialisation and high temperature yields collapse
  is folklore in the mixture-of-experts literature, and the inhibiting effect of
  routing overlap is documented empirically (arXiv:2505.22323, arXiv:2501.11873).
  The delta candidate lives in P-10, not here.
