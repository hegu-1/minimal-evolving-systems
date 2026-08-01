# Conjecture Ledger

Rules (`AI_PROTOCOL.md`): every entry is precise and falsifiable; status ∈
{OPEN, UNDER ATTACK, REFUTED, PROVED}, where UNDER ATTACK ⟺ the attack log
is non-empty and undecided; attack logs are **append-only**. A PROVED
conjecture moves to `book/06_theorems.md` with its proof filed in `proofs/`.

### C-001 · Universal quadruple representation

- **Statement (as received, third intake 2026-07-24):** every system capable
  of long-term persistence and sustained evolution can be represented as a
  quadruple (Δ, P, K, I).
- **Status:** UNDER ATTACK — not yet falsifiable as stated
- **Attack log:**
  - 2026-07-24 — Claude (Writer) — *Triviality attack.* Without (i) a
    structure-preservation requirement on "represented as" and (ii)
    non-degeneracy conditions (K a proper restriction, I non-constant, P
    non-identity), universal frameworks represent everything and the claim is
    unfalsifiable — the fate of "everything is a category". Outcome: the
    statement must be strengthened before any mapping proof (ROADMAP items
    2–4) can count as evidence.
  - 2026-07-24 — Claude (Writer) — *Structure revision.* The target quadruple
    changed to 𝓜 = (X, Φ, K, B) (fourth intake; I deleted by counterexample,
    OP-7). The statement must be re-issued for 𝓜; the triviality conditions
    above still apply. Additional bite: OP-15 (non-canonicity of B) means
    "representable" must either specify a canonical B or quantify over B —
    until then the conjecture cannot even be restated.
  - 2026-07-25 — Claude (Writer) — *Restatement (v2 below).* OP-15 resolved
    (B out of the structure), removing that obstruction; non-degeneracy
    conditions incorporated per the first attack. Residual dependence: the
    ambient class 𝒞 is still undefined (OP-3), and D3's split-relativity
    (OP-17) infects "evolving" itself.

### C-001 (v2) · Non-degenerate two-layer representation

- **Statement (2026-07-25, maintainer-directed step):** every system of the
  evolving class (D3, under a declared state/law split) within the ambient
  class 𝒞 [OP-3 — to be defined] admits a representation 𝓜 = (X, K, U)
  that is:
  (i) *structure-preserving* — a trajectory-level embedding of the system's
  dynamics into the coupled-layer dynamics, commuting with time evolution;
  (ii) *non-degenerate* — K ⊊ 𝓕(X) (the constraint is real), U ≢ 0 (the
  system is not merely persisting), and the embedding is non-constant.
- **Falsification target:** exhibit a system in 𝒞 admitting no such
  representation, or show that some system admits only degenerate ones.
- **Status:** UNDER ATTACK — falsifiability improved but still contingent on
  OP-3 (𝒞 undefined) and OP-17 (split-relativity)
- **Attack log:**
  - 2026-07-25 — Claude (Writer) — *Residual-dependence note (above), carried
    into the restatement itself.* Until 𝒞 is defined, "every system in 𝒞"
    quantifies over nothing checkable.
  - 2026-07-28 — Claude (Writer) — *Predictive-minimality attack (motivated
    by `mappings/cognition.md`).* Clause (ii) excludes U ≡ 0 but not *idle*
    U: inflate the state space (X′ = history space × a dummy factor), let U
    act non-trivially only on the dummy factor, and embed the process as its
    own accumulating history. The result is structure-preserving, has K ⊊
    𝓕(X′), U ≢ 0, and a non-constant embedding — yet compresses nothing and
    carries no information about the system's law. C-001 v2 is then
    satisfiable for every system in any reasonable 𝒞: unfalsifiable again
    (same family as the 07-24 triviality attack). Candidate repair: add
    (iii) *predictive minimality* — the representation admits no proper
    reduction (quotient or closed subspace) that remains structure-preserving
    and predictively sufficient; cf. Kalman minimal realization and
    causal-state minimality. With (iii), divergent-statistical-complexity
    processes become a live falsification family (they admit no bounded
    minimal state). Outcome: the statement needs clause (iii) before the
    ROADMAP mapping proofs can count as evidence.

### C-002 · Collapse–instability transfer

- **Motivation.** The OP-14 chain P-5…P-9 is classical *per domain*; its
  candidate contribution is a *transfer* (OP-16 locus iii): one abstract
  statement whose instantiation gives a non-obvious, checkable parallel across
  unrelated domains. This conjecture states that candidate precisely so it can
  be attacked.
- **Setting.** Let 𝒟 be the class of dissipative iterative systems on ℝⁿ — a
  flow (or the Euler flow of a map) with a bounded absorbing region C (P-1) and
  finitely many equilibria in C. Call convergence of a trajectory to an
  equilibrium **collapse**.
- **Statement (three clauses, (b)/(c) falsifiable):**
  - **(a) [proved: P-9 instantiated]** In any member of 𝒟, a.e. trajectory
    avoids collapse **if** every equilibrium in C has a *linear escape direction*
    (an eigenvalue of DF with Re > 0). (One-way, per P-9; the converse fails on
    the d_u = 0 residue — cf. the ẋ = x² example — so this is not an iff.)
  - **(b) [structural transfer]** The following are the same phenomenon —
    collapse in 𝒟 — under a common cure: *representation collapse / oversmoothing*
    in deep residual-network depth dynamics; *plateau/mode collapse* in policy
    optimization; *laminar collapse* in forced-dissipative fluid flow. In each,
    the empirical anti-collapse device — skip connections / normalization;
    exploration / entropy regularization; sustained forcing — acts by giving the
    collapsed equilibrium a linear escape direction (introducing an eigenvalue
    with Re > 0).
  - **(c) [quantitative transfer]** Near the collapsed equilibrium in the
    low-noise / weak-coupling regime, the escape (non-collapse) rate is governed
    by the leading unstable eigenvalue Re λ⁺ of the collapsed equilibrium, with
    the *same* functional dependence across the three domains.
- **Falsification targets:** a domain anti-collapse device that provably does
  **not** add an unstable direction to the collapsed equilibrium; a collapse
  that occurs while every equilibrium is unstable; or a domain whose escape-rate
  law is not governed by Re λ⁺.
- **First checkable instance (transformer, `mappings/transformer.md`):** for a
  residual attention block δ_{ℓ+1} = δ_ℓ + Attn(δ_ℓ) the collapsed (rank-1)
  fixed point has Jacobian I + D(Attn); pure attention contracts (rank collapse,
  cf. Dong–Cordonnier–Loukas 2021, *to be read*), while the residual `+I` shift
  can push an eigenvalue past the unit circle — a linear escape direction. (b)
  then predicts: skip connections prevent oversmoothing a.e. **iff** they
  destabilize the rank-1 fixed point; (c) predicts the un-collapse rate tracks
  the leading unstable eigenvalue. Both are measurable.
- **Status:** OPEN (proposed 2026-08-01, Writer). Novelty is *not* claimed for
  (a); the OP-16 delta, if any, is the transfer (b)+(c) — specifically the
  common quantitative law (c) — and it is unverified. (a) is classical.
- **Attack log:**
  - 2026-08-01 — Claude (Writer) — *Obviousness self-attack.* Each clause-(b)
    instance is separately known in its own field (oversmoothing↔rank collapse;
    RL plateaus; laminar–turbulent transition). The conjecture has content only
    if (c)'s common functional law is real and not merely the shared triviality
    "linear instability sets the local escape rate." Guard: (c) must be checked
    with an *independently computed* Re λ⁺ predicting the rate, not fit post hoc
    (the discipline used on the earlier RL escape-time / Arrhenius study, which
    is prior cross-domain evidence for a shared escape law). Until (c) survives
    that check in ≥ 2 domains, C-002 is DISCUSSION-grade, not evidence.
  - 2026-08-01 — Claude (Writer) — *(c) REFUTED for the transformer/RL pair
    (experiment).* `MES_transformer_collapse_test.py`, real softmax attention.
    (b) confirmed: destabilizing the transverse (consensus-orthogonal) mode
    stops oversmoothing. (c) refuted: under step noise ε the transformer's
    stationary non-consensus energy is V_stat ∝ ε (log–log slope 1.006,
    V/ε ≈ 43 constant) — the linear / Ornstein–Uhlenbeck law — whereas the RL
    barrier-plateau escape obeys exp(barrier/ε) (Arrhenius). The two escape laws
    differ, so **there is no common quantitative law (c)**. "Collapse" splits
    into ≥ 2 universality classes (linear spectral-gap vs nonlinear Arrhenius),
    distinguished by whether the collapsed state is a linearly-stable fixed
    point or a barrier-separated well. Consequence: C-002's *structural* clause
    (b) holds but is a reframing of known per-domain facts; the *quantitative*
    delta the conjecture was built to test does not exist. **No OP-16 novelty in
    this transfer.** Status downgraded: (a) classical, (b) DISCUSSION reframing,
    (c) REFUTED. The candidate is closed as a novelty source; see
    `mappings/transformer.md`.

### C-003 · The slow-drift transfer (the U-layer candidate)

- **Motivation.** C-002 tested only the *state layer* (classical). This
  conjecture tests the layer that is v2's actual novelty candidate: the
  law-update U (OP-9). If any OP-16 delta exists, the strongest prior is here.
- **Setting.** A two-layer 𝓜 with a *slow* law: dδ/dt = F_φ(δ) (fast; δ relaxes
  to the attractor A(φ) of the frozen law φ), ε dφ/dt = U(φ) (slow), and U the
  gradient of a fast-attractor functional, U(φ) = ∇_φ Ψ(φ), Ψ(φ) a scalar read
  off A(φ).
- **Statement:**
  - **(a) [classical — Fenichel / averaging].** To leading order in ε the slow
    layer is a gradient flow on law-space, dφ/dt = ∇_φ Ψ(φ), with the fast layer
    slaved to A(φ).
  - **(b) [structural transfer].** The **canonical equation of adaptive
    dynamics** (φ = trait, fast layer = ecology, Ψ = invasion fitness;
    Dieckmann–Law) and the **meta-learning outer loop** (φ = meta-parameter,
    fast layer = inner-loop task, Ψ = meta-objective at the inner solution) are
    both this slow gradient flow.
  - **(c) [delta candidate — falsifiable].** The adaptive-dynamics
    *classification of singular points* transfers. At a singular φ* the sign of
    the fast-functional Hessian in the "mutant" direction decides the fate:
    convergence-stable **and** a fitness maximum ⇒ ESS (the slow layer stays
    put); convergence-stable **but** a fitness *minimum* ⇒ **branching** — the
    slow layer spontaneously splits into coexisting specialized values. C-003(c)
    claims *any* two-layer 𝓜 in this class inherits the same dichotomy — in
    particular **meta-learning specializes into coexisting sub-solutions at a
    convergence-stable-non-ESS meta-optimum**, governed by the same Hessian sign.
- **Falsification target:** a meta-learning (or other U-layer) system at a
  branching-classified φ* that does **not** split, or a split that violates the
  Hessian sign; equivalently, a domain where the singular-point classification
  fails to control the slow layer's fate.
- **Status:** OPEN (proposed 2026-08-01, Writer). (a) classical; (b) a reframing
  of two known derivations; **(c) is the delta candidate and is UNTESTED** — the
  novelty-deciding step is a meta-learning experiment plus a literature check.
- **Attack log:**
  - 2026-08-01 — Claude (Writer) — *Structural check + honest prior.* The
    adaptive-dynamics side is textbook: for the Doebeli–Dieckmann model
    (Gaussian resource σ_k, competition σ_a) the mutant-direction fitness
    Hessian at x*=0 is s'' = 1/σ_a² − 1/σ_k², so branching ⟺ σ_a < σ_k — a
    clean, domain-agnostic second-order condition, which is the transferable
    object. (An individual-based simulation was attempted but was
    under-resolved in the ESS case and is **not** used as evidence; the
    analytic condition suffices for the adaptive-dynamics side.) *Honest prior
    on novelty:* the evolution↔learning correspondence is heavily studied
    (Baldwin effect; evolutionary game theory ↔ RL; mixture-of-experts /
    multi-task specialization). C-003(c) may therefore be a *known* reframing,
    as C-002(b) was. It is worth stating precisely and testing because it is the
    one candidate that uses the U-layer and makes a *non-obvious, checkable*
    prediction (meta-learning branching), but the burden is on (c) surviving a
    meta-learning experiment and a literature delta. Until then C-003 is
    DISCUSSION-grade, not evidence, and the two-refuted/likely-known pattern
    (with C-002) is itself evidence that the honest project frame may be (A)
    reformulation, not a novelty theorem.

## Template

### C-000 · <short name>

- **Statement:** <a single falsifiable mathematical statement>
- **Status:** OPEN
- **Attack log:**
  - YYYY-MM-DD — <agent> — <attack attempted, outcome>
