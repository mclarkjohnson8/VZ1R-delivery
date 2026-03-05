# ServiceNow IRM: Deliver Phase Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

The Deliver phase covers the Build → Test → Close lifecycle of a ServiceNow IRM implementation. This document provides the configuration standards, sprint execution model, UAT framework, and release management approach used on the Verizon OneRisk engagement.

---

## Deliver Phase Objectives

1. Configure all in-scope modules to approved FDD/TDD specifications
2. Validate configuration through unit testing, system testing, and UAT
3. Complete data migration and validate data integrity
4. Obtain client go-live sign-off
5. Execute cutover and go-live

---

## Sprint Execution Model

### Sprint Structure (10 business days)

| Day | Activities |
|-----|-----------|
| Day 1 | Sprint Planning — confirm DoR; review capacity; assign stories; team commits |
| Day 1–9 | Development, configuration, unit testing, daily standups |
| Day 8–9 | Sprint Review/Demo preparation; defect triage |
| Day 10 | Sprint Review/Demo (stakeholder demo; DoD consensus); Sprint Retrospective |

### Sprint Metrics

| Metric | Calculation | Target |
|--------|-------------|--------|
| Velocity | Story points completed / sprint | Rolling 2-sprint average |
| Defect Density | Defects found in sprint / stories completed | Decreasing trend |
| Blocker Resolution | Avg days to resolve blockers | <2 days |
| UAT Acceptance Rate | UAT scripts passed / total | >95% at go-live |

---

## Definition of Ready (DoR) Checklist

Before a story enters a sprint:
- [ ] User story written in "As a [role], I want [action], so that [outcome]" format
- [ ] Acceptance criteria defined (measurable, testable)
- [ ] Dependencies identified and cleared
- [ ] Configuration environment available (DEV ready)
- [ ] Test data identified or available
- [ ] Team capacity confirmed to complete in sprint
- [ ] Integration dependencies documented

---

## Definition of Done (DoD) Checklist

Before a story is marked complete:
- [ ] Configured in DEV per FDD/TDD
- [ ] Unit tested by developer
- [ ] Peer reviewed (configuration review)
- [ ] Demo-ready with test data
- [ ] Documented (inline configuration notes + change log entry)
- [ ] Update Set created and named per convention
- [ ] DoD consensus from delivery team

---

## Configuration Promotion Path

```
DEV → TEST/UAT → PROD (Pre-Go-Live)
```

**Rules:**
- No manual changes in TEST or PROD outside of the Update Set process
- Each Update Set corresponds to one story or change
- TEST must be at same plugin/patch level as PROD
- Regression testing required after each TEST promotion
- PROD promotion only after UAT sign-off

---

## Update Set Naming Convention

```
[SPRINT]-[STORY-ID]-[Short Description]
Format: S12-VZ-0042-BitSight-C2-Issue-Generation-Fix
```

---

## UAT Framework

### UAT Phases (Verizon OneRisk)

| Phase | Scope | Lead | Target Date |
|-------|-------|------|-------------|
| IRQ UAT | IRQ scoring, workflow, portal | Heidi + VZ stakeholders | 2026-03-05 |
| BitSight C1 UAT | Score intake, alerts dashboard | Heidi | Underway |
| BitSight C2 UAT | Issue generation from alerts | Heidi / Vidhya | Pending C2 fix |
| Avetta UAT | Integration, data display | Alec / Gary | Pending staging fix |
| Ariba UAT | Contract data ingestion | TBD | Pending stage fix |
| Full Regression UAT | End-to-end workflow | Lauren (ERM), Jennifer (VCS) | 2026-03-12 |

### UAT Defect Severity

| Severity | Definition | Go-Live Impact |
|----------|-----------|----------------|
| **Critical** | Core functionality broken; no workaround | Blocks go-live |
| **High** | Major workflow broken; workaround exists but unacceptable | Blocks go-live |
| **Medium** | Partial functionality impaired; workaround exists | Does not block; track for Sprint 1 hypercare |
| **Low** | Minor UI/cosmetic issue | Does not block |

### UAT Sign-Off Authority
- ERM workflows: **Lauren** (client UAT lead)
- VCS workflows: **Jennifer** (client UAT lead)
- Technical integrations: **Vidhya Sagar** + **Arav Sundareswaran**
- Program sign-off: **Tony Scott** (go/no-go authority)

---

## Cutover Plan (Go-Live 2026-03-13)

### Pre-Cutover Checklist (by 2026-03-12)
- [ ] All UAT sign-offs received
- [ ] Data migration validated in PROD-parallel environment
- [ ] Integration endpoints switched to PROD
- [ ] Vendor freeze confirmed (no changes to legacy system)
- [ ] Support team briefed and on standby
- [ ] Rollback plan documented and rehearsed
- [ ] Go/No-Go gate cleared (2026-03-09)

### Cutover Window
- **Start**: End of business 2026-03-12 (or early morning 2026-03-13)
- **Completion target**: Business open 2026-03-13
- **Blackout period**: Legacy Vendor Risk system locked from 3/12 EOD

### Post-Cutover Validation (Day 1)
- [ ] Login and access validation for all user groups
- [ ] Integration smoke tests (BitSight C1, Avetta, Ariba)
- [ ] Sample record creation and workflow completion
- [ ] Notification delivery validation
- [ ] Performance baseline check

---

## Release Management

### Version Control
- ServiceNow: Update Sets (tracked in ServiceNow + project SharePoint)
- Configuration: documented in TDD (updated each sprint)
- Integration configs: version-controlled in this repository

### Rollback Procedure
- Pre-go-live rollback: restore to previous Update Set state in PROD
- Post-go-live: activate legacy system as fallback (vendor freeze must be reversible for 30 days)

---

*Reference document. Deliver phase is active — Sprint 12 of 12. Go-live target: 2026-03-13.*
