# Issues & Remediation Reference

## Table of Contents
1. Module Overview
2. Issues Data Model
3. Issue Lifecycle Configuration
4. SLA Configuration
5. Remediation Tracking
6. Common Configuration Decisions
7. Anti-Patterns

---

## 1. Module Overview

Issues & Remediation is the cross-module action management layer in ServiceNow IRM. Issues can be
created manually or auto-generated from Risk (threshold breach), Audit (findings), PCM (failed
attestations), TPRM (vendor risk), or Privacy (DPIA findings).

**Primary Use Cases:**
- Centralized issue register across all GRC domains
- Remediation task tracking with ownership and due dates
- SLA enforcement and escalation
- Cross-module issue aggregation for executive reporting

---

## 2. Issues Data Model

### Core Tables
- `sn_risk_issue` — Issue record (primary)
- `sn_risk_issue_task` — Individual remediation tasks under an issue
- `sn_risk_remediation_plan` — Formal remediation plan for complex issues

### Issue Sources (Integration Points)
- Risk Management: auto-created when residual score exceeds tolerance
- Audit Management: created from high/critical findings
- Policy & Compliance: created from failed control attestations
- TPRM: created from high-risk vendor assessment results
- Privacy: created from DPIA high-risk findings
- Manual: created directly by risk, compliance, or audit teams

---

## 3. Issue Lifecycle Configuration

### Standard Issues Deliverable Workflows (Deloitte Baseline)
These three workflows are the standard delivery baseline for Issues Management:

1. **Auto Issue Owner Assignment** — business rules that assign issue ownership based on entity owner, risk owner, or control owner depending on issue source; eliminates unassigned issue backlogs
2. **End-to-End Issue Management Workflow Design** — full lifecycle from intake through closure: Draft → Open → In Remediation → Pending Verification → Closed / Accepted Risk / Exception; includes escalation automation
3. **Issue Remediation Task Workflow** — structured remediation task creation under each issue with named owner, due date, progress update requirements, and evidence attachment for closure

### Issue States (OOB)
Draft → Open → In Remediation → Pending Verification → Closed / Accepted Risk / Exception

### Priority / Severity Mapping

| Severity | Definition | Initial Response SLA | Remediation SLA |
|----------|------------|---------------------|-----------------|
| Critical | Immediate risk of loss, breach, or regulatory violation | 4 business hours | 30 days |
| High | Significant control gap; elevated risk exposure | 1 business day | 60 days |
| Medium | Moderate control gap; manageable risk | 3 business days | 90 days |
| Low | Minor gap; minimal risk impact | 5 business days | 180 days |

### Workflow Configuration
- Issue creation → auto-notify issue owner
- 14-day SLA: reminder to owner if no progress update
- SLA breach: escalate to owner's manager
- Remediation complete: owner requests verification → auditor/risk team verifies → close or return
- Exception request workflow: issue owner requests exception → risk manager approves with rationale → documented on issue record

---

## 4. SLA Configuration

### SLA Types to Configure
1. **Initial Response SLA:** Time from issue creation to first status update
2. **Remediation SLA:** Time from issue creation (or agreed start date) to closure
3. **Verification SLA:** Time from "Pending Verification" to close/return decision

### SLA Pause Conditions
SLA clock should pause when:
- Issue is pending third-party action (vendor remediation, tool procurement)
- Formal exception has been submitted and is pending approval
- Issue is blocked by a dependency documented in the record

### ⚠️ Risk: SLA Thresholds Too Aggressive
SLAs that are routinely breached create noise and erode trust in the system. Calibrate SLAs
against the organization's actual remediation capacity. Tighten after adoption is established.

---

## 5. Remediation Tracking

### Remediation Task Schema
Each Issue can have multiple remediation tasks:
- Task title and description
- Owner (named individual)
- Due date
- Status (Not Started / In Progress / Complete)
- Progress notes (required on each update)
- Evidence attachment (required for closure)

### Progress Update Requirements
Configure a mandatory progress update cadence:
- Critical/High issues: weekly update required
- Medium issues: bi-weekly update required
- Automated reminder if no update within cadence window

---

## 6. Common Configuration Decisions

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Issue ownership | Risk/Compliance team owns all issues | Business unit owns issues; risk team oversees | Business unit owns; risk team is accountable — drives accountability where control lives |
| Exception process | Informal acceptance | Formal documented exception with time limit and re-review | Formal exception with max 1-year term and mandatory re-review |
| Issue deduplication | Manual review | Automated duplicate detection | Manual for Phase 1; configure duplicate logic in Phase 2 |

---

## 7. Anti-Patterns

**Anti-Pattern: Issues Module as a Dumping Ground**
Without intake governance, Issues becomes a catch-all for every observation, complaint, and
enhancement request. Enforce issue intake criteria: must have an identified control gap or risk
exposure; must have a named owner; must have a due date.

**Anti-Pattern: "Accepted Risk" as a Way to Close Issues Without Remediation**
Some clients use Accepted Risk status to clear issues without actually closing them. Require
executive sign-off (not just the issue owner) for Accepted Risk status and set a mandatory
re-review date.

---

---

# Privacy Management Reference

## Module Overview

ServiceNow Privacy Management operationalizes data privacy program requirements: data inventory,
privacy impact assessments (DPIA/PIA), consent management, breach notification, and regulatory
compliance tracking (GDPR, CPRA, HIPAA, etc.).

**Primary Use Cases:**
- Data inventory and data element classification
- Privacy Impact Assessment (PIA) and Data Protection Impact Assessment (DPIA)
- Consent record management
- Privacy incident and breach management
- Regulatory obligation tracking and data subject rights management

---

## Privacy Data Model

### Core Tables
- `sn_privacy_assessment` — PIA/DPIA record
- `sn_privacy_data_element` — Data element definitions (PII types, sensitivity)
- `sn_privacy_data_flow` — Documents how data moves between systems/entities
- `sn_privacy_consent` — Consent records for data subjects
- `sn_privacy_incident` — Privacy incident and breach records
- `sn_privacy_request` — Data subject rights requests (access, deletion, portability)

---

## Key Configuration Decisions

### DPIA Triggering Criteria
Configure automatic DPIA triggers for:
- New processing activities involving sensitive data (health, financial, biometric)
- New technology implementations (AI/ML, tracking technologies, large-scale monitoring)
- Third-party data sharing arrangements
- Cross-border data transfers

### Data Inventory Scope
Phase 1 minimum viable scope:
- Tier 1 entities: full data inventory (data elements, sensitivity, retention, legal basis)
- Tier 2 entities: key data elements identified
- Tier 3/4: entity-level data categories only

### Integration with Risk Module
High-risk DPIA findings → auto-create Risk record in Risk Management module
Privacy incidents → auto-create Issue record in Issues module

### ⚠️ Anti-Pattern: Privacy Without Data Inventory
A privacy program without a data inventory is compliance theater. Data inventory (even if
imperfect) is the prerequisite for meaningful DPIA, consent management, and data subject rights.
Build the inventory framework before configuring assessment workflows.

---

---

# Business Continuity Management (BCM) Reference

BCM coverage has been moved to a dedicated standalone reference file due to expanded scope.

**Load `references/bcm.md` for all BCM guidance**, including full BIA methodology, BCP/DRP
documentation standards, exercise and testing program, crisis management and incident response
integration, recovery task management during active events, ServiceNow configuration scope,
and anti-patterns.

---

## BCM Data Model

### Core Tables
- `sn_bcm_plan` — BCP or DRP document record
- `sn_bcm_bia` — Business Impact Analysis record
- `sn_bcm_test` — Continuity test/exercise record
- `sn_bcm_recovery_task` — Recovery action during an active event

### BIA → Plan Dependency
BIA results (RTO, RPO, criticality ratings) must be completed before BCP/DRP documents are
finalized. This is a hard sequencing dependency — do not start plan documentation without BIA data.

---

## Key Configuration Decisions

### BIA Scope
- Conduct BIA at the process and application level (not entity level)
- For each critical process: capture RTO (max downtime tolerable), RPO (max data loss tolerable),
  MTPD (maximum tolerable period of disruption), and dependencies (upstream/downstream processes)
- BIA results feed back to Entity Framework — update application entity criticality ratings

### Plan Types to Configure
- Business Continuity Plan (BCP): how to continue critical business operations during disruption
- Disaster Recovery Plan (DRP): how to recover IT systems and infrastructure
- Crisis Management Plan: how leadership responds and communicates during a crisis
- Each plan type can have a distinct template in ServiceNow

### Test/Exercise Schedule
- Tabletop exercise: Annual minimum for all Tier 1 plans
- Simulation: Annual for critical IT systems (DRP)
- Full-scale: Bi-annual for highest-criticality plans (or per regulatory requirement)
- Test results → findings → Issues if gaps identified

### ⚠️ Anti-Pattern: BCP Plans That Are Never Tested
An untested plan is an assumption. Configure a testing schedule at go-live and enforce it.
Plans that have not been tested within the required cycle should show as overdue in the dashboard.

### Integration with Risk Module
- BIA results inform operational risk assessments (single-point-of-failure risks)
- Test failures generate Issues in the Issues module
- Critical dependency gaps surface as Risks
