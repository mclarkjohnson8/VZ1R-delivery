# ServiceNow IRM: Policy & Compliance Management (PCM) Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow Policy and Compliance Management (PCM) automates the policy lifecycle, control management, and compliance program tracking. PCM integrates with Risk, Audit, and TPRM modules to provide an integrated GRC view.

---

## Module Architecture

### Core Objects

| Object | Description |
|--------|-------------|
| **Policy** | A formal statement of organizational intent, rule, or requirement |
| **Policy Statement** | Individual requirement within a policy |
| **Control** | A specific safeguard or countermeasure addressing a policy statement or risk |
| **Control Test** | Procedure to verify control effectiveness (design and operating effectiveness) |
| **Control Test Result** | Outcome of a control test (Pass, Fail, Exception, Not Applicable) |
| **Compliance Program** | Organized set of controls mapped to a regulatory framework or standard |
| **Citation** | External regulatory/standard requirement mapped to a policy statement |
| **Attestation** | Periodic sign-off by a control owner on control status |
| **Exception** | Documented deviation from a policy requirement |

---

## Policy Lifecycle

```
Draft → Review → Approved → Published → Active → Review Due → Retire
```

| State | Who Manages | Notes |
|-------|------------|-------|
| Draft | Policy Author | Content creation |
| Review | Policy Owner | Internal review, legal/compliance sign-off |
| Approved | Approver (role-based) | Formal approval before publication |
| Published | Policy Admin | Available to organization |
| Active | Policy Admin | Current version; attestation cycles running |
| Review Due | Automated trigger | SLA-based or change-triggered review notification |
| Retired | Policy Admin | Superseded or discontinued; archived for audit trail |

---

## Control Lifecycle

```
Create → Map to Policy/Risk → Test (Design) → Test (Operating) → Attest → Exception (if needed)
```

### Control Testing

| Test Type | Description | Frequency |
|-----------|-------------|-----------|
| **Design Effectiveness** | Does the control design address the risk/policy requirement? | Once (at creation or major change) |
| **Operating Effectiveness** | Is the control consistently operating as designed? | Annual minimum; risk-driven |
| **Management Attestation** | Control owner confirms control is in place and operating | As configured (quarterly, annual) |
| **Continuous Monitoring** | Automated test via data pull or integration | Real-time or scheduled |

### Control Test Results

| Result | Meaning |
|--------|---------|
| Pass | Control operating effectively; no exceptions |
| Fail | Control not operating; issue must be created |
| Exception | Partial pass; deviation documented and risk-accepted |
| Not Applicable | Control not applicable to this entity/scope |

---

## Compliance Programs

A Compliance Program maps a regulatory framework or standard to a set of controls across the organization.

### Common Frameworks
- ISO 27001
- SOC 2 Type II
- NIST CSF
- GDPR / CCPA (Privacy)
- PCI-DSS
- Verizon Internal Policy Framework

### Program Structure
```
Compliance Program
└── Scoping Rule (which entities are in scope)
    └── Control Families
        └── Controls
            └── Tests
                └── Test Results
```

---

## Attestation Workflow

1. Attestation period opens (automated trigger)
2. Control owner notified
3. Owner reviews evidence and confirms control status
4. Manager review (optional, configurable)
5. Attestation submitted
6. Results aggregated into compliance program scorecard
7. Exceptions or failures trigger Issue creation

---

## Integration with TPRM

PCM and TPRM connect through:

- **Vendor Controls**: Third-party compliance assessed via TPRM assessment questionnaires (DDQ includes compliance-related questions)
- **Shared Risk Framework**: Compliance failures (control failures) feed into the same Risk register as TPRM risks
- **Policy Citation in Assessments**: IRQ and DDQ questions can be mapped to Policy Statements
- **Regulatory Mapping**: External regulations mapped to TPRM assessment requirements

---

## Role Matrix

| Role | OOB Role Name | Access Level |
|------|---------------|-------------|
| Compliance Manager | sn_compliance.manager | Full CRUD on policies, controls, programs |
| Compliance Analyst | sn_compliance.analyst | Create/update control tests, attestations |
| Control Owner | sn_compliance.control_owner | Attest controls; manage exceptions |
| Policy Author | sn_compliance.policy_author | Draft and edit policy documents |
| Reader | sn_compliance.read | Read-only access |

---

## OOTB Configuration Standards

### Always Use OOB For:
- Policy lifecycle states
- Control test result taxonomy (Pass/Fail/Exception/N/A)
- Exception workflow (creation → approval → monitoring)
- Attestation scheduling
- Compliance scorecard dashboards

### Common Customizations (require documented justification):
- Custom regulatory frameworks not in the ServiceNow citation library
- Custom control hierarchies for enterprise-specific taxonomy
- Integration with external GRC tools (Archer, MetricStream)

---

## Verizon-Specific PCM Notes

- PCM module is in scope for Phase 2 post-TPRM go-live
- TPRM questionnaire questions (DDQ, IRQ) should be mapped to Verizon policy statements in Phase 2
- Vendor risk acceptance process (in TPRM) will integrate with the PCM exception workflow
- BitSight findings that constitute compliance violations should flow into PCM in Phase 2

---

## Key Metrics

- **Policy Currency**: % of active policies reviewed within required cycle
- **Control Coverage**: % of in-scope risks/policies with at least one control
- **Control Effectiveness**: % of tested controls passing (design + operating)
- **Exception Rate**: % of controls with active exceptions
- **Attestation Completion**: % of attestations completed on time

---

*Reference document. PCM is Phase 2 for Verizon OneRisk. Focus is TPRM for current sprint.*
