<!--
  OneRisk | TPRM Closeout
  Monthly Synthesis Deck — February 2026
  Prepared by: Deloitte Delivery Team
  As of: 3/4/2026 (Sprint 12, Day 1 of 10)
  Audience: All Stakeholders (Steering Committee, VZ Leads, Delivery Team)
-->

---

# OneRisk | TPRM Closeout
## Monthly Synthesis — February 2026
**Prepared by:** Deloitte Delivery Team
**As of:** March 4, 2026
**Sprint:** 12 of 12 (Day 1 of 10)
**Go-Live:** March 13, 2026

---
---

## SLIDE 1 — EXECUTIVE DASHBOARD

> *Primary view. Every number and status on this slide is sourced directly from the current delivery state.*

---

### OneRisk TPRM Closeout | Executive Dashboard
**As of March 4, 2026 · Sprint 12 of 12 · Day 1 of 10**

---

#### OVERALL STATUS: 🟡 YELLOW — IRQ RESOLVED; BITSIGHT ISSUE GENERATION & EXTERNAL INTEGRATIONS ACTIVE; UAT UNDERWAY

| Dimension | Status | Signal |
|-----------|--------|--------|
| Schedule | 🟡 Yellow | On track to 3/13 go-live; BitSight Component 2 and external integration blockers (Avetta, Ariba) must resolve by 3/5–3/6 |
| Scope | 🟢 Green | 86.3% design and build complete (11 of 17 epics done); 5 finalizing |
| UAT | 🟡 Yellow | IRQ UAT targeted 3/5; BitSight Component 1 UAT underway; Component 2 UAT pending fix; Avetta and Ariba UAT blocked pending external resolution |
| Risks & Issues | 🟡 Yellow | IRQ resolved (no customization); BitSight GRC issue generation active blocker; Avetta firewall approved pending validation; Ariba stage misconfiguration pending Ariba team fix |
| Transition | 🟢 Green | Transition window active (2/10–3/17); on track; vendor freeze enforced |
| Training | 🟢 Green | Risk Intelligence session complete 2/26; Due Diligence Requests session in progress (3/4–3/5) |
| Go/No-Go Readiness | 🟡 Yellow | Decision gate: 3/9 — BitSight Component 2 scope decision required; all other items tracking to resolution |

---

#### SPRINT 12 SNAPSHOT

| Item | Value |
|------|-------|
| Sprint | 12 of 12 |
| Days Complete | 1 of 10 |
| Focus | UAT completion · BitSight issue generation fix · External integration unblocking · Go/No-Go prep |
| Capacity (typical) | 70–80 points |
| Epics On Track | DQDs · Notifications · BitSight Component 1 · Workspaces · Reports · IRQ |
| Epics Requiring Attention | BitSight Component 2 (GRC issue generation) · Avetta · Ariba |

---

#### PATH TO GO-LIVE AT A GLANCE

```
TODAY         3/5          3/6          3/9          3/12-13       3/17
  |            |            |            |              |            |
  | BitSight   | BitSight   | UAT        | Go/No-Go    | Go-Live    | Hypercare
  | Component 2| fix target | Signoff    | Decision    | + Smoke    | Begins
  | fix in     | Avetta &   | deadline   | + BitSight  | Test       |
  | progress   | Ariba      |            | scope call  |            |
  | IRQ func.  | resolve    |            |             |            |
```

---

#### KEY DECISIONS REQUIRED

| # | Decision | Owner | By When | If Yes | If No |
|---|----------|-------|---------|--------|-------|
| 1 | ~~Approve IRQ scoring customization~~ — **CLOSED: No customization required. Config fix applied 3/4.** | Deloitte Tech Lead | Closed | N/A | N/A |
| 2 | Accept BitSight Component 2 descope (GRC issue generation) if not resolved by 3/5 | Verizon Leads | 3/9 (Go/No-Go) | Component 1 goes live; Component 2 as Phase 2 enhancement | Hold go-live; re-evaluate scope and date |
| 3 | UAT Signoff — Go or No-Go | ERM & VCS Leads | 3/9 | Proceed to production migration 3/12 | Evaluate scope, timeline, or risk acceptance |

---

#### OPEN ISSUES — SUMMARY

| Issue | Severity | Root Cause | Status | Target | If Unresolved |
|-------|----------|------------|--------|--------|----------------|
| IRQ Scoring Logic | ~~High~~ → **RESOLVED** | Hidden OOB bias factor (normalized input) not documented in ServiceNow — not a misconfiguration | Config fix applied 3/4 (no customization); functional testing EOD 3/4; UAT 3/5 with Lauren (ERM) & Jennifer (VCS) | 3/5 (UAT) | N/A — resolved |
| BitSight — Component 1 (OOB Alerts & Scores Intake) | Low | N/A — OOB functional | Fully functional; UAT underway as of 3/4 | 3/6 (UAT signoff) | N/A — working |
| BitSight — Component 2 (GRC Issue Generation) | High | Verizon-specific alert criteria not triggering 1Risk Issue generation; believed fixed 9:30 ET 3/4 — not yet validated | Active development (Deloitte Technical Lead); fix target 3/5; if unresolved, descope decision at 3/9 Go/No-Go | 3/5 (fix) / 3/9 (scope decision) | Component 2 descoped; Component 1 goes live; findings mapping as Phase 2 |
| Avetta — Staging Connectivity | Medium | Firewall policy change on Verizon sub-prod instance blocking data to test environment — outside Deloitte control | Firewall policy fix approved 5 PM ET 3/4; awaiting implementation; offshore team validating tonight | 3/5 (validation) | UAT cannot proceed in staging; go-live risk if unresolved |
| Ariba — Stage Environment Misconfiguration | Medium | Ariba test environment misconfigured on Ariba side — no Deloitte changes made to this integration; functioning in Production | Ariba team and Verizon ServiceNow platform team engaged and supporting; environment remediation required | 3/6 (remediation) | UAT of contracting scope blocked; note: UAT validation not required, only environment fix |

---

#### PROGRAM ACHIEVEMENT CONTEXT (Last ~1 Month)

| Workstream | Headline Achievement |
|-----------|---------------------|
| TPRM | IRQ resolved without customization; BitSight Component 1 UAT live; training underway; transition window enforced |
| VCS | 50% faster audit evidence collection validated in Q4'25 audit |
| ERM | 17 Slack alerts automated; control library ready for bulk import |
| Privacy Legal | Platform stabilized; zero critical incidents over 3-week period |
| Incident Mgmt | 30+ production incidents resolved; cross-workstream L2/L3 model operational |

---

## SLIDE 2 — TPRM WORKSTREAM OBJECTIVE & SCOPE

---

### TPRM Closeout | Workstream Objective

**Mission:** Convert Verizon's existing ServiceNow Vendor Risk solution to the enhanced TPRM application — modernizing workflows and eliminating legacy customizations — while maintaining continuity of operations through go-live.

**Dual Ownership:** Verizon Cyber Security (VCS) + Enterprise Risk Management (ERM)

---

#### What We Are Delivering

| Capability | Description |
|-----------|-------------|
| TPRM Module Migration | Full transition from legacy Vendor Risk to TPRM application |
| Legacy Customization Removal | ~1,800+ fields and 100+ access rules eliminated (~70% custom footprint) |
| Assessment Framework Rationalization | Reduced questionnaires from ~21 to 11; clarified domain ownership |
| Vendor Portal Restoration | Data replication fixed; vendor self-service re-enabled |
| Access Model Simplification | Custom ACLs reduced; OOB roles aligned to least-privilege |
| Notification Rationalization | 50%+ reduction in notification volume |
| BitSight Integration — Component 1 | OOB alert and scores intake functional; UAT underway |
| BitSight Integration — Component 2 | GRC issue generation (Verizon-specific criteria) — fix in progress; go-live inclusion dependent on 3/5 resolution |
| IRQ Scoring | Resolved via admin config 3/4; UAT 3/5 |
| Training | 7-session program across all process areas through 3/17 |

---

#### What This Is Not

- Not a net-new TPRM implementation — this is a modernization and migration of an existing solution
- Not a full-suite IRM expansion — TPRM is the final workstream in the OneRisk program before closeout
- Not a customization project — OOTB-first is the non-negotiable default; every deviation is documented and escalated

---

## SLIDE 3 — PATH TO GO-LIVE (DETAILED)

---

### Path to Go-Live | March 13, 2026

---

#### Track Status Overview

| Track | Window | Status | Next Gate |
|-------|--------|--------|-----------|
| UAT | 2/12 – 3/9 | Yellow | IRQ UAT 3/5; BitSight Component 1 UAT underway; Component 2 pending fix; Avetta/Ariba pending external resolution; signoff by 3/6 |
| Transition / Freeze | 2/10 – 3/17 | Green | Process freeze and cutover 3/6–3/13 |
| Training | 2/26 – 3/17 | Green | Due Diligence Requests: in progress (3/4–3/5) |
| Go-Live / Cutover | 3/12–3/13 | Green | Prod migration + smoke test 3/12 |

---

#### UAT Detail

- **Test Scripts:** 11 (+ new shorter scripts for Workspaces added)
- **IRQ:** Functional testing EOD 3/4; stakeholder UAT 3/5 (Lauren — ERM; Jennifer — VCS)
- **BitSight Component 1 (OOB):** UAT underway as of 3/4 — previously held; now open to stakeholders
- **BitSight Component 2 (Issue Generation):** UAT on hold pending fix; fix target 3/5; if unresolved, descoped at 3/9 Go/No-Go
- **Avetta:** UAT blocked in staging pending firewall validation (offshore team tonight 3/4); target 3/5
- **Ariba:** UAT of contracting scope blocked pending Ariba environment remediation; target 3/6
- **Minimum bar:** 80% of testers complete their work; all critical process flows tested regardless
- **Gate:** Written signoff from ERM & VCS leads by 3/6; no critical open defects

---

#### Transition Window — Why It Exists

The transition window (2/10–3/17) is a deliberate operational pause on specific TPRM activities to prevent data conflicts during cutover.

**Why it is required:**
- Re-architecture removes legacy customizations and changes underlying data structures, workflow logic, and integrations
- Vendor assessment response cycles run 15–30 business days — assessments started before go-live cannot cleanly migrate
- Without the freeze: in-flight record collisions, data divergence between users/vendors/migrated data, and post-go-live manual reconciliation that delays adoption

**What is frozen:**
- New assessment creation: 2/12 – 3/13
- Process freeze and cutover: 3/6 – 3/13
- Post go-live re-import of assessments: 3/17

---

#### Training Schedule

| Session | Date | Status |
|---------|------|--------|
| Risk Intelligence Process | 2/26 | Complete |
| Due Diligence Requests | 3/4 – 3/5 | In Progress |
| Issues Management | 3/5 | Upcoming |
| Integrations: EHS, Avetta | 3/10 | Upcoming |
| Workspaces & Reporting | 3/12 | Upcoming |
| Integrations: BitSight | 3/13 | Dependent on BitSight Component 2 resolution |
| Questionnaire Administration | 3/17 | Upcoming |

---

#### Go / No-Go Readiness Checklist

| Criteria | Status |
|----------|--------|
| UAT execution 80%+ testers complete | In Progress — IRQ 3/5; BitSight Component 1 underway; Component 2 pending; Avetta/Ariba pending external teams |
| UAT signoff by ERM & VCS (no critical defects) | Pending — gate: 3/6 |
| Testing evidence submitted | Pending |
| Transition compliance confirmed | On Track |
| Training Reference Guides complete | In Progress |
| Go/No-Go decision held (VZ Leads) | Pending |
| Release Team approves all EPCs | Pending |
| Prod migration and smoke test complete | Pending — 3/12 |

---

## SLIDE 4 — OPEN ISSUES: IRQ SCORING LOGIC

---

### Open Issue #1 — IRQ Scoring Logic
**Severity:** ~~High~~ → **RESOLVED** | **Resolution Date:** 3/4 | **Owner:** Deloitte Technical Lead

---

#### What Happened

During Sprint 11 UAT and final configuration review, a discrepancy was identified in how the Risk Intelligence Questionnaire (IRQ) calculates scoring. A hidden out-of-box bias factor value in ServiceNow was impacting scoring logic and was not documented, causing no scenario to produce a "high" or "very high" result.

The issue is compounded by the use of multi-select choice fields in the IRQ, where multiple selections should contribute equally to the risk score.

---

#### Resolution — Applied 3/4

**RESOLVED 3/4:** Config-based fix confirmed viable. "Maximize normalized input" checkbox enabled; metric weight adjusted. Admin-level configuration — no code, no OOB deviation. Functional testing EOD 3/4; stakeholder UAT 3/5.

⚠️ **Documentation required:** These configuration settings must be documented for TPRM admins. The impact of the "maximize normalized input" setting and metric weight on scoring results must be understood by anyone administering the IRQ going forward. Aravindhan and Sudhakar confirmed this requirement on the 3/4 architecture review call.

⚠️ **DDQ monitoring:** Minor possibility of impact on DDQs assessed and confirmed low. Multi-select field type must be documented and monitored if introduced into future DDQs — agreed by Heidi and Tony on the 3/4 call.

---

#### Technical Root Cause

| Element | Detail |
|---------|--------|
| Expected behavior | Normalized values drive IRQ scoring per ServiceNow documentation |
| Actual behavior | Hidden bias factor (OOB, undocumented) overriding normalized input — scoring discrepancies result |
| Complicating factor | Multi-select fields cannot map cleanly to actual values when equal contribution is required |
| Downstream risk | DDQ triggers are dynamically tied to IRQ scoring — configuration settings must be preserved and documented |
| Resolution | "Maximize normalized input" checkbox enabled; metric weight adjusted — admin config, no code |

---

#### Go-Live Impact

- **Resolved:** Config fix applied 3/4. Functional testing EOD 3/4. Stakeholder UAT 3/5 with Lauren (ERM) and Jennifer (VCS). Go-live on 3/13 intact pending UAT pass.

---

## SLIDE 5 — OPEN ISSUES: BITSIGHT INTEGRATION

---

### Open Issue #2 — BitSight Integration
**Severity:** High (Component 2) | **Target Resolution:** 3/5 | **Owner:** Deloitte Technical Lead

---

#### Two-Component Structure — Critical Distinction

| Component | Description | Status |
|-----------|-------------|--------|
| Component 1 — OOB Alerts & Scores Intake | Alerts received in ServiceNow; scores ingested; issues created via OOB flow | ✅ Functional — UAT underway as of 3/4 |
| Component 2 — GRC Issue Generation (Verizon-specific criteria) | Workflow generating 1Risk Issues based on Verizon-specific alert criteria | 🔴 Active defect — fix targeted 3/5 |

---

#### Component 2 — What Happened

The BitSight OOB integration is functional as designed (Component 1). Component 2 — the workflow that generates ServiceNow GRC Issues based on Verizon's specific alert criteria — is not functioning. The team believed a fix was in place as of 9:30 ET on 3/4; this has not been validated. Active development continues with fix target 3/5.

Additionally, a known Bitsight bug exists where the system generates issues only for operational alerts, not critical ones. A workaround requiring slight customization has been identified.

⚠️ **Risk:** The findings-to-alert linkage logic (alerts based on "percent change" spanning multiple risk vectors) is complex. Tony raised concerns about brittleness and operational feasibility. Deloitte Technical Lead has confirmed the logic is sound and applicable for the majority of cases. Vidhya's architectural diagram is pending approval and will be shared this week.

---

#### Recommended Path Forward

| Option | Description | Recommendation |
|--------|-------------|----------------|
| Option A — Fix Component 2 by 3/5; include in go-live | Fix validated; UAT completed; Component 2 included in 3/12 go-live | Preferred — pursue aggressively through 3/5 |
| Option B — Descope Component 2; deliver OOB only | Component 1 goes live 3/13; Component 2 delivered as Phase 2 post-go-live enhancement | Recommended fallback if fix not validated by 3/5 |

---

#### UAT Impact

- Component 1 (OOB): UAT underway — stakeholders testing as of 3/4
- Component 2 (Issue Generation): UAT on hold pending fix; if resolved 3/5, UAT can proceed; if not, descoped at 3/9 Go/No-Go
- Go/No-Go on 3/9 will present "what's in vs. what's out" if Component 2 is not resolved

---

## SLIDE 5B — OPEN ISSUES: EXTERNAL INTEGRATIONS

---

### Open Issue #3 — Avetta Integration: Staging Connectivity
**Severity:** Medium | **Target Resolution:** 3/5 | **Owner:** Verizon Network/Platform Team + Avetta

---

#### What Happened

A firewall policy change on Verizon's sub-prod (subrogation) instance began blocking data from reaching the staging, test, and dev environments. This was introduced during the conversion period and is outside Deloitte's control. A new API component bringing in fourth-party data — set up during conversion — is the specific element affected.

Gary Vick (Verizon ServiceNow Platform) and Marc Vanderveen (Avetta) have been actively engaged. The firewall policy fix (request #108) was **approved as of 5 PM ET on 3/4**. Implementation is pending. Offshore team will validate once implementation is complete tonight.

| Element | Detail |
|---------|--------|
| Root cause | Firewall policy on Verizon sub-prod blocking sub-prod-to-prod connectivity |
| Deloitte control? | No — Verizon network policy change required |
| Fix status | Approved 3/4 5 PM ET; awaiting implementation |
| Validation | Offshore team validating tonight (3/4) |
| UAT impact | Cannot proceed in staging until validated; production working |

---

### Open Issue #4 — Ariba Integration: Stage Environment Misconfiguration
**Severity:** Medium | **Target Resolution:** 3/6 | **Owner:** Ariba Team + Verizon ServiceNow Platform Team

---

#### What Happened

The Ariba integration predates the TPRM engagement. No changes were made to this integration by Deloitte. UAT identified the integration is not functioning in the staging environment due to a misconfiguration on the Ariba side. The integration is confirmed working in Production.

| Element | Detail |
|---------|--------|
| Root cause | Ariba test environment misconfigured — Ariba-side issue, not ServiceNow or Deloitte |
| Production status | Working |
| Staging status | Broken — pending Ariba team remediation |
| UAT impact | Contracting portion of TPRM UAT blocked until Ariba fixes their environment |
| Note | UAT validation not required for this item — only environment remediation needed |
| Deloitte control? | No — Ariba team must remediate |

---

## SLIDE 6 — EPIC & MILESTONE STATUS

---

### Sprint 12 | Epic & Milestone Tracker
**As of March 4, 2026**

---

#### Epic Summary

| Metric | Value |
|--------|-------|
| Total Epics | 17 |
| Finalizing Design | 1 |
| Currently Being Built | 5 |
| Complete (Design and Build) | 11 |
| Weighted Design and Build Complete | 86.3% |

---

#### Epic Detail

| Epic | Sprints | Target Finish | Status |
|------|---------|---------------|--------|
| DQDs | 10–11 | 3/3 | Complete |
| Notifications | 10–11 | 3/3 | Complete |
| BitSight Component 1 (OOB) | 10–11 | 3/4 | Complete — UAT underway |
| BitSight Component 2 (Issue Generation) | 11–12 | 3/5 (fix) / TBD (UAT) | Active defect — fix target 3/5; go-live inclusion TBD |
| Workspaces | 11 | 3/3 | Complete |
| Reports | 11 | 3/3 | Complete |
| IRQ Scoring | 11–12 | 3/5 (UAT) | Resolved in Dev 3/4; UAT 3/5 |
| UAT | 10–12 | 3/6 (signoff) | In Progress — multiple tracks active |

---

#### Milestones

| Milestone | Sprints | Finish Date | Status |
|-----------|---------|-------------|--------|
| Transition Period | 10–12 | 3/17 | On Track |
| Training | 11–12 | 3/17 | On Track — DDR session in progress |
| Go/No-Go Decision | 12 | 3/9 | Pending — dependent on BitSight Component 2, Avetta, Ariba resolution |
| Go-Live | 12 | 3/13 | Dependent on 3/9 Go/No-Go |

---

## SLIDE 7 — PROGRAM ACHIEVEMENT CONTEXT (LAST ~1 MONTH)

---

### OneRisk Program | February 2026 Achievements

> Context for stakeholders new to the engagement or reviewing across workstreams. TPRM is the final workstream; all others have reached operational state.

---

#### TPRM (Active — Closing Out)

| Achievement | Impact |
|-------------|--------|
| IRQ scoring resolved without customization (3/4) | Major blocker cleared; UAT on track for 3/5 |
| BitSight Component 1 (OOB) UAT opened to stakeholders (3/4) | Risk intelligence data flowing; testing underway |
| ~1,800+ fields and 100+ access rules eliminated | ~70% custom footprint removed; OOB capabilities unlocked |
| Assessment framework: ~21 to 11 questionnaires | Reduced respondent burden; clarified domain ownership |
| Vendor portal restored (data replication fixed) | Vendor self-service re-enabled; manual data entry reduced |
| 50%+ reduction in notification volume | Reduced noise; improved signal for risk owners |
| E2E UAT in progress | Multiple tracks active; on track for 3/6 signoff |
| Transition window active and enforced | Data integrity protected through go-live |
| Due Diligence Requests training in progress (3/4–3/5) | 5 sessions remaining through 3/17 |

---

#### Verizon Cyber Security (VCS) — Operational

| Achievement | Impact |
|-------------|--------|
| Control framework cleaned: 1,109 to 790 controls (28% reduction) | Reduced audit scope; NIST mappings preserved |
| 450+ unmanaged control objects removed (retired GCSO domain) | Eliminated legacy debt; cleaner data model |
| 50+ Policies mapped to 400+ Controls in Policy Hub | Centralized compliance traceability |
| Entity classes reduced: 37 to 15 | Aligned to CMDB and Clarity; reduced configuration complexity |
| Unified Issue Management implemented | VCS as initiators of critical GRC process |
| 50% faster audit evidence collection | Validated by Q4'25 audit — quantified business value |

---

#### Enterprise Risk Management (ERM) — Operational

| Achievement | Impact |
|-------------|--------|
| SOX customizations removed | Aligned to OneRisk data model; technical debt eliminated |
| Control library ready for bulk import | Eliminates manual re-keying from EY; enables self-service |
| Tracfone audit finding remediated by deadline | Next audit can commence; TPRM workflows enhanced pre-conversion |
| ~150 non-strategic backlog items cleared | Team focused on priority 1 items |
| 17 Slack alert automations deployed | Reduced notification reliance; improved response time |

---

#### Privacy Legal (PL) — Operational

| Achievement | Impact |
|-------------|--------|
| 30+ complex incidents resolved over ~4 months | Platform stabilized from unusable to operational |
| 250+ lines of custom code eliminated | Upgrade blockers removed |
| Zero critical incidents over 3-week sustained period | Business expectation of stability met |
| Issue Management expedited (Deloitte investment) | Delivered ahead of client request |

---

#### Incident Management — Operational

| Achievement | Impact |
|-------------|--------|
| 30+ production incidents resolved | Centralized L2/L3 response across all workstreams |
| Cross-workstream alignment established | Balanced feature delivery with platform stabilization |
| Structured root cause analysis implemented | Prevented recurring defects |

---

## SLIDE 8 — RISKS & ESCALATION MATRIX

---

### Active Risks & Escalation Framework

---

#### Risk Register (Active)

| # | Risk | Likelihood | Impact | Overall | Mitigation | Escalation Owner | Deadline |
|---|------|-----------|--------|---------|------------|-----------------|----------|
| R1 | ~~IRQ scoring issue~~ — **CLOSED: Resolved 3/4 via admin config; no OOB deviation** | Low | Low | Low | Config fix applied; functional testing EOD 3/4; UAT 3/5 | Deloitte Tech Lead | Closed |
| R2 | BitSight Component 2 (GRC issue generation) — fix not yet validated; go-live inclusion at risk | High | High | High | Fix target 3/5; if unresolved, descope to Phase 2 at 3/9 Go/No-Go; Component 1 OOB goes live | Deloitte Tech Lead + Verizon Leads | 3/5 / 3/9 |
| R3 | UAT not signed off by 3/6 | Medium | High | High | IRQ UAT 3/5; BitSight Component 1 active; Avetta/Ariba dependent on external teams; daily status updates | ERM & VCS Leads | 3/6 |
| R4 | Go-live delayed beyond 3/13 | Low-Medium | High | Medium | Contingency: BitSight Component 2 descoped; Avetta/Ariba tracked daily; risk acceptance option available | Steering Committee | 3/9 |
| R5 | BitSight training session (3/13) — scope dependent on Component 2 resolution | Medium | Medium | Medium | Reschedule to post-go-live if OOB-only scope confirmed at 3/9 | Deloitte PM | 3/9 |
| R6 | Avetta staging connectivity — firewall policy blocking sub-prod data flow | Medium | Medium | Medium | Policy fix approved 3/4; offshore validation tonight; escalation if issues persist post-approval | Verizon Network Team + Avetta | 3/5 |
| R7 | Ariba stage environment misconfiguration — UAT of contracting scope blocked | Medium | Medium | Medium | Ariba team and Verizon platform team engaged; environment remediation required by 3/6; no UAT validation needed — env fix only | Ariba Team + Verizon ServiceNow Platform | 3/6 |

---

#### If-This-Then-That Decision Framework

| Scenario | Trigger | Action | Owner | By |
|----------|---------|--------|-------|----|
| BitSight Component 2 — fix validated | Confirmed 3/5 | Proceed to UAT; include in go-live 3/12 | Delivery team | 3/5 |
| BitSight Component 2 — fix NOT validated by 3/5 | Confirmed 3/5 | Prepare in-vs-out scope view for 3/9 Go/No-Go; communicate to business | Deloitte PM | 3/5 EOD |
| BitSight — Verizon accepts Component 2 descope | Confirmed 3/9 | Close Component 2; deliver as Phase 2; UAT OOB flow only | Delivery team | 3/9 |
| BitSight — Verizon rejects descope | Confirmed 3/9 | Hold go-live; re-evaluate date; Steering Committee discussion | Steering Committee | 3/9 |
| Avetta — validation passes tonight | Confirmed 3/4–3/5 | Proceed to UAT in staging | Delivery team | 3/5 |
| Avetta — validation fails post-approval | Confirmed 3/5 | Immediate escalation; assess prod-only validation path | Deloitte PM + Verizon Network | 3/5 EOD |
| Ariba — environment remediated by 3/6 | Confirmed 3/6 | Proceed to contracting UAT | Delivery team | 3/6 |
| Ariba — not remediated by 3/6 | Confirmed 3/6 | Assess risk acceptance; contracting scope flagged at Go/No-Go | Deloitte PM + Verizon Leads | 3/6 EOD |
| UAT 80%+ complete, no critical defects | 3/6 | Proceed to Go/No-Go call on 3/9 | ERM & VCS Leads | 3/9 |
| UAT less than 80% or critical defects open | 3/6 | Convene emergency triage; assess scope/date options | Deloitte PM + Verizon Leads | 3/6 EOD |
| Go/No-Go = GO | 3/9 | Proceed to prod migration 3/12 + smoke test | Delivery team | 3/12 |
| Go/No-Go = NO-GO | 3/9 | Define revised plan; communicate to all stakeholders | Steering Committee | 3/9 EOD |

---

#### Escalation Protocol

Any solution requiring deviation from OOB must follow this path:

```
1. Deloitte technical lead confirms OOB fix not viable (documented)
2. Deloitte PM prepares escalation package:
   - Issue description (technical root cause, not project failure)
   - Options with associated risks and timeline impact
   - Recommended path with rationale
   - Reference to ServiceNow / vendor documentation
3. Escalation presented to Verizon Leads for approval
4. Written approval obtained before build begins
5. Deviation logged in project decision register
```

---

## SLIDE 9 — NEXT STEPS & DECISION CALENDAR

---

### Next Steps | March 4–17, 2026

---

#### Critical Path — Next 2 Weeks

| Date | Event | Owner | Decision / Output |
|------|-------|-------|------------------|
| 3/3 | IRQ + BitSight technical analysis | Deloitte Tech Lead | Complete — IRQ resolved; BitSight OOB cleared; Component 2 fix in progress |
| 3/4 (Today) | IRQ config fix applied; functional testing underway | Deloitte Tech Lead | Config fix confirmed (no customization); functional testing EOD; UAT 3/5 |
| 3/4 (Today) | BitSight Component 1 UAT opened to stakeholders | UAT team | Test execution underway |
| 3/4–3/5 | Due Diligence Requests training session | Deloitte | Training in progress |
| 3/5 | BitSight Component 2 fix target | Deloitte Tech Lead | Fix validated or descope decision triggered |
| 3/5 | IRQ stakeholder UAT | Lauren (ERM) / Jennifer (VCS) | UAT pass or defect identified |
| 3/5 | Issues Management training session | Deloitte | Training delivered |
| 3/5 | Avetta staging validation (offshore team) | Offshore Dev Team | Connectivity confirmed or escalation triggered |
| 3/5 | UAT completion target (80%+ testers; all critical flows) | ERM & VCS teams | UAT evidence package |
| 3/6 | UAT written signoff submitted | ERM & VCS Leads | Signoff document |
| 3/6 | Ariba environment remediation target | Ariba Team | Contracting UAT unblocked |
| 3/6–3/13 | Process freeze and cutover | All teams | Data integrity preserved |
| 3/9 | Go / No-Go Decision | ERM & VCS Leads + Verizon | Go or No-Go; BitSight Component 2 scope decided |
| 3/10 | EHS + Avetta integrations training | Deloitte | Training delivered |
| 3/12 | Prod migration + smoke test | Deloitte + Release Team | Production live |
| 3/12 | Workspaces & Reporting training | Deloitte | Training delivered |
| 3/13 | GO-LIVE | All | OneRisk TPRM live |
| 3/13 | BitSight training (scope per 3/9 decision) | Deloitte | Training delivered |
| 3/17 | Questionnaire Administration training | Deloitte | Training delivered |
| 3/17 | Post-go-live assessment imports complete | Verizon + Deloitte | Data migration complete |
| 3/17–3/27 | Hypercare | Deloitte | Issue tracking + rapid response |

---

#### Resource Notes

- **Offshore team:** Validating Avetta connectivity tonight (3/4) post-firewall approval
- **Deloitte Technical Lead:** BitSight Component 2 fix — output expected 3/5
- **On-shore/Off-shore coordination:** Critical over next 48–72 hours given compressed timeline
- **BitSight vendor:** Engaged and responsive; dedicated SME support requested for Component 2 resolution
- **Ariba team:** Engaged; environment remediation required by 3/6
- **Avetta (Marc Vanderveen):** Actively engaged and responsive

---

#### What Stakeholders Should Expect Next

| Audience | What is Coming | When |
|----------|--------------|------|
| Steering Committee | Go/No-Go outcome + BitSight Component 2 scope decision | 3/9 |
| Verizon ERM & VCS Leads | IRQ UAT request + BitSight Component 1 UAT + resolution updates | 3/5–3/6 |
| End Users | Training sessions per schedule above | 3/4–3/17 |
| Delivery Team | Sprint 12 execution: BitSight Component 2 fix + UAT completion + external integration unblocking | Daily |

---

---

## APPENDIX — ENGAGEMENT HISTORY & PROGRAM CONTEXT

---

### OneRisk Program | Engagement History

| Phase | Period | Workstreams Active | Status |
|-------|--------|-------------------|--------|
| Initial Phase | July 2024 – December 2024 | VCS (Jul–Dec); ERM initiated Nov 2024 | Complete |
| Stabilization Phase | January 2025 | VCS, ERM, Privacy Legal | Complete |
| Operationalization Phase | May 2025 | All workstreams | Complete |
| Maturity Phase | October 2025 | All workstreams | Complete (non-TPRM work closed Dec 2025) |
| TPRM Closeout | Jan 2026 – Mar 2026 | TPRM (VCS + ERM ownership) | In Progress — Go-Live 3/13 |

---

### OneRisk | Solution Overview

OneRisk is Verizon's unified platform for Governance, Risk, and Compliance (GRC) across risk management functions including Cybersecurity, Enterprise Risk, and Privacy. Built on ServiceNow IRM, it automates business process owner workflows: controls evaluation, risk assessment measurement, and issue management resolution.

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

### Key Challenges to Address Post-TPRM (Program Level)

These are program-level themes for the next engagement phase — not in scope for TPRM closeout but important context for stakeholders:

| Theme | Description |
|-------|-------------|
| Establish Governance | Shared resources, cross-workstream ownership, remove remaining customizations |
| Update Data and Processes | Risk and compliance framework cleanup with CMDB alignment; shared taxonomy across workstreams; Policy Library for ERM |
| Enable Self-Service | Harmonized/shared processes; reduce admin dependency |

---

*Prepared by Deloitte Delivery Team · OneRisk TPRM Closeout · March 4, 2026*
*Deloitte Global Elite ServiceNow Partner*