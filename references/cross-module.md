# ServiceNow IRM: Cross-Module Integration Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow IRM is designed as an integrated suite. This document covers how the IRM modules interconnect, share data, and reinforce each other. Understanding cross-module dependencies is essential for architecture decisions and avoiding unintended impacts.

---

## Module Relationship Map

```
Entity Framework (Foundation Layer)
        │
        ├── Risk Management
        │       ├── Risk Register
        │       ├── Risk Indicators (KRIs)
        │       └── Risk Acceptance / Exception
        │
        ├── Policy & Compliance
        │       ├── Policy Library
        │       ├── Control Library
        │       ├── Attestation
        │       └── Compliance Programs
        │
        ├── Audit Management
        │       ├── Audit Universe
        │       ├── Engagement Lifecycle
        │       └── Audit Issues
        │
        ├── TPRM (Third-Party Risk Management)
        │       ├── Third-Party Records
        │       ├── Engagements
        │       ├── Assessments (IRQ, DDQ)
        │       ├── Vendor Portal
        │       └── External Integrations (BitSight, Avetta, Ariba, EHS)
        │
        └── BCM (Business Continuity Management)
                ├── Business Impact Analysis
                ├── Recovery Plans
                └── Continuity Tests
```

---

## Entity Framework as Foundation

**Every IRM module operates against entities.** The entity framework is not optional — it is the structural backbone that enables:

- Cross-module record linkage (a vendor is an entity; a risk can be attributed to that entity)
- Hierarchical scoping (enterprise → division → department → system → vendor)
- Consistent ownership and accountability model
- Unified dashboard and reporting across modules

⚠️ **Rule**: No module configuration work is correct without a validated entity hierarchy. For Verizon, this has been completed. Any new scope item that requires entity framework changes must be flagged before proceeding.

---

## Key Cross-Module Data Flows

### Risk ↔ TPRM
- Third-party risks identified in TPRM assessments create Risk records
- Risk appetite (set in Risk module) drives TPRM risk scoring thresholds
- BitSight signals can trigger automatic risk indicator updates
- Vendor risk exceptions flow through the Risk module approval workflow

### Risk ↔ Compliance
- Compliance failures generate Risk exceptions
- Control effectiveness ratings feed into residual risk calculations
- Risk appetite statements are referenced by compliance programs

### Compliance ↔ Audit
- Audit scope is driven by compliance program structure
- Audit findings create compliance exceptions and issues
- Control test results from Audit feed back into compliance posture

### TPRM ↔ BCM
- Critical vendor dependencies (Avetta, Ariba) documented in BCM BIAs
- TPRM assessment responses include BCM capability questions (DDQ)
- Vendor incidents trigger BCM workflow review

### Audit ↔ Risk
- Audit findings can directly create Risk register entries
- Risk-ranked audit universe is built from the Risk module
- Issue remediation tracked through Risk module

---

## Shared Configuration Objects

| Object | Shared By | Notes |
|--------|-----------|-------|
| **Entities** | All modules | Master record for any subject of risk/compliance activity |
| **Users / Groups** | All modules | Role assignments determine access across all modules |
| **Notification Engine** | All modules | Centrally configured; one rationalized set of templates |
| **Task Framework** | Risk, Compliance, Audit, TPRM | Common task/assignment model |
| **Issue Framework** | All modules | Issues from any module follow the same lifecycle |
| **Document Library** | All modules | Policies, evidence, reports stored in common repository |
| **Workflow Engine** | All modules | Approval chains, escalation rules, SLA policies |

---

## Upgrade Impact Considerations

Cross-module customizations carry the highest upgrade risk:
- Custom fields shared between modules can break upgrade scripts
- Business rules that span module scopes are fragile
- Custom relationships between module objects are not upgrade-safe

**Design principle**: Prefer module-native relationships over cross-module custom fields.

---

## Verizon Delivery Notes

### Current Sprint (Sprint 12) — Cross-Module Impact Items
- ISS-002 (BitSight C2): Custom issue generation could create Risk records via cross-module link — validate Risk module impact before deploying fix
- ISS-005 (VCS Outbound API): API must traverse TPRM entities, engagements, assessments, and risks — architecture review with Arav required
- Notification rationalization: Changes to TPRM notifications must not break Risk or Compliance notification flows

### Post-Go-Live Architecture
- BCM module planned for Phase 2 — entity framework is already in place
- Risk module integration with TPRM will deepen post-go-live (KRI linkage to vendor scores)
- Compliance module integration is in the program roadmap

---

*Reference document. Cross-module dependencies require senior architect review before configuration. Escalate to Tony Scott / Vidhya Sagar for complex cross-module design decisions.*
