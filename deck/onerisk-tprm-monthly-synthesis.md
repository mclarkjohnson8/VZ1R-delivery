# OneRisk TPRM Monthly Synthesis
## Verizon | Deloitte | ServiceNow IRM (Zurich) | Sprint 12 of 12

**As of:** 2026-03-05 | **Go-Live Target:** 2026-03-13 | **Go/No-Go Gate:** 2026-03-09

---

## Overall Program Status: 🟡 YELLOW

**Summary:** IRQ resolved without customization; BitSight Component 2 and external integrations (Avetta, Ariba) are active blockers; UAT underway. On track to 3/13 if blockers resolve by 3/6.

---

## Status Dashboard

| Dimension | Status | Summary |
|-----------|--------|---------|
| **Schedule** | 🟡 YELLOW | On track to 3/13; BitSight C2 and integration blockers must resolve by 3/5–3/6 |
| **Scope** | 🟢 GREEN | 86.3% complete; 11 of 17 epics done; 5 finalizing |
| **UAT** | 🟡 YELLOW | IRQ UAT targeted 3/5; BitSight C1 UAT underway; C2/Avetta/Ariba UAT blocked |
| **Risks & Issues** | 🟡 YELLOW | IRQ resolved; BitSight C2 active blocker; Avetta/Ariba pending resolution |
| **Transition** | 🟢 GREEN | Transition window active 2/10–3/17; on track; vendor freeze enforced |
| **Training** | 🟢 GREEN | Risk Intelligence session complete 2/26; Due Diligence session in progress 3/4–3/5 |
| **Go/No-Go Readiness** | 🟡 YELLOW | Decision gate 3/9; BitSight C2 scope decision required |

---

## Key Dates

| Date | Event |
|------|-------|
| **2026-03-05** | IRQ functional testing + stakeholder UAT |
| **2026-03-06** | Avetta / Ariba blocker resolution target |
| **2026-03-09** | **Go/No-Go Gate** — BitSight C2 scope decision |
| **2026-03-12** | Final UAT completion target |
| **2026-03-13** | **Go-Live Target** |
| **2026-03-17** | Transition window close |
| **2026-03-27** | Hypercare window close |

---

## Active Issues & Risks

### ISS-001 — IRQ Scoring: Bias Factor ✅ RESOLVED

| Field | Value |
|-------|-------|
| **Status** | RESOLVED |
| **Resolved Date** | 2026-03-04 |
| **Owner** | Heidi |
| **Resolution** | Resolved without customization. Configuration changes: maximize normalized input checkbox + metric weight adjustment |
| **Impact** | UAT unblocked. Functional testing 3/4 complete. UAT with stakeholders targeted 3/5. |
| **Notes** | Bias factor in ServiceNow scoring was undocumented. Gemini used to identify. Admin-level config only — no code changes. Settings documentation required. |

---

### ISS-002 — BitSight: GRC Issue Generation (Component 2) 🔴 ACTIVE BLOCKER

| Field | Value |
|-------|-------|
| **Status** | IN PROGRESS — ACTIVE BLOCKER |
| **Owner** | Heidi / Vidhya Sagar |
| **Decision Needed By** | 2026-03-09 |
| **Issue** | Known ServiceNow bug: only generating issues for operational alerts, not critical ones. Workaround requires slight customization. Enhanced findings-to-alerts logic in development. |
| **Impact** | Component 2 UAT blocked. Go-live scope decision required by 3/9. |
| **Options** | (A) Include with customization at go-live; (B) Defer C2 to post-go-live hypercare sprint |
| **Notes** | OOTB plugin (Component 1) is functional and can enable for UAT. Enhanced findings considered nice-to-have for initial launch. Tony Scott raised brittleness concern re: customization sustainability. |

---

### ISS-003 — Avetta Integration: Staging Environment Access 🔴 ACTIVE BLOCKER

| Field | Value |
|-------|-------|
| **Status** | IN PROGRESS — ACTIVE BLOCKER |
| **Owner** | Alec Barone / Gary S Vick |
| **Decision Needed By** | 2026-03-06 |
| **Issue** | Staging environment not connecting to Avetta due to subrogation instance policy changes. Firewall issue previously resolved by Gary Vick. New server error on Avetta side. Mark engaged for root cause + fix (ETA 24 hours from 3/5). |
| **Impact** | Cannot UAT Avetta integration in staging. Production validation in progress. |
| **Notes** | Fourth-party data component introduced during conversion. Gary Vick confirming production status. Subro endpoint exposure needed long-term. |

---

### ISS-004 — Ariba Integration: Stage Environment Misconfiguration 🟡 IN PROGRESS

| Field | Value |
|-------|-------|
| **Status** | IN PROGRESS |
| **Owner** | TBD |
| **Decision Needed By** | 2026-03-06 |
| **Issue** | Stage environment misconfiguration pending Ariba team fix. |
| **Impact** | Ariba UAT blocked in staging. |

---

### ISS-005 — Outbound API: VCS Integration Request 🔵 NEW — IN SCOPING

| Field | Value |
|-------|-------|
| **Status** | NEW — IN SCOPING |
| **Owner** | Anthony James (Tony) Scott / Arav Sundareswaran |
| **Issue** | Business request (CSG-supported) for outbound read API exposing full TPRM dataset (TPR records, engagements, IRQs, DDQs, attachments, contacts, risks). Architecture North Star is GCP push but read-only API acceptable. Rate limits and pull strategy (daily vs delta) TBD. |
| **Impact** | Scope addition; architecture discussion required. |
| **Notes** | Arav confirmed read-only consumption acceptable. Volume, frequency, and pull strategy details needed from business. |

---

## Scope Progress

| Metric | Value |
|--------|-------|
| **Epics Complete** | 11 of 17 (64.7%) |
| **Epics Finalizing** | 5 |
| **Overall Completion** | 86.3% |
| **Sprint** | 12 of 12 (Final Sprint) |
| **Sprint Day** | 2 of 10 |

### What Was Delivered
- Full migration from legacy Vendor Risk application to TPRM
- ~1,800+ fields and 100+ access rules eliminated (~70% custom footprint removed)
- Assessment framework rationalized: ~21 questionnaires → 11
- Vendor portal restored (data replication fixed; self-service re-enabled)
- Access model simplified (OOB roles; least-privilege)
- Notification volume reduced 50%+
- BitSight integration (Component 1 OOB + Component 2 custom issue generation in progress)
- IRQ scoring resolved via admin config (no code)
- Training program: 7 sessions through 3/17

---

## Integration Architecture Summary

| Integration | Type | Status | Notes |
|-------------|------|--------|-------|
| **BitSight C1** (OOB) | Alerts + scores intake | ✅ Functional | UAT underway |
| **BitSight C2** (custom) | Alert → 1Risk Issue generation | 🔴 Active defect | GRC issue generation bug; fix in dev |
| **Avetta** | Fourth-party data via API | 🔴 Staging blocked | Firewall fixed; Avetta server error pending |
| **Ariba** | Contracting data | 🟡 Stage blocked | Ariba team remediating |
| **EHS** | Integration scope | 🟡 Pending | Training scheduled 3/10 |

---

## Training Program

| Session | Date | Status |
|---------|------|--------|
| Risk Intelligence (IRQ) | 2026-02-26 | ✅ Complete |
| Due Diligence Requests (DDQ) | 2026-03-04 to 2026-03-05 | 🟡 In Progress |
| Additional sessions (5 remaining) | Through 2026-03-17 | ⏳ Scheduled |

---

## Stakeholder Map

| Name | Role | Org |
|------|------|-----|
| Clark Johnson | Delivery Lead / PM | Deloitte |
| Anthony James (Tony) Scott | Delivery Architect | Deloitte |
| Heidi | Functional Lead, TPRM | Deloitte |
| Vidhya Sagar | Technical Architect | Deloitte |
| Alec Barone | Developer | Deloitte |
| Gary S Vick | Integrations Lead | Deloitte/VZ |
| Sudhakar Sivasubramanian | VZ Program Lead | Verizon |
| Aravindhan "Arav" Sundareswaran | VZ Architect | Verizon |
| Lauren | ERM UAT Lead | Verizon |
| Jennifer | VCS UAT Lead | Verizon |
| Merlyn | Program Sponsor | CSG / Verizon |

---

## Go/No-Go Decision Framework (Gate: 2026-03-09)

| Criterion | Required | Current | Risk |
|-----------|----------|---------|------|
| IRQ UAT complete | Yes | 🟡 In progress (3/5) | Medium |
| BitSight C1 UAT complete | Yes | 🟡 Underway | Medium |
| BitSight C2 scope decided | Yes | 🔴 Pending (3/9) | High |
| Avetta validated | Yes | 🔴 Staging blocked | High |
| Ariba validated | Yes | 🔴 Stage blocked | High |
| Training on track | Yes | 🟢 On track | Low |
| Cutover plan confirmed | Yes | 🟡 Pending UAT | Medium |

---

*Maintained by the VZ1R Delivery Agent. Source of truth: `state/engagement-state.json`.*
*To propose updates: drop meeting notes in `updates/meeting-notes/` or chat with the agent.*
