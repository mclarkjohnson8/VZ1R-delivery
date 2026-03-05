# Risk Management Module Reference

## Table of Contents
1. Module Overview
2. Risk Hierarchy & Data Model
3. Risk Scoring Configuration
4. Risk Assessment Design
5. Risk Response & Treatment
6. Risk Register Design
7. Common Configuration Decisions
8. Anti-Patterns & Technical Debt Risks

---

## 1. Module Overview

ServiceNow Risk Management operationalizes enterprise risk identification, assessment, response,
and monitoring. It connects directly to Entity Framework (every risk is scoped to an entity),
PCM (control effectiveness informs residual risk), Issues (risk threshold breach triggers issues),
and Audit (audits validate risk and control design).

**Primary Use Cases:**
- Enterprise Risk Management (ERM)
- Operational Risk Management (ORM)
- IT Risk Management
- Cyber Risk Quantification (with extensions)
- Regulatory Risk Tracking

---

## 2. Risk Hierarchy & Data Model

### Core Tables
- `sn_risk_definition` — Risk taxonomy (the "type" of risk, reusable across entities)
- `sn_risk` — Scoped risk instance (a risk definition applied to a specific entity)
- `sn_risk_assessment` — Assessment record capturing scoring at a point in time
- `sn_risk_response` — Treatment/response plan for a risk
- `sn_risk_indicator` — Key Risk Indicators (KRIs) for continuous monitoring

### Risk Hierarchy Levels
```
Risk Category (top-level grouping, e.g., Cyber, Operational, Compliance)
└── Risk Definition (reusable risk type, e.g., "Data Breach")
    └── Scoped Risk (risk instance for a specific entity)
        └── Risk Assessment (point-in-time evaluation)
            └── Risk Response (treatment plan)
```

### Key Design Decision: Definition-First vs. Instance-First
- **Definition-First (Recommended):** Build the risk taxonomy first; scope to entities second.
  Enables consistency, rollup reporting, and reuse.
- **Instance-First:** Create risks directly on entities without a shared taxonomy.
  Leads to duplicates, inconsistent naming, and reporting fragmentation.

---

## 3. Risk Scoring Configuration

### Standard Scoring Matrix (Customize per Client)

**Likelihood Scale:**

| Score | Label | Definition |
|-------|-------|------------|
| 1 | Rare | May occur only in exceptional circumstances (<10% probability) |
| 2 | Unlikely | Could occur at some time (10-30%) |
| 3 | Possible | Might occur at some time (30-50%) |
| 4 | Likely | Will probably occur in most circumstances (50-70%) |
| 5 | Almost Certain | Expected to occur in most circumstances (>70%) |

**Impact Scale:**

| Score | Label | Financial | Operational | Reputational |
|-------|-------|-----------|-------------|--------------|
| 1 | Negligible | <$10K | Minor disruption, <4 hours | Minimal; internal only |
| 2 | Minor | $10K-$100K | Moderate; <1 day | Limited; local media |
| 3 | Moderate | $100K-$1M | Significant; <1 week | Regional attention |
| 4 | Major | $1M-$10M | Severe; <1 month | National coverage |
| 5 | Critical | >$10M | Catastrophic; >1 month | International; regulatory action |

**Risk Score = Likelihood × Impact (1-25 scale)**

**Risk Heat Map Thresholds (Recommended Defaults):**

| Score Range | Rating | Color |
|-------------|--------|-------|
| 1-4 | Low | Green |
| 5-9 | Medium | Yellow |
| 10-19 | High | Orange |
| 20-25 | Critical | Red |

### ⚠️ Risk: Scoring Methodology Lock-In
Once risk assessments are completed at scale, changing the scoring scale or thresholds requires
data migration and re-assessment. Obtain executive sign-off on scoring methodology before Sprint 1
Risk module configuration. Document it as a locked decision.

### Inherent vs. Residual Risk
- **Inherent Risk:** Risk score before controls are applied (Likelihood × Impact without controls)
- **Residual Risk:** Risk score after controls are applied
- **Target Risk:** The risk level the organization aspires to reach
- Configuration: ServiceNow supports all three natively; ensure all three are captured per scoped risk

---

## 4. Risk Assessment Design

### Assessment Types
- **Self-Assessment:** Risk owner completes assessment for their entity's risks
- **Facilitated Assessment:** Risk team facilitates with business unit
- **Automated Assessment:** KRI thresholds trigger automatic score updates
- **Continuous Monitoring:** Real-time data feeds update risk indicators

### Assessment Questionnaire Design Principles
- Keep questions to 10-15 per assessment; >20 drives abandonment
- Each question should directly inform likelihood or impact — remove questions that don't
- Use consistent scale language across all questions
- Pilot with 2-3 users before full rollout; UX issues surface quickly

### Assessment Scheduling
- Tier 1 entities: Quarterly or continuous
- Tier 2 entities: Semi-annually
- Tier 3/4 entities: Annually or on-change trigger
- Scheduling is driven by entity tier — confirm tier assignments in Entity Framework first

---

## 5. Risk Response & Treatment

### Treatment Options (Standard Taxonomy)
- **Accept:** Acknowledge risk; no action; document acceptance rationale and approver
- **Mitigate:** Implement controls to reduce likelihood or impact
- **Transfer:** Insurance, contracts, third-party arrangements
- **Avoid:** Eliminate the activity that creates the risk

### Response Record Configuration
Each Risk Response should capture:
- Treatment type (above)
- Response plan description
- Target residual risk score (after treatment)
- Owner (named individual)
- Due date
- Related control(s) — link to PCM if applicable
- Status (Planned / In Progress / Complete)
- Actual residual score post-treatment

### Issue Integration
Configure a threshold rule: when residual risk score exceeds the defined tolerance threshold,
automatically create an Issue record. Key configuration points:
- Threshold value (e.g., residual score ≥ 15)
- Issue priority mapping from risk score
- Issue owner defaults (risk owner vs. entity owner)
- Notification to risk manager on auto-creation

---

## 6. Risk Register Design

### Risk Register View Requirements
The standard risk register should support filtering by:
- Entity / Entity Hierarchy (rollup view)
- Risk Category
- Risk Rating (Critical / High / Medium / Low)
- Assessment status (Current / Overdue / Not assessed)
- Owner
- Treatment status

### Executive Risk Dashboard Components
- Heat map: Count of risks by Likelihood vs. Impact quadrant
- Top 10 risks by residual score (across all Tier 1 entities)
- Risk trend: Residual score movement over time (improving / stable / deteriorating)
- Treatment plan progress: % of High/Critical risks with active response plans
- Overdue assessments count

### Risk Appetite Statement Integration
- Risk appetite is typically set at the risk category level
- Configure appetite thresholds in ServiceNow to drive visual indicators on the dashboard
- Risks exceeding appetite should be visually distinguished and drive escalation workflows

---

## 7. Common Configuration Decisions

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Risk ownership model | Risk owner = entity owner | Risk owner = separate named individual | Separate named owner; entity owner is accountable but risk owner manages |
| Scoring type | Qualitative (1-5 scale) | Quantitative (financial impact) | Start qualitative; layer quantitative in Phase 2 if appetite exists |
| Control linkage | Link risks to controls in PCM | Standalone risk module | Always link to PCM if PCM is in scope; critical for residual scoring accuracy |
| KRI integration | Manual KRI updates | Automated data feed | Manual first; automate in Phase 2 when data sources are confirmed |
| Risk rollup | Entity-level only | Category-level + entity rollup | Category + entity rollup for meaningful executive reporting |

---

## 9. Risk Framework & Methodology Selection

### Preferred Risk Frameworks — Deloitte Standard

**ISO 27005 — Primary recommended standard for information security risk management**
- Provides the risk management process aligned to ISO 27001's ISMS requirements
- Defines risk identification, estimation, evaluation, treatment, acceptance, communication, and monitoring
- Use when: client has or is pursuing ISO 27001 certification; needs a structured, internationally recognized methodology
- ServiceNow mapping: ISO 27005 risk process maps directly to the Risk module lifecycle (identify → assess → treat → monitor)

**ISO 27001 — ISMS framework; risk management is a core requirement (Clause 6)**
- Risk assessment and treatment are mandatory for certification
- Annex A controls serve as a control library source in PCM
- Use when: client is pursuing or maintaining ISO 27001 certification
- ServiceNow mapping: Annex A controls imported as control library; risk treatment plans as risk responses

**ISO 27002 — Code of practice; provides implementation guidance for ISO 27001 Annex A controls**
- 93 controls across 4 themes: Organizational, People, Physical, Technological
- Use as: the control design reference when building the control library in PCM
- ServiceNow mapping: ISO 27002 controls imported as citations and mapped to client controls

**ISO 27003 — Implementation guidance for ISO 27001**
- Provides practical guidance on establishing, implementing, maintaining, and improving an ISMS
- Use when: client is in early stages of ISMS implementation alongside ServiceNow IRM
- Reference during: Imagine phase design workshops for program design decisions

**ISO 27004 — Measurement and evaluation of information security**
- Defines how to measure ISMS effectiveness, including risk management performance
- Use when: client needs a KRI/KPI framework tied to ISO standards
- ServiceNow mapping: informs dashboard KPI design and risk indicator configuration

**FAIR (Factor Analysis of Information Risk)**
- Quantitative risk methodology that translates cyber/operational risk into financial terms
- **Do not assume or recommend FAIR for clients who are early in their risk program maturity.** FAIR requires significant methodology design effort, dedicated analytical capability to sustain, and typically a separate quantification tool feeding ServiceNow.
- Use only when: client explicitly requests financial risk quantification; board-level reporting in dollar terms is a stated requirement; the client has or is building the internal capability to maintain quantitative models post-implementation
- ⚠️ Risk: FAIR scoping without confirmed client analytical capability and dedicated workstream leads to an incomplete implementation that becomes shelf-ware. Validate readiness before committing to FAIR in scope.

### Framework Selection Decision Guide

| Client Situation | Recommended Approach |
|-----------------|---------------------|
| Program just getting started | Qualitative scoring (Likelihood × Impact) with defined appetite thresholds; no framework complexity until foundation is stable |
| ISO 27001 certified or pursuing certification | ISO 27001 + 27002 (control library) + 27005 (risk process) |
| Needs international standard without full ISMS | ISO 27005 standalone |
| Regulatory-driven (NIST, PCI, SOX) | NIST CSF / SP 800-53 as primary; ISO as secondary mapping |
| Multiple frameworks in scope | UCF as harmonization layer; map all frameworks to unified control library |
| Mature program seeking measurement | Add ISO 27004 for KPI/KRI framework design |
| Mature program needing financial risk expression | FAIR — only after qualitative foundation is established and client capability is confirmed |

**Anti-Pattern: Risk Definitions Created at Entity Level Without Taxonomy**
When every entity creates its own risks without shared definitions, you end up with 500 variations
of "Data Breach" that can't be rolled up. Build the taxonomy first; enforce it via governance.

**Anti-Pattern: Skipping Inherent Risk Capture**
Clients sometimes want to skip inherent risk scoring and go straight to residual. This loses the
ability to measure control effectiveness over time. Always capture inherent risk.

**Anti-Pattern: No Risk Appetite Configured**
Without appetite thresholds, the risk register is a list with no actionability. Operationally,
nothing triggers escalation. Configure appetite — even if approximate — before go-live.

**Anti-Pattern: KRI Overload**
Clients want 50+ KRIs per risk. In practice, more than 5-7 KRIs per risk category creates data
quality problems (someone has to maintain them) and dilutes the signal. Be ruthless about KRI
selection criteria.
