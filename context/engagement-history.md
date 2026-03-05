# Engagement History: Verizon OneRisk
### Deloitte | Clark Johnson, Engagement Manager

---

## 1. Client & Engagement Overview

- **Client:** Verizon Communications
- **Program Name:** OneRisk
- **Platform:** ServiceNow IRM (Integrated Risk Management)
- **Engagement Manager:** Clark Johnson (Deloitte)
- **Engagement Start:** July 2024
- **Current Date Context:** March 5, 2026
- **Current Status:** TPRM Closeout — final sprint (Sprint 12 of 12), Go-Live March 13, 2026

**What OneRisk Is:**
OneRisk is Verizon's unified Governance, Risk, and Compliance (GRC) platform built on ServiceNow IRM. It automates business process owner workflows: controls evaluation, risk assessment measurement, and issue management resolution across Cybersecurity, Enterprise Risk, and Privacy.

**Use Cases in Production:**

| Capability | VCS | ERM | Privacy Legal | TPRM |
|-----------|-----|-----|---------------|------|
| Core Data Management | Yes | Yes | Yes | Yes |
| Policy Management | Yes | | | |
| Risk Management | Yes | Yes | | |
| Controls and Compliance | Yes | Yes | | |
| Third Party Risk Management | Yes | Yes | | Yes |
| Privacy Management | | | Yes | |
| Audit Management | Yes | | | |

---

## 2. Contract History

| Contract | Period | Scope Summary |
|----------|--------|---------------|
| Contract 1 | July 2024 – ~late 2024 | Initial IRM implementation — VCS workstream primary; ERM initiated late in period |
| Contract 2 | Jan 2025 – ~mid 2025 | Stabilization and operationalization — VCS, ERM, Privacy Legal, Incident Management |
| Contract 3 | ~mid 2025 – March 2026 | Maturity phase + TPRM Closeout; all workstreams; program closes post-TPRM go-live |

---

## 3. Engagement Phases

| Phase | Period | Workstreams Active | Status |
|-------|--------|-------------------|--------|
| Initial Phase | July 2024 – December 2024 | VCS (Jul–Dec); ERM initiated Nov 2024 | Complete |
| Stabilization Phase | January 2025 | VCS, ERM, Privacy Legal | Complete |
| Operationalization Phase | May 2025 | All workstreams | Complete |
| Maturity Phase | October 2025 | All workstreams | Complete (non-TPRM work closed Dec 2025) |
| TPRM Closeout | Jan 2026 – Mar 2026 | TPRM (VCS + ERM ownership) | In Progress — Go-Live 2026-03-13 |

---

## 4. Deloitte Engagement Team

| Name | Role | Workstream(s) |
|------|------|---------------|
| Clark Johnson | Engagement Manager | All — program oversight |
| Aravindhan | Technical Lead (Architect) | TPRM / Platform |
| Sudhakar | Technical Lead | TPRM / Platform |
| Vidhya | Technical Architect | TPRM (BitSight integration) |
| Heidi | Functional Lead | TPRM |
| Tony | Functional Lead / SME | TPRM |
| [Offshore Dev Team] | Development | TPRM integrations (Avetta, BitSight) |

---

## 5. Key Client Stakeholders

| Name | Organization | Role |
|------|-------------|------|
| Lauren | Verizon ERM | UAT Lead — IRQ / TPRM |
| Jennifer | Verizon VCS | UAT Lead — TPRM |
| Gary Vick | Verizon ServiceNow Platform | Platform Lead — infrastructure, firewall, release |
| Marc Vanderveen | Avetta | Avetta Integration Lead |
| [Ariba team contact] | Ariba | Ariba integration |

**Dual Ownership of TPRM:** Verizon Cyber Security (VCS) + Enterprise Risk Management (ERM)

---

## 6. Workstream History & Achievements

### 6.1 Verizon Cyber Security (VCS) — Operational

VCS was the founding workstream, initiated July 2024.

Key Achievements:
- Control framework cleaned: 1,109 to 790 controls (28% reduction); NIST mappings preserved
- 450+ unmanaged control objects removed (retired GCSO domain); eliminated legacy debt
- 50+ Policies mapped to 400+ Controls in Policy Hub; centralized compliance traceability
- Entity classes reduced: 37 to 15; aligned to CMDB and Clarity; reduced configuration complexity
- Unified Issue Management implemented; VCS as initiators of critical GRC process
- 50% faster audit evidence collection — validated by Q4'25 audit; quantified business value
- Access model simplified; custom ACLs reduced to OOB roles aligned to least-privilege

### 6.2 Enterprise Risk Management (ERM) — Operational

ERM initiated November 2024.

Key Achievements:
- SOX customizations removed; aligned to OneRisk data model; technical debt eliminated
- Control library ready for bulk import; eliminates manual re-keying from EY; enables self-service
- Tracfone audit finding remediated by deadline; next audit can commence; TPRM workflows enhanced pre-conversion
- ~150 non-strategic backlog items cleared; team focused on priority items
- 17 Slack alert automations deployed; reduced notification reliance; improved response time

### 6.3 Privacy Legal (PL) — Operational

Key Achievements:
- 30+ complex incidents resolved over ~4 months; platform stabilized from unusable to operational
- 250+ lines of custom code eliminated; upgrade blockers removed
- Zero critical incidents over 3-week sustained period; business expectation of stability met
- Issue Management expedited (Deloitte investment); delivered ahead of client request

### 6.4 Incident Management — Operational

Key Achievements:
- 30+ production incidents resolved; centralized L2/L3 response across all workstreams
- Cross-workstream alignment established; balanced feature delivery with platform stabilization
- Structured root cause analysis implemented; prevented recurring defects
- Cross-workstream L2/L3 model fully operational

### 6.5 TPRM — Closeout (Active)

Mission: Convert Verizon's existing ServiceNow Vendor Risk solution to the enhanced TPRM application — modernizing workflows and eliminating legacy customizations — while maintaining continuity of operations through go-live.

What Was Delivered:
- TPRM Module Migration: Full transition from legacy Vendor Risk to TPRM application
- Legacy Customization Removal: ~1,800+ fields and 100+ access rules eliminated (~70% custom footprint)
- Assessment Framework Rationalization: Reduced questionnaires from ~21 to 11; clarified domain ownership
- Vendor Portal Restoration: Data replication fixed; vendor self-service re-enabled
- Access Model Simplification: Custom ACLs reduced; OOB roles aligned to least-privilege
- Notification Rationalization: 50%+ reduction in notification volume
- BitSight Integration — Component 1: OOB alert and scores intake functional; UAT underway (as of 2026-03-04)
- BitSight Integration — Component 2: GRC issue generation (Verizon-specific criteria) — fix in progress; go-live inclusion dependent on resolution
- IRQ Scoring: Resolved via admin config 2026-03-04 (no customization); UAT 2026-03-05
- Training: 7-session program across all process areas through 2026-03-17

**IRQ Resolution Detail:** During Sprint 11 UAT, a hidden OOB bias factor in ServiceNow's IRQ scoring engine was found to prevent any scenario from producing "high" or "very high" results. Config-based fix confirmed: "Maximize normalized input" checkbox enabled; metric weight adjusted. Admin-level config — no code, no OOB deviation. Resolved 2026-03-04.

**TPRM Epic Status (Sprint 12, as of 2026-03-04):**

| Epic | Status |
|------|--------|
| DQDs | Complete |
| Notifications | Complete |
| BitSight Component 1 (OOB) | Complete — UAT underway |
| BitSight Component 2 (Issue Generation) | Active defect — fix target 2026-03-05; go-live inclusion TBD |
| Workspaces | Complete |
| Reports | Complete |
| IRQ Scoring | Resolved in Dev 2026-03-04; UAT 2026-03-05 |
| UAT | In Progress — multiple tracks active |

---

## 7. Current State (as of 2026-03-05)

**Sprint:** 12 of 12 (Day 2 of 10)
**Go-Live Target:** 2026-03-13
**Overall Status:** 🟡 YELLOW

**Status by Dimension:**

| Dimension | Status | Signal |
|-----------|--------|--------|
| Schedule | 🟡 Yellow | On track to 2026-03-13 go-live; BitSight Component 2 and external integration blockers must resolve |
| Scope | 🟢 Green | 86.3% design and build complete (11 of 17 epics done) |
| UAT | 🟡 Yellow | IRQ UAT 2026-03-05; BitSight Component 1 UAT underway; Component 2 UAT pending fix; Avetta/Ariba blocked pending external teams |
| Risks & Issues | 🟡 Yellow | IRQ resolved; BitSight GRC issue generation active blocker; Avetta firewall approved pending validation; Ariba stage misconfiguration pending |
| Transition | 🟢 Green | Transition window active (2026-02-10 – 2026-03-17); on track; vendor freeze enforced |
| Training | 🟢 Green | Risk Intelligence session complete 2026-02-26; DDR session in progress (2026-03-04 – 2026-03-05) |
| Go/No-Go Readiness | 🟡 Yellow | Decision gate: 2026-03-09 — BitSight Component 2 scope decision required |

**Open Issues:**

| Issue | Severity | Status |
|-------|----------|--------|
| IRQ Scoring Logic | RESOLVED (2026-03-04) | Config fix applied; UAT 2026-03-05 |
| BitSight Component 1 | Low | Functional; UAT underway |
| BitSight Component 2 (GRC Issue Generation) | High | Active defect; fix target 2026-03-05; descope option at 2026-03-09 Go/No-Go |
| Avetta Staging Connectivity | Medium | Firewall fix approved 2026-03-04; offshore validation pending |
| Ariba Stage Environment | Medium | Ariba-side misconfiguration; environment remediation target 2026-03-06 |

**Active Risks:**

| # | Risk | Overall | Deadline |
|---|------|---------|----------|
| R2 | BitSight Component 2 — fix not validated; go-live inclusion at risk | High | 2026-03-05 / 2026-03-09 |
| R3 | UAT not signed off by 2026-03-06 | High | 2026-03-06 |
| R4 | Go-live delayed beyond 2026-03-13 | Medium | 2026-03-09 |
| R5 | BitSight training scope dependent on Component 2 | Medium | 2026-03-09 |
| R6 | Avetta staging connectivity | Medium | 2026-03-05 |
| R7 | Ariba stage environment | Medium | 2026-03-06 |

**Key Decisions Pending:**

| # | Decision | Owner | By When |
|---|----------|-------|---------|
| 2 | Accept BitSight Component 2 descope if not resolved | Verizon Leads | 2026-03-09 (Go/No-Go) |
| 3 | UAT Signoff — Go or No-Go | ERM & VCS Leads | 2026-03-09 |

**Critical Path — Remaining:**

| Date | Event | Owner |
|------|-------|-------|
| 2026-03-05 | BitSight Component 2 fix target | Deloitte Tech Lead |
| 2026-03-05 | IRQ stakeholder UAT | Lauren (ERM) / Jennifer (VCS) |
| 2026-03-05 | Avetta validation | Offshore Dev Team |
| 2026-03-06 | UAT written signoff | ERM & VCS Leads |
| 2026-03-06 | Ariba environment remediation | Ariba Team |
| 2026-03-09 | Go / No-Go Decision | Verizon Leads |
| 2026-03-12 | Prod migration + smoke test | Deloitte + Release Team |
| 2026-03-13 | GO-LIVE | All |
| 2026-03-17 – 2026-03-27 | Hypercare | Deloitte |

---

## 8. Post-TPRM Program Themes (Future Engagement)

These are program-level themes for the next engagement phase — not in scope for TPRM closeout but important context:

| Theme | Description |
|-------|-------------|
| Establish Governance | Shared resources, cross-workstream ownership, remove remaining customizations |
| Update Data and Processes | Risk and compliance framework cleanup with CMDB alignment; shared taxonomy; Policy Library for ERM |
| Enable Self-Service | Harmonized/shared processes; reduce admin dependency |

---

## 9. Delivery Operating Model

- **Methodology:** Agile — 2-week sprints
- **Sprint Capacity:** 70–80 story points (typical)
- **Ceremonies:** Sprint planning, daily standup, sprint review, retrospective
- **Status Cadence:** Weekly status report to executive sponsor; steering committee per governance model
- **OOTB-First Policy:** Non-negotiable default. Any deviation requires: (1) Deloitte Tech Lead documents OOB fix not viable, (2) Deloitte PM prepares escalation package, (3) Verizon Leads approve in writing, (4) deviation logged in decision register
- **Escalation Path:** Delivery team → Deloitte PM → Verizon Workstream Lead → Steering Committee

---

## 10. Key Terminology

| Term | Definition |
|------|-----------|
| OneRisk | Verizon's unified GRC platform name |
| VCS | Verizon Cyber Security — workstream and organizational unit |
| ERM | Enterprise Risk Management — workstream and organizational unit |
| PL | Privacy Legal — workstream |
| TPRM | Third Party Risk Management — final workstream; currently in closeout |
| IRQ | Intelligent Risk Questionnaire — risk tiering instrument in TPRM |
| DDQ | Due Diligence Questionnaire — vendor assessment instrument |
| OOB / OOTB | Out of the Box — ServiceNow native functionality; deviation requires documented justification |
| BitSight | Third-party cyber risk intelligence vendor; integrated with TPRM |
| Avetta | Supply chain risk management vendor; integrated with TPRM |
| Ariba | SAP procurement platform; integrated with TPRM for contract data |
| EHS | Environmental Health & Safety — third-party integration in TPRM |
| Go/No-Go | Decision gate on 2026-03-09 to authorize production migration on 2026-03-12 |
| Transition Window | Deliberate operational pause (2026-02-10 – 2026-03-17) on TPRM activities to protect data integrity through go-live |
| Hypercare | Post-go-live stabilization period (2026-03-17 – 2026-03-27); high-touch support |

---

*Last updated: 2026-03-05. Source: program status artifacts, Sprint 12 standup, engagement state.*
*Update this file whenever Clark provides new status information, milestone completions, or decisions.*
