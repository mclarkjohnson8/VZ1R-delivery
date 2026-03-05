# Entity Framework Reference

## Table of Contents
1. Entity Framework Overview
2. Entity Hierarchy Design
3. Entity Classes
4. Entity Tiers
5. Entity Profile Configuration
6. Common Design Decisions & Anti-Patterns
7. Scoping Guidance

---

## 1. Entity Framework Overview

The Entity Framework is the structural backbone of all ServiceNow IRM modules. Every risk, control,
policy, audit engagement, vendor relationship, and issue ultimately attaches to an entity. Poor entity
design at the outset is the single most common root cause of IRM implementation rework.

Entity Framework components:
- **Entity:** A business unit, legal entity, vendor, application, product, location, or other
  organizational construct that is subject to risk and compliance activities
- **Entity Class:** The category/type of entity (e.g., Business Unit, Legal Entity, Vendor, Application)
- **Entity Tier:** The risk-based classification that drives assessment frequency, control depth,
  and profile completeness requirements
- **Entity Hierarchy:** The parent-child relationship structure that enables rollup reporting,
  inherited controls, and scoped assessments
- **Entity Profile:** The set of attributes, relationships, and metadata associated with a specific entity

---

## 2. Entity Hierarchy Design

### Design Principles
- Hierarchy should reflect the organization's risk reporting structure, not its org chart
- Maximum recommended depth: 5 levels (deeper hierarchies create reporting complexity)
- Every entity must have exactly one parent (except root-level entities)
- Hierarchy changes post-launch require re-scoping of active assessments and risk registers — treat as a change request

### Typical Enterprise Hierarchy Pattern
```
Level 1: Enterprise (root)
Level 2: Business Domain / Division
Level 3: Business Unit / Legal Entity
Level 4: Department / Function
Level 5: Process / Application / Location
```

### Telecom Pattern Example
```
Enterprise
├── Consumer
│   ├── Mobility
│   ├── Home Internet
│   └── Device Sales
├── Enterprise/B2B
│   ├── Managed Services
│   └── Network Solutions
├── Technology & Infrastructure
│   ├── Network Operations
│   └── IT / Platforms
└── Corporate Functions
    ├── Legal & Compliance
    ├── Finance
    └── HR
```

### ⚠️ Risk: Hierarchy Lock-In
Entity hierarchy restructuring mid-implementation is high-effort. Facilitate a dedicated workshop
with the client's risk and compliance leadership before finalizing. Get sign-off documented.

---

## 3. Entity Classes

Entity classes define the type/category of entity and drive which profile attributes, assessment
templates, and module behaviors apply.

### Standard Entity Classes (OOB + Common Custom)

| Class | Description | Typical Modules |
|-------|-------------|-----------------|
| Business Unit | Internal organizational unit | Risk, PCM, Audit |
| Legal Entity | Registered corporate entity | Risk, PCM, Privacy |
| Vendor / Third Party | External supplier or partner | TPRM, Risk |
| Application / System | IT application or platform | Risk, PCM, BCM |
| Location / Facility | Physical site or data center | BCM, Risk |
| Product / Service | Client-facing or internal product | Risk, Privacy |
| Process | Business or IT process | Risk, PCM, BCM |
| Project | Temporary initiative | Risk |

### Configuration Notes
- Entity classes are configured in the Entity Class table (`[sn_grc_entity_class]`)
- Each class can have a distinct set of profile attributes (via related lists and custom fields)
- Avoid over-proliferating classes — consolidate where profile structures are >80% identical
- Class assignment drives scoped list filtering across all IRM modules

---

## 4. Entity Tiers

Entity tiers provide risk-based stratification that governs assessment frequency, control depth,
and resource allocation.

### Standard Tiering Model (Recommended)

| Tier | Label | Definition | Assessment Frequency | Profile Completeness |
|------|-------|------------|---------------------|----------------------|
| 1 | Critical | Highest inherent risk; regulatory exposure; systemic impact | Quarterly or continuous | Full profile required at go-live |
| 2 | High | Significant risk; material compliance obligations | Semi-annually | Full profile required |
| 3 | Medium | Moderate risk; standard compliance requirements | Annually | Core profile required |
| 4 | Low | Minimal risk; limited compliance scope | Bi-annually or on-change | Minimal profile |

### Tiering Criteria (Customize per Client)
- Revenue / operational dependency
- Data sensitivity (PII, PHI, financial)
- Regulatory obligation (SOX, HIPAA, PCI, state privacy laws)
- Third-party access to systems/data
- Single point of failure / business continuity exposure
- Geographic/jurisdictional risk

### ⚠️ Risk: Tier Inflation
Clients often want everything at Tier 1. Enforce tiering criteria rigorously — tier inflation collapses
assessment prioritization and creates capacity problems for risk/compliance teams post-go-live.

---

## 5. Entity Profile Configuration

### Profile Attributes to Configure per Class

**Core Attributes (All Classes):**
- Entity Name, Description, Owner, Delegate Owner
- Entity Class, Entity Tier, Parent Entity
- Status (Active/Inactive), Effective Date
- Primary Contact, Secondary Contact

**Extended Attributes by Class:**

*Business Unit / Legal Entity:*
- Geographic Location(s), Jurisdiction
- Revenue Band, Headcount Band
- Regulatory Obligations (multi-select)
- Business Domain

*Vendor / Third Party:*
- Vendor Type, Service Category
- Engagement Start/End Date
- Data Access Level, System Access Level
- Primary Contract Reference
- Inherent Risk Score (pre-assessment)

*Application / System:*
- Hosting Type (Cloud/On-Prem/Hybrid)
- Data Classification
- Criticality Rating
- Business Owner, Technical Owner
- Upstream/Downstream Dependencies

### Relationship Configuration
- Entity-to-Policy: scopes policy applicability
- Entity-to-Risk: scopes risk ownership and rollup
- Entity-to-Control: enables control inheritance and scoped attestation
- Entity-to-Vendor: enables TPRM scoping and continuous monitoring

---

## 6. Common Design Decisions & Anti-Patterns

### Decision: Flat vs. Deep Hierarchy
- **Flat (2-3 levels):** Simpler to maintain; less granular reporting; preferred for smaller programs
- **Deep (4-5 levels):** Enables granular scoping and rollup; requires more governance overhead
- **Recommendation:** Default to 3-4 levels; add depth only where risk differentiation demands it

### Anti-Pattern: Using Org Chart as Entity Hierarchy
The org chart changes frequently (reorgs, M&A, restructuring). The IRM entity hierarchy should reflect
risk accountability structure, which is more stable. Map the two separately and document the relationship.

### Anti-Pattern: Creating Entity Classes for Every Nuance
Five distinct vendor classes that all have the same profile and the same assessment templates is waste.
Use custom attributes on a single Vendor class to capture nuance.

### Anti-Pattern: Deferring Entity Tiering to Post-Go-Live
Without tiering, assessment scheduling defaults to "everything at the same frequency," which is
operationally unsustainable. Tier at least Tier 1/2 entities before go-live.

---

## 7. Scoping Guidance

### Minimum Viable Entity Scope for Phase 1 Go-Live
- Tier 1 and Tier 2 entities fully profiled
- Entity hierarchy finalized through Level 3 minimum
- All entity classes defined and configured
- Entity-to-module relationships scoped (which entities are in scope for which modules)
- Tier 3/4 entities: names and classes loaded; full profiling deferred to Phase 2

### Workshop Agenda: Entity Framework Design Session
1. Review current org/risk structure (30 min)
2. Define entity classes and reach consensus (30 min)
3. Draft entity hierarchy — top 3 levels (45 min)
4. Define tiering criteria and apply to known entities (45 min)
5. Validate cross-module scoping implications (30 min)
6. Document decisions, open items, and owners (15 min)

*Total: ~3 hours; recommend splitting across two sessions for large enterprises*
