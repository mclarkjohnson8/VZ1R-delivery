# ServiceNow IRM: Third-Party Risk Management (TPRM) Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

ServiceNow TPRM (Third-Party Risk Management) automates the lifecycle of third-party risk from vendor onboarding through ongoing monitoring and offboarding. For Verizon OneRisk, TPRM is the primary in-scope module — the migration from the legacy Vendor Risk application to TPRM is the core deliverable of this engagement.

---

## Module Architecture

### Core Objects

| Object | Description |
|--------|-------------|
| **Third-Party Profile (TPR)** | Master record for a vendor/third-party. Contains tier, risk rating, contacts, and all associated records. |
| **Engagement** | An assessment event against a vendor. Links to the assessment questionnaire and response workflow. |
| **Assessment (IRQ/DDQ)** | The questionnaire sent to or completed about a vendor. IRQ = Risk Intelligence; DDQ = Due Diligence. |
| **Response Portal** | The vendor-facing portal where third parties complete self-assessment questionnaires. |
| **Risk** | Third-party risk records created from assessment findings or external signals. |
| **Issue** | Active problem requiring remediation. Linked to TPR and entity. |
| **Finding** | Individual assessment finding. Can aggregate into Issues or Risks. |
| **Contact** | Vendor-side individual associated with a TPR record. |
| **Attachment** | Evidence documents, contracts, certifications linked to TPR or Engagement. |

---

## TPRM Lifecycle

```
Onboard → Profile → Assess → Risk-Rate → Monitor → Review → Offboard
```

### 1. Vendor Onboarding
- New vendor request created (manual or via integration trigger)
- Vendor entity created in entity framework
- TPR record created with tier assignment
- Initial data population (contacts, contract data from Ariba)
- Vendor portal credentials issued (if self-assessment applicable)

### 2. Vendor Profiling
- Tier assignment based on: data access, spend, operational dependency, geographic/regulatory exposure
- Tier-based assessment schedule (Tier 1: annual DDQ + quarterly IRQ; Tier 2: annual; Tier 3: periodic)
- Risk appetite alignment: high-tier vendors receive enhanced scrutiny

### Vendor Tier Model

| Tier | Risk Level | Assessment Frequency | Assessment Types |
|------|-----------|---------------------|-----------------|
| Tier 1 — Critical | High | Annual DDQ + Quarterly IRQ | Full DDQ + IRQ + Interviews |
| Tier 2 — High | Medium-High | Annual | DDQ + IRQ |
| Tier 3 — Medium | Medium | Bi-annual | Abbreviated DDQ |
| Tier 4 — Low | Low | Triennial or event-driven | Lite assessment |

### 3. Assessment (IRQ / DDQ)

#### IRQ — Risk Intelligence Questionnaire
- Scoring-enabled questionnaire
- Assesses vendor risk posture across domains: Security, Business Continuity, Privacy, Financial
- Outputs: Risk score, risk tier (confirmation or tier change), recommended actions
- Verizon config: bias factor resolved via admin config (maximize normalized input + metric weight adjustment)

#### DDQ — Due Diligence Questionnaire
- Comprehensive due diligence
- Covers: corporate governance, financial stability, security program, BCM/DR, privacy, compliance, sub-processors
- Outputs: Findings, issues, remediation requests, risk decisions

### 4. Risk Rating
- Risk calculated from: IRQ score + BitSight signal + DDQ findings + manual adjustments
- Risk response options: Accept (with approval), Mitigate (remediation plan), Transfer (contractual), Avoid (offboard)
- Risk acceptance requires documented approval (see Risk module reference)

### 5. Ongoing Monitoring
- **BitSight**: Continuous external threat intelligence feed
  - Component 1 (OOB): Scores + alert intake → displayed in TPRM dashboard
  - Component 2 (custom, in progress): Alert → 1Risk Issue generation
- **Avetta**: Fourth-party contractor management data
- **Ariba**: Contract status, renewal dates, financial data
- **EHS**: Environmental/Health/Safety signals
- Assessment review triggered by: scheduled cycle, material change, signal threshold breach

### 6. Vendor Offboarding
- Contract expiry or termination triggers offboarding workflow
- Data retention review (per Verizon data governance policy)
- TPR record archived (not deleted — audit trail required)
- Access revoked: vendor portal, any integrations
- Outstanding issues resolved or formally deferred

---

## Assessment Workflow (Engagement Lifecycle)

```
Create Engagement → Assign to Vendor → Send Assessment → Vendor Responds → 
Review Responses → Score/Rate → Create Findings → Risk Decision → Close
```

### Engagement States

| State | Description |
|-------|-------------|
| Draft | Engagement created; not yet sent |
| Sent | Assessment sent to vendor (portal notification) |
| In Progress | Vendor completing responses |
| Under Review | Responses submitted; under internal review |
| Remediation | Findings sent to vendor for remediation |
| Closed | Assessment cycle complete; outcomes documented |

---

## Vendor Portal

The Vendor Portal allows third-party vendors to:
- Complete self-assessment questionnaires
- Upload evidence documents
- Respond to remediation requests
- View their risk status (configurable)

**Verizon status**: Vendor portal restored to OOB functionality. Data replication fixed. Self-service re-enabled. Password/notification workflow confirmed.

---

## Integration Architecture (Verizon-Specific)

### BitSight (External Risk Intelligence)

#### Component 1 — OOB (Active)
- **Plugin**: ServiceNow OOB BitSight integration
- **Data flow**: BitSight API → MID Server → Staging table → TPRM entity records
- **Data types**: Company scores, industry benchmarks, alert feeds
- **Status**: ✅ Functional. UAT underway.

#### Component 2 — Custom (In Progress)
- **Design**: BitSight alert → enhanced findings logic → 1Risk GRC Issue creation
- **Defect**: Known ServiceNow bug — issues generated only for operational alerts, not critical
- **Status**: 🔴 Active blocker. Fix in development. Scope decision required by 2026-03-09.
- **Decision**: Include at go-live (with customization) or defer to hypercare sprint?

### Avetta (Fourth-Party / Contractor Data)
- **Purpose**: Contractor management and compliance data for subcontractor population
- **Data flow**: Avetta API → Staging → TPRM entity enrichment
- **Current issue**: Staging environment connectivity broken (subro instance policy change; Avetta-side server error)
- **Status**: 🔴 Active blocker. ETA resolution: 24 hours from 2026-03-05.
- **Long-term**: Subro endpoint exposure needed for resilient integration

### Ariba (Contracting Data)
- **Purpose**: Contract data, renewal dates, spend data → vendor profile enrichment
- **Data flow**: Ariba API → Staging → TPRM entity (contract fields)
- **Current issue**: Stage environment misconfiguration
- **Status**: 🟡 In Progress. Ariba team remediating.

### EHS (Environmental/Health/Safety)
- **Purpose**: EHS compliance data for vendor risk profiles
- **Status**: ⏳ Integration training scheduled 2026-03-10.

---

## Role Matrix

| Role | OOB Role Name | Access |
|------|---------------|--------|
| TPRM Manager | sn_vdr_risk.manager | Full CRUD on TPR records, engagements, assessments |
| TPRM Analyst | sn_vdr_risk.analyst | Create/update engagements, findings, issues |
| TPRM Reader | sn_vdr_risk.read | Read-only access |
| Vendor Portal User | sn_vdr_risk.vendor_portal | Vendor self-service portal only |
| Risk Manager | sn_risk.manager | Risk acceptance, risk register management |

---

## Questionnaire Library (Verizon Rationalized — 11 of 21)

| # | Questionnaire | Type | Tier Applicability |
|---|--------------|------|-------------------|
| 1 | IRQ — Standard | IRQ | Tier 1, 2, 3 |
| 2 | DDQ — Full | DDQ | Tier 1 |
| 3 | DDQ — Abbreviated | DDQ | Tier 2, 3 |
| 4 | IT Security Assessment | DDQ supplement | Tier 1 (IT vendors) |
| 5 | Business Continuity Assessment | DDQ supplement | Tier 1 (critical) |
| 6 | Privacy / Data Protection | DDQ supplement | Tier 1 (data-handling) |
| 7 | Financial Stability | DDQ supplement | Tier 1 (high-spend) |
| 8 | Fourth-Party Sub-Processor | DDQ supplement | Avetta-type vendors |
| 9 | EHS Assessment | Domain-specific | EHS-regulated vendors |
| 10 | New Vendor Onboarding Lite | Onboarding | All new vendors |
| 11 | Annual Re-attestation | Attestation | Tier 3, Tier 4 |

---

## TPRM Reporting & Dashboards

| Dashboard | Audience | Key Metrics |
|-----------|----------|------------|
| Executive TPRM Summary | Merlyn, Sudhakar, Tony | Risk exposure, open criticals, go-live readiness |
| TPRM Operational Dashboard | Heidi, team | Open assessments, issues, overdue items |
| Vendor Risk Scorecard | VCS/ERM leads | Per-vendor risk scores, BitSight trends |
| Integration Health Dashboard | Gary Vick, Vidhya | MID Server status, API health, error rates |

---

*Reference document. TPRM is the primary in-scope module. Current sprint (Sprint 12 of 12) — Go-Live: 2026-03-13. See engagement-state.json for current issue status.*
