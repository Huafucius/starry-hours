#!/usr/bin/env python3
"""Skeleton audit for a generated figure skill.

Checks structural integrity only — the critical, binary gates that a script
can verify without judgment:
  1. Do all required files and directories exist?
  2. Does SKILL.md have name + description in frontmatter? (needed for triggering)
  3. Is manifest.json valid JSON with at least one source? (proves Phase 3-4 ran)

Content quality, research depth, mode coverage — those are the LLM's job,
enforced through the smoke test in Phase 6, not through this script.

Usage:
    python3 audit.py --skill-dir skills/<figure-slug>

Exit code 0 on pass, 1 on any issue.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_MODES = ["dialogue", "voice", "methodology", "critique", "advisory"]
REQUIRED_AXES = ["identity", "thinking", "expression", "boundaries"]
REQUIRED_STRUCTURED_CATEGORIES = ["primary", "critical", "distillations"]


def check_frontmatter_fields(path: Path, required: list[str]) -> list[str]:
    text = path.read_text()
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return [f"{path.name}: missing YAML frontmatter"]
    fields: set[str] = set()
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line:
            key = line.split(":", 1)[0].strip()
            fields.add(key)
    return [f"{path.name}: frontmatter missing field '{k}'" for k in required if k not in fields]


def audit(skill_dir: Path) -> list[str]:
    issues: list[str] = []

    # Top-level files
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        issues.append("SKILL.md missing")
    else:
        issues.extend(check_frontmatter_fields(skill_md, ["name", "description"]))

    if not (skill_dir / "meta.json").is_file():
        issues.append("meta.json missing")

    # modes/ — files must exist; content quality is the LLM's call
    modes_dir = skill_dir / "modes"
    if not modes_dir.is_dir():
        issues.append("modes/ missing")
    else:
        for mode in REQUIRED_MODES:
            if not (modes_dir / f"{mode}.md").is_file():
                issues.append(f"modes/{mode}.md missing")

    # research/ — files must exist; depth is the LLM's call
    research_dir = skill_dir / "research"
    if not research_dir.is_dir():
        issues.append("research/ missing")
    else:
        for axis in REQUIRED_AXES:
            if not (research_dir / f"{axis}.md").is_file():
                issues.append(f"research/{axis}.md missing")

    # sources/
    sources_dir = skill_dir / "sources"
    if not sources_dir.is_dir():
        issues.append("sources/ missing")
    else:
        manifest = sources_dir / "manifest.json"
        if not manifest.is_file():
            issues.append("sources/manifest.json missing")
        else:
            try:
                data = json.loads(manifest.read_text())
                if not data.get("sources"):
                    issues.append("sources/manifest.json has no entries (run manifest.py after Phase 4)")
            except json.JSONDecodeError as e:
                issues.append(f"sources/manifest.json is not valid JSON: {e}")

        for category in REQUIRED_STRUCTURED_CATEGORIES:
            for sub in ["raw", "cleaned", "summaries"]:
                if not (sources_dir / category / sub).is_dir():
                    issues.append(f"sources/{category}/{sub}/ missing")

        if not (sources_dir / "prior").is_dir():
            issues.append("sources/prior/ missing")

        # --- Programmatic quality gates (checked only when artifacts exist) ---

        # Gate: research-plan.md must have ≥50 queries (anti-laziness for Phase 3)
        research_plan = sources_dir / "research-plan.md"
        if research_plan.is_file():
            lines = [l for l in research_plan.read_text().splitlines() if l.strip()]
            if len(lines) < 50:
                issues.append(
                    f"research-plan.md has {len(lines)} non-empty lines (minimum 50 queries)"
                )

        # Gate: adversarial pass must complete — claims.md implies adversarial-findings.md
        claims_path = sources_dir / "claims.md"
        adversarial_path = sources_dir / "adversarial-findings.md"
        if claims_path.is_file() and not adversarial_path.is_file():
            issues.append(
                "claims.md exists but adversarial-findings.md is missing "
                "(adversarial pass incomplete)"
            )

        # Gate: every numbered claim must appear in adversarial-findings.md
        if claims_path.is_file() and adversarial_path.is_file():
            claim_numbers: set[str] = set()
            for line in claims_path.read_text().splitlines():
                m = re.match(r"^\s*(\d+)", line)
                if m:
                    claim_numbers.add(m.group(1))
            adv_text = adversarial_path.read_text()
            missing_claims = sorted(
                [n for n in claim_numbers if n not in adv_text], key=int
            )
            if missing_claims:
                preview = ", ".join(missing_claims[:10])
                issues.append(
                    f"adversarial-findings.md missing entries for claim(s): {preview}"
                )

        # Gate: every cleaned source must have a corresponding summary (Phase 5.1)
        for category in REQUIRED_STRUCTURED_CATEGORIES:
            cleaned_dir = sources_dir / category / "cleaned"
            summaries_dir = sources_dir / category / "summaries"
            if cleaned_dir.is_dir() and summaries_dir.is_dir():
                cleaned_stems = {f.stem for f in cleaned_dir.glob("*.md")}
                summary_stems = {f.stem for f in summaries_dir.glob("*.md")}
                missing_summaries = sorted(cleaned_stems - summary_stems)
                if missing_summaries:
                    preview = ", ".join(missing_summaries[:5])
                    issues.append(
                        f"sources/{category}/summaries/ missing for: {preview}"
                    )

    return issues


def main() -> None:
    parser = argparse.ArgumentParser(description="Audit a generated figure skill's skeleton.")
    parser.add_argument("--skill-dir", required=True, help="Path to the generated skill.")
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    if not skill_dir.is_dir():
        print(f"Error: {skill_dir} not found.", file=sys.stderr)
        sys.exit(1)

    issues = audit(skill_dir)
    if not issues:
        print(f"OK · {skill_dir} passes skeleton audit.")
        sys.exit(0)

    print(f"FAIL · {skill_dir} has {len(issues)} issue(s):")
    for issue in issues:
        print(f"  - {issue}")
    sys.exit(1)


if __name__ == "__main__":
    main()
