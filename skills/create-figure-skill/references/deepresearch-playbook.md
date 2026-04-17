# DeepResearch Playbook

Concrete procedures for Phase 3 (Forage) and Phase 5 (Distill). These are the phases where laziness costs the most and tempts the most.

The core move in both phases: **the main agent orchestrates; subagents extract and retrieve in parallel**. The main agent does not read every source itself. Mass parallelism is the agent's signature advantage over human researchers — use it deliberately.

---

## Phase 3 · Forage — sub-workflow

### 3.1 Query Explosion

Draft an explicit research plan before issuing any search. Without one, agents default to 3-5 obvious searches and stop. A written plan makes laziness visible and ensures dimensional coverage (every axis gets queries) rather than topic-driven clustering. Generate **at least 50 targeted queries** from the figure's name combined with the dimensions in `four-axes.md`.

Distribution guidance:

- Per cognition dimension (there are 10): at least 3 queries.
- Per voice layer (there are 5): at least 2 queries.
- Identity dimensions (timeline, relationships, key events): at least 10 queries total.
- Boundaries (named critics, reassessments, documented failings): at least 10 queries.
- Primary originals (named books, speeches, letter collections): at least 10 queries.

Save the plan to `sources/research-plan.md`. Each query has a category label and a one-line intent. Example:

```text
- "鲁迅 致朱安 信件"          → primary/letters — surface private correspondence
- "鲁迅 刻薄 指控"            → critical/character — test character critique
- "苏雪林 反鲁迅 论战"        → critical/adversaries — named antagonist
- "鲁迅 晚年 左翼 被利用"     → boundaries/evolution — late-period politics
```

Search in the figure's native language first. For Chinese figures, Chinese queries usually surface richer material than English translations — by a wide margin.

### 3.2 Round 1 · Parallel Scrape

Fire all planned queries in parallel via subagents. Parallel retrieval is the agent's superpower over human researchers — batching prevents the main agent from becoming the bottleneck and keeps wall-clock time short even for 50+ queries.

Dispatch subagents in batches. Each subagent takes 5-10 queries; their task is **retrieval, not judgment** — download everything that looks germane, save to the appropriate `raw/` under the appropriate category (primary/critical/distillations), and return a short inventory to the main agent.

Target wall-clock: all 50+ queries executed within a few minutes. Expect several hundred files in `raw/` afterward. That is normal.

### 3.3 Gap Analysis

Map what Round 1 missed. Round 1 is broad but blind — it fires all pre-planned queries without knowing which hit and which failed. Gap analysis turns Round 2 from "search more" into "search specifically for X" and produces a permanent record of what was attempted but unfindable.

The main agent reads `research-plan.md` alongside the Round 1 inventory. Answer, explicitly in writing:

- Which axis dimensions currently have fewer than three independent sources?
- Which primary self-claims have no critical counterpart yet?
- Which time periods of the figure's life are underrepresented?
- Which named events, works, or relationships did the plan expect but didn't surface?

Write `sources/gap-report.md`. Be concrete. "Identity dim #4 (relational patterns) has strong coverage for peers but none for institutional engagement" is useful. "Coverage is uneven" is not.

### 3.4 Round 2 · Targeted Fill

Fill the specific holes that Round 1 left — adversarial material, minor-era coverage, private correspondence. Targeted fill is efficient because it already knows what's missing. Un-fillable gaps are information, not failure; they become "no evidence found" entries in research/.

From `gap-report.md`, derive a second query batch (typically 20-40 queries). Narrower, more specific — you now know where the holes are. Dispatch subagents again in parallel.

After Round 2, some gaps will remain un-fillable. That is acceptable — the gap itself is information, and will be recorded in the relevant `research/` file as "no evidence found, tried [list]".

### 3.5 Adversarial Pass

For every strong claim collected so far, actively search for people who disagree. Primary and distillation sources have a structural pro-figure bias — the figure's own narrative and their admirers' summaries naturally converge on a flattering picture. This is the only step that deliberately fights that gravity. Without it, the skill is a well-formatted whitewash. With it, every major claim carries either a named counter-argument or a documented record of "we looked and found none."

**Mandatory, not optional.** The cost is high; the research-cost budget is designed to absorb it.

1. Read everything in `sources/primary/raw/` and `sources/distillations/raw/`.

2. Extract every **claim about the figure that a serious critic could plausibly dispute**:
   - claims about their methods or principles
   - claims about their character, motives, or integrity
   - claims about their historical impact or originality
   - claims about their correctness on specific issues

   Skip purely biographical facts (dates, affiliations, marriages) **unless they are contested**.

3. Number the claims in `sources/claims.md` (1..N). Keep the numbering stable — downstream artifacts reference it.

4. For each claim, generate 3-5 adversarial queries. Dispatch subagents in batches (typically 20 claims per subagent). Each subagent runs all adversarial queries for its claim batch and records findings back against claim numbers.

5. Results go to `sources/adversarial-findings.md`, keyed by claim number.

6. Claims where no adversarial material was found get the explicit label:

   `[no adversarial found, tried: <list of specific queries>]`

   This is a legitimate state. It means either the claim is genuinely uncontroversial or the research was insufficient. The researcher must explicitly judge which.

The total volume can be large — a 200-claim figure may mean 600-1000 adversarial queries. Use parallel subagents. Do not cut the pass short for budget reasons. If the main agent is running out of context, dispatch a subagent to continue.

### 3.6 Triangulation Check

Require at least two independent sources for every claim that will enter research/. Single-source claims are anecdotes; two independent sources make a claim defensible. This step also catches cases where a single early profile propagated unchecked across many outlets — those count as one source, not many.

Before Phase 5 starts, every candidate claim that will enter `research/` requires **at least two independent sources**. Independent means:

- different authors
- different outlets or venues
- different perspectives (not two reprints of the same piece)

Claims failing triangulation either get marked `[weak evidence]` and kept as leads, or dropped entirely with a note.

---

## Phase 5 · Distill — sub-workflow

The naive approach — main agent reads all cleaned sources and writes research — will not fit in context and produces shallow results. Use agent-native parallelism.

### 5.1 Summary Sweep

Produce a ~200-word summary of each cleaned source in parallel. Cleaned sources are too long for any single agent context to hold at once; summaries create a fast index that axis-extraction subagents use to decide what's worth reading in full. The summaries also serve use-time agents who need to locate relevant material without re-parsing every file.

Dispatch one subagent per cleaned source, or batch 5-10 short sources per subagent for efficiency. Each subagent produces a ~200-word summary saved to `sources/<category>/summaries/<same-filename>.md`.

The summary file mirrors the cleaned file's frontmatter and adds `summary_of:` pointing at the original.

Content requirements for the summary:

- What the source actually contains — who, when, what topic.
- Which axis dimensions it touches (e.g., "relevant to thinking #3, voice layer 句, boundaries #2").
- Notable or adversarial points worth flagging.
- Do not editorialize beyond what the source does.

The summaries layer is **also valuable at use-time** — future agents using the generated skill can locate relevant primary material by reading summaries without re-parsing every `cleaned/` file.

### 5.2 Four-Axis Extraction

Write the four research files in parallel, one subagent per axis. A single agent trying all four would need to hold the entire corpus in context and context-switch between very different analytical frames. Splitting lets each subagent specialize — reading only sources relevant to its axis and producing a cohesive document without cross-axis distraction.

Dispatch four subagents in parallel, one per axis (identity, thinking, expression, boundaries). Each subagent:

1. Reads all summaries (fast, fits in one context).
2. Identifies which full sources are relevant to their assigned axis.
3. Selectively reads those full sources in `cleaned/`.
4. Writes `research/<axis>.md` following `four-axes.md`.

Each subagent receives:

- The relevant section of `four-axes.md`.
- A pointer to `sources/*/summaries/`.
- `research-stance.md` and the Principle + Trace + Limits requirement.
- `sources/claims.md` and `sources/adversarial-findings.md` — especially load-bearing for `thinking.md` (adversarial enters Trace+Limits) and `boundaries.md` (adversarial enters named critics).

The four subagents do not coordinate. Overlap between axes is expected and fine — the main agent resolves it in the next step.

### 5.3 Cross-Axis Reconciliation

Reconcile the four independently written research files into a coherent whole. The subagents inevitably produce overlapping observations, inconsistent terminology, and occasionally contradictory claims. Only the main agent has the cross-axis view to resolve tensions, deduplicate, and spot gaps no single-axis subagent could see (e.g., an identity event that explains a cognitive shift).

The main agent reads the four drafts as a set. Tasks:

- **Deduplicate** — the same observation showing up in thinking and expression. Keep it where it fits best; cross-reference from the other.
- **Surface contradictions between axes** — e.g., `identity.md` describes the figure as reclusive while `expression.md` describes them as expansive. These are interesting, not errors. Document the tension explicitly.
- **Enforce honesty labels** — any dimension with thin evidence gets explicit "no evidence found, tried X/Y/Z". Do not quietly leave sections empty.
- **Write `research/README.md`** — a short index: one paragraph per axis describing what's there and how it connects to the others.

After reconciliation, move to Phase 6.

---

## Anti-laziness checklist

The following are **minimums**, not targets. A figure skill generated below these thresholds is not complete:

- [ ] `sources/research-plan.md` contains ≥ 50 queries with category labels.
- [ ] `sources/gap-report.md` exists and names specific shortfalls.
- [ ] `sources/claims.md` exists with numbered claims.
- [ ] `sources/adversarial-findings.md` has an entry for every claim number (even if the entry is "no adversarial found").
- [ ] Every `research/` file either has dense evidence across all its dimensions OR contains at least one "no evidence found, tried:" section. Silent empty dimensions are not allowed.
- [ ] `research/boundaries.md` names at least one critic and one documented failing (or explicitly notes the search was unsuccessful with specific queries tried).

If the main agent is tempted to skip a step for token-budget reasons, **delegate it to a subagent**. Never skip for laziness. Never compress the Adversarial Pass into "oh, I think the common critiques are..." — actually search.
