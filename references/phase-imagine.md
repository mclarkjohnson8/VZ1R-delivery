# ServiceNow IRM: Imagine Phase Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

The Imagine phase is the first phase of Deloitte's Imagine → Deliver → Run delivery framework. It covers program initiation, solution design, and architecture definition. This document describes the Imagine phase approach, deliverables, and quality standards applied to the Verizon OneRisk engagement.

---

## Imagine Phase Objectives

1. Align stakeholders on program vision, scope, and success criteria
2. Design the target state architecture (entity framework, module configuration, integrations)
3. Define the data migration approach
4. Establish the delivery governance model
5. Produce the FDD and TDD that will govern the Deliver phase
6. Identify and document assumptions, risks, and constraints

---

## Imagine Phase Activities

### Program Initiation

| Activity | Output | Key Stakeholders |
|----------|--------|-----------------|
| Program kick-off | Project Charter | All stakeholders |
| Stakeholder mapping | RACI matrix | Clark Johnson |
| Program governance setup | Steering committee charter; meeting cadence | Tony Scott, Sudhakar |
| Risk register initialization | Initial RAID log | Clark Johnson |
| Environment provisioning | DEV, TEST, PROD instances provisioned | Vidhya Sagar, Arav |

### Discovery & Current State Assessment

| Activity | Output | Key Stakeholders |
|----------|--------|-----------------|
| Legacy system analysis | Current state assessment | Heidi, VZ team |
| Process workshops (TPRM lifecycle) | As-Is process maps | Heidi, VCS, ERM leads |
| Data inventory | Field mapping spec (1,800+ fields) | Alec Barone |
| Integration discovery | Integration architecture doc | Vidhya Sagar, Gary Vick |
| User analysis | User roles + access matrix | Heidi, VZ IT |
| Questionnaire rationalization | Mapping: 21 questionnaires → 11 | Heidi, VCS/ERM |

### Solution Design

| Activity | Output | Key Stakeholders |
|----------|--------|-----------------|
| Entity framework design | Entity hierarchy + type definitions | Tony Scott, Arav |
| TPRM module design | FDD: TPRM workflows, assessments, vendor portal | Heidi, Vidhya Sagar |
| Integration design | TDD: BitSight C1/C2, Avetta, Ariba, EHS | Vidhya Sagar, Gary Vick |
| Data migration design | Data migration plan + scripts | Alec Barone |
| Access model design | RBAC matrix; OOB role mapping | Heidi, VZ IT |
| Training plan | Training schedule, materials outline | Clark Johnson |

---

## Key Deliverables

### Functional Design Document (FDD)
- Module-by-module functional specification
- Workflow diagrams (TPRM engagement lifecycle, assessment flows, issue management)
- Role-based access model
- Notification specifications
- Vendor portal design
- Assessment questionnaire mapping
- Reporting and dashboard specifications

### Technical Design Document (TDD)
- Entity framework schema
- Integration architecture (API specs, MID Server topology, credential management)
- Data migration technical approach
- Custom development specifications (where OOTB insufficient, with justification)
- Update Set strategy
- Performance and scalability considerations

### Architecture Decision Record (ADR)
Key decisions made during Imagine and their rationale:
- OOTB vs. customization decisions
- Integration approach selections
- Data migration vs. cutover-only decisions
- Entity framework structure choices

---

## Architecture Review Board (ARB) — Imagine Phase

During Imagine, the ARB reviews and approves:

| Decision | ARB Review | Outcome |
|----------|-----------|---------|
| Entity framework design | Yes | Approved |
| OOTB-first assessment framework | Yes | Approved (21 → 11 questionnaires) |
| BitSight C1 (OOB plugin) vs C2 (custom) | Yes | C1 OOB approved; C2 custom scoped |
| Integration architecture (Avetta, Ariba) | Yes | REST API approach approved |
| Access model (OOB roles vs custom) | Yes | OOB least-privilege approved |
| Data migration approach | Yes | Full migration approved |

---

## OOTB-First Analysis Framework

During Imagine, every capability requirement is evaluated:

```
Requirement → OOTB capability check → Gap analysis → Design decision
```

| Decision | Criteria |
|----------|---------|
| **Use OOTB** | Requirement met by OOB; no material gap |
| **Configure OOTB** | Requirement met by configuring OOB (fields, workflows, rules) |
| **Extend OOTB** | Requirement requires minor extension (custom field, minor script) |
| **Custom build** | Requirement cannot be met by any OOB approach; fully justified |

For Verizon OneRisk:
- **~85-90% OOTB target** — achieved
- **Custom**: BitSight C2 enhanced issue generation (only active custom item at Sprint 12)
- **~70% custom footprint eliminated** from legacy Vendor Risk application

---

## Imagine Phase Quality Gates

Before exiting Imagine and entering Deliver:

- [ ] FDD approved by client leads (Lauren, Jennifer, Heidi)
- [ ] TDD approved by architecture team (Tony Scott, Arav Sundareswaran)
- [ ] Entity framework validated and approved
- [ ] ARB sign-offs documented
- [ ] Data migration plan reviewed and approved
- [ ] Risk register reviewed; critical risks have mitigation plans
- [ ] Environment provisioning complete (DEV accessible)
- [ ] Sprint 1 backlog created and stories meet DoR

---

## Verizon OneRisk — Imagine Phase Notes

The Imagine phase for Verizon OneRisk was completed before Sprint 1 (July 2024 engagement start). Key outcomes:

- Entity framework: Designed and validated (stable through Sprint 12)
- Assessment framework: Rationalized from ~21 to 11 questionnaires
- Legacy footprint: 1,800+ fields and 100+ access rules mapped for elimination
- Integration scope: BitSight (OOB + custom), Avetta, Ariba, EHS defined
- OOTB target: 85-90% established; delivered at program close
- Vendor portal: Restored to OOB (data replication fix + self-service re-enabled)

---

*Reference document. Imagine phase is complete for Verizon OneRisk. This document is retained for decision traceability and post-go-live reference.*
