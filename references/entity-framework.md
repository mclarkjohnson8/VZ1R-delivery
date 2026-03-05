# ServiceNow IRM: Entity Framework Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

The Entity Framework is the foundation of every ServiceNow IRM implementation. Every module — Risk, Compliance, Audit, TPRM, BCM — operates against entities. This document describes the entity framework architecture, configuration standards, and Verizon-specific implementation.

---

## What Is an Entity?

An **entity** is any organizational unit, technology asset, vendor, or business subject that can own, create, or be associated with a risk, control, compliance obligation, or third-party relationship.

**Examples:**
- Verizon Business Unit (Entity Type: Business Unit)
- SAP ERP (Entity Type: Technology Asset / Application)
- Accenture (Entity Type: Vendor)
- Verizon Consumer Group (CSG) (Entity Type: Legal Entity)
- Avetta (Entity Type: Vendor — also a Fourth-Party provider)

---

## Entity Hierarchy

```
Enterprise (Root)
└── Legal Entity / Division
    └── Business Unit / Department
        ├── Business Process
        ├── Technology Asset (Application / Infrastructure)
        └── Vendor / Third Party
            └── Fourth-Party (Sub-vendor)
```

For Verizon OneRisk:
```
Verizon Communications Inc. (Root)
├── Verizon Consumer Group (CSG)
│   ├── VCS (Vendor & Contracting Services)
│   └── ERM (Enterprise Risk Management)
└── [Other Business Units]
    └── Vendors (TPRM scope)
        ├── BitSight (Data Provider)
        ├── Avetta (Contractor Management / Fourth-Party)
        ├── Ariba (Procurement / Contracting Data)
        └── [Additional Vendors]
```

---

## Entity Types (Verizon Configuration)

| Entity Type | Description | Module Usage |
|-------------|-------------|-------------|
| **Enterprise** | Root organization | All modules |
| **Legal Entity** | Incorporated business unit | Risk, Compliance |
| **Business Unit** | Operational division (CSG, ERM, VCS) | All modules |
| **Business Process** | Key operational processes | BCM (BIA), Risk |
| **Application** | Technology systems | Risk, Compliance, BCM |
| **Infrastructure** | Network, servers, cloud assets | Risk, BCM |
| **Vendor** | Third-party organization | TPRM (primary) |
| **Fourth Party** | Sub-vendors / sub-processors | TPRM |
| **Data Asset** | Classified data sets | Compliance, Privacy |

---

## Entity Framework Rules

### Rule 1: Always First
Entity framework design is always completed before any module configuration. You cannot configure TPRM assessments, risk registers, or controls without knowing what entities own them.

### Rule 2: Hierarchy Integrity
- Every entity must have a parent (except the root)
- Circular references are not permitted
- Deletion of entities with active records requires archival, not hard delete

### Rule 3: Ownership
- Every entity must have a designated owner (user or group)
- Owner is responsible for risk acceptance, control attestation, and assessment responses
- Owner changes trigger notification and re-scoping review

### Rule 4: Scoping Consistency
- Module scoping rules (which records apply to which entities) must be consistent
- If a vendor is in scope for TPRM, they must be an entity in the entity framework
- New vendor onboarding always starts with entity creation

---

## Verizon Entity Framework Status

| Status | Detail |
|--------|--------|
| **Framework State** | Completed and validated |
| **Completion Date** | Imagine phase (before Sprint 1) |
| **Vendors in Scope** | [Actual count from engagement data] |
| **Entity Types Deployed** | Enterprise, Legal Entity, Business Unit, Vendor, Fourth-Party |
| **Integration** | BitSight entity scores linked to Vendor entity records |

**Key Note**: The entity framework is stable. Any proposed change to scope (new vendor, new department) must go through change control and entity framework impact assessment.

---

## Entity-Linked Record Types

When an entity is created, the following records can be linked to it:

| Record Type | Module | Description |
|-------------|--------|-------------|
| Third-Party Profile | TPRM | Vendor profile, tier, risk rating |
| Engagement | TPRM | Assessment engagement (IRQ, DDQ) |
| Risk | Risk | Risk record attributed to entity |
| Control | Compliance | Control owned by entity |
| Audit Subject | Audit | Entity included in audit scope |
| BIA | BCM | Business Impact Analysis for entity |
| Issue | All | Active issue attributed to entity |

---

## Configuration Standards

### Naming Conventions
- Entity names: Official legal/operating name (no abbreviations unless standard)
- Entity codes: [Type prefix]-[Sequential number] (e.g., VND-0042 for a vendor)
- Entity groups: Defined by business function, not org chart (org charts change; functions are stable)

### Scoped Application
All entity framework customizations (custom types, custom fields) must be in the IRM scoped application — never global.

### Change Control
Entity type changes require ARB review. Entity instance changes (adding/modifying a vendor record) are managed by the TPRM manager role.

---

*Reference document. Entity framework is the foundation layer — validate it first for any new scope. Escalate entity framework changes to Tony Scott / Vidhya Sagar.*
