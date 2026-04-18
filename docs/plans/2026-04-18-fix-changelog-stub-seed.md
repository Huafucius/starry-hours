# Fix CHANGELOG Stub Seed

**Goal:** The scaffold-time `CHANGELOG.md` stub currently pre-writes a bootstrap entry that claims `Operations: ingest (initial corpus)`. Scaffold runs before Phase 3 Evidence Expansion, so this claim is forward-looking — a lie at seed time. Fix it.

**Why:** Surfaced by the maintenance-layer eval (iteration-1). The with-skill P1 subagent noted:

> "The scaffold seeds a CHANGELOG.md bootstrap entry dated today with route `bootstrap` and operations `ingest`, even though Phase 1 has not yet ingested anything. That is forward-looking boilerplate."

The current seed violates the append-only invariant's spirit: we're seeding an entry that will need to be edited (not appended) once ingest actually happens.

**Fix:** Seed `CHANGELOG.md` with header + entry format instructions, **no pre-written entry**. The first real entry is written by the bootstrap agent after Phase 2 (or the first update/repair/extend agent, whichever finishes the first substantive pass).

**Success criteria:**

- `scripts/scaffold.py` produces a `CHANGELOG.md` that is non-empty (header + format comment) but contains zero dated entries.
- `references/maintenance-operations.md` is consistent with the new behavior — says the bootstrap agent writes the first entry, not scaffold.
- Running scaffold + audit on a throwaway slug behaves the same as before (audit still only reports the pre-existing empty-manifest issue).

## Docs Impact

| File | Action | What changes |
|------|--------|-------------|
| `docs/README.md` | Update | Add plan row |
| `docs/plans/2026-04-18-fix-changelog-stub-seed.md` | Create | This plan |
| `skills/create-figure-skill/scripts/scaffold.py` | Update | Rewrite `CHANGELOG_STUB`; adjust docstring |
| `skills/create-figure-skill/references/maintenance-operations.md` | Update | One-line clarification: first entry is agent-written, not scaffold-seeded |

## Out of scope

- No changes to the four routes, four axes, or the `probe-log.md` stub (which was correctly format-only — no pre-written entries).
- No retrofit operation for skills that predate the maintenance layer (separate future task).
