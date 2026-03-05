# ServiceNow IRM: Run Phase Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

The Run phase covers hypercare, stabilization, and transition to business-as-usual (BAU) managed service operations. For Verizon OneRisk, the Run phase begins at go-live (2026-03-13) and hypercare closes on 2026-03-27. This document describes the operational model, support framework, and BAU procedures.

---

## Run Phase Objectives

1. Support stable go-live operations through the hypercare window
2. Resolve P1/P2 incidents within SLA
3. Complete the transition from delivery team to managed service / BAU operations
4. Hand off knowledge: admin documentation, runbooks, support procedures
5. Capture and action post-go-live enhancements

---

## Hypercare Model (2026-03-13 → 2026-03-27)

### Staffing Model

| Role | Hypercare Status | Post-Hypercare |
|------|-----------------|----------------|
| Clark Johnson (PM) | Available | Transitions to oversight |
| Heidi (Functional Lead) | Full presence | Transitions to BAU support |
| Vidhya Sagar (Architect) | On call | Transitions to managed service |
| Alec Barone (Developer) | Available | Transitions as needed |
| Gary Vick (Integrations) | On call | Available for integration issues |
| Tony Scott (Architect) | Available for escalations | Advisory role |

### Hypercare Incident Response SLAs

| Priority | Definition | Response | Resolution Target |
|----------|-----------|----------|------------------|
| **P1 — Critical** | System down; core TPRM workflow broken; data integrity issue | 4 hours | Same business day |
| **P2 — High** | Major feature broken; business impact; no workaround | 8 hours | Next business day |
| **P3 — Medium** | Feature impaired; workaround available | Next business day | Within 5 business days |
| **P4 — Low** | Minor issue; cosmetic; enhancement | 3 business days | Managed service backlog |

### Hypercare Daily Standup
- **Frequency**: Daily during hypercare window
- **Time**: [To be set at go-live]
- **Participants**: Clark, Heidi, Vidhya, VZ operations lead
- **Format**: Incident review → Resolution status → New issues → Actions

---

## Post-Go-Live Watch Items

| Item | Risk Level | Owner | Monitoring |
|------|-----------|-------|------------|
| BitSight C2 (if deferred) | Medium | Heidi / Vidhya | Daily check on issue generation |
| Avetta production stability | Medium | Gary Vick | Daily API health check |
| IRQ scoring accuracy | Medium | Heidi | Validate with live vendor data |
| Notification volume | Low | Heidi | Track daily volume vs. baseline |
| Vendor portal performance | Low | Vidhya | Monitor page load times |
| VCS Outbound API (ISS-005) | Medium | Tony / Arav | Architecture sprint scheduling |

---

## Transition to BAU

### Transition Checklist (by 2026-03-27)

#### Knowledge Transfer
- [ ] Admin Guide delivered and reviewed by Verizon admin team
- [ ] Integration Operations Runbook delivered
- [ ] User Guide delivered (TPRM Manager, Analyst, Vendor Portal roles)
- [ ] Training sessions complete (7 of 7)
- [ ] Hypercare findings documented and actioned or logged for managed service

#### Technical Handoff
- [ ] ServiceNow Admin role granted to Verizon admin team
- [ ] MID Server credentials and documentation transferred
- [ ] Integration credentials documented in Connection Aliases (not hardcoded)
- [ ] Update Set inventory finalized
- [ ] Performance baseline documented

#### Process Handoff
- [ ] Support model activated (service desk integration or direct ServiceNow support)
- [ ] Escalation path documented (Level 1 → Level 2 → Platform support)
- [ ] Change management process defined (who approves changes post-BAU)
- [ ] TPRM operational calendar established (assessment cycles, review cadences)

#### Governance Handoff
- [ ] Steering Committee meeting to formally close delivery engagement
- [ ] Lessons learned captured (retrospective)
- [ ] Post-go-live enhancement backlog documented (ISS-005, BitSight C2 if deferred, etc.)

---

## BAU Operating Model

### Platform Operations
- **Instance monitoring**: ServiceNow OOB monitoring + custom dashboards
- **Plugin/patch updates**: Coordinate with Verizon IT for quarterly ServiceNow releases
- **Performance monitoring**: Review quarterly; flag degradation proactively
- **Integration health**: MID Server status; API error rates; integration logs

### TPRM Operational Calendar

| Activity | Frequency | Owner |
|----------|-----------|-------|
| New vendor onboarding | As needed | TPRM Manager |
| IRQ scoring review | Quarterly | TPRM Manager + ERM |
| DDQ campaigns | Annual (per vendor tier) | TPRM Manager |
| BitSight score review | Monthly | TPRM Analyst |
| Risk acceptance review | Quarterly | Risk Manager |
| Access review (RBAC) | Semi-annual | System Admin |
| Policy/notification review | Annual | TPRM Manager |

### Change Management Post-BAU
- All changes require documented business justification
- Configuration changes follow DEV → TEST → PROD path (no exceptions)
- Custom code changes require architect review (Tony Scott / Vidhya Sagar advisory)
- ServiceNow upgrades (major releases): Deloitte upgrade assessment recommended

---

## Hypercare Close Criteria

Hypercare closes on 2026-03-27 if:
- [ ] No open P1 or P2 incidents
- [ ] All critical go-live issues resolved or tracked in managed service backlog with owners
- [ ] Transition checklist 100% complete
- [ ] Verizon operations lead confirms readiness
- [ ] Steering Committee formally accepts go-live completion

---

## Vendor Freeze Lift (2026-03-17)

The vendor freeze (no changes to legacy Vendor Risk system) lifts on 2026-03-17 regardless of hypercare status. After 3/17:
- Legacy system decommission planning can begin
- New vendor onboarding goes exclusively through 1Risk (TPRM)
- Legacy data archival plan to be executed within 90 days

---

*Reference document. Run phase begins 2026-03-13. This document governs hypercare operations and BAU transition.*
