# Deliver Phase Artifacts Reference

## Table of Contents
1. Phase Overview
2. Sprint Capacity Calculator
3. Sprint Planning Artifacts
4. Sprint Tracker
5. Configuration Build Spec Template
6. UAT Plan
7. UAT Test Script Template
8. Defect Tracker
9. Go-Live Readiness Checklist
10. Cutover Plan Template
11. Weekly Status Report Template

---

## 1. Phase Overview

**Deliver** encompasses Build (sprint execution), Test (UAT), and Close (go-live + release).

Exit criteria before transitioning to Run:
- [ ] All sprint stories at Definition of Done
- [ ] UAT executed and signed off by client
- [ ] All P1/P2 defects resolved; P3/P4 disposition documented
- [ ] Go-Live Readiness Assessment passed
- [ ] Cutover plan executed
- [ ] Training completed for all user groups
- [ ] PROD environment validated post-cutover
- [ ] Hypercare team and process confirmed

---

## 2. Sprint Capacity Calculator

### Inputs

| Input | Description | Default |
|-------|-------------|---------|
| Sprint Duration | Working days | 10 |
| Team Members | Count by role | Variable |
| Meeting Overhead | % of time in ceremonies | 15% |
| Buffer | % for unplanned work, admin | 10% |
| PTO / Holidays | Days off per member | Per sprint |

### Capacity Formula per Team Member
```
Available Hours = (Sprint Days - PTO/Holiday Days) × Daily Hours
Net Capacity = Available Hours × (1 - Meeting Overhead % - Buffer %)
Story Points = Net Capacity ÷ Hours-per-Point
```

### Sprint Capacity Table Template

| Team Member | Role | Sprint Days Available | PTO/Holiday Days | Available Days | Hours/Day | Available Hours | Overhead (15%) | Buffer (10%) | Net Hours | Est. Story Points |
|------------|------|----------------------|-----------------|----------------|-----------|-----------------|----------------|--------------|-----------|-------------------|
| | SA | | | | 8 | | | | | |
| | Dev | | | | 8 | | | | | |
| | Dev | | | | 8 | | | | | |
| | QA | | | | 8 | | | | | |
| | PM | | | | 8 | | | | | |
| **Total** | | | | | | | | | | |

### Velocity Guidance
- Sprint 1: Use capacity-based estimate only; no velocity baseline yet
- Sprint 2: Establish baseline from Sprint 1 actuals
- Sprint 3+: Use rolling 2-sprint average for planning; flag if variance >20%
- ⚠️ Risk: Committing to velocity targets before Sprint 2 actuals are known leads to overcommitment

---

## 3. Sprint Planning Artifacts

### Sprint Planning Agenda (2-Hour Session)

1. Confirm DoR — verify all committed stories meet Definition of Ready (15 min)
2. Capacity review — confirm team availability, PTO, holidays (15 min)
3. Backlog review — Prioritization Committee has pre-ranked epics; confirm story priorities with Product Owner (15 min)
4. Story breakdown — decompose stories to task level; assign owners (60 min)
5. Team commitment — team confirms sprint scope based on capacity and DoR (10 min)
6. Dependency and blocker check — surface cross-team dependencies (5 min)

### Definition of Ready (DoR) — Story Enters Sprint When:
- [ ] User story scope defined and estimated (story points assigned)
- [ ] Acceptance criteria written, reviewed, and agreed
- [ ] Dependencies identified and cleared or risk-accepted with documented mitigation
- [ ] Test steps drafted
- [ ] Team capacity confirmed for the sprint
- [ ] Design spec / build spec available or confirmed to be ready before development begins

### Sprint Backlog Schema

| Story ID | Epic | User Story | Module | Acceptance Criteria | Story Points | Assignee | Sprint | Status | DoR Met | Dependencies | Notes |
|----------|------|-----------|--------|--------------------|-----------  |----------|--------|--------|---------|--------------|-------|

### Story Point Reference (IRM Context)

| Points | Effort Level | IRM Example |
|--------|-------------|-------------|
| 1 | Trivial | Update a field label; add a choice list value |
| 2 | Small | Configure a single UI policy; create a simple notification |
| 3 | Medium-Small | Configure a catalog item; build a simple workflow |
| 5 | Medium | Full control attestation workflow; risk scoring configuration |
| 8 | Large | Full module scoped setup; complex integration business rule |
| 13 | X-Large | Break down — story is too large; decompose before sprint |

### Definition of Done (DoD) — IRM Configuration Story is Done When:
- [ ] Configured in DEV per design/build spec
- [ ] Unit tested by developer (positive and negative scenarios)
- [ ] Peer reviewed by another team member
- [ ] Demo-ready without additional setup
- [ ] Documented in configuration workbook / build notes
- [ ] Stakeholder consensus in sprint review that DoD is met

---

## 4. Sprint Tracker

### Sprint Tracker Schema

| Story ID | Title | Assignee | Points | Status | Start Date | End Date | Actual Hours | Blockers | Notes |
|----------|-------|----------|--------|--------|------------|----------|--------------|----------|-------|

### Status Values
- **Not Started** — In backlog, meets DoR, not yet in progress
- **In Progress** — Active development/configuration
- **In Review** — Peer review or PM review pending
- **Blocked** — Cannot progress; blocker documented with date raised
- **Done** — Meets all DoD criteria; confirmed in sprint review

### Sprint Retrospective — Like / Learn / Lack / Long For Format

| Category | Question | Examples |
|----------|----------|---------|
| **Like** | What worked well and should continue? | Effective standups, clear design specs, good client engagement |
| **Learn** | What did we learn — about process, platform, or client? | UCF mapping complexity, entity scoping insight |
| **Lack** | What was missing that hurt delivery? | Late design decisions, incomplete test data, unclear acceptance criteria |
| **Long For** | What do we wish we had? | Earlier client SME access, automated test scripts, integrated environments |

Action items from retro are owned by named individuals and tracked in RAID log.

### Sprint Health Indicators
- **On Track:** Burndown trending to zero; no P1 blockers
- **At Risk:** Burndown behind by >20%; blocker unresolved >2 days
- **Off Track:** Committed stories will not complete; escalation required

---

## 5. System Integration Testing (SIT)

SIT is a distinct phase between sprint execution and UAT. It validates that all modules work together
correctly end-to-end and that integrations function as designed. SIT is owned by the Deloitte delivery
team; UAT is owned by the client.

### SIT Scope
- Cross-module workflow validation (e.g., Risk → Issue auto-creation; Audit Finding → Issue)
- Integration endpoint testing (any system integrations configured during Deliver)
- Data flow validation (entity relationships, rollup reporting, scoped list filtering)
- Notification and workflow trigger validation across all modules
- Performance validation on key pages and scheduled jobs

### SIT Entry Criteria
- [ ] All sprint stories at DoD
- [ ] TEST environment refreshed from DEV
- [ ] Integration test cases written and reviewed
- [ ] Test data loaded

### SIT Exit Criteria
- [ ] All integration scenarios pass
- [ ] No P1/P2 defects open
- [ ] Cross-module workflows validated end-to-end
- [ ] Deloitte tech lead sign-off
- [ ] UAT environment prepared from SIT-validated build

### ⚠️ Risk: Skipping SIT and Going Straight to UAT
Clients often want to compress timelines by merging SIT and UAT. This is a false economy — integration
failures discovered during UAT by business users are higher-cost to remediate and damage client confidence.
Hold the SIT gate.

---

## 5. Configuration Build Spec Template

### Purpose
Documents the exact configuration to be built for each sprint story, serving as the
developer's instruction set and the QA baseline.

### Build Spec Structure

**Header:**
- Story ID, Title, Module, Sprint, Author, Date, Reviewer

**Business Context:**
- Why this is being built; what business problem it solves

**Configuration Details:**
- Table / Form / Workflow being modified
- Field-by-field specification (name, type, default value, mandatory, visible, read-only)
- Business rule logic (written in plain English + pseudocode)
- UI Policy conditions and actions
- Workflow stages, transitions, and notifications

**Integration Points:**
- Upstream data sources (what feeds this)
- Downstream consumers (what this feeds)
- Cross-module dependencies

**Test Criteria:**
- Positive test: Expected behavior when used correctly
- Negative test: Expected behavior when misused or edge case
- Data setup required for testing

**Sign-Off:**
- Developer confirms build complete
- Reviewer confirms peer review complete

---

## 6. UAT Plan

### Required Sections

1. **Purpose & Scope** — What is being tested; what is explicitly out of scope
2. **UAT Approach** — Scenario-based testing; who executes; tools used (ServiceNow, Excel tracker)
3. **Entry Criteria** — What must be true before UAT begins
4. **Exit Criteria** — What must be true before UAT is declared complete
5. **Test Environment** — Instance, data set, access provisioning
6. **Roles & Responsibilities**

   | Role | Responsibility |
   |------|---------------|
   | UAT Coordinator (Consultant) | Test plan, script management, defect triage |
   | Business Tester (Client) | Script execution, defect logging |
   | Tech Lead (Consultant) | Defect resolution |
   | UAT Sign-Off Authority (Client) | Final approval |

7. **Test Scenarios** — Mapped to modules and user roles
8. **Defect Management Process** — Severity definitions, triage cadence, resolution SLAs
9. **UAT Schedule** — Dates for execution windows, defect fix sprints, re-test, sign-off
10. **Sign-Off Document Reference** — Who signs and what they are approving

### UAT Entry Criteria
- [ ] All sprint stories at Definition of Done
- [ ] TEST environment refreshed from DEV
- [ ] Test data loaded and validated
- [ ] UAT test scripts reviewed and approved by client
- [ ] All testers provisioned with correct roles/access
- [ ] Defect tracker established and shared

### UAT Exit Criteria
- [ ] All P1 defects resolved and re-tested
- [ ] All P2 defects resolved or formally deferred with sponsor approval
- [ ] P3/P4 defect disposition documented
- [ ] Client UAT sign-off obtained in writing
- [ ] No open design questions

---

## 7. UAT Test Script Template

### Script Header
- Script ID, Module, Test Scenario, Author, Date, Tester, Execution Date

### Script Body

| Step | Action | Test Data | Expected Result | Actual Result | Pass/Fail | Defect ID | Notes |
|------|--------|-----------|-----------------|---------------|-----------|-----------|-------|
| 1 | Navigate to... | | | | | | |
| 2 | Click / Enter... | | | | | | |

### Scenario Coverage by Module

**Policy & Compliance:**
- Create and publish a policy
- Map controls to policy statements
- Initiate and complete a control attestation
- Escalate failed attestation to issue

**Risk Management:**
- Create a risk definition and scoped risk
- Complete a risk assessment (likelihood + impact scoring)
- Create a risk response / treatment plan
- Trigger issue creation from risk threshold breach

**Audit Management:**
- Create and schedule an audit engagement
- Assign audit tasks to auditors
- Create and resolve an audit finding
- Generate finding → issue integration

**Issues & Remediation:**
- Create an issue manually
- Assign remediation task with due date
- Update progress and close the issue
- Escalate overdue issue

**TPRM:**
- Onboard a new vendor (entity creation)
- Launch vendor risk assessment
- Review assessment results and score
- Create vendor risk issue

**Entity Framework:**
- Create entity with correct class, tier, parent
- Update entity profile attributes
- Validate entity appears correctly in module scoped lists

---

## 8. Defect Tracker

### Defect Schema

| Defect ID | Title | Module | Severity | Priority | Status | Steps to Reproduce | Expected | Actual | Assignee | Date Logged | Target Fix Date | Date Resolved | Regression Tested |
|-----------|-------|--------|----------|----------|--------|-------------------|----------|--------|----------|-------------|-----------------|---------------|-------------------|

### Severity Definitions

| Severity | Definition | Resolution SLA |
|----------|------------|----------------|
| P1 — Critical | System unusable; data loss risk; security issue; blocks core workflow | 24 hours |
| P2 — High | Core functionality broken; workaround exists but unacceptable for go-live | 48-72 hours |
| P3 — Medium | Non-critical functionality impaired; workaround exists; acceptable for go-live with waiver | Next sprint |
| P4 — Low | Cosmetic issue; minor UX problem; no functional impact | Post go-live backlog |

### Defect Triage Cadence
- Daily defect triage during active UAT (15-30 min)
- P1/P2 defects: immediate escalation to tech lead; same-day acknowledgment
- P3/P4 defects: batch reviewed at daily triage
- ⚠️ Risk: Allowing P3 defects to accumulate without disposition creates go-live ambiguity

---

## 9. Go-Live Readiness Checklist

### Technical Readiness
- [ ] All UAT exit criteria met and sign-off obtained
- [ ] PROD environment provisioned and validated
- [ ] Cutover plan reviewed and approved
- [ ] Rollback plan documented and tested
- [ ] All user accounts and roles provisioned in PROD
- [ ] Integrations tested end-to-end in TEST; cutover approach for PROD confirmed
- [ ] Performance/load testing completed (if applicable)
- [ ] Security review completed (if required)

### Operational Readiness
- [ ] Training delivered to all user groups
- [ ] Training materials published to accessible location
- [ ] Support model documented (hypercare contacts, escalation path, ticketing process)
- [ ] Runbook published and distributed to support team
- [ ] SLAs and KPIs defined for hypercare period

### Business Readiness
- [ ] Executive sponsor confirms go-live authorization
- [ ] All in-scope business process owners briefed on go-live date and changes
- [ ] Communications sent to end users
- [ ] Hypercare support schedule communicated

### Go/No-Go Decision Meeting Agenda
1. Review readiness checklist status (15 min)
2. Open defect disposition — confirm P1/P2 resolved (10 min)
3. Cutover plan walkthrough (15 min)
4. Risk review — any last-minute concerns (10 min)
5. Formal go/no-go decision by executive sponsor (10 min)

---

## 10. Cutover Plan Template

### Sections
1. **Cutover Overview** — Date, time window, objectives, go-live definition
2. **Pre-Cutover Activities** — Steps to complete before cutover window opens
3. **Cutover Runbook** — Step-by-step execution with owner, time estimate, and validation step for each action
4. **Validation Checklist** — Post-cutover checks to confirm PROD is functioning correctly
5. **Rollback Triggers** — Conditions that would initiate rollback
6. **Rollback Procedure** — Step-by-step rollback with owner assignments
7. **Communication Plan** — Who is notified at each stage; go/no-go announcement template

### Cutover Runbook Schema

| Step | Activity | Owner | Start Time | Duration | Validation | Status |
|------|----------|-------|------------|----------|------------|--------|

---

## 11. Weekly Status Report Template

### Header
- Project Name, Reporting Period, Report Date, Prepared By, Distribution

### Sections

**1. Executive Summary** (3-5 sentences)
Overall project health, key accomplishments this week, and top priority for next week.

**2. Project Health Dashboard**

| Dimension | Status | Trend | Notes |
|-----------|--------|-------|-------|
| Schedule | 🟢 Green / 🟡 Yellow / 🔴 Red | ↑ ↔ ↓ | |
| Budget | | | |
| Scope | | | |
| Quality | | | |
| Resources | | | |
| Risks | | | |

**3. Accomplishments This Week**
Bullet list of completed milestones, delivered artifacts, and closed items.

**4. Planned for Next Week**
Bullet list of sprint commitments, milestones, and key activities.

**5. Key Risks & Issues**
Top 3-5 active RAID items with status and action.

**6. Decisions Needed**
Any decisions required from client leadership before next reporting period.

**7. Upcoming Milestones**

| Milestone | Target Date | Status |
|-----------|------------|--------|
