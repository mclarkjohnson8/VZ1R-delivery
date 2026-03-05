# ServiceNow IRM: Business Continuity Management (BCM) Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow Business Continuity Management (BCM) automates the planning, testing, and management of business continuity and disaster recovery programs. It integrates with the IRM Risk module and the TPRM module to provide a holistic view of organizational resilience.

---

## Module Architecture

### Core Objects

| Object | Description |
|--------|-------------|
| **Business Continuity Plan (BCP)** | Master plan document linking processes, recovery strategies, and teams |
| **Business Impact Analysis (BIA)** | Assessment of criticality, RTO/RPO, and dependencies for each business process |
| **Recovery Strategy** | Defined approach for restoring a process or system after disruption |
| **Continuity Test** | Tabletop, walkthrough, or full-scale test of BCP activation |
| **Continuity Issue** | Exception or gap identified during testing or incident activation |
| **Crisis Team** | Personnel roster and contact list activated during a BCM event |
| **Dependency Map** | Upstream/downstream dependencies between processes, systems, and vendors |

---

## BCM Lifecycle

```
Identify → Analyze (BIA) → Design Recovery → Document Plan → Test → Maintain
```

### 1. Business Impact Analysis (BIA)
- Identify critical business processes
- Assign Maximum Tolerable Downtime (MTD)
- Define Recovery Time Objective (RTO) and Recovery Point Objective (RPO)
- Map process dependencies (internal and third-party)
- Assign business owners

### 2. Recovery Strategy Design
- Identify recovery options (hot site, warm site, cold site, cloud, manual)
- Evaluate cost vs. RTO tradeoffs
- Assign recovery resources (personnel, technology, facilities)
- Document activation triggers and escalation paths

### 3. Plan Documentation
- BCP structure: scope, activation criteria, team roster, recovery procedures, communication plan
- Supplier/vendor recovery dependencies linked to TPRM records
- Plan approval and version control

### 4. Testing
- **Tabletop Exercise**: Discussion-based walkthrough of scenarios
- **Walkthrough Test**: Step-by-step procedure review without full activation
- **Full-Scale Exercise**: Complete BCP activation simulation
- Test results and issues tracked in ServiceNow
- Issue remediation assigned and tracked

### 5. Maintenance
- Annual review cycle
- Change-triggered reviews (org changes, system changes, vendor changes)
- Attestation workflow for plan owners
- Version history maintained

---

## Integration with TPRM

BCM and TPRM intersect at:

- **Fourth-Party Risk**: Vendor's BCM capability is assessed in DDQ/IRQ
- **Vendor Dependency Mapping**: Critical vendor dependencies recorded in BIA and linked to TPR records
- **BitSight Signals**: Vendor resilience/continuity signals can trigger BCP review
- **Incident-Triggered BCP**: Third-party incident (e.g., Avetta outage) can activate vendor BCP review workflow

---

## OOTB Configuration Standards

### Always Use OOB For:
- BIA criticality ratings (Mission Critical, High, Medium, Low)
- Standard RTO/RPO tiers
- Plan lifecycle states (Draft, Review, Approved, Active, Retired)
- Test scheduling and notification workflows
- Issue severity and aging rules

### Common Customizations (with documented justification):
- Industry-specific BIA question sets
- Custom dependency visualization for complex architectures
- Integration with external crisis communication tools (e.g., Everbridge, Rave)

---

## Role Matrix

| Role | OOB Role Name | Access Level |
|------|---------------|-------------|
| BCM Manager | sn_bcm.manager | Full CRUD on plans, BIAs, tests |
| BCM Analyst | sn_bcm.analyst | Create/update BIAs, recovery strategies, test records |
| Plan Owner | sn_bcm.plan_owner | Manage assigned plans; approve tests |
| Crisis Team Member | sn_bcm.crisis_team | View plans; update during activations |
| Reader | sn_bcm.read | Read-only |

---

## Verizon-Specific BCM Notes

- BCM module is in scope for Phase 2 post-TPRM go-live
- TPRM vendor assessments include BCM-specific questions in the DDQ
- Critical vendor list (Avetta, Ariba, BitSight) requires BIA entry with RTO/RPO targets
- Vendor portal exposes BCM-related assessment questions to third parties

---

## Key Metrics

- **Plan Coverage**: % of critical processes with approved BCPs
- **Test Completion**: % of plans tested within required cycle
- **Issue Close Rate**: Open BCM issues closed within SLA
- **BIA Currency**: % of BIAs reviewed within last 12 months

---

*Reference document. BCM is a Phase 2 module for Verizon OneRisk. Focus is TPRM for current sprint.*
