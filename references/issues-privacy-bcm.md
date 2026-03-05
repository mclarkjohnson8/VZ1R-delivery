# ServiceNow IRM: Issues, Privacy & BCM Cross-Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

This document covers the intersection of three IRM domains with specific Verizon engagement relevance: Issue Management (universal across modules), Privacy/Data Protection compliance, and BCM integration points. These three areas share common framework components and frequently interact in enterprise IRM implementations.

---

## Part 1: Issue Management Framework

### What Is an IRM Issue?

A ServiceNow IRM Issue is a formal record of an identified problem, gap, exception, or risk event that requires remediation. Issues can originate from any IRM module:

| Source | Typical Issue Types |
|--------|-------------------|
| **TPRM** | Vendor non-compliance, assessment failure, integration defect |
| **Risk** | Risk limit breach, KRI threshold exceeded |
| **Compliance** | Control failure, policy exception, regulatory finding |
| **Audit** | Audit finding requiring remediation |
| **BCM** | BCP test failure, dependency gap |

### Issue Lifecycle

```
Identify → Categorize → Assign → Remediate → Verify → Close
```

| State | Description |
|-------|-------------|
| **New** | Issue logged; pending review |
| **Open** | Reviewed; assigned; active remediation |
| **Pending Verification** | Remediation complete; awaiting closure verification |
| **Closed** | Verified resolved |
| **Accepted** | Risk accepted; will not remediate (requires approval) |
| **Deferred** | Remediation postponed with documented rationale |

### Issue Severity Classification

| Severity | Definition | SLA (Default) |
|----------|-----------|---------------|
| **Critical** | Immediate operational or regulatory impact; potential for significant loss | 24 hours |
| **High** | Material risk to program, compliance, or operations | 5 business days |
| **Medium** | Moderate risk; manageable with planned remediation | 15 business days |
| **Low** | Minor gap; low impact if not immediately addressed | 30 business days |

### Verizon Active Issues (see engagement-state.json for current status)

| Issue ID | Title | Severity | Status |
|----------|-------|----------|--------|
| ISS-001 | IRQ Scoring — Bias Factor | High | RESOLVED |
| ISS-002 | BitSight GRC Issue Generation (C2) | High | IN PROGRESS — ACTIVE BLOCKER |
| ISS-003 | Avetta Staging Environment Access | High | IN PROGRESS — ACTIVE BLOCKER |
| ISS-004 | Ariba Stage Misconfiguration | Medium | IN PROGRESS |
| ISS-005 | VCS Outbound API Request | Medium | NEW — IN SCOPING |

---

## Part 2: Privacy & Data Protection

### ServiceNow IRM Privacy Module Capabilities

ServiceNow IRM supports Privacy/Data Protection compliance through:

| Capability | Description |
|------------|-------------|
| **Privacy Impact Assessment (PIA)** | Structured assessment of data processing activities |
| **Data Asset Registry** | Catalog of data assets with classification and ownership |
| **Consent Management** | Tracking of data subject consent |
| **DSAR Workflows** | Data Subject Access Request processing |
| **Breach Management** | Privacy incident detection, notification, and remediation |
| **Vendor Privacy Assessment** | TPRM + Privacy: assess third-party data handling |

### TPRM and Privacy Intersection

For Verizon OneRisk, privacy considerations intersect with TPRM at:

- **DDQ Sections**: Data handling, breach notification, sub-processor agreements, data residency
- **Avetta (Fourth-Party)**: Data sharing with Avetta involves sub-processor assessment requirements
- **Ariba**: Contracting data includes PII — privacy classification required
- **BitSight**: Signals processing — data classified as non-PII but vendor data handling assessed

### Key Privacy Principles (Verizon Engagement)

1. **Data Minimization**: TPRM assessments collect only data required for risk decision-making
2. **Sub-Processor Visibility**: Fourth-party data (Avetta) requires sub-processor disclosure
3. **Breach Notification Path**: Vendor breaches detected via BitSight → TPRM Issue → Privacy team notification
4. **Data Residency**: Confirm ServiceNow instance data residency aligns with Verizon data governance policy

---

## Part 3: BCM-Privacy-Issues Integration

### How They Work Together

```
BCM Event (e.g., vendor disruption)
    → Creates TPRM Issue (vendor risk event)
    → Triggers Privacy review (if data was exposed)
    → Risk record updated
    → Audit trail maintained
```

### Verizon-Specific Integration Points

| Trigger | BCM | Privacy | Issues |
|---------|-----|---------|--------|
| BitSight critical alert | BCP review triggered for affected vendor | Data exposure check | ISS created in TPRM |
| Avetta outage | BIA dependency gap flagged | Sub-processor incident review | ISS-003 type issue |
| Ariba incident | Contracting data continuity | PII exposure assessment | ISS-004 type issue |

---

## Configuration Guidelines

### Issue Management
- Use OOB severity taxonomy (Critical/High/Medium/Low/Informational) — do not create custom levels
- SLA policies defined at the severity level — not the issue level
- Escalation rules: auto-notify PM for issues approaching SLA breach
- Issue closure requires verification evidence upload

### Privacy
- Data Asset Registry must be populated before privacy assessments are active
- PIA template selection driven by data classification (PII, Sensitive PII, Non-PII)
- Sub-processor assessment built into TPRM DDQ (not a separate workflow)

### BCM
- BCP activation workflow linked to TPRM Issue creation for critical vendor incidents
- BCM test failures auto-create Medium-severity Issues with 15-day SLA
- Crisis team notification integrated with ServiceNow notification engine

---

*Reference document. Issues, Privacy, and BCM are interconnected — changes to one module's issue framework can impact all three. Always validate cross-module impact.*
