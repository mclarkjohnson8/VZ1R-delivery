# Current Status: Verizon OneRisk TPRM
### Deloitte | Clark Johnson, Engagement Manager

**Last Updated:** 2026-03-05
**Sprint:** 12 of 12 — Day 2 of 10
**Go-Live Date:** 2026-03-13
**Go/No-Go Gate:** 2026-03-09

---

## Overall Status: 🟡 YELLOW

BitSight Component 2 GRC issue generation defect is an active blocker; descope option open at Go/No-Go (2026-03-09). Avetta and Ariba blocked pending external team actions. IRQ resolved; UAT on track for 2026-03-05. Go-live on track contingent on 2026-03-06 UAT signoff and 2026-03-09 Go/No-Go decision.

---

## Status by Dimension

| Dimension | Status | Signal |
|-----------|--------|--------|
| Schedule | 🟡 Yellow | On track to 2026-03-13 go-live; BitSight C2 and external integration blockers must resolve |
| Scope | 🟢 Green | 86.3% design and build complete (11 of 17 epics done) |
| UAT | 🟡 Yellow | IRQ UAT 2026-03-05; BitSight C1 UAT underway; C2/Avetta/Ariba blocked pending external actions |
| Risks & Issues | 🟡 Yellow | IRQ resolved; BitSight C2 active blocker; Avetta firewall approved pending validation; Ariba stage misconfigured |
| Transition | 🟢 Green | Transition window active (2026-02-10 – 2026-03-17); vendor freeze enforced |
| Training | 🟢 Green | Risk Intelligence complete 2026-02-26; DDR session in progress (2026-03-04 – 2026-03-05) |
| Go/No-Go Readiness | 🟡 Yellow | Decision gate 2026-03-09 — BitSight C2 scope decision required |

---

## Open Issues

| ID | Issue | Severity | Status | Owner | Target |
|----|-------|----------|--------|-------|--------|
| ISS-001 | IRQ Scoring — Bias Factor | Medium | ✅ RESOLVED 2026-03-04 | Heidi | — |
| ISS-002 | BitSight GRC Issue Generation (C2) | High | 🔴 ACTIVE BLOCKER | Vidhya Sagar | 2026-03-09 |
| ISS-003 | Avetta Staging Environment Access | Medium | 🔴 ACTIVE BLOCKER | Alec Barone / Gary S Vick | 2026-03-06 |
| ISS-004 | Ariba Stage Misconfiguration | Medium | 🟡 IN PROGRESS | TBD (Ariba Team) | 2026-03-06 |
| ISS-005 | VCS Outbound API Request | Low | 🔵 IN SCOPING | Tony Scott / Arav | TBD |

---

## Active Risks

| # | Risk | Overall | Owner | Deadline |
|---|------|---------|-------|----------|
| R2 | BitSight C2 — fix not validated; go-live inclusion at risk | High | Vidhya Sagar | 2026-03-09 |
| R3 | UAT not signed off by 2026-03-06 | High | Lauren / Jennifer | 2026-03-06 |
| R4 | Go-live delayed beyond 2026-03-13 | Medium | Clark Johnson | 2026-03-09 |
| R5 | BitSight training scope dependent on C2 resolution | Medium | Heidi | 2026-03-09 |
| R6 | Avetta staging connectivity not validated | Medium | Gary S Vick | 2026-03-05 |
| R7 | Ariba stage environment not remediated | Medium | Ariba Team | 2026-03-06 |

---

## Key Decisions Pending

| # | Decision | Owner | By When |
|---|----------|-------|---------|
| 2 | Accept BitSight C2 descope if not resolved by 2026-03-09 | Verizon Leads (Lauren / Jennifer) | 2026-03-09 (Go/No-Go) |
| 3 | UAT Signoff — Go or No-Go | ERM & VCS Leads | 2026-03-09 |

---

## Critical Path — Next 2 Weeks

| Date | Event | Owner | Status |
|------|-------|-------|--------|
| 2026-03-05 | BitSight C2 fix target | Deloitte Tech Lead (Vidhya Sagar) | 🔴 In progress |
| 2026-03-05 | IRQ stakeholder UAT | Lauren (ERM) / Jennifer (VCS) | 🟡 Scheduled |
| 2026-03-05 | Avetta staging validation | Offshore Dev Team / Gary S Vick | 🔴 Pending |
| 2026-03-06 | UAT written signoff | ERM & VCS Leads | 🟡 Pending UAT completion |
| 2026-03-06 | Ariba environment remediation | Ariba Team | 🟡 External dependency |
| 2026-03-09 | **Go / No-Go Decision** | Verizon Leads | ⏳ Gate |
| 2026-03-10 | EHS integration training | TBD | ⏳ Scheduled |
| 2026-03-12 | Final UAT completion + prod migration + smoke test | Deloitte + Release Team | ⏳ Pending |
| **2026-03-13** | **GO-LIVE** | All | 🎯 Target |
| 2026-03-17 | Transition window close; vendor freeze lift | Clark Johnson | ⏳ |
| 2026-03-17 – 2026-03-27 | **Hypercare** | Deloitte | ⏳ |

---

## Epic Status (Sprint 12)

| Epic | Status | Notes |
|------|--------|-------|
| DQDs | ✅ Complete | — |
| Notifications | ✅ Complete | — |
| BitSight Component 1 (OOB) | ✅ Complete | UAT underway |
| BitSight Component 2 (Issue Generation) | 🔴 Active defect | Fix target 2026-03-05; descope option at Go/No-Go |
| Workspaces | ✅ Complete | — |
| Reports | ✅ Complete | — |
| IRQ Scoring | ✅ Resolved | Config fix applied 2026-03-04; UAT 2026-03-05 |
| UAT | 🟡 In Progress | Multiple tracks active |
| Avetta Integration | 🔴 Blocked | Staging connectivity pending |
| Ariba Integration | 🟡 Blocked | Stage environment remediation pending |

---

*Last updated: 2026-03-05 — update this file whenever Clark provides a new status artifact.*
*Source of truth for automated tools: `state/engagement-state.json`*
*Human-readable synthesis deck: `deck/onerisk-tprm-monthly-synthesis.md`*
