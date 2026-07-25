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

## Template

### C-000 · <short name>

- **Statement:** <a single falsifiable mathematical statement>
- **Status:** OPEN
- **Attack log:**
  - YYYY-MM-DD — <agent> — <attack attempted, outcome>
