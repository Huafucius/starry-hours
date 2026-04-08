# Finalize Figure Index Plan

**Goal:** Replace the current loose figure table with the final approved list of celebrity-centered repositories, grouped by role and aligned with the stricter long-lived awesome-list information architecture.
**Scope:** Update `README.md`, `README.en.md`, and `docs/README.md`. Keep the latest bilingual split, no-star-table style, and existing books/brands sections. Remove weak or generic figure entries, add the approved figure list, and organize the figure index into the five approved groups.
**Architecture:** The repository now follows a stricter editorial model: exact entity names, no fluctuating star columns, and no mixed-target figure rows. The figure index should read like a stable taxonomy of celebrity-centered skills rather than a temporary trend board.
**Success criteria:** The figure section contains only the 19 approved repositories, grouped as `思想家 / 政治家 / 企业家 / 技术领袖 / 公众人物` in Chinese and equivalent role groups in English; `autoresearch`, `wardley-mapping`, and `colleague-skill` are gone; the latest README format and bilingual split remain intact; docs index references this plan.

---

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Add this plan to the docs index |
| `docs/plans/2026-04-08-finalize-figure-index.md` | Create | Record the approved figure list and editorial constraints |
| `README.md` | Update | Replace the loose figure table with the approved grouped figure index |
| `README.en.md` | Update | Mirror the approved grouped figure index in English |

---

## Tasks

### Task 1: Record the final editorial plan

**Files:**
- Create: `docs/plans/2026-04-08-finalize-figure-index.md`
- Modify: `docs/README.md`

**Steps:**
1. Write acceptance criteria in this plan
2. Verify `docs/README.md` does not yet reference this plan
3. Add the new plan file and update the docs index
4. Re-read the docs index to confirm the new entry appears
5. Commit: `docs: record final figure index plan`

---

### Task 2: Replace the figure index in Chinese README

**Files:**
- Modify: `README.md`

**Steps:**
1. Verify the current figure section still contains weak rows such as `autoresearch`, `wardley-mapping`, or other non-celebrity/generic entries
2. Replace the figure section with the approved 19-entry grouped figure index
3. Keep the latest README structure, featured section, books section, brands section, and no-star-table style intact
4. Re-read the edited figure section for taxonomy and naming accuracy
5. Commit: `docs: finalize Chinese figure index`

---

### Task 3: Mirror the taxonomy in English README

**Files:**
- Modify: `README.en.md`

**Steps:**
1. Verify the current English figure section still mirrors the outdated loose figure set
2. Translate and mirror the approved grouped figure index into `README.en.md`
3. Keep links, entity names, and the rest of the English README structure consistent
4. Re-read for terminology consistency across both languages
5. Commit: `docs: mirror finalized figure taxonomy in English`

---

## Verification (Phase 5)

- [ ] `README.md` contains exactly the approved 19 figure entries under the five approved groups
- [ ] `README.en.md` mirrors the same figure set and grouping in English
- [ ] `README.md` no longer contains `uditgoenka/autoresearch`, `haberlah/wardley-mapping`, or `titanwings/colleague-skill`
- [ ] `docs/README.md` references this plan
- [ ] `git diff --name-only` matches the planned file set
- [ ] `git status` is clean
