# Audit Management Reference

## Table of Contents
1. Module Overview
2. Audit Data Model
3. Audit Planning
4. Engagement Execution
5. Findings & Issue Integration
6. Workpaper Management
7. Common Configuration Decisions
8. Anti-Patterns

---

## 1. Module Overview

ServiceNow Audit Management operationalizes the internal audit lifecycle: annual audit plan,
individual engagement scoping, fieldwork execution, findings management, and issue integration.

**Primary Use Cases:**
- Annual audit universe and risk-based audit planning
- Engagement management (scope, schedule, assign, execute)
- Audit finding capture and rating
- Finding → Issue integration for remediation tracking
- Audit committee reporting

---

## 2. Audit Data Model

### Core Tables
- `sn_audit_engagement` — Individual audit engagement record
- `sn_audit_task` — Workstream or fieldwork task within an engagement
- `sn_audit_finding` — Finding identified during audit
- `sn_audit_workpaper` — Evidence and documentation for audit tasks
- `sn_audit_plan` — Annual audit plan record

### Hierarchy
```
Annual Audit Plan
└── Audit Engagement (e.g., "IT General Controls Audit Q3")
    ├── Audit Tasks (e.g., "Test user access reviews")
    │   └── Workpapers (evidence attached)
    └── Audit Findings
        └── Issues (auto-created or linked via integration)
```

---

## 3. Audit Planning

### Audit Universe
The audit universe is the complete inventory of auditable entities, processes, and controls.
- Source from Entity Framework — every auditable entity should be in the entity hierarchy
- Rate each audit subject by inherent risk, last audit date, regulatory significance
- Risk-rate the universe to drive annual plan prioritization

### Annual Audit Plan Configuration
- Create audit plan record for the fiscal year
- Populate planned engagements with: entity/scope, audit type, planned start/end, resource estimate
- Get audit plan approved by audit committee before Sprint 1 (if Audit is in scope for Phase 1)
- Track plan vs. actual throughout the year (planned engagements vs. completed)

### Resource Planning
- Audit staff assignments: hours by engagement × staff × quarter
- Track utilization across planned engagements
- Reserve capacity for unplanned/ad hoc audits (typically 15-20% of total capacity)

---

## 4. Engagement Execution

### Engagement Lifecycle States (OOB)
Planning → Fieldwork → Reporting → Closed

### Standard Audit Deliverable Workflows (Deloitte Baseline)
These four workflows are the standard delivery baseline for Audit Management:

1. **Audit Plans & Audit Engagements** — annual plan creation, engagement scheduling from plan, resource assignment
2. **Audit Control Test Workflow** — control test steps executed within engagement tasks; evidence attached; pass/fail recorded
3. **Audit Observation Workflow** — observation/finding creation, rating, management response capture, agreement on remediation date
4. **Audit Evidence Request Workflow** — formal evidence requests issued to process owners; evidence submission tracked; status visible to auditor

### Engagement Planning Checklist
- [ ] Scope and objectives defined
- [ ] Entity/process owner notified
- [ ] Engagement team assigned
- [ ] Audit program (control objectives and test steps) created from template
- [ ] Kick-off meeting scheduled and pre-read distributed

### Audit Tasks
- Each task maps to a control objective or audit step
- Task owner = assigned auditor
- Task status tracks fieldwork progress
- Workpapers attached to tasks as evidence

### Finding Rating Scale

| Rating | Definition |
|--------|------------|
| Critical | Significant deficiency; immediate risk of financial loss, regulatory action, or operational disruption |
| High | Material weakness; requires prompt remediation |
| Medium | Control gap; addressable within standard remediation cycle |
| Low | Minor observation; best practice recommendation |
| Informational | Positive observation or process improvement opportunity |

---

## 5. Findings & Issue Integration

### Finding → Issue Integration (Key Configuration)
When a finding meets severity threshold (Critical or High), automatically create an Issue record:
- Finding severity → Issue priority mapping (1:1 recommended)
- Finding owner → Issue owner (or configurable default)
- Finding due date → Issue remediation due date
- Link maintained between Finding and Issue for traceability

### Management Response Workflow
- Finding draft → Entity/process owner provides management response
- Management response captured on finding record
- Agreed remediation date and owner captured
- Auditor validates response adequacy before closing finding

---

## 6. Workpaper Management

### Workpaper Structure
- One workpaper per audit task (minimum)
- Workpaper contains: objective, procedures performed, evidence reviewed, conclusion
- Evidence attached as files to workpaper record
- Workpaper review/approval by audit manager before task closure

### Evidence Retention
- Configure retention policy aligned to client's records retention schedule
- Typical: 7 years for SOX-related workpapers; 3-5 years for operational
- ServiceNow supports attachment lifecycle management — configure per policy

---

## 7. Common Configuration Decisions

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Audit program templates | Build per engagement | Reusable program templates by audit type | Reusable templates; build library during Imagine |
| Finding distribution | Auditor emails draft findings | Portal-based management response workflow | Portal workflow for scale; email acceptable for small audit teams |
| Engagement calendar | Manual scheduling | Automated scheduling from audit plan | Automate from plan; manual override available |
| Workpaper review | Single-level (manager) | Multi-level (manager + quality review) | Single-level for Phase 1; add QA layer in Phase 2 |

---

## 8. Anti-Patterns

**Anti-Pattern: Building Audit Without a Rationalized Audit Universe**
If the audit universe isn't defined, scope for every engagement becomes a negotiation. Build the
universe in Imagine phase.

**Anti-Pattern: No Agreed Finding Rating Scale**
When auditors and management disagree on finding ratings, findings get downgraded before reaching
leadership. Lock the rating scale and escalation thresholds before go-live.

**Anti-Pattern: Treating Audit as Standalone**
Audit findings that don't integrate with Issues and Risk create a closed-loop problem — audit work
doesn't drive remediation or risk profile updates. Integration with Issues module is non-negotiable.
