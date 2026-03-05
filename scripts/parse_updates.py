#!/usr/bin/env python3
"""
parse_updates.py — VZ1R Delivery Agent: Meeting Notes Parser

Usage:
    python scripts/parse_updates.py [--dry-run]

Description:
    Scans `updates/meeting-notes/` for the newest unprocessed file,
    reads the current engagement state from `state/engagement-state.json`
    and the synthesis deck from `deck/onerisk-tprm-monthly-synthesis.md`,
    then calls OpenAI GPT-4o to identify what has changed and propose
    specific field-level updates.

    Proposed changes are written to `updates/proposed-changes/YYYY-MM-DD-HH-MM-proposed-changes.md`.

    With `--dry-run`, proposals are printed to stdout without writing any files.

Requirements:
    - OPENAI_API_KEY environment variable must be set
    - openai>=1.0.0
    - PyYAML (for any YAML-format meeting notes)

Options:
    --dry-run    Print proposals to stdout; do not write output files.
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

from openai import OpenAI


# ---------------------------------------------------------------------------
# Paths (relative to repository root)
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
MEETING_NOTES_DIR = REPO_ROOT / "updates" / "meeting-notes"
PROPOSED_CHANGES_DIR = REPO_ROOT / "updates" / "proposed-changes"
STATE_FILE = REPO_ROOT / "state" / "engagement-state.json"
DECK_FILE = REPO_ROOT / "deck" / "onerisk-tprm-monthly-synthesis.md"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_text(path: Path) -> str:
    """Read a file and return its content as a string."""
    return path.read_text(encoding="utf-8")


def get_processed_sources() -> set[str]:
    """
    Return the set of source filenames already referenced in
    updates/proposed-changes/ so we can skip already-processed files.
    """
    processed = set()
    if not PROPOSED_CHANGES_DIR.exists():
        return processed
    for f in PROPOSED_CHANGES_DIR.glob("*-proposed-changes.md"):
        content = f.read_text(encoding="utf-8")
        # Look for "Source file:" lines in each proposal
        for line in content.splitlines():
            if line.lower().startswith("**source file:**") or line.lower().startswith("source file:"):
                parts = line.split(":", 1)
                if len(parts) == 2:
                    processed.add(parts[1].strip())
    return processed


def find_newest_unprocessed_file() -> Path | None:
    """
    Return the most recently modified .md or .txt file in meeting-notes/
    that has not already been processed.
    """
    if not MEETING_NOTES_DIR.exists():
        return None

    processed = get_processed_sources()
    candidates = [
        f for f in MEETING_NOTES_DIR.iterdir()
        if f.suffix in {".md", ".txt", ".csv"}
        and f.name != "README.md"
        and f.name not in processed
    ]

    if not candidates:
        return None

    return max(candidates, key=lambda f: f.stat().st_mtime)


def build_prompt(meeting_notes: str, state: str, deck: str) -> str:
    """Build the structured GPT-4o prompt."""
    return f"""You are the VZ1R Delivery Agent — a senior ServiceNow IRM architect and Big 4 delivery lead
for the Verizon OneRisk TPRM engagement.

Your task is to compare new meeting notes or status updates against the current engagement state
and synthesis deck, then propose precise, justified field-level changes.

---

## CURRENT STATE (engagement-state.json)

```json
{state}
```

---

## CURRENT SYNTHESIS DECK (onerisk-tprm-monthly-synthesis.md)

```markdown
{deck}
```

---

## NEW MEETING NOTES / INPUT

```
{meeting_notes}
```

---

## YOUR TASK

1. Read the new input carefully.
2. Identify every piece of information that changes the current state.
3. For each change, produce a row in the table below.
4. Be specific: reference exact JSON fields, issue IDs, status colors, dates, and stakeholder names.
5. Rate your confidence: High (explicit in the notes), Medium (strongly implied), Low (inferred).
6. Include only changes supported by the new input — do not invent information.

## OUTPUT FORMAT

Begin your response with:

**Source file:** [filename]
**Processed at:** [ISO timestamp]
**Summary:** [1-2 sentence summary of what the input contained and what changed]

Then produce this table:

| Field | Was | Will Be | Reason | Confidence | File to Update |
|-------|-----|---------|--------|------------|----------------|

Then provide a section:

## Instructions for Clark

List the specific edits Clark should make to each file, referencing the table above.
Be precise: specify JSON path for engagement-state.json changes and section headers for deck changes.

## Conflicts / Flags

List any information in the new input that conflicts with current state, is ambiguous,
or requires a human decision before applying.

---

Important rules:
- Never propose deleting history — only propose appending or updating specific fields
- Always show Was → Will Be for every proposed change
- If the input contains no new information (duplicate or already reflected in state), say so clearly
- Use Verizon terminology: 1Risk (client-facing), ServiceNow (technical), OneRisk (program),
  IRQ, DDQ, BitSight, Avetta, Ariba, EHS
"""


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Parse VZ1R meeting notes and propose engagement state updates."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print proposals to stdout without writing output files.",
    )
    args = parser.parse_args()

    # ── Validate environment ──────────────────────────────────────────────
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    # ── Find newest unprocessed meeting note ──────────────────────────────
    source_file = find_newest_unprocessed_file()
    if source_file is None:
        print("No unprocessed meeting notes found in updates/meeting-notes/. Nothing to do.")
        sys.exit(0)

    print(f"Processing: {source_file.name}")

    # ── Load context files ────────────────────────────────────────────────
    if not STATE_FILE.exists():
        print(f"ERROR: State file not found: {STATE_FILE}", file=sys.stderr)
        sys.exit(1)

    if not DECK_FILE.exists():
        print(f"ERROR: Synthesis deck not found: {DECK_FILE}", file=sys.stderr)
        sys.exit(1)

    meeting_notes = load_text(source_file)
    state = load_text(STATE_FILE)
    deck = load_text(DECK_FILE)

    if not meeting_notes.strip():
        print(f"WARNING: Meeting notes file is empty: {source_file.name}")
        sys.exit(0)

    # ── Build prompt and call OpenAI ──────────────────────────────────────
    prompt = build_prompt(meeting_notes, state, deck)

    print("Calling OpenAI GPT-4o...")
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are the VZ1R Delivery Agent. You produce precise, justified, "
                        "field-level change proposals for the Verizon OneRisk TPRM engagement state. "
                        "You are thorough, specific, and never hallucinate information not present in the input."
                    ),
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.2,
            max_tokens=4096,
        )
    except Exception as e:
        print(f"ERROR: OpenAI API call failed: {e}", file=sys.stderr)
        sys.exit(1)

    proposal_text = response.choices[0].message.content

    # Prepend metadata header
    now = datetime.now(timezone.utc)
    header = (
        f"# Proposed Changes — Auto-Generated\n\n"
        f"**Generated at:** {now.strftime('%Y-%m-%d %H:%M UTC')}\n"
        f"**Source file:** {source_file.name}\n"
        f"**Model:** gpt-4o\n\n"
        f"---\n\n"
    )
    full_output = header + proposal_text

    # ── Output ─────────────────────────────────────────────────────────────
    if args.dry_run:
        print("\n" + "=" * 60)
        print("DRY RUN — Proposed Changes (not written to disk)")
        print("=" * 60)
        print(full_output)
        return

    # Write to proposed-changes/
    PROPOSED_CHANGES_DIR.mkdir(parents=True, exist_ok=True)
    output_filename = f"{now.strftime('%Y-%m-%d-%H-%M')}-proposed-changes.md"
    output_path = PROPOSED_CHANGES_DIR / output_filename

    output_path.write_text(full_output, encoding="utf-8")
    print(f"Proposed changes written to: updates/proposed-changes/{output_filename}")
    print("Review the proposal in updates/proposed-changes/ before applying any changes.")


if __name__ == "__main__":
    main()
