# Imagine Phase Artifacts Reference

## Table of Contents
1. Phase Overview
2. Project Charter
3. RAID Log
4. Stakeholder Register
5. WBS / Project Plan
6. Governance Framework
7. Discovery & Design Workshop Structure
8. Module Scoping Matrix
9. High-Level Roadmap Template
10. Entity & Data Model Design Artifacts

---

## 1. Phase Overview

**Imagine** encompasses Plan and Design. Unlike a traditional waterfall gate, Imagine overlaps with early
Deliver activities by design — development kickoff and IRM Core Data build begin during Imagine while
later-module requirements are still being finalized.

**Standard Imagine Activities (concurrent tracks):**

| Track | Activities |
|-------|-----------|
| PMO & Governance | Kickoff, stakeholder alignment, Ways of Working, governance model, RAID log, project plan |
| IRM Core Data | Entity/asset inventory requirements, risk & control library sourcing, data modeling, record form design |
| Module Requirements | Sequential per module: PCM → Risk → Issues → Audit (later modules overlap with early build sprints) |
| Key Decisions | Compliance content source (UCF evaluation), risk register source, policy management platform decision |
| OOB Demo Series | Facilitated demos of each in-scope module to inform design before build begins |
| Backlog | Continuous refinement from Day 1; user story drafting and acceptance criteria development |

**Imagine Exit Criteria (per module — not a single gate):**
- [ ] Finalized user stories with acceptance criteria signed off
- [ ] Key design decisions documented and approved
- [ ] Entity/asset hierarchy design approved
- [ ] Data model design document approved
- [ ] Sprint backlog for next module groomed and estimated
- [ ] DEV environment provisioned and accessible

**Full program Imagine exit (before final Deliver sprints):**
- [ ] All module requirements finalized
- [ ] All key decisions documented
- [ ] Governance model operating
- [ ] Compliance content source selected
- [ ] Policy management platform decision made
- [ ] Risk register source confirmed

---

## 2. Project Charter

### Required Sections
1. **Project Overview** — 2-3 sentence executive summary of purpose and scope
2. **Objectives** — 3-5 SMART objectives tied to business outcomes
3. **Scope** — In-scope modules, entities, integrations, and geographies; explicit out-of-scope list
4. **Deliverables by Phase** — Imagine / Deliver / Run deliverables listed
5. **Delivery Approach** — Imagine → Deliver → Run model; sprint cadence; hybrid agile/waterfall governance
6. **Team Structure** — Client roles + consultant roles with names where known
7. **RACI Summary** — Key decisions and activities mapped to R/A/C/I
8. **Assumptions** — Documented assumptions that, if violated, trigger scope/schedule impact
9. **Constraints** — Budget, timeline, resource, technical
10. **Risks (High-Level)** — Top 3-5 project-level risks with initial mitigations
11. **Success Criteria** — How the project will be declared complete/successful
12. **Governance** — Steering committee, workstream leads, escalation path, meeting cadence
13. **Budget Summary** — Total authorized, by phase if available
14. **Sign-Off** — Executive Sponsor, PM (client), PM (consultant), Date

### Quality Gate
Charter must be reviewed in a dedicated session — not circulated for async sign-off on complex
engagements. Ensure client sponsor has read and can articulate objectives before signing.

---

## 3. RAID Log

### Standard RAID Log Schema

| Field | Description |
|-------|-------------|
| ID | Sequential (R-001, A-001, I-001, D-001) |
| Category | Risk / Assumption / Issue / Dependency |
| Title | Short descriptive label |
| Description | Full description of the item |
| Impact | High / Medium / Low |
| Probability (Risks) | High / Medium / Low |
| Status | Open / In Progress / Closed / Accepted |
| Owner | Named individual — never a team |
| Due Date | For action items and issues |
| Mitigation / Resolution | What is being done |
| Date Raised | When logged |
| Date Closed | When resolved |

### Operating Rules
- Review RAID log at every weekly status meeting — it is a living document, not a one-time exercise
- Every risk with High Impact + High Probability requires a documented mitigation AND contingency plan
- Issues that remain Open for >5 business days without progress escalate to the steering committee
- Assumptions that are violated convert to Issues immediately

### Common IRM Implementation RAID Items

**Risks:**
- Client data for entity population not available on schedule → delays Sprint 1 entity load
- Control library not rationalized prior to PCM build → scope creep in attestation design
- Key client SME availability constrained during UAT → UAT timeline compression risk
- ServiceNow upgrade scheduled during Deliver phase → regression testing overhead

**Assumptions:**
- Client will provide a rationalized control framework prior to PCM design workshop
- DEV environment will be provisioned by [date] and maintained by client IT
- Named client workstream leads will participate in all design workshops
- Out-of-scope integrations will not be introduced during Deliver phase

**Dependencies:**
- Entity hierarchy design must be complete before Risk and PCM module build begins
- Identity and Access Management (IAM) integration required before UAT
- Executive sign-off on risk scoring methodology before Risk module configuration

---

## 4. Stakeholder Register

### Schema

| Name | Title | Organization | Role on Project | Influence | Interest | Engagement Strategy | Primary Contact |
|------|-------|--------------|-----------------|-----------|----------|--------------------|----|
| | | | Sponsor / Champion / SME / End User / Reviewer | High/Med/Low | High/Med/Low | Inform / Consult / Collaborate / Lead | Yes/No |

### Engagement Strategy Definitions
- **Inform:** One-way communication; receives status updates
- **Consult:** Input solicited; not a decision-maker
- **Collaborate:** Active participant in workshops and design sessions
- **Lead:** Decision authority; escalation target

---

## 5. WBS / Project Plan

### WBS Structure for IRM Implementation

```
1.0 Imagine
  1.1 Project Initiation
    1.1.1 Project Charter development and sign-off
    1.1.2 Stakeholder identification and register
    1.1.3 Governance framework setup
    1.1.4 Environment provisioning coordination
  1.2 Discovery
    1.2.1 Current state assessment
    1.2.2 Stakeholder interviews
    1.2.3 Data source identification
  1.3 Design
    1.3.1 Entity Framework design workshop
    1.3.2 Module scoping workshops (per module)
    1.3.3 Data model design
    1.3.4 Integration architecture design
    1.3.5 Design document review and approval
  1.4 Plan
    1.4.1 Sprint backlog development
    1.4.2 Resource plan finalization
    1.4.3 Sprint calendar
    1.4.4 Imagine phase closeout

2.0 Deliver
  2.1 Sprint [N] (repeat per sprint)
    2.1.1 Sprint planning
    2.1.2 Configuration / development
    2.1.3 Unit testing
    2.1.4 Sprint demo
    2.1.5 Sprint retrospective
  2.2 System Integration Testing
  2.3 UAT
    2.3.1 UAT planning
    2.3.2 UAT execution
    2.3.3 Defect management
    2.3.4 UAT sign-off
  2.4 Go-Live Preparation
    2.4.1 Cutover planning
    2.4.2 Training delivery
    2.4.3 Go-live readiness assessment
    2.4.4 Go-live execution

3.0 Run
  3.1 Hypercare
    3.1.1 Hypercare support
    3.1.2 Issue tracking and resolution
    3.1.3 Hypercare exit assessment
  3.2 Transition
    3.2.1 Knowledge transfer
    3.2.2 Runbook finalization
    3.2.3 Managed service / BAU handoff
  3.3 Project Close
    3.3.1 Lessons learned
    3.3.2 Final project report
    3.3.3 Project closure sign-off
```

---

## 6. Governance Framework

### Meeting Cadence Template

| Meeting | Frequency | Participants | Purpose | Owner |
|---------|-----------|--------------|---------|-------|
| Steering Committee | Bi-weekly or Monthly | Executive Sponsors, Program Leads | Milestone review, escalation resolution, strategic decisions | Program Manager |
| Project Status | Weekly | PMs, Workstream Leads | RAID review, milestone tracking, blocker resolution | PM (Client) |
| Sprint Planning | Every 2 weeks (Day 1) | Delivery team | Sprint commitment, story point assignment, dependency review | Scrum Master / PM |
| Sprint Demo | Every 2 weeks (Day 10) | Delivery team + client SMEs | Demo completed stories, gather feedback | Workstream Lead |
| Sprint Retro | Every 2 weeks (Day 10) | Delivery team | Process improvement, team health | Scrum Master |
| Architecture Review | As needed | Architects, Tech Leads | Configuration decisions, integration design, debt review | Solution Architect |
| Design Workshops | Per module (Imagine) | SMEs, Workstream Leads, Consultants | Requirements, design decisions, sign-off | Functional Lead |

### Decision Rights Framework

| Decision Type | Who Decides | Who Approves | Who is Informed |
|--------------|-------------|--------------|-----------------|
| Scope change | PM (client) | Executive Sponsor | Steering Committee |
| Configuration design | Workstream Lead | Functional Lead | PM |
| Customization approval | Solution Architect | Program Manager + Client IT | Steering Committee |
| Go-live authorization | PM (client) + PM (consultant) | Executive Sponsor | All stakeholders |
| Budget reforecast | PM (client) | Executive Sponsor | Steering Committee |

### Escalation Path
1. Team level — resolve within sprint
2. Workstream Lead — resolve within 2 business days
3. Program Manager — resolve within 3 business days
4. Steering Committee — next scheduled meeting or emergency session

---

## 7. Discovery & Design Workshop Structure

### Standard Workshop Template

**Pre-Work Package (distributed 5 business days prior):**
- Workshop objectives and agenda
- Pre-read materials (current state docs, reference frameworks, preliminary questions)
- Participant list and roles
- Required decisions to be made in the session

**Workshop Agenda Structure (Half-Day / 4 Hours):**
1. Context setting and objectives (15 min)
2. Current state walkthrough (45 min)
3. Future state design discussion (90 min)
4. Decision capture and validation (45 min)
5. Open items, next steps, owners (15 min)
6. Wrap-up (10 min)

**Post-Workshop Deliverable:**
- Workshop notes published within 2 business days
- Decisions log updated
- Open items added to RAID log with owners and due dates
- Design document section drafted based on outputs

---

## 8. Module Scoping Matrix

Use this matrix to confirm in-scope modules, phase, and go-live definition:

| Module | In Scope (Y/N) | Phase | Key Entities in Scope | Primary Use Cases | Go-Live Definition | SME Owner |
|--------|---------------|-------|----------------------|-------------------|--------------------|-----------|
| Policy & Compliance | | | | | | |
| Risk Management | | | | | | |
| Audit Management | | | | | | |
| Issues & Remediation | | | | | | |
| Privacy | | | | | | |
| BCM | | | | | | |
| TPRM | | | | | | |
| Entity Framework | Always Y | Phase 1 | All | Full hierarchy + tiering | All Tier 1/2 entities loaded | |

---

## 9. High-Level Roadmap Template

### Roadmap Structure

```
Phase         | Timeline       | Key Milestones
--------------|----------------|------------------------------------------
Imagine       | Weeks 1-8      | Charter signed, Design docs approved,
              |                | Sprint 1 backlog groomed
Deliver       | Weeks 9-36     | Sprint 1-N complete, UAT signed off,
(Sprints 1-N) |                | Go-live executed
Run           | Weeks 37+      | Hypercare (Weeks 37-44), BAU handoff
Hypercare     |                | (Week 45+)
```

### Roadmap Caveats to Always Include
- Timeline contingent on: environment availability, SME participation, data delivery, sign-off cadence
- Sprint count subject to change based on scope confirmed in Imagine workshops
- Dependencies on client IT delivery (environment provisioning, integrations, data) shown as swim lane

---

## 10. Entity & Data Model Design Artifacts

### Entity Framework Design Document — Required Sections
1. Entity hierarchy diagram (visual)
2. Entity class definitions with profile attribute list
3. Entity tier definitions and assignment criteria
4. Entity-to-module scoping matrix
5. Entity population source and data migration approach
6. Open decisions and assumptions

### Data Model Design Document — Required Sections
1. Scope and purpose
2. Module-by-module table/field inventory (OOB + custom)
3. Integration data flows (source → target, field mapping)
4. Custom field justifications
5. Data quality requirements and validation rules
6. Data migration approach (if applicable)
7. Sign-off

---

## 10. Ways of Working Session

One of the first Imagine activities. Establishes how the team will operate together for the duration of the engagement.

### Agenda
1. Team introductions and roles (15 min)
2. Communication norms — primary channels, response expectations, escalation path (20 min)
3. Meeting cadence confirmation — finalize all recurring sessions (15 min)
4. Environment strategy — DEV/TEST/PROD access, update set governance, change control (20 min)
5. Decision-making protocol — who decides what, how decisions are documented (15 min)
6. Agile operating model walkthrough — sprint cadence, ceremonies, DoR/DoD (20 min)
7. Tools and collaboration platforms — project tracker, documentation repository, status reporting (15 min)

**Output:** Ways of Working document distributed within 2 business days; becomes standing reference for the engagement.

---

## 11. OOB Demo Series

A structured series of facilitated ServiceNow IRM demonstrations conducted during Imagine to inform
design decisions before build begins. Each demo session covers one module and is tailored to the
client's current state challenges and target use cases.

### Demo Session Structure (per module, ~2 hours)
1. Module overview — OOB capabilities walkthrough (30 min)
2. Targeted scenarios — demonstrate workflows relevant to client's stated needs (60 min)
3. Gap identification — what OOB does vs. what the client needs (20 min)
4. Design decisions triggered — document what needs to be decided before build (10 min)

### Demo Series Sequencing
1. IRM Core Data & Entity Framework
2. Policy & Compliance Management
3. Risk Management
4. Issues Management
5. Audit Management
6. TPRM (if in scope)
7. BCM / Privacy (if in scope)

**Key output per demo:** Decision log update with open items requiring client resolution before that module enters build.

---

## 12. Key Decision Documentation

Formal decisions that must be documented, distributed, and signed off as Imagine milestones.
Undocumented decisions become scope disputes during Deliver.

### Standard Key Decisions Register

| Decision | Options | Owner | Required By |
|----------|---------|-------|-------------|
| Compliance content source | UCF license / manual mapping / other provider | Client (guided by Deloitte) | Before PCM build |
| Risk register source | ServiceNow native / import from existing / UCF-mapped | Client | Before Risk build |
| Policy management platform | ServiceNow native PCM / Mitratech PolicyHub / other | Client + Legal + Cyber alignment | Before PCM build |
| Risk scoring methodology | Qualitative (5×5) / Semi-quantitative / FAIR | Client risk leadership | Before Risk build |
| Entity hierarchy design | Structure + depth approved | Client risk/compliance leadership | Before IRM Core Data build |
| OOTB vs. customize decisions | Per-requirement sign-off using complexity scale | Deloitte SA + Client IT | Rolling through Imagine |
| Integration scope | Which integrations are in/out of scope | Client IT + Deloitte Architect | Before Sprint 1 |
| Regulatory framework mapping | Which frameworks (NIST, ISO, PCI, etc.) are in scope | Client compliance | Before PCM build |
