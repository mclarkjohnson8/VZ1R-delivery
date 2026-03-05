# VZ1R Delivery Agent
### Deloitte | OneRisk | Verizon | Clark Johnson, Engagement Manager

A purpose-built GitHub Copilot agent for the Verizon OneRisk engagement. This agent has full programmatic context of the engagement loaded and acts as a senior trusted advisor to Clark Johnson (Engagement Manager). It combines the ServiceNow IRM expertise of the base skill with deep engagement-specific knowledge of the Verizon OneRisk program — its history, team, workstreams, current state, open issues, and critical path.

---

## Repository Structure

| Path | Purpose |
|------|---------|
| `system-instructions.md` | Agent identity, operating principles, and detailed instructions |
| `skill.md` | Copilot skill definition and trigger configuration |
| `context/engagement-history.md` | Full engagement history and current state — canonical context; load first on any engagement-specific question |
| `context/recommended-next-steps.md` | AI-generated strategic recommendations; improves as history is populated |
| `status/current-status.md` | Rolling current status tracker — updated as the engagement progresses |
| `deck/onerisk-tprm-monthly-synthesis.md` | Human-readable status synthesis deck — primary stakeholder artifact |
| `state/engagement-state.json` | Machine-readable engagement state — source of truth for automated tools |
| `references/` | IRM module reference library (do not modify these files) |
| `updates/meeting-notes/` | Drop zone for incoming meeting notes, RAID exports, status updates |
| `updates/proposed-changes/` | Auto-generated diff proposals from the parser — review before accepting |
| `scripts/parse_updates.py` | OpenAI-powered parser; reads meeting notes, generates proposed changes |
| `CLAUDE.md` | Repository operating manual for AI assistants |

---

## How to Use

### Asking Questions About the Engagement

The agent automatically loads `context/engagement-history.md` before answering any engagement-specific question. Ask about:
- Current status, risks, issues, or decisions
- Specific workstreams (VCS, ERM, Privacy Legal, TPRM)
- Team members and stakeholder communication
- Integration status (BitSight, Avetta, Ariba, EHS)
- Go-live readiness and critical path

### Updating Engagement State

**Method 1 — Drop a file** into `updates/meeting-notes/` (any format: .md, .txt, .xlsx, .pptx). A GitHub Action will parse it and generate a proposed-changes file for review.

**Method 2 — Chat update**: Paste meeting notes, email summaries, or bullet points. The agent reads current state, identifies changes, presents a before/after comparison, and awaits your approval before pushing.

**Method 3 — Quick update**: Say in plain English, e.g., "Mark Avetta UAT as complete." The agent proposes the precise change and pushes after your approval.

All changes require explicit approval ("go", "approved", or "yes") before anything is written to the repository.

### Generating Artifacts

Ask for any delivery artifact by name or description. The agent produces complete, client-ready output — no placeholders. Reference the Imagine → Deliver → Run framework for phase-appropriate artifacts.

---

## Modules Covered

| Module | Description |
|--------|-------------|
| Policy & Compliance Management | Policy lifecycle, control mapping, attestation, regulatory frameworks |
| Risk Management | Risk register, appetite/tolerance, scoring, heat maps, remediation |
| Audit Management | Audit plans, engagements, findings, workpapers, issue integration |
| Issues & Remediation | Issue capture, SLA, remediation tracking, closure |
| Privacy Management | DPIA, consent, data inventory, GDPR/CPRA workflows |
| Business Continuity Management | BIA, BCP/DRP, exercise program, crisis management |
| Third Party Risk Management | Vendor onboarding, assessments, tiering, continuous monitoring |
| Entity Framework | Entity hierarchy, entity class, entity tier, profile configuration |

---

## Delivery Framework

All work follows the Deloitte **Imagine → Deliver → Run** lifecycle:

| Phase | Scope | Current State |
|-------|-------|---------------|
| **Imagine** | Plan + Design | Complete for all workstreams |
| **Deliver** | Build + Test + Close | Sprint 12 of 12 (Final Sprint) — Go-Live 2026-03-13 |
| **Run** | Hypercare + Managed Service | Begins 2026-03-13; Hypercare through 2026-03-27 |

---

## Artifact Output Standards

- **Complete:** No placeholders unless explicitly requested
- **Structured:** Tables for trackers, numbered lists for processes, prose for narrative
- **Client-ready:** Verizon terminology applied; Deloitte quality standards
- **Risk-aware:** `⚠️ Risk:` callouts for any configuration decisions carrying technical debt or scope risk
- **OOTB-first:** Every deviation from ServiceNow out-of-the-box requires documented justification

---

## Current Engagement Snapshot (as of 2026-03-05)

| Field | Value |
|-------|-------|
| Client | Verizon Communications |
| Program | OneRisk (unified GRC platform) |
| Platform | ServiceNow IRM (Zurich release) |
| Phase | TPRM Closeout — Sprint 12 of 12 |
| Go-Live | 2026-03-13 |
| Overall Status | 🟡 YELLOW |
| Engagement Manager | Clark Johnson (Deloitte) |

> ⚠️ Always verify current state against `state/engagement-state.json` — this snapshot may be outdated.

---

*VZ1R Delivery Agent — maintained by Clark Johnson and the Verizon OneRisk delivery team.*
*Reference `CLAUDE.md` for full operating instructions for AI assistants working in this repository.*
