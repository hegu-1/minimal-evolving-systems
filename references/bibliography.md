# Bibliography

STATUS: to survey (Destroyer role, `AI_PROTOCOL.md`). No entry may be cited
in `book/` or `proofs/` unless the citing agent has actually read it.
Attribution pointers ("cf.") to standard references are permitted
provisionally, but must be verified against the actual texts before v0.1.

Areas to compare against before Version 0.1 claims any novelty:

- Dynamical systems / topological dynamics (flows, generators, semigroups)
- Abstract state machines and automata theory
- Category-theoretic and compositional systems theory
- Algorithmic information theory (minimal description length)
- Open-ended evolution literature (artificial life)

## Mandatory comparison targets for OP-16 (added fourth intake)

𝓜 = (X, Φ, K, B) with P-1 currently reconstructs classical dissipative
dynamical systems theory. Before any novelty claim, the following must be
actually read and the delta stated:

- R. Temam, *Infinite-Dimensional Dynamical Systems in Mechanics and
  Physics* — absorbing sets, global attractors, energy estimates (P-1's
  home ground).
- J. C. Robinson, *Infinite-Dimensional Dynamical Systems* — semigroups,
  attractors for PDE flows.
- Metastability literature (e.g., Bovier & den Hollander, *Metastability*) —
  the τ_internal ≪ τ_lifetime definition of Object.
- Non-autonomous / random dynamical systems (processes, cocycles) — the
  mathematical home of the missing U-layer (OP-9).
- Coherent structures in turbulence — the vortex-as-object claim.

## U-layer comparison targets (added 2026-08-01, off P-10 / C-003)

The v2 U layer is the OP-16 locus (ii). A literature check was run 2026-08-01
(arXiv API over cs.LG/cs.AI/cs.NE/cs.MA/stat.ML plus web search). These are the
works whose delta must be stated before any claim about the law layer. Items
marked **read** were checked directly; the rest are recorded targets.

Adaptive dynamics (the source of the two-argument fitness):
- J. A. J. Metz, S. A. H. Geritz, et al. — adaptive dynamics foundations;
  S. A. H. Geritz, É. Kisdi, G. Meszéna, J. A. J. Metz (1998), "Evolutionarily
  singular strategies and the adaptive growth and branching of the evolutionary
  tree", *Evolutionary Ecology* 12:35–57 — the singular-point classification
  used in P-10 R1.
- U. Dieckmann & R. Law (1996) — the canonical equation.
- M. Doebeli & U. Dieckmann — the Gaussian resource/competition branching
  condition σ_a < σ_k.

Prior art on exporting adaptive dynamics **outside biology** (so the *move* is
not claimable):
- F. Dercole, U. Dieckmann, M. Obersteiner, S. Rinaldi (2008), "Adaptive
  dynamics and technological change", *Technovation* 28(6):335–348.
- F. Dercole & S. Rinaldi (2008), *Analysis of Evolutionary Processes*,
  Princeton.
- C. Chow, C. Wilke, C. Ofria, R. Lenski, C. Adami (2004), "Adaptive radiation
  from resource competition in digital organisms", *Science* 305:84–86 —
  branching inside a computational substrate.

Two-timescale / slaved-fast-layer formulations in learning (so C-003(a) is
conceded classical):
- V. Borkar (1997), "Stochastic approximation with two time scales",
  *Systems & Control Letters* 29(5):291–294.
- M. Heusel et al. (2017), "GANs trained by a two time-scale update rule …",
  NeurIPS, arXiv:1706.08500.
- M. Hong, H.-T. Wai, Z. Wang, Z. Yang, "A two-timescale framework for bilevel
  optimization", arXiv:2007.05170.
- **Most threatening prior work for the U layer:** G. Borghi, S. Im,
  L. Pareschi (2026), "Two-time-scale learning dynamics: a population view of
  neural network training", arXiv:2603.19808 — fast layer equilibrates to a
  Gibbs measure, *inducing an effective fitness* F̄(h) for the slow layer, tied
  explicitly to bilevel optimization and replicator–mutator models; Remark 11
  raises multimodal steady states as open. F̄ is a function of h alone, hence
  resident-independent, hence inside P-10's hypothesis (A) — the framework
  provably cannot branch. Must be cited whenever C-003 (v2) c₁ is stated.
- Fenichel / geometric singular perturbation theory applied to bilevel or
  meta-learning: **absent from the search**; the field uses Borkar's ODE method
  and Lyapunov constructions instead.

The fixed-objective vs interaction-derived-fitness distinction (so half of
C-003 v2 c₁ is conceded):
- S. Ficici (2004), *Solution Concepts in Coevolutionary Algorithms*, PhD
  thesis, Brandeis; E. Popovici, A. Bucci, R. P. Wiegand, E. de Jong (2012),
  "Coevolutionary principles", in *Handbook of Natural Computing* — objective
  vs subjective fitness, stated ~20 years ago without adaptive-dynamics
  machinery or a branching theorem.
- D. Balduzzi et al. (2018/2019), "The mechanics of n-player differentiable
  games" / "Differentiable game mechanics", arXiv:1905.04926 — the
  potential/Hamiltonian (symmetric/antisymmetric) decomposition: the ML-native
  form of "is this the gradient of a fixed scalar?", but silent on
  diversification.
- D. Balduzzi et al. (2019), "Open-ended learning in symmetric zero-sum games",
  arXiv:1901.08106 — game-theoretic niching, transitive vs cyclic.
- J. Z. Leibo et al. (2019), "Malthusian reinforcement learning",
  arXiv:1812.07019 — competition ⇒ niche differentiation, empirical.
- C. Mouzouni (2026), "Three phases of expert routing", arXiv:2604.04230 — MoE
  routing as a congestion/potential game; relevant to P-11 R1.

**Known gaps in this search** (recorded so the novelty question stays open):
arXiv queries hit abstracts only; Semantic Scholar was rate-limited, so the
decisive check — enumerating CS-category citers of Geritz et al. 1998 — was
**not** run; GECCO / ALIFE / ECJ / IEEE-TEVC are underrepresented, and that is
where a hidden precedent is most likely to sit.
