# Deloitte Delivery Model Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

Deloitte's ServiceNow IRM delivery methodology follows the **Imagine → Deliver → Run** framework, aligned with PMBOK and Agile principles. This document describes the Deloitte-specific delivery standards, governance model, and quality checkpoints applied to the Verizon OneRisk engagement.

---

## Delivery Framework: Imagine → Deliver → Run

### Phase 1: Imagine (Plan + Design)
**PMBOK**: Initiating + Planning | **Agile**: Inception, Discovery

#### Objectives
- Define program scope, objectives, and success criteria
- Design solution architecture and entity framework
- Establish governance model and RACI
- Identify integrations, data migration needs, and training requirements
- Produce Functional Design Document (FDD) and Technical Design Document (TDD)

#### Key Deliverables
- Program Charter
- Functional Design Document (FDD)
- Technical Design Document (TDD)
- Entity Framework Design
- Integration Architecture
- Data Migration Plan
- Training Plan
- Risk Register (Initial)

#### Quality Gates
- Architecture Review Board (ARB) sign-off on entity framework
- Client sign-off on FDD and TDD before Deliver phase begins
- Integration design reviewed by platform architect

---

### Phase 2: Deliver (Build + Test + Close)
**PMBOK**: Executing, M&C, Closing | **Agile**: Sprint cycles, UAT, release

#### Sprint Ceremonies (Deloitte Standard)

| Ceremony | Timing | Duration | Purpose |
|----------|--------|----------|---------|
| Sprint Planning | Day 1 | Half-day | Confirm DoR; review capacity; assign stories; team commits |
| Daily Standup | Daily | 15 min | Yesterday / Today / Impediments |
| Backlog Refinement | Ongoing | As needed | READY stories prepared for next sprint |
| Sprint Review/Demo | Day 10 | 2 hours | Stakeholder demo; DoD consensus; unmet stories carry |
| Sprint Retrospective | Day 10 | 1 hour | Like / Learn / Lack / Long For |

#### Definition of Ready (DoR)
Before a story enters a sprint:
- [ ] Scope defined
- [ ] Acceptance criteria written
- [ ] Dependencies cleared
- [ ] Capacity confirmed
- [ ] Test approach identified

#### Definition of Done (DoD)
Before a story is marked complete:
- [ ] Configured in DEV
- [ ] Unit tested
- [ ] Peer reviewed
- [ ] Demo-ready
- [ ] Documented
- [ ] DoD consensus from team

#### Velocity Tracking
- Rolling 2-sprint average velocity
- Blocker escalation: >2 days → PM; >3 days → Steering Committee

#### UAT Standards
- UAT scripts written from acceptance criteria
- Defect severity: Critical, High, Medium, Low
- Critical/High defects block go-live sign-off
- UAT sign-off required from designated client leads (Lauren for ERM; Jennifer for VCS)

---

### Phase 3: Run (Hypercare + Managed Service)
**PMBOK**: M&C in sustain mode | **Agile**: Kanban

#### Hypercare Window
- Duration: 2 weeks post-go-live (Verizon: 3/13 → 3/27)
- Staffing: Full delivery team on standby
- Incident response SLA: P1 = 4 hours; P2 = 8 hours; P3 = next business day
- Daily stand-up during hypercare

#### Transition to BAU
- Managed Service agreement activated
- Support model and escalation path documented
- Admin team certified (ServiceNow Admin)
- Runbook delivered (admin guide, integration operations, user guide)
- Vendor freeze lifted after hypercare close

---

## Governance Model

### Steering Committee
- **Frequency**: Monthly (or as-needed for critical decisions)
- **Members**: Merlyn (CSG sponsor), Tony Scott, Sudhakar Sivasubramanian, Clark Johnson
- **Purpose**: Program status, scope changes, go/no-go decisions, budget/resource approvals

### Delivery Team Standup
- **Frequency**: Daily
- **Members**: Full delivery team
- **Format**: Yesterday / Today / Impediments

### Architecture Review Board (ARB)
- **Members**: Tony Scott (chair), Vidhya Sagar, Arav Sundareswaran
- **Triggers**: Custom development proposals, integration architecture changes, entity framework changes

---

## RAID Management

| Category | Definition | Review Frequency |
|----------|-----------|-----------------|
| **R**isks | Potential future issues; probability × impact assessed | Weekly |
| **A**ssumptions | Stated program assumptions | Monthly or when challenged |
| **I**ssues | Active problems requiring resolution | Daily (standup); Weekly (PM review) |
| **D**ecisions | Key decisions made and pending | Sprint close; Steering Committee |

### Escalation Thresholds
- Issue open > 2 business days: PM escalation
- Issue open > 3 business days: Steering Committee notification
- Risk probability > 70% + High impact: Immediate PM + client notification

---

## Quality Standards

### Artifact Standards
- All deliverables in Deloitte template format
- Client-facing artifacts use "1Risk" (not "ServiceNow")
- No placeholder content in client-delivered artifacts
- Version control: Major.Minor (e.g., 1.0 = approved; 1.1 = minor revision; 2.0 = major revision)

### Code / Configuration Standards
- All customizations in scoped application (never global)
- Update Sets: one per story or change, named descriptively
- DEV → TEST/UAT → PROD promotion only (never manual changes in TEST or PROD)
- Code review required before TEST promotion

### Communication Standards
- Status reports: Weekly (internal); Bi-weekly (client)
- Executive communication: crisp Issue → Impact → Ask format
- All written communications timestamped and filed in project SharePoint

---

*Reference document. Deloitte delivery standards are non-negotiable on Verizon OneRisk engagement. Deviations require PM + client lead approval.*
