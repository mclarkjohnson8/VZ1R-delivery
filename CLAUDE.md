# CLAUDE.md — VZ1R Delivery Repository
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Repository Purpose

This repository is the **VZ1R Delivery Agent** — an AI-powered delivery management system for the Verizon OneRisk TPRM program, operated by Clark Johnson (Deloitte Delivery Lead).

The repository serves two functions:
1. **Knowledge Store**: All program context, history, reference materials, and current state live here
2. **Update Engine**: Meeting notes dropped here trigger automated parsing and proposed state updates

---

## Complete File Structure Reference

```
mclarkjohnson8/VZ1R-delivery
│
├── .github/
│   ├── copilot-instructions.md     ← Copilot agent identity and behavior rules
│   └── workflows/
│       └── parse-meeting-notes.yml ← GitHub Action: auto-parses meeting notes
│
├── context/
│   ├── engagement-history.md       ← Full program history (Clark fills in)
│   └── recommended-next-steps.md  ← AI-generated strategic recommendations
│
├── deck/
│   └── onerisk-tprm-monthly-synthesis.md  ← Human-readable status deck (PRIMARY ARTIFACT)
│
├── references/
│   ├── accelerators.md             ← Deloitte + ServiceNow IRM accelerators
│   ├── audit.md                    ← Audit Management module reference
│   ├── bcm.md                      ← Business Continuity Management reference
│   ├── cross-module.md             ← Cross-module integration patterns
│   ├── deloitte-delivery-model.md  ← Imagine → Deliver → Run framework
│   ├── entity-framework.md         ← Entity framework design and standards
│   ├── issues-privacy-bcm.md       ← Issues, Privacy, and BCM intersection
│   ├── pcm.md                      ← Policy & Compliance Management reference
│   ├── phase-deliver.md            ← Deliver phase standards and procedures
│   ├── phase-imagine.md            ← Imagine phase reference (historical)
│   ├── phase-run.md                ← Run phase / hypercare / BAU reference
│   ├── risk.md                     ← Risk Management module reference
│   ├── servicenow-technical-best-practices.md  ← ServiceNow technical standards
│   └── tprm.md                     ← TPRM module reference (PRIMARY MODULE)
│
├── updates/
│   ├── meeting-notes/
│   │   └── README.md               ← Drop zone instructions
│   └── proposed-changes/
│       └── README.md               ← Proposed change format documentation
│
├── state/
│   └── engagement-state.json       ← Machine-readable source of truth (GROUND TRUTH)
│
├── scripts/
│   └── parse_updates.py            ← OpenAI-powered parser script
│
├── skill.md                        ← Agent identity, capabilities, trigger conditions
├── CLAUDE.md                       ← This file — repository operating instructions
└── system-instructions.md          ← Detailed agent operating instructions
```

---

## AI Assistant Behavior in This Repository

### Before Answering Any Status Question
1. **Read `state/engagement-state.json`** — this is the machine-readable source of truth
2. **Read `deck/onerisk-tprm-monthly-synthesis.md`** — this is the human-readable current state
3. If the two files conflict, **flag the conflict explicitly** — do not silently resolve it
4. **Never answer from memory alone** — memory is not ground truth; the files are

### Before Proposing Any Change
1. Read the current state from both source of truth files
2. Present the change in Was → Will Be + Reason format
3. Do not apply the change until Clark explicitly approves
4. Apply the change to both files simultaneously to keep them in sync

### For Governance or Methodology Questions
Reference `references/` first. The reference library contains authoritative content for:
- All ServiceNow IRM modules
- Deloitte delivery methodology
- OOTB vs. customization decisions
- Integration architecture patterns
- Phase-specific procedures

### For Historical Questions
Read `context/engagement-history.md`. Note that this file is being populated by Clark — it may be incomplete for early phases.

### For Strategic Recommendations
Read `context/recommended-next-steps.md`. Note this is AI-generated and improves as `context/engagement-history.md` is populated.

---

## The Update Workflow

### How Clark Updates the Engagement State

**Method 1: Meeting Notes Drop (Automated)**
1. Create a meeting notes file: `YYYY-MM-DD-[topic].md`
2. Drop it into `updates/meeting-notes/`
3. Push to the branch
4. GitHub Action triggers `parse_updates.py` automatically
5. Review the proposed-changes file generated in `updates/proposed-changes/`
6. Apply approved changes to synthesis deck and state

**Method 2: Direct Chat Update (Most Common)**
1. Paste meeting notes, email, or bullet points to the AI assistant
2. AI reads current state and identifies changes
3. AI presents structured before/after table
4. Clark approves (single word: "go", "approved", "yes")
5. AI pushes changes to both files in one commit

**Method 3: Quick Single-Field Update**
1. Tell the AI in plain English: "Mark Avetta UAT as complete"
2. AI reads current state, identifies the exact field
3. AI proposes the change
4. Clark approves
5. AI pushes

---

## Key Conventions

### Date Format
Always use `YYYY-MM-DD` (ISO 8601). No ambiguous formats (no `3/5/26`, no `March 5`).

### Status Colors
| Color | Meaning |
|-------|---------|
| `GREEN` | On track. No action needed. |
| `YELLOW` | At risk or requires monitoring. Action may be needed. |
| `RED` | Blocked or critical. Immediate action required. |

### Issue IDs
Sequential format: `ISS-NNN` (e.g., ISS-001, ISS-002). Do not reuse IDs — retired issues remain in history.

### Meeting Note File Naming
`YYYY-MM-DD-[topic-with-hyphens].md`
Examples:
- `2026-03-05-sprint-12-standup.md`
- `2026-03-09-go-no-go-meeting.md`
- `2026-03-13-go-live-day-notes.md`

### Proposed Change File Naming (Auto-Generated)
`YYYY-MM-DD-HH-MM-proposed-changes.md`

---

## Engagement Context Quick Reference

### Program
- **Client**: Verizon (VZ)
- **Program**: OneRisk TPRM
- **Platform**: ServiceNow IRM (Zurich release)
- **Delivery Partner**: Deloitte (Global Elite ServiceNow Partner)
- **Current Sprint**: Sprint 12 of 12 (Final Sprint, as of 2026-03-05)
- **Go-Live Target**: 2026-03-13
- **Go/No-Go Gate**: 2026-03-09

### Stakeholders
| Name | Role | Org | Communication Style |
|------|------|-----|-------------------|
| Clark Johnson | Delivery Lead / PM | Deloitte | Operator of this agent |
| Tony Scott | Delivery Architect | Deloitte | Decision-ready: options, risks, recommendation |
| Sudhakar Sivasubramanian | VZ Program Lead | Verizon | Decision-ready: clear ask |
| Heidi | Functional Lead, TPRM | Deloitte | Technical depth; owns IRQ and BitSight |
| Vidhya Sagar | Technical Architect | Deloitte | Technical depth; owns integration design |
| Arav Sundareswaran | VZ Architect | Verizon | Technical depth; architecture rationale |
| Alec Barone | Developer | Deloitte | Task assignments; blocker escalation |
| Gary S Vick | Integrations Lead | Deloitte/VZ | Integration operations; MID Server |
| Merlyn | Program Sponsor | CSG / Verizon | Executive crisp: Issue → Impact → Ask |
| Lauren | ERM UAT Lead | Verizon | UAT sign-off; ERM workflow owner |
| Jennifer | VCS UAT Lead | Verizon | UAT sign-off; VCS workflow owner |

### Active Issues (as of 2026-03-05 — verify from state.json)
| ID | Issue | Status |
|----|-------|--------|
| ISS-001 | IRQ Scoring — Bias Factor | RESOLVED |
| ISS-002 | BitSight GRC Issue Generation (C2) | ACTIVE BLOCKER |
| ISS-003 | Avetta Staging Environment Access | ACTIVE BLOCKER |
| ISS-004 | Ariba Stage Misconfiguration | IN PROGRESS |
| ISS-005 | VCS Outbound API | IN SCOPING |

### Terminology
- Client-facing platform name: **"1Risk"** (not "ServiceNow")
- Program name: **"OneRisk"**
- Questionnaires: **IRQ** (Risk Intelligence), **DDQ** (Due Diligence)
- TPRM ownership: **VCS + ERM** (dual ownership)
- Integrations: **BitSight**, **Avetta**, **Ariba**, **EHS**
- Team reference in client-facing output: **"the team"** (not "Deloitte")

---

## What NOT to Do

- **Never auto-apply changes** to synthesis deck or state.json without Clark's approval
- **Never use memory** as a substitute for reading the state files
- **Never ignore a conflict** between state.json and the synthesis deck — always surface it
- **Never delete history** — only append or update; archived issues remain in records
- **Never use "ServiceNow"** in client-facing outputs — use "1Risk"
- **Never guess status** — if you don't have current information, say so and ask Clark

---

## GitHub Action: parse-meeting-notes.yml

The workflow triggers on any push that includes a file in `updates/meeting-notes/`.

**Requirements:**
- `OPENAI_API_KEY` must be set as a GitHub repository secret
- Python 3.11 is used (set up by the workflow)
- `openai` and `PyYAML` are installed by the workflow

**What it does:**
1. Checks out the repo
2. Installs dependencies
3. Runs `scripts/parse_updates.py`
4. Commits and pushes any generated proposed-changes files

**The proposed-changes output is never auto-applied to state files or the deck.** Clark always reviews and approves manually.

---

*CLAUDE.md is the operating manual for AI assistants working in this repository.*
*Last updated: 2026-03-05. Maintained by Clark Johnson and the VZ1R Delivery Agent.*
