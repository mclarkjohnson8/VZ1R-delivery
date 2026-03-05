# ServiceNow IRM Accelerators Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow IRM accelerators are pre-built assets — templates, scripts, configurations, and frameworks — that reduce implementation time and improve outcome quality. This document catalogs the accelerators applicable to the Verizon OneRisk TPRM delivery.

---

## Deloitte ServiceNow IRM Accelerators

### 1. Entity Framework Bootstrap Template

A pre-configured entity hierarchy template for enterprise implementations. Includes:
- Entity types: Vendor, Legal Entity, Business Unit, System, Product
- Hierarchical relationship definitions
- Pre-seeded risk appetite tiers
- Default scoping rules for TPRM

**Usage:** Applied during Imagine phase. Deployed and rationalized on Verizon engagement.

---

### 2. TPRM Questionnaire Library

Pre-built assessment questionnaire templates including:
- Third-Party Risk Assessment (TPRA) — 250+ question bank
- Due Diligence Questionnaire (DDQ) — standard and enhanced variants
- Risk Intelligence Questionnaire (IRQ) — scoring-enabled
- Vendor Portal Self-Assessment variant
- Domain-specific supplements: IT Security, Business Continuity, Privacy/Data Protection

**Usage:** Rationalized from ~21 questionnaires to 11 for Verizon. IRQ scoring configured with custom weight adjustments.

---

### 3. Role-Based Access Control (RBAC) Accelerator

OOB role mapping template for IRM implementations:
- sn_risk.manager, sn_risk.analyst, sn_risk.reader
- sn_compliance.manager, sn_compliance.analyst
- sn_audit.manager, sn_audit.read
- Custom TPRM roles: tprm_manager, tprm_analyst, vendor_portal_user

**Usage:** Applied to replace 100+ custom access rules with OOB least-privilege model.

---

### 4. Integration Connector Templates

Pre-built MID Server and Scripted REST API configurations for:
- **BitSight** (OOB ServiceNow IRM plugin): C1 scores + alerts intake
- **BitSight C2** (custom): Enhanced findings → 1Risk Issue generation
- **Avetta**: Fourth-party data via REST API
- **Ariba**: Contract data ingestion
- **EHS**: Environmental/Health/Safety data

---

### 5. Reporting & Dashboard Pack

Pre-configured dashboards and reports:
- Executive TPRM Summary Dashboard (Merlyn-level)
- Operational TPRM Dashboard (Heidi/team-level)
- Vendor Risk Scorecard
- Issue & Exception Tracker
- Go-Live Readiness Dashboard

---

### 6. Notification Template Library

Rationalized notification templates (50%+ volume reduction target):
- Vendor portal invitations and reminders
- Assessment completion notices
- Risk acceptance / exception approvals
- Issue escalation notifications
- Scheduled digest patterns

---

### 7. Data Migration Toolkit

Tools and scripts for migrating from legacy Vendor Risk application:
- Field mapping specification (1,800+ fields mapped → rationalized set)
- Data cleansing scripts
- Validation query library
- Rollback procedures

**Usage:** ~70% custom footprint eliminated in Verizon migration.

---

### 8. Training Package

Session-by-session training assets:
- Risk Intelligence (IRQ) — delivered 2/26/2026
- Due Diligence Requests (DDQ) — delivered 3/4–3/5/2026
- Vendor Portal Administration
- Report Writer / Power User
- System Administrator
- Integration Operations
- Hypercare/BAU Operations

---

## ServiceNow Native Accelerators (Zurich)

### Now Assist for GRC

AI-powered features native to ServiceNow IRM Zurich:
- Control test generation
- Risk assessment scoring assistance
- Questionnaire summarization
- Issue identification from assessment responses

### Workspace Layouts

Pre-built IRM Workspace layouts for:
- TPRM Manager workspace
- Risk Manager workspace
- Compliance Manager workspace

### Mobile Support

Native mobile support for:
- Approvals (risk acceptance, exceptions)
- Assessment completion
- Issue status updates

---

## Accelerator Selection Matrix

| Accelerator | Phase | Applicable Modules | VZ Status |
|-------------|-------|-------------------|-----------|
| Entity Framework Bootstrap | Imagine | All | ✅ Applied |
| TPRM Questionnaire Library | Imagine/Deliver | TPRM | ✅ Applied (rationalized) |
| RBAC Accelerator | Deliver | All | ✅ Applied |
| Integration Connectors | Deliver | TPRM | 🟡 BitSight C1 ✅; C2 in progress |
| Reporting Pack | Deliver | All | ✅ Applied |
| Notification Library | Deliver | All | ✅ Applied |
| Data Migration Toolkit | Deliver | TPRM | ✅ Applied |
| Training Package | Deliver/Run | All | 🟡 In progress |

---

*Reference document. For current sprint status, see `state/engagement-state.json`.*
