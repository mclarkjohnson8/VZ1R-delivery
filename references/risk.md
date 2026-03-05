# ServiceNow IRM: Risk Management Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow Risk Management is the core module of the IRM suite. It provides a structured approach to identifying, assessing, treating, and monitoring risks across the enterprise. All other IRM modules (TPRM, Compliance, Audit, BCM) feed risk information into the Risk module and consume risk context from it.

---

## Module Architecture

### Core Objects

| Object | Description |
|--------|-------------|
| **Risk** | Individual risk record. Owned by an entity. Has a lifecycle from identification through closure. |
| **Risk Statement** | The formal statement of the risk: what could happen, why, and what the impact would be. |
| **Risk Assessment** | Periodic evaluation of likelihood and impact. Produces inherent and residual risk scores. |
| **Risk Response** | The chosen treatment: Accept, Avoid, Mitigate, Transfer. |
| **Risk Indicator (KRI)** | A measurable leading/lagging indicator used to monitor risk levels over time. |
| **Risk Acceptance** | Formal documented approval to accept a risk above tolerance. |
| **Risk Exception** | Time-limited deviation from a control or policy, with approval and expiry. |
| **Risk Appetite Statement** | Enterprise-level tolerance for risk by category. |
| **Risk Program** | Organized set of risks under a common theme (e.g., Third-Party Risk, Cyber Risk). |

---

## Risk Lifecycle

```
Identify → Assess → Respond → Monitor → Review → Close
```

### 1. Identify
- Risk sources: TPRM assessments, control failures, audit findings, operational incidents, strategic planning
- Documented with: risk statement, category, owner, entity attribution, date identified

### 2. Assess
- **Inherent Risk**: Risk before any controls are applied
  - Likelihood × Impact = Inherent Score
- **Control Effectiveness**: Assessment of how well controls reduce the risk
- **Residual Risk**: Risk after controls are applied
  - Inherent Risk × (1 - Control Effectiveness) = Residual Score

### Risk Scoring Matrix (Default OOB)

| Likelihood / Impact | Low | Medium | High | Critical |
|---------------------|-----|--------|------|----------|
| **Very Likely** | Medium | High | Critical | Critical |
| **Likely** | Low | Medium | High | Critical |
| **Possible** | Low | Medium | High | High |
| **Unlikely** | Low | Low | Medium | High |
| **Rare** | Low | Low | Low | Medium |

### 3. Respond
| Response | Definition | Verizon Usage |
|----------|-----------|--------------|
| **Mitigate** | Implement controls to reduce likelihood or impact | Primary response |
| **Accept** | Acknowledge and tolerate; document with approval | When residual within appetite |
| **Avoid** | Eliminate the activity creating the risk | Rare; major process changes |
| **Transfer** | Shift risk to third party (insurance, contract) | Contract risk transfer to vendors |

### 4. Monitor
- KRI thresholds set; auto-alerts when breached
- Risk indicator dashboards (operational level + executive)
- Quarterly risk review cycles (minimum)

---

## Risk Categories (Verizon IRM)

| Category | Description | Module Link |
|----------|-------------|------------|
| **Third-Party Risk** | Risks from vendor relationships | TPRM |
| **Cyber / Technology Risk** | IT security, data, system risks | TPRM + internal |
| **Operational Risk** | Process failure, human error, system downtime | BCM, Compliance |
| **Compliance Risk** | Regulatory violations, policy non-compliance | PCM |
| **Strategic Risk** | Business model, competitive, market risks | Executive |
| **Privacy/Data Risk** | PII handling, data protection, breach | Privacy + TPRM |
| **Financial Risk** | Fraud, financial reporting, credit | Compliance |

---

## Risk Appetite

Risk appetite is set at the enterprise level by the Steering Committee. It defines:
- **Risk Tolerance**: Maximum acceptable residual risk per category
- **Risk Capacity**: Total risk the organization can absorb
- **Risk Attitude**: Spectrum from risk-averse to risk-seeking

For Verizon OneRisk:
- Third-Party Risk appetite: **Low to Medium** (TPRM is a risk reduction program)
- Technology/Integration Risk: **Low** (real-time systems; 99.9% SLA targets)
- Operational Risk: **Medium**

---

## Key Risk Indicators (KRIs) — TPRM Focus

| KRI | Trigger Threshold | Source | Action |
|-----|------------------|--------|--------|
| BitSight score drop (vendor) | >10 point decline in 30 days | BitSight C1 | Trigger TPRM review |
| Overdue IRQ assessments | >30 days past due date | TPRM | Escalate to TPRM Manager |
| Open critical issues (vendor) | >2 open critical issues | TPRM Issues | Escalate to Risk Manager |
| Vendor SLA breach | Reported breach | Contract data (Ariba) | Trigger risk assessment update |
| DDQ non-response | >60 days overdue | TPRM | Escalate; consider tier change |

---

## Risk Acceptance Workflow

1. Risk owner identifies residual risk above tolerance
2. Risk Acceptance record created (references: Risk, Control, Assessment)
3. Justification documented (why mitigation is not feasible)
4. Risk Manager reviews
5. Executive approver sign-off (per risk category and threshold)
6. Acceptance period set (1 year maximum; renewable)
7. Risk flagged for next review cycle

---

## OOTB Configuration Standards

### Always Use OOB For:
- Risk lifecycle states
- Risk scoring methodology (likelihood × impact matrix)
- Risk category taxonomy
- KRI alerting framework
- Risk acceptance workflow
- Exception management workflow

### Common Customizations (require justification):
- Custom risk scoring formulas (Verizon IRQ bias factor adjustment is an example)
- Industry-specific risk taxonomies
- Custom KRI data sources (BitSight integration as KRI feed is in scope)

---

## Verizon-Specific Risk Notes

- Risk module integration with TPRM: third-party risks from assessments propagate to Risk register
- IRQ scoring (bias factor): resolved via admin config; no code change; settings documented
- BitSight signals as KRIs: Phase 2 — automated KRI updates from BitSight score changes
- VCS Outbound API (ISS-005): risk and engagement data exposed via read API in roadmap

---

*Reference document. Risk module is foundational — changes to risk scoring or appetite require Steering Committee approval.*
