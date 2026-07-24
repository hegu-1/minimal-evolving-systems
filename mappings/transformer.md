# Mapping: Transformer

STATUS: DISCUSSION — correspondence proposed (third intake, 2026-07-24);
the representation proof is ROADMAP item 3 and has not begun.

## Proposed correspondence (training regime)

| NEPM-0 | Transformer candidate |
|---|---|
| Δ | loss / error signal |
| P | backpropagation |
| K | architecture |
| U | gradient update (parameters define the operator) |
| I | (unidentified) |

Writer's note: the correspondence conflates regimes. At inference time the
natural propagation is the forward pass, with Δ as activation differences —
a *different* quadruple. Whether training and inference are one system with
two propagations, or two systems, must be settled by the formal definitions;
OP-9 (where U lives) is upstream of this.

## What this mapping does NOT establish

A mapping is an interpretation, never evidence. I is not even identified yet.
