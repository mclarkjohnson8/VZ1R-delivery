# ServiceNow IRM: Audit Management Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow Audit Management is an IRM module that automates the internal audit lifecycle from planning through issue tracking. It integrates natively with Risk, Compliance, and TPRM modules.

---

## Module Architecture

### Core Objects

| Object | Description |
|--------|-------------|
| **Audit Engagement** | Top-level audit entity. Contains scope, schedule, team, and status. |
| **Audit Task** | Individual work item within an engagement. |
| **Audit Test** | Specific test procedure for a control or risk area. |
| **Audit Finding** | Identified exception, gap, or risk from testing. |
| **Audit Issue** | Formal issue requiring remediation. Linked to Risk module. |
| **Audit Report** | Structured deliverable — draft, review, issued. |
| **Audit Entity** | The organizational unit, vendor, or system being audited. |

---

## Audit Lifecycle

```
Plan → Scope → Fieldwork → Reporting → Issue Tracking → Close
```

### 1. Planning
- Annual/Rolling Audit Universe definition
- Risk-ranked audit schedule
- Resource allocation
- Engagement creation and team assignment

### 2. Scoping
- Scope definition (entities, processes, controls)
- Audit approach selection (controls-based, risk-based, hybrid)
- Materiality thresholds set

### 3. Fieldwork
- Audit Tasks assigned to team members
- Evidence collection (document uploads, interview notes)
- Control testing via Audit Tests
- Finding documentation (preliminary)

### 4. Reporting
- Draft Audit Report generation
- Management response workflow
- Report review and approval chain
- Issued Report with management action plans

### 5. Issue Tracking
- Findings converted to Audit Issues
- Remediation plans assigned with due dates
- Issue aging and escalation rules
- Closure verification

---

## Integration with TPRM

For the Verizon OneRisk engagement, Audit Management intersects with TPRM in:

- **Third-Party Audits**: Audit Engagements can be scoped to Vendor entities from the TPRM module
- **Finding Cross-Reference**: Audit Findings linked to Third-Party Risks
- **Issue Linkage**: Audit Issues can originate from TPRM assessment findings
- **Shared Entity Framework**: Both modules operate against the same entity hierarchy

---

## OOTB Configuration Standards

### Always Use OOB For:
- Audit Engagement lifecycle states
- Finding severity classification (Critical, High, Medium, Low, Informational)
- Report approval workflows
- Issue aging / escalation rules
- Management response workflows

### Documented Customization Justification Required For:
- Custom finding categories beyond OOB taxonomy
- Non-standard approval chains
- Custom reporting beyond standard templates
- Integrations with external audit management tools

---

## Role Matrix

| Role | OOB Role Name | Access Level |
|------|---------------|-------------|
| Audit Manager | sn_audit.manager | Full CRUD on engagements, tasks, findings, reports |
| Audit Analyst | sn_audit.analyst | Create/update tasks, tests, findings |
| Audit Reader | sn_audit.read | Read-only access to all audit content |
| Control Owner | sn_compliance.control_owner | Respond to control testing requests |
| Management Reviewer | sn_audit.management_reviewer | Review and respond to draft reports |

---

## Key Configuration Settings (Zurich)

- **Engagement Approvals**: Configurable multi-step approval chain before engagement activation
- **Materiality Thresholds**: Set at department or engagement level
- **Finding Aggregation**: Auto-group related findings into single issues
- **SLA Definitions**: Configurable response windows per finding severity
- **Attestation**: Periodic control attestation separate from engagement lifecycle

---

## Verizon-Specific Notes

- Audit module is in scope for Phase 2 (post-TPRM go-live)
- TPRM findings should be tagged for potential audit follow-up
- Vendor audit history integration with TPRM entity records is in the roadmap

---

*Reference document. See `references/tprm.md` for current-sprint module details.*
