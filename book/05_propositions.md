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
evolving-class analogue — balance bounds that survive a moving law — is open
and waits on OP-18 (well-posedness of the coupled layers).
