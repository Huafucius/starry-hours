---
name: create-figure-skill
description: Methodology and workflow for distilling a specific public figure into a reusable, callable agent skill. Use this skill whenever the user wants to turn a specific historical or contemporary public figure into a skill artifact — including requests like "做一个鲁迅 skill", "make me a Feynman skill", "distill how Munger thinks into something reusable", "build a [person] perspective", "create a figure skill for X", or any request that names a specific real person and asks to package their mindset, judgment, or voice into a reusable skill folder. Triggers on verbs like create / build / make / distill / generate / 做 / 建 / 生成 combined with a specific named person. Do NOT trigger when the user is merely asking about or discussing a figure without requesting a skill artifact be created ("explain Feynman's method", "tell me about 鲁迅"). Do NOT trigger for books or brands — those will have sister skills.
---

# Create Figure Skill

The user wants to turn a specific public figure into a reusable agent skill. The output is a complete `skills/<figure-slug>/` folder that future agents can invoke in five modes: dialogue, voice, methodology, critique, advisory.

This is a methodology, not a template filler. Every figure is different; the research must be responsive to the evidence that actually exists for that person.

## Four principles that bind every phase

1. **Research must be saturated.** Do not ration, do not sample. If a source is findable, find it. Agents have a superpower humans lack — parallel retrieval at scale. Use it.
2. **Adversarial is an obligation.** Every strong claim about the figure is checked against its opposition. A skill built only from admiring sources is a whitewash.
3. **Honesty over completeness.** If evidence runs out for a dimension, say so — and record the queries you tried. Do not fabricate plausible content. This is Malcolm's "show the seams".
4. **The model's prior is a corpus.** Before any web access, snapshot what the model already believes about this figure. That snapshot is a source in its own right — the distilled consensus of training data — and must be weighed against external evidence later. It is never deleted or revised.

Before starting, read `references/research-stance.md`. That file encodes the posture that makes research non-trivial; without it, every later step reverts to laziness.

## The workflow — six phases

Each phase produces concrete artifacts that the next phase consumes. Do not skip phases. Do not reorder them.

### Phase 1 · Frame

Anchor who is being distilled and how the skill will be triggered. Ambiguity here cascades through every later phase — a skill built for the wrong person, or one that fires on the wrong prompts, is worse than no skill.

1. Confirm the exact figure with the user. Disambiguate same-name cases (which Charlie Chaplin, which Zhang Yimou, which Graham).
2. Choose the output slug (e.g., `lu-xun-skill`, `feynman-skill`).
3. Draft the generated skill's `description` frontmatter, including both **triggers** and **anti-triggers**. Anti-triggers are as important as triggers.
4. Run scaffold to create the empty skeleton:

   ```bash
   python3 skills/create-figure-skill/scripts/scaffold.py --slug <figure-slug>
   ```

**Produces:** `skills/<slug>/` with all folders and placeholder files + `meta.json`.

### Phase 2 · Prior-Sweep

Snapshot the model's pre-existing beliefs before any external source contaminates them. The training-data impression of a famous person is an invisible default that silently shapes every later judgment; making it explicit now lets us later see where the prior was wrong — and those deltas are often the most interesting findings.

Do **not** search anything in this phase. Write freely into `sources/prior/snapshot.md`: what you currently think the figure is known for, their reputation, what training exposed you to about them. Include the uncertainties — "I am not sure whether X" is valuable data.

This snapshot is frozen. It is never revised in later phases; it stands as a record of "what the pre-research model thought" and is cited later when prior conflicts with evidence.

**Produces:** `sources/prior/snapshot.md`.

### Phase 3 · Forage

Large-scale DeepResearch across primary, critical, and distillation sources. A skill is only as good as its evidence base, and primary/distillation sources carry a structural pro-figure bias — without deliberate adversarial counterpressure, the skill drifts toward hagiography.

This is the most important phase and the most tempting to shortcut. Follow `references/deepresearch-playbook.md` — it defines query explosion, parallel subagent dispatch, gap analysis, the adversarial pass, and triangulation. Do not improvise a lighter version.

**Produces:** `sources/{primary,critical,distillations}/raw/` full of raw files + `sources/research-plan.md` + `sources/gap-report.md` + `sources/claims.md` + `sources/adversarial-findings.md`.

### Phase 4 · Cull

Clean raw files into a uniform, queryable substrate. Raw files are heterogeneous — HTML, PDF, multiple languages, mixed quality — and no agent can work at scale with this mess. Cull standardizes format, frontmatter, and reliability labels so that Phase 5 subagents read efficiently and use-time agents can grep reliably.

For each file in `raw/`:

- If PDF, extract to markdown (see `references/source-policy.md` for format handling).
- Strip HTML, ads, navigation chrome, pagination artifacts.
- Add YAML frontmatter per the schema in `references/source-policy.md`.
- Preserve the full text. `cleaned/` is not a summary layer — it is a fidelity-preserving layer.

Then rebuild the manifest:

```bash
python3 skills/create-figure-skill/scripts/manifest.py --skill-dir skills/<slug>
```

**Produces:** `sources/*/cleaned/*.md` with consistent frontmatter + `sources/manifest.json`.

### Phase 5 · Distill

Compress the cleaned corpus into four thematic research files — the skill's working memory. Cleaned sources are too voluminous for a use-time agent to re-read on every invocation; without this compression, using the skill would require re-processing the entire source library every time.

Do not read all cleaned sources sequentially in the main agent — that wastes context and produces shallow output. Use agent-native parallelism per `references/deepresearch-playbook.md`:

1. **Summary Sweep** — each cleaned source gets a ~200-word summary in `sources/<category>/summaries/` (parallel subagents).
2. **Four-Axis Extraction** — four subagents in parallel, one per axis, each reads summaries and selectively re-reads full sources, producing one `research/*.md`.
3. **Cross-Axis Reconciliation** — the main agent reads all four drafts as a set, resolves tensions, enforces honesty labels, and writes `research/README.md`.

The four axes and their dimensions are in `references/four-axes.md`. Every strong claim cites a source file (file-level granularity is sufficient).

**Produces:** `sources/*/summaries/*.md` + `research/{identity,thinking,expression,boundaries}.md` + `research/README.md`.

### Phase 6 · Compose & Probe

Write the five mode files and SKILL.md router, then smoke-test every mode with real prompts. Research without a use interface is a library nobody visits; Probe is the reality check — does the skill actually work on real questions? Failures feed back into boundaries.md, which is why this phase must come last.

1. Write the five mode files following `references/mode-writing-guide.md`. Each mode is prose instructions specific to how that mode operates this particular figure. Not a template fill.
2. Write the generated skill's `SKILL.md` as a slim entry + router (~30-60 lines). It identifies the user's intent and points to the relevant mode file. The heavy content is in the mode files and research, not here.
3. Run the audit:

   ```bash
   python3 skills/create-figure-skill/scripts/audit.py --skill-dir skills/<slug>
   ```

4. Smoke-test: for each of the five modes, try two real prompts — one straightforward, one probing a known boundary. Record failures and surprises in `research/boundaries.md`. This feedback loop is the last and most important honesty check.

**Produces:** complete, usable `skills/<slug>/`.

## Where to read what

| Situation | File to consult |
|---|---|
| Any time — posture and anti-patterns | `references/research-stance.md` |
| Phase 3 Forage — query explosion, parallelism, adversarial pass | `references/deepresearch-playbook.md` |
| Phase 4 Cull — frontmatter schema, reliability labels, format handling | `references/source-policy.md` |
| Phase 5 Distill — the four axes and their dimensions | `references/four-axes.md` |
| Phase 5 Distill — summary sweep, axis extraction, reconciliation | `references/deepresearch-playbook.md` |
| Phase 6 Compose — how to write a mode file | `references/mode-writing-guide.md` |
