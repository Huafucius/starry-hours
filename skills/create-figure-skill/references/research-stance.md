# Research Stance

This file is the posture that makes a figure skill non-trivial. Without it, the skill will drift toward a whitewash.

Read it before Phase 1. Re-read it whenever Phase 3 or Phase 5 starts feeling formulaic.

## The core problem

Famous people generate admiring material. Search engines surface that material first. Training data contains more of that material. If you research a figure by reading what comes easily, you will produce a skill that sounds like a fan letter with chapter headings.

Good research actively fights this gravity.

## Four ideas to internalize

### 1. Turn every page (Caro)

Robert Caro, on researching Lyndon Johnson:

> Turn every page. Never assume anything. Turn every goddamned page.

Agents have an advantage here: we can turn pages in parallel. Don't stop at the first three results. If the figure has forty years of output, expect to surface it across categories, languages, and decades. The numeric targets in `deepresearch-playbook.md` exist so that "enough" is not a feeling.

### 2. Show the seams (Malcolm)

Janet Malcolm, on biography:

> A fundamental rule of journalism is to tell a story and stick to it. Cinderella must remain good and the stepsisters bad.

A researcher who shows no seams is lying. When three sources contradict, do not pick one and discard the rest — keep all three and explain the tension. When a dimension has no evidence, write "no evidence found" and list the queries actually tried. Never invent plausible content to fill a gap. The gap is information.

### 3. The four corpora, and what each betrays

An agent researching a figure has four source types, each with a built-in bias:

- **Prior** (the model's training-data impression) — the ambient consensus. Safe, bland, sanded-smooth. Useful as a baseline to cross-check against. Never as ground truth.
- **Primary** (the figure's own words) — the figure's preferred self-narrative. Weight highly, but watch for the too-clean story. People curate their own record; so do their estates.
- **Critical** (adversaries, reassessments, rivals) — the correction force. Without it, the skill is hagiography. Over-weight this deliberately when primary sources feel monotonically flattering — the imbalance you feel is probably real.
- **Distillations** (what other thinkers have already compressed about this figure) — useful acceleration, dangerous amplification. If every distillation makes the same point, ask why. Sometimes a single early profile propagates unchecked for decades.

Never collect from only one category. Phase 3's three-lane forage exists to force balance. See `source-policy.md` for category rules.

### 4. Principle + Trace + Limits

Peter Kaufman's preface to *Poor Charlie's Almanack* does not just list Munger's principles — it shows each one executing on a real problem and names where it breaks. That is the structure to imitate.

When writing `research/thinking.md`, no mental model appears as "name + one-liner + an anecdote". That is the most common failure mode of figure skills — a trope dressed as insight. Demand three pieces for every mental model you record:

- **Principle** — the claim, stated plainly.
- **Trace** — a specific decision or text where the figure applied this principle, with source citation.
- **Limits** — a case where the principle fails, or a named critic who disputes its generality.

If you cannot produce the Trace and Limits for a given principle, the principle is not yet established. Either keep researching or drop it. "Provisional" principles without traces become slogans.

## Anti-patterns that will produce a bad skill

| Pattern | What it looks like | What to do instead |
|---|---|---|
| **Quote-scaffold** | "[Figure]'s five core principles: 1. A slogan. 2. A slogan. ..." | Principle + Trace + Limits. No Trace → no principle. |
| **Hagiography** | The research reads like the figure's Wikipedia on a good day. | Run the Adversarial Pass. No principle without a named critic or a documented failure. |
| **Template fatigue** | Every figure fills the same ten dimensions in the same rhythm. | Dimensions without evidence get "no evidence found, tried X/Y/Z". A figure with no sense of humor gets a thin humor section. |
| **Cosplay as distillation** | The skill is evaluated by "does it sound like him" rather than "does it reason like him". | Judgment and method are the substance. Voice is one axis of four, not the whole. |
| **Decision by access** | The figure's 1,000-page memoir shapes the skill because it was easy to parse. | Source weight is by evidence quality, not by word count. A single letter can outweigh a memoir. |
| **Convergence theater** | Contradictions smoothed into a clean narrative. | Keep the contradiction visible. Contradictions are data, not noise. |

## The smell test before moving on

Before considering `research/` done, answer:

- Can I point to a moment where the figure was publicly wrong? Is it in `boundaries.md`?
- Does `thinking.md` name at least one critic for each major principle?
- Does `expression.md` cover 字/词/句/段/章文 as separate layers, or did I collapse them into one blob?
- Did I search in the figure's native language if they wrote in one?
- Is every "no evidence found" paired with the specific queries I actually tried?
- Does `identity.md` include relational patterns and key stress events, not just birth and death?

If any answer is no, research is not done. Go back.
