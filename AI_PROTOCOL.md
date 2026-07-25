# AI Protocol

This file is the contract for every contributor, human or AI. Reading it is
mandatory before writing anything. If a conversation and the repository
disagree, the repository wins — change the repository, do not argue in chat.

## Reading order (mandatory before contributing)

`README.md` → `AI_PROTOCOL.md` → `ROADMAP.md` → `book/02_problem.md`

## Prime directive

> Delete assumptions before adding concepts.

A deletion with an argument is a contribution. An addition without demonstrated
necessity is damage.

## Epistemic classes

Every normative statement in `book/` or `proofs/` carries exactly one label:

| Label | Admission rule |
|---|---|
| **DEFINITION** | Mathematically precise; uses no undefined non-standard terms; usable without the surrounding prose. |
| **CANDIDATE** | A proposed primitive or definition that has not yet survived the four tests. The default state of everything in this repository. |
| **AXIOM** | An assumption we explicitly *failed to delete*. Must carry a note recording why deletion failed. |
| **PROPOSITION / THEOREM** | Carries a complete proof in `proofs/`. No proof, no label — "proof sketch" does not qualify. |
| **CONJECTURE** | Precise and falsifiable; lives in `proofs/conjectures.md` with a status and an append-only attack log. |
| **DISCUSSION** | Everything else. Non-normative; deletable without ceremony. |

## The four tests

No concept may be promoted to DEFINITION or claimed as primitive without
passing all four:

1. **Definition Test** — can it be mathematically defined?
2. **Minimality Test** — can it be removed? If yes, it is **not** primitive.
3. **Counterexample Test** — has a serious search for counterexamples been recorded?
4. **Mapping Test** — does it map to at least two unrelated domains? (`mappings/`)

## Roles

Roles bound *default behavior*, not permissions — any agent may record a
counterexample at any time.

| Agent | Role | Primarily writes |
|---|---|---|
| ChatGPT | **Builder** — constructs definitions, proposes structures, reduces assumptions | `notebook/`, proposals into `book/` as CANDIDATE |
| Claude | **Writer** — organizes documents, maintains consistency, writes formal text | `book/`, structural edits everywhere |
| Codex | **Formalizer** — LaTeX, proofs, repository tooling, PDF generation | `proofs/`, build tooling |
| Gemini (optional) | **Destroyer** — counterexamples, literature comparison, weakness identification | attack logs, `references/` |
| naze (maintainer) | Final authority on promotions, renames, and anything public-facing | everything |

## Rules for `mappings/`

A mapping is DISCUSSION, never evidence. Analogies do not support promotion.
Every mapping file must contain a section titled
**"What this mapping does NOT establish"**.

## Allowed / gated / forbidden

**Allowed without asking:** counterexamples; tightened definitions; refutations;
deletions with argument; notebook entries; consistency fixes.

**Gated on the maintainer:** introducing an AXIOM; renaming core terms;
promoting CONJECTURE → THEOREM; making anything public.

**Forbidden:** prose inflation; results without proofs; editing or deleting
attack-log entries (append only); importing terminology, claims, or branding
from the maintainer's other projects — this theory stands alone or not at all.

**Maintainer override.** The maintainer may explicitly override any rule in
this file, including Forbidden items; the override must be recorded in
`notebook/` with date and scope (precedent: the working name "NEPM-0",
2026-07-24). An unrecorded override is void.

**Boundary rule.** Propagating an already-recorded supersession into stale
files is a *consistency fix* (allowed without asking). Introducing or
changing a symbol or name not yet in the supersession chain is a *rename*
(gated on the maintainer).

*(Both clauses added 2026-07-25 by the Writer after a cold-read audit;
ratified by maintainer directive the same day — see `notebook/2026-07-25.md`.)*

## Style

The shortest correct statement wins. Every chapter opens with its STATUS line.
Write so that a mathematician with no context can object precisely.
