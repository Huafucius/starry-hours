#!/usr/bin/env python3
"""Create the empty skeleton for a new figure skill.

Usage:
    python3 scaffold.py --slug <figure-slug> [--output-dir <path>]

Produces:
    <output-dir>/<slug>/
        SKILL.md             (stub with frontmatter)
        meta.json            (slug, created_at)
        CHANGELOG.md         (append-only pass log; header + format only — first entry is agent-written)
        modes/               (five placeholder .md files)
        research/            (four placeholder .md files)
            README.md        (stub index for the research layer)
            probe-log.md     (append-only probe log)
        sources/
            manifest.json    (empty sources array)
            prior/
                snapshot.md  (placeholder prior baseline)
            primary/{raw,cleaned,summaries}/
            critical/{raw,cleaned,summaries}/
            distillations/{raw,cleaned,summaries}/

No network access, no content generation. Pure structural setup.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from pathlib import Path


MODES = ["dialogue", "voice", "methodology", "critique", "advisory"]
AXES = ["identity", "thinking", "expression", "boundaries"]
SOURCE_CATEGORIES_STRUCTURED = ["primary", "critical", "distillations"]
SOURCE_CATEGORIES_FLAT = ["prior"]
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


SKILL_MD_STUB = """---
name: {slug}
description: <TODO · fill in Phase 6 · Interface Assembly: write a pushy description with triggers AND anti-triggers. Triggers are example user phrasings that should activate this skill. Anti-triggers are phrasings that look similar but should NOT activate it.>
---

# <TODO · Figure Name>

<TODO · One paragraph identifying this figure skill and what it is for. Written in Phase 6 after all research is done.>

## Choose a mode

<TODO · Routing logic. Identify the user's intent and point to the appropriate modes/*.md file. See create-figure-skill/references/mode-writing-guide.md for the spirit of mode routing. Keep this section under 30 lines.>

<!-- This file is a stub created by scaffold.py. Complete it in Phase 6 · Interface Assembly. -->
"""


RESEARCH_STUB = """# {axis_title}

<!-- Stub created by scaffold.py. Fill in Phase 5 · Knowledge Distillation. -->
<!-- See create-figure-skill/references/four-axes.md for the dimensions of this axis. -->
"""


RESEARCH_README_STUB = """# Research

<!-- Stub created by scaffold.py. Update this in Phase 5 · Knowledge Distillation. -->
<!-- Summarize what the current research layer contains and how the axes connect. -->
"""


MODE_STUB = """# {mode_title} Mode

<!-- Stub created by scaffold.py. Fill in Phase 6 · Interface Assembly. -->
<!-- See create-figure-skill/references/mode-writing-guide.md for the shape of a mode file. -->
"""


PRIOR_SNAPSHOT_STUB = """# Prior Snapshot

<!-- Stub created by scaffold.py. Fill this in during Phase 2 · Prior Capture before external search. -->
"""


CHANGELOG_STUB = """# Changelog

Append-only. One entry per pass. Newest entry on top.
See `create-figure-skill/references/maintenance-operations.md` for the operation vocabulary.

<!-- Entry format:

## YYYY-MM-DD · <route>

- Route: `bootstrap` | `update` | `repair` | `extend`
- Operations: <operations invoked, or "none">
- Touched: <axes / modes / sources touched>
- Evidence delta: <new sources, deletions, reclassifications>
- Notes: <what actually happened and why>

The first entry is written by the agent running the first substantive pass
(usually bootstrap), not by this scaffold. Scaffold creating the skeleton
is not itself a pass worth logging.
-->
"""


PROBE_LOG_STUB = """# Probe Log

<!-- Append-only. One entry per probe during Phase 6 · Interface Assembly & Probe. -->
<!-- Format per entry: -->
<!--   ## YYYY-MM-DD · <mode> · <pass/fail/surprise> -->
<!--   - Prompt: ... -->
<!--   - Outcome: ... -->
<!--   - Boundary update: (link to boundaries.md section, or "none") -->

<!-- Probes that failed and were fixed in the same pass stay in the log as historical record. -->
"""


def create_skeleton(slug: str, output_dir: Path) -> Path:
    skill_dir = output_dir / slug
    if not SLUG_RE.fullmatch(slug):
        print(
            "Error: slug must match ^[a-z0-9][a-z0-9-]*$.",
            file=sys.stderr,
        )
        sys.exit(1)
    if output_dir.resolve() not in skill_dir.resolve().parents:
        print("Error: slug escapes the output directory.", file=sys.stderr)
        sys.exit(1)
    if skill_dir.exists():
        print(f"Error: {skill_dir} already exists. Refusing to overwrite.", file=sys.stderr)
        sys.exit(1)

    skill_dir.mkdir(parents=True)

    # modes/
    modes_dir = skill_dir / "modes"
    modes_dir.mkdir()
    for mode in MODES:
        (modes_dir / f"{mode}.md").write_text(MODE_STUB.format(mode_title=mode.capitalize()))

    # research/
    research_dir = skill_dir / "research"
    research_dir.mkdir()
    for axis in AXES:
        (research_dir / f"{axis}.md").write_text(RESEARCH_STUB.format(axis_title=axis.capitalize()))
    (research_dir / "README.md").write_text(RESEARCH_README_STUB)

    # sources/
    sources_dir = skill_dir / "sources"
    sources_dir.mkdir()

    for category in SOURCE_CATEGORIES_STRUCTURED:
        (sources_dir / category / "raw").mkdir(parents=True)
        (sources_dir / category / "cleaned").mkdir()
        (sources_dir / category / "summaries").mkdir()

    for category in SOURCE_CATEGORIES_FLAT:
        (sources_dir / category).mkdir()

    (sources_dir / "prior" / "snapshot.md").write_text(PRIOR_SNAPSHOT_STUB)

    (sources_dir / "manifest.json").write_text(
        json.dumps({"count": 0, "sources": []}, indent=2) + "\n"
    )

    # SKILL.md
    (skill_dir / "SKILL.md").write_text(SKILL_MD_STUB.format(slug=slug))

    # meta.json
    today = dt.date.today().isoformat()
    (skill_dir / "meta.json").write_text(
        json.dumps(
            {"slug": slug, "created_at": today},
            indent=2,
        )
        + "\n"
    )

    # Maintenance-layer artifacts. Append-only; LLM writes content, audit does not check.
    # Scaffold does NOT pre-write a first entry — that is for the bootstrap agent to do
    # after the first real pass completes, so the log never contains forward-looking claims.
    (skill_dir / "CHANGELOG.md").write_text(CHANGELOG_STUB)
    (research_dir / "probe-log.md").write_text(PROBE_LOG_STUB)

    return skill_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Scaffold a new figure skill.")
    parser.add_argument("--slug", required=True, help="Figure slug (e.g., lu-xun-skill).")
    parser.add_argument(
        "--output-dir",
        default="skills",
        help="Parent directory to place the skill under (default: skills).",
    )
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    if not output_dir.exists():
        print(f"Error: output directory {output_dir} does not exist.", file=sys.stderr)
        sys.exit(1)

    skill_dir = create_skeleton(args.slug, output_dir)
    print(f"Created skeleton at {skill_dir}")


if __name__ == "__main__":
    main()
