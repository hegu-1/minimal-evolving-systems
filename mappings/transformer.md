# Mapping: Transformer

STATUS: DISCUSSION — correspondence proposed (third intake, 2026-07-24);
the representation proof is ROADMAP item 3 and has not begun.

## Proposed correspondence (training regime)

*(Updated after the fourth intake: I deleted, B in its place; symbols aligned
to 𝓜 = (X, Φ, K, B).)*

| 𝓜 | Transformer candidate |
|---|---|
| X (δ ∈ X) | loss / error signal |
| Φ | backpropagation |
| K | architecture |
| U | gradient update (parameters define the operator) — U is outside 𝓜, see OP-9 |
| B | training loss as balance functional (candidate; balance decomposition unexamined) |

Writer's note: the correspondence conflates regimes. At inference time the
natural propagation is the forward pass, with Δ as activation differences —
a *different* quadruple. Whether training and inference are one system with
two propagations, or two systems, must be settled by the formal definitions;
OP-9 (where U lives) is upstream of this. A second overlap is deliberate but
not yet precise: backpropagation (Φ) *computes* gradients — error
propagation — while U *applies* them, updating the law; the formal
definitions must separate these cleanly.

## Depth / inference regime: representation collapse (C-002 test)

A second, cleaner instantiation — the *depth* dynamics, not training. Tokens
X ∈ ℝ^{N×d} propagate through residual attention blocks

  X_{ℓ+1} = X_ℓ + η (A(X_ℓ) − I) X_ℓ,   A = row-softmax(X X^ᵀ/√d),

the Euler flow of a dissipative system: normalization/boundedness supplies the
absorbing region (P-1), the consensus (rank-1) state is an equilibrium, and
repeated averaging contracts toward it — **oversmoothing** = collapse to that
equilibrium (cf. Dong–Cordonnier–Loukas 2021, *to be read*).

This is the transformer instance of **C-002** (collapse–instability transfer).
A laptop experiment (`MES_transformer_collapse_test.py`, run 2026-08-01, real
softmax attention, N=24, d=8) gives:

- **(b) structural — HOLDS.** Pure smoothing collapses (non-consensus energy
  V_ℓ → 5·10⁻¹¹). Adding a transverse-amplifying term (an anti-collapse device)
  pushes the transverse multiplier past 1 and stops collapse (V grows). So the
  anti-collapse device acts exactly by *destabilizing the collapsed
  equilibrium* — P-9's mechanism, as C-002(b) predicts.
- **(c) quantitative — FAILS.** Under step noise ε, the stationary
  non-consensus energy is **V_stat ∝ ε** (log–log slope 1.006; V/ε ≈ 43,
  constant) — the **linear / Ornstein–Uhlenbeck** law, *not* Arrhenius. The
  RL barrier-plateau instance (prior work) obeys **exp(barrier/ε)**. The two
  domains obey **different** escape laws.

**Reading.** C-002's *structural* unification survives; its *quantitative*
common-law clause is refuted for this pair. "Collapse" is therefore **not one
universality class**: it splits into linear / spectral-gap (oversmoothing — you
fall into a stable fixed point, escape by local instability, OU under noise) and
nonlinear / Arrhenius (a plateau separated by a barrier, escape by large
deviations). The distinguishing invariant is whether the collapsed state is a
linearly-stable fixed point or a barrier-separated well — elementary once named.

## What this mapping does NOT establish

A mapping is an interpretation, never evidence. **The C-002 test above is
evidence only against C-002(c)** (a refutation, which the protocol admits from
any agent) — it does *not* promote any concept, and it does not by itself
locate an OP-16 delta. On the contrary: it *eliminates* the common-quantitative-
law candidate. The surviving structural transfer (b) is a reframing of known
per-domain facts (oversmoothing; RL plateaus; laminar collapse), not a theorem.
The training-regime quadruple above remains unsettled (I is not identified;
regime-conflation open, OP-9 upstream).
