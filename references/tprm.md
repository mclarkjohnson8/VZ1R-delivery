# Third Party Risk Management (TPRM) Reference

## Table of Contents
1. Module Overview
2. TPRM Data Model
3. Vendor Onboarding Design
4. Assessment Framework
5. Vendor Tiering
6. Continuous Monitoring
7. Common Configuration Decisions
8. Anti-Patterns

---

## 1. Module Overview

ServiceNow TPRM operationalizes third-party risk identification, assessment, monitoring, and issue
management across the vendor lifecycle — from onboarding through offboarding.

**Primary Use Cases:**
- Vendor risk assessments (inherent and control-based)
- Vendor tiering and prioritization
- Continuous monitoring (news feeds, questionnaire-based, KRI tracking)
- Regulatory-driven vendor due diligence (OCC, DORA, FTC, state regulations)
- Fourth-party risk (sub-processor and downstream vendor tracking)

---

## 2. TPRM Data Model

### Core Tables
- `sn_vendor_profile` — Vendor entity record (extends `sn_grc_entity`)
- `sn_vendor_risk_assessment` — Assessment instance for a vendor
- `sn_vendor_contact` — Vendor-side contacts for assessment distribution
- `sn_vendor_risk` — Vendor-specific risk records (integrates with Risk module)
- `sn_vendor_document` — Contracts, certifications, SOC reports stored against vendor

### Vendor as Entity
TPRM vendors are entities within the Entity Framework. This means:
- Entity class = Vendor (or sub-classes: Software Vendor, Service Provider, Cloud Provider, etc.)
- Entity tier drives assessment frequency and depth
- All risk, issues, and audit records can be scoped to vendor entities

---

## 3. Vendor Onboarding Design

### Onboarding Workflow Stages
1. **Intake:** Business requestor submits new vendor request (name, category, service description, estimated spend)
2. **Preliminary Screening:** Risk team reviews; assigns initial tier; determines assessment depth
3. **Vendor Questionnaire:** Send inherent risk questionnaire to vendor contact
4. **Due Diligence Review:** Review questionnaire responses + third-party evidence (SOC 2, ISO cert, pen test results)
5. **Risk Scoring:** Score vendor on key risk dimensions; determine residual tier
6. **Approval:** Risk owner approves or escalates based on residual tier
7. **Onboarding Complete:** Vendor profile activated; monitoring schedule set; contract reference linked

### Key Onboarding Data Points to Capture
- Legal entity name, primary business address, parent company
- Service/product category and description
- Data access: types of data shared (PII, PHI, financial, IP), sensitivity level
- System access: which internal systems vendor can access, access type (read/write/admin)
- Sub-processors: does vendor use fourth parties who also access our data?
- Certifications held: SOC 2 Type II, ISO 27001, PCI-DSS, etc. (with expiration dates)
- Contract reference: MSA, SOW, DPA
- Business owner: who in the organization owns this vendor relationship

---

## 4. Assessment Framework

### Assessment Types

| Type | When Used | Delivery Method | Frequency |
|------|-----------|-----------------|-----------|
| Inherent Risk Questionnaire | At onboarding; determines initial tier | Portal / Email | Once (plus annual refresh) |
| Control Assessment | For Tier 1/2 vendors; evaluates control environment | Portal / Email | Annual (Tier 1), Bi-annual (Tier 2) |
| Abbreviated Assessment | Tier 3/4 vendors | Email questionnaire | Annual |
| Event-Triggered Assessment | After security incident, breach, M&A at vendor | Ad hoc | As needed |
| Fourth-Party Assessment | When sub-processors are identified | Portal / Email | Annual for critical sub-processors |

### Assessment Domain Coverage (Standard)
- Information Security (access controls, encryption, vulnerability management, incident response)
- Data Privacy (data handling, retention, deletion, consent management, breach notification)
- Business Continuity (BCP/DRP, RTO/RPO, testing history)
- Compliance (regulatory certifications, audit findings, regulatory actions)
- Financial Stability (for critical vendors — financial health indicators)
- Operational (SLA history, personnel practices, key-person dependency)

### Scoring Approach
- Domain-level scoring: each domain scored independently
- Composite score: weighted average of domain scores
- Weighting should reflect the client's risk priorities (e.g., data-heavy companies weight Privacy higher)
- Inherent risk score + control score → residual risk score → final vendor tier assignment

---

## 5. Vendor Tiering

### Standard Tiering Model

| Tier | Label | Criteria | Assessment Depth | Frequency |
|------|-------|----------|-----------------|-----------|
| 1 | Critical | Access to sensitive data; mission-critical service; no substitution possible; high spend | Full assessment + independent validation | Quarterly monitoring; annual full assessment |
| 2 | High | Significant data access or operational dependency; viable alternatives exist | Standard assessment | Semi-annual monitoring; annual assessment |
| 3 | Medium | Limited data access; non-critical service; standard contractual protections sufficient | Abbreviated assessment | Annual |
| 4 | Low | No data access; commodity service; easily replaceable | Self-certification or registration only | Bi-annual or on-change |

### Tiering Criteria Scoring Card
Design a tiering scorecard clients complete at onboarding, scoring each dimension:

| Dimension | Weight | Score 1 | Score 2 | Score 3 |
|-----------|--------|---------|---------|---------|
| Data Sensitivity | 25% | No sensitive data | Internal/confidential | PII/PHI/financial/regulated |
| System Access | 20% | No system access | Read-only | Read/write or privileged |
| Operational Dependency | 20% | Easily replaceable | Moderate dependency | Mission critical; no substitute |
| Regulatory Obligation | 20% | None | Indirect | Direct regulatory requirement |
| Annual Spend | 15% | <$100K | $100K-$1M | >$1M |

Final score maps to Tier 1-4 assignment.

---

## 6. Continuous Monitoring

### Monitoring Inputs
- **Assessment refresh cadence** (per tier — see above)
- **Certification expiration tracking** (SOC 2, ISO certs stored in vendor profile with expiration dates; automated alerts before expiry)
- **Adverse news monitoring** (integration with news/risk intelligence feeds — BitSight, SecurityScorecard, Dun & Bradstreet)
- **Incident notification tracking** (vendor-reported incidents; regulatory breach notifications)
- **SLA performance data** (if operationally integrated)

### Automated Alerts to Configure
- Certification expiring in 60/30 days → notify vendor manager
- Assessment overdue (vendor has not responded in 14 days) → escalate to vendor manager
- High-severity incident reported by vendor → trigger event-based assessment
- Vendor tier change (upgrade or downgrade) → notify business owner

### ⚠️ Risk: Monitoring Without Response Protocols
Continuous monitoring is only valuable if there are defined response protocols. Configure
alert workflows with clear escalation paths and response SLAs, not just notification emails.

---

## 7. Common Configuration Decisions

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Vendor portal | Use ServiceNow vendor portal for external questionnaires | Email-based questionnaire distribution | Vendor portal for Tier 1/2; email acceptable for Tier 3/4 |
| Fourth-party tracking | Track sub-processors in ServiceNow | Track in separate register | Track critical sub-processors in ServiceNow; lower-risk in separate register |
| Assessment distribution | Risk team sends to vendor | Business owner sends to vendor | Risk team owns; business owner co-signed on communication |
| SOC report review | Upload and manually review | Automated control mapping from SOC | Manual for Phase 1; explore automation in Phase 2 |
| Offboarding workflow | Manual offboarding process | Automated offboarding triggered by contract end | Configure automated trigger; include data deletion confirmation step |

---

## 8. Anti-Patterns

**Anti-Pattern: Tier 1 for Everything**
Same pattern as entity tiering — clients want all vendors at Tier 1. Apply the tiering scorecard
rigorously. Most enterprises have 5-15 Tier 1 vendors and hundreds at Tier 3/4.

**Anti-Pattern: Sending Assessments Without Vendor Contacts Configured**
Assessment emails go to nobody. Before launching the first assessment cycle, validate that every
in-scope vendor has a named contact with a valid email in the vendor profile.

**Anti-Pattern: TPRM as a One-Time Exercise**
Clients complete vendor onboarding assessments and consider TPRM "done." The value is in
continuous monitoring and periodic reassessment. Configure the re-assessment schedule and
assign a TPRM program manager before go-live.

**Anti-Pattern: No Integration with Contract Management**
Vendor profiles without contract references create governance gaps. Connect vendor records to
contract data at minimum by reference (contract number, expiration date, DPA reference).
Full CLM integration is Phase 2.
