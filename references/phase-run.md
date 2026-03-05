# Run Phase Artifacts Reference

## Table of Contents
1. Phase Overview
2. Hypercare Plan
3. Hypercare Issue Tracker
4. SLA/KPI Framework
5. Knowledge Transfer Plan
6. Runbook Template
7. Lessons Learned
8. Project Closure Checklist

---

## 1. Phase Overview

**Run** encompasses Hypercare (stabilization) and the transition to Business-as-Usual (BAU) or
a managed service model.

Hypercare typically runs 4-8 weeks post go-live for standard IRM implementations; complex or
enterprise-wide rollouts may warrant 8-12 weeks.

Exit criteria before declaring project closure:
- [ ] All hypercare issues resolved or formally transitioned to BAU backlog
- [ ] Runbook published and accepted by operational team
- [ ] Knowledge transfer completed and signed off
- [ ] SLA/KPI baseline established
- [ ] Lessons learned documented and distributed
- [ ] Project closure document signed by executive sponsor

---

## 2. Hypercare Plan

### Required Sections

**1. Hypercare Scope**
Which modules, entities, and user groups are covered. What is explicitly out of scope (e.g., Phase 2 modules
not yet live).

**2. Hypercare Duration & Exit Criteria**

| Week | Focus | Exit Gate |
|------|-------|-----------|
| 1-2 | Stabilization — high-touch support; daily check-ins | P1 issue rate drops below threshold |
| 3-4 | Optimization — address P2/P3 backlog; user adoption monitoring | P2 resolution complete |
| 5-6 | Transition — knowledge transfer; runbook validation | KT sign-off obtained |
| 7-8 | Exit — final assessment; BAU handoff | Closure criteria met |

**3. Support Model During Hypercare**

| Support Tier | Scope | Response SLA | Contact Method |
|-------------|-------|-------------|----------------|
| Tier 1 (Client Help Desk) | Basic user questions, access issues | 4 business hours | Ticketing system |
| Tier 2 (Consultant Functional) | Configuration questions, process issues | 1 business day | Dedicated channel |
| Tier 3 (Consultant Technical) | System errors, integration failures, data issues | 4 hours (P1), 1 day (P2) | Direct escalation |
| Tier 4 (ServiceNow Support) | Platform defects, licensing | Per contract | ServiceNow portal |

**4. Staffing Plan**
Consultant team availability by week (full-time vs. reduced capacity) and client operational team
members taking ownership during transition.

**5. Issue Management During Hypercare**
All hypercare issues logged in tracker; triage daily for first 2 weeks, then 3x/week.
P1 issues have dedicated war-room response; P2+ follow standard SLA.

**6. Communication During Hypercare**
- Daily standup (Weeks 1-2): 15 min; consultant + client operational leads
- Weekly hypercare status report to executive sponsor
- Issue summary distributed to stakeholders weekly

---

## 3. Hypercare Issue Tracker

### Schema

| Issue ID | Title | Module | Severity | Reported By | Date Reported | Description | Root Cause | Resolution | Owner | Target Date | Status | Date Closed | Type |
|----------|-------|--------|----------|-------------|---------------|-------------|------------|------------|-------|-------------|--------|-------------|------|

### Type Classifications
- **Defect:** System not behaving as designed
- **Enhancement Request:** New capability not in original scope — log as backlog item; do not fix during hypercare without scope approval
- **User Error:** Training gap; address with targeted coaching
- **Data Issue:** Data quality problem introduced during cutover or by users
- **Process Issue:** Business process not aligned to system design; requires process intervention

### ⚠️ Risk: Enhancement Requests Disguised as Defects
Users frequently log "the system doesn't do X" as a defect when X was never in scope. Gate every
incoming issue against the UAT sign-off baseline. If it wasn't tested and approved, it's not a defect.

---

## 4. SLA/KPI Framework

### Operational KPIs to Establish at Go-Live

**System Health KPIs:**

| KPI | Definition | Target | Measurement |
|-----|------------|--------|-------------|
| System Availability | % uptime during business hours | >99.5% | ServiceNow platform monitoring |
| Average Page Load Time | Seconds for primary IRM pages | <3 seconds | Performance analytics |
| Scheduled Job Success Rate | % of scheduled assessment/notification jobs completing | >98% | Job log review |

**Process Health KPIs (Customize per Module):**

| Module | KPI | Definition | Target |
|--------|-----|------------|--------|
| Risk | Risk Assessment Completion Rate | % of scheduled assessments completed on time | >90% |
| Risk | Average Residual Risk Score | Aggregate residual risk across Tier 1 entities | Establish baseline |
| PCM | Control Attestation Completion Rate | % of attestations completed by due date | >85% |
| PCM | Overdue Attestation Rate | % of attestations past due | <5% |
| Audit | Finding Remediation Rate | % of findings remediated within SLA | >80% |
| Issues | Average Issue Age (Open) | Avg days open for unresolved issues | <30 days |
| Issues | SLA Breach Rate | % of issues past remediation due date | <10% |
| TPRM | Vendor Assessment Completion Rate | % of scheduled assessments completed | >85% |

### KPI Reporting Cadence
- Weekly during hypercare
- Monthly post-hypercare (BAU)
- Quarterly executive summary to sponsor

---

## 5. Knowledge Transfer Plan

### KT Scope

| Topic | Format | Audience | Owner | Completion Target |
|-------|--------|----------|-------|-------------------|
| System administration | Hands-on walkthrough + documentation | Client IT Admin | Tech Lead | Week 5 |
| Module configuration and maintenance | Recorded walkthrough + runbook | Module Owners | Functional Lead | Week 5 |
| User support and troubleshooting | Q&A session + FAQ document | Help Desk / Tier 1 Support | Functional Lead | Week 4 |
| Reporting and dashboards | Live session + guide | Risk/Compliance Managers | Functional Lead | Week 5 |
| Platform upgrade preparation | Documentation + checklist | Client IT | Tech Lead | Week 6 |

### KT Sign-Off Criteria
Each KT session should conclude with the recipient confirming:
- [ ] I can perform this task independently
- [ ] I know where to find the documentation
- [ ] I know the escalation path if I encounter an issue beyond my scope

### ⚠️ Risk: KT Treated as a Checkbox
KT is not a document drop. Require live demonstration from the client team — have them perform
the task while the consultant observes. If they can't, the KT is not complete.

---

## 6. Runbook Template

### Runbook Sections

**1. System Overview**
Brief description of the ServiceNow IRM environment: instance URL(s), modules in scope, key integrations,
and admin contacts.

**2. Instance Access & Administration**

| Task | Steps | Notes |
|------|-------|-------|
| Admin login | | |
| User provisioning | | |
| Role assignment | | |
| Update Set management | | |

**3. Routine Operations by Module**
For each module, document:
- Scheduled jobs and their purpose
- Routine maintenance tasks (data cleanup, archive, etc.)
- How to launch and close assessment cycles
- How to handle common exceptions (failed job, unassigned record, etc.)

**4. Integration Monitoring**
For each integration:
- What it does
- How to verify it's running
- What a failure looks like
- How to restart / remediate

**5. Common Issues & Resolutions**

| Symptom | Likely Cause | Resolution Steps |
|---------|-------------|-----------------|

**6. ServiceNow Upgrade Procedure**
- Pre-upgrade checklist
- Upgrade execution steps
- Post-upgrade validation checklist
- Rollback procedure
- Custom code regression test list

**7. Support Escalation Path**
Who to call, when, and how — from Tier 1 through ServiceNow Support.

**8. Change Management Process**
How to request, approve, test, and deploy configuration changes post-go-live.
Enforce: all changes via Update Sets; no direct PROD modifications.

---

## 7. Lessons Learned

### Facilitation Approach
Conduct a structured lessons learned session at project close (or end of hypercare).
Use a retrospective format: What went well? What could be improved? What do we do differently next time?
Separate client-facing version (delivery experience) from internal version (engagement execution).

### Lessons Learned Template

**Project Information:**
- Project Name, Client, Duration, Modules Delivered, Team Size

**Delivery Performance Summary:**

| Dimension | Planned | Actual | Variance | Notes |
|-----------|---------|--------|----------|-------|
| Duration | | | | |
| Budget | | | | |
| Scope (stories delivered) | | | | |
| Defect count (P1/P2) | | | | |
| UAT cycles required | | | | |

**What Went Well:**
(Narrative + bullet list — practices to replicate)

**What Could Be Improved:**
(Narrative + bullet list — be specific and constructive; avoid blame)

**Recommendations for Future Engagements:**
(Actionable guidance for the next team)

**Risks That Materialized:**
(Which RAID risks actually occurred; was the mitigation effective)

**Client Satisfaction Summary:**
(Qualitative summary; include any formal CSAT scores if available)

---

## 8. Project Closure Checklist

### Deliverable Sign-Off
- [ ] All Imagine deliverables signed off (charter, design docs, scoping matrix)
- [ ] All Deliver deliverables signed off (build specs, UAT sign-off, go-live authorization)
- [ ] All Run deliverables signed off (runbook, KT, hypercare exit)

### Administrative Closure
- [ ] Final project status report distributed
- [ ] Lessons learned documented and distributed (internal + client versions)
- [ ] Project files archived per firm policy
- [ ] Consultant access to client systems deprovisioned (per agreed date)
- [ ] Client access revocation confirmed for any consultant-provisioned test accounts
- [ ] Invoicing complete; final invoice issued

### Transition Confirmation
- [ ] Client operational team confirmed as accountable for system going forward
- [ ] Managed service engagement (if applicable) transitioned and active
- [ ] Client confirmed receipt of all deliverables
- [ ] Executive sponsor sign-off on project closure obtained

### Internal Closure
- [ ] Engagement code closed
- [ ] Team performance documentation completed
- [ ] Reference-able client relationship confirmed with sponsor
- [ ] Case study / win wire submitted (if applicable and approved by client)
