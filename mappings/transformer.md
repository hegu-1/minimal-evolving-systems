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

## What this mapping does NOT establish

A mapping is an interpretation, never evidence. I is not even identified yet.
