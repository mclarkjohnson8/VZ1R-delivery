# Cross-Module Architecture Reference

## Table of Contents
1. IRM Data Model Overview
2. Module Integration Patterns
3. Common Integration Sequences
4. Technical Debt Prevention
5. Scoping Decision Framework
6. Platform Configuration Standards

---

## 1. IRM Data Model Overview

### Core Tables by Module

| Module | Primary Table | Key Related Tables |
|--------|--------------|-------------------|
| Entity Framework | `sn_grc_entity` | `sn_grc_entity_class`, `sn_grc_entity_profile` |
| Policy & Compliance | `sn_compliance_policy`, `sn_compliance_control` | `sn_compliance_policy_statement`, `sn_compliance_attestation` |
| Risk Management | `sn_risk_definition`, `sn_risk` | `sn_risk_assessment`, `sn_risk_response` |
| Audit Management | `sn_audit_engagement`, `sn_audit_task` | `sn_audit_finding`, `sn_audit_workpaper` |
| Issues | `sn_risk_issue` | `sn_risk_issue_task`, `sn_risk_remediation_plan` |
| Privacy | `sn_privacy_assessment`, `sn_privacy_data_element` | `sn_privacy_dpia`, `sn_privacy_consent` |
| BCM | `sn_bcm_plan`, `sn_bcm_test` | `sn_bcm_bia`, `sn_bcm_recovery_task` |
| TPRM | `sn_vendor_risk_assessment` | `sn_vendor_profile`, `sn_vendor_contact` |

### Universal Relationship: Everything Touches Entity
All module records relate back to `sn_grc_entity`. The entity's tier, class, and hierarchy drive:
- Which assessments apply
- What scoping filters appear in list views
- How rollup reporting aggregates
- Which stakeholders receive notifications

### Key Platform Dependencies
- **Common Framework:** Shared assessment engine, questionnaire builder, and scoring engine used
  across Risk, Audit, TPRM, and Privacy
- **Scoped Applications:** Each IRM module runs as a scoped app; cross-module references require
  explicit cross-scope access grants
- **GRC Dependency Map:** Risk → Issues → Audit → PCM represents the most common dependency chain;
  build and test in this order

---

## 2. Module Integration Patterns

### Pattern 1: Risk → Issues (Most Common)
When a risk's residual score exceeds tolerance threshold, an Issue is automatically generated.
- Configuration: Risk Response record + Issue threshold rule
- Key decision: Auto-create issues vs. manual issue creation from risk
- ⚠️ Risk: Auto-creation without ownership rules creates unassigned issue backlogs

### Pattern 2: Audit Finding → Issues
Audit findings that meet severity criteria automatically generate Issues for remediation tracking.
- Configuration: Audit Finding close action → Issue creation business rule
- Key decision: Map finding severity to issue priority (1:1 mapping recommended)
- ⚠️ Risk: Without agreed mapping, audit and risk teams use inconsistent severity definitions

### Pattern 3: Control Failure → Risk / Issue
Failed control attestation in PCM triggers risk re-assessment or issue creation.
- Configuration: Attestation result → workflow trigger → risk/issue record
- Key decision: Which control failures warrant automatic risk escalation vs. standard issue creation

### Pattern 4: TPRM Assessment → Risk
Vendor risk assessment results feed into the enterprise risk register as third-party risk items.
- Configuration: Vendor Assessment completion → Risk record creation/update
- Key decision: Vendor-level risks vs. aggregated third-party risk category

### Pattern 5: Privacy DPIA → Risk
Privacy impact assessments surface data risks that should appear in the enterprise risk register.
- Configuration: DPIA high-risk findings → Risk record creation
- Ensure Privacy and Risk module owners agree on risk taxonomy alignment

### Pattern 6: BCM → Entity / Risk
BIA results (RTOs, RPOs, criticality) update entity profiles and inform risk assessments for
critical processes and applications.

---

## 3. Common Integration Sequences

### Recommended Build Sequence — Deloitte Standard Module Order

This sequence reflects the dependency chain and mirrors the Deloitte delivery timeline. Modules build
on the data and configuration established by their predecessors.

```
Sprint 1-2:   IRM Core Data (entity/asset hierarchy, risk & control library import,
              data modeling, record form design, automated ownership assignment)
Sprint 3-5:   Policy & Compliance Management (PCM)
              (depends on entity framework + control library)
Sprint 4-7:   Risk Management (overlaps with late PCM sprints)
              (depends on entities + controls from PCM)
Sprint 6-8:   Issues Management
              (depends on risk threshold configuration)
Sprint 8-10:  Audit Management
              (depends on risk register + issues integration)
Sprint 6-10:  TPRM (can parallel-track after IRM Core Data is stable)
Sprint 9-12:  BCM / Privacy (data-intensive; typically Phase 2 unless explicitly scoped)
```

**IRM Core Data components (Sprint 1-2 must-haves):**
- Asset/entity inventory and hierarchy
- Imported risk and control libraries
- Asset-to-control and asset-to-risk mapping
- Automated control ownership assignment
- Data modeling and record form designs
- Notification framework (spans all in-scope modules)
- Comprehensive reporting and dashboard scaffolding
- Imported regulatory framework citations

### ⚠️ Risk: Parallel Module Build Without Integration Planning
Teams building modules simultaneously without agreed integration contracts create rework at
integration sprints. Conduct an Integration Design Workshop before Sprint 1 and lock integration
points in writing.

---

---

## 4. OOTB-First: Customization Decision Framework

Deloitte's standard is 85-90% out-of-the-box. Every customization is evaluated against this framework
before any build decision is made.

### Step 1: Identify
- Analyze current state and document goals and objectives
- Identify and document all requirements that appear to need deviation from OOB

### Step 2: Assess Complexity

| Complexity Tier | Definition | Risk Level |
|----------------|------------|-----------|
| **Low** | Foundational configurations, initial data entry, basic workflow setup | Lower Risk |
| **Light** | Minor modifications to standard OOB functionality to meet a specific business need | Lower Risk |
| **Medium** | Requires skills beyond point-and-click; typically involves some scripting | Moderate |
| **High** | Large effort for component design and implementation; multiple complex configurations or significant business logic testing | Higher Risk |
| **Very High** | Custom applications with many custom tables and scripts; platform performance requirements involved | Higher Risk |

### Step 3: Decide Build Approach

| Approach | When to Use | Complexity Tier |
|----------|-------------|-----------------|
| **Configure (OOTB-first)** | Leverage native IRM and TPRM features with minor adjustments | Low → Medium |
| **Customize** | Native modules implement the customization; business case required | High → Very High |
| **Extend with App Engine** | Build upgrade-safe, CSDM-aligned workflows that integrate with core IRM modules | High |
| **Build New** | Entirely new application; no OOB integration; requires executive approval, design review, and risk mitigation sign-off | Very High only |

### Governance Over Customization Decisions
All customization decisions are evaluated against: cost to implement, cost to operate, and impact on
business process change. Quick wins (high business value + high feasibility) proceed. Low business
value items are not implemented regardless of technical feasibility.

### Documentation Required for Every Non-Low Complexity Decision

| Field | Required Content |
|-------|-----------------|
| Requirement ID | Links to user story |
| Complexity Tier | Low / Light / Medium / High / Very High |
| Build Approach | Configure / Customize / Extend / Build New |
| Business Justification | Why OOB couldn't meet the need |
| Upgrade Risk | Low / Medium / High |
| Executive Approval | Required for Very High / Build New |
| Owner | Who maintains post go-live |

---

## 5. Scoping Decision Framework

### Module Inclusion Criteria
Before committing a module to scope, validate:
- [ ] Executive sponsor identified for this module's domain
- [ ] Business process owner(s) identified and engaged
- [ ] Data sources for population identified (entity data, control libraries, risk libraries)
- [ ] Integration dependencies with other in-scope modules documented
- [ ] Go-live definition agreed (what does "done" look like for this module)

### Phasing Principles
- Phase 1 should be narrower than the client wants and broader than the vendor recommends
- Prioritize modules that deliver standalone value (don't require other modules to be useful)
- Defer modules that depend heavily on data quality improvements not yet complete
- BCM and Privacy are most frequently deferred to Phase 2 — both are data-intensive

### Common Scope Trap: "We'll Just Add It Later"
Modules added post-go-live require entity re-scoping, stakeholder re-engagement, and often
re-training. Document deferred modules as a formal backlog with estimated sprint requirements.

---

## 6. Platform Configuration Standards

### Naming Conventions (Enforce from Day 1)
- Records: `[ClientAbbrev]_[ObjectType]_[Description]` (e.g., `VZW_CTL_DataEncryption`)
- Scripts: `[Module]_[Trigger]_[Action]` (e.g., `Risk_Threshold_CreateIssue`)
- Groups: `[Client]_[Function]_[Role]` (e.g., `VZW_Risk_Manager`)
- Update Sets: `[Sprint]_[Module]_[Description]` (e.g., `S03_Risk_ScoringConfig`)

### Update Set Management
- One update set per sprint per module — never mix modules in a single update set
- Commit and export at end of every sprint before demo
- Never develop in production; enforce DEV → TEST → PROD pipeline
- ⚠️ Risk: Ad-hoc updates in TEST or PROD without update sets create environments that can't be rebuilt

### Instance Strategy
| Environment | Purpose | Refresh Cadence |
|------------|---------|-----------------|
| DEV | Active development and unit testing | As needed |
| TEST/QA | Client UAT and regression testing | Pre-UAT sprint |
| PROD | Live environment | Post go-live approval only |
| TRAINING (optional) | End-user training | Post-UAT |

### Access Control Standards
- Use Groups, not individual users, for all role assignments
- Implement Row-Level Security (RLS) for entity-scoped data access
- Document ACL deviations from OOB in the customization log
- Admin accounts must not be used for day-to-day operations post-go-live
