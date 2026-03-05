# Meeting Notes Drop Zone

## How to Use This Folder

Drop any of the following file types here to trigger an automated state update:
- AI-generated meeting notes (`.md` or `.txt`)
- RAID log exports (`.md`, `.csv`, or `.txt`)
- Status deck summaries (`.md` or `.txt`)
- Any freeform status update text

## What Happens When You Drop a File

1. GitHub Actions triggers automatically on push
2. `parse_updates.py` reads the dropped file against current `state/engagement-state.json`
3. A proposed changes file is written to `updates/proposed-changes/`
4. Review the proposal, then manually apply approved changes to the synthesis deck and state

## Naming Convention

Use descriptive names: `YYYY-MM-DD-[topic].md`
Example: `2026-03-05-architecture-review-call.md`

## Important

- Do not delete files from this folder — they serve as an audit trail
- Proposed changes are in `../proposed-changes/` — review before accepting
