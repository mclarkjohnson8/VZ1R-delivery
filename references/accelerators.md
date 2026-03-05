# Deloitte IRM Accelerator Library Reference

## Table of Contents
1. Accelerator Overview
2. Tailored SDLC Methodology
3. User Story Inventory (50 Stories)
4. IRM Data Import Templates (~10)
5. IRM Reporting Templates (~10)
6. IRM Process Flows (~10)
7. IRM Data Model Templates (~12)
8. IRM Implementation Design Binder
9. IRM Maturity Rating Matrix
10. OCM Impact Tracker & Adoption Scorecard
11. Best Practice IRM Strategy & Implementation Roadmap
12. Deloitte Risk AI Capabilities
13. Accelerator Deployment Guidance

---

## 1. Accelerator Overview

Deloitte's IRM accelerator library is built from 50+ certified IRM practitioners across 250+ global
GRC engagements. Accelerators reduce design time, establish quality baselines, and provide
proven starting points that are then tailored to the client's specific requirements.

**Important:** Not all accelerators are deployed on every engagement. Selection is based on
client requirements, scope, and maturity. Confirm which accelerators are applicable during
Imagine and document them in the project plan.

---

## 2. Tailored SDLC Methodology (Imagine → Deliver → Run)

**What it is:** Deloitte's proprietary delivery lifecycle framework adapted for ServiceNow IRM.
Maps the Imagine → Deliver → Run phases with agile sprint execution, governance touchpoints,
and quality gates.

**When to reference:** Kickoff, Ways of Working session, governance model design, any time
a client questions the delivery approach or requests methodology documentation.

**Key components:**
- Phase definitions and exit criteria
- Sprint cadence and ceremony structure
- Definition of Ready / Definition of Done standards
- Governance model overlay
- Quality review checkpoints

---

## 3. User Story Inventory (~50 Stories)

**What it is:** Pre-built library of 50 user stories covering the core IRM modules with
acceptance criteria, story point estimates, and test step guidance.

**When to deploy:** Sprint 1 backlog population; backlog refinement sessions; new client
engagements where requirements gathering is accelerating.

**Coverage by module:**
- IRM Core Data: entity/asset setup, control library import, risk library import
- Policy & Compliance: policy creation, attestation, exception workflow, compliance scoring
- Risk Management: risk assessment, risk response, risk scoring, KRI setup
- Issues Management: issue creation, remediation task, SLA escalation, closure
- Audit Management: engagement setup, control test, finding creation, evidence request
- TPRM: vendor onboarding, assessment launch, tiering, monitoring

**Usage guidance:** Use as starting templates, not final stories. Every story must be reviewed
and tailored to the client's specific requirements, terminology, and acceptance criteria before
sprint commitment.

---

## 4. IRM Data Import Templates (~10)

**What it is:** Pre-formatted import templates for loading foundational IRM data into ServiceNow.
Reduces manual data entry and accelerates IRM Core Data sprint.

**Templates available:**
- Entity/Asset hierarchy import template
- Risk library import (risk definitions, categories, descriptions)
- Control library import (control ID, name, description, type, frequency, owner)
- Regulatory citation import (framework mappings)
- Vendor/third-party inventory import
- Policy document metadata import
- User and group provisioning template
- Entity-to-control mapping template
- Entity-to-risk mapping template
- Compliance framework citation mapping template

**When to deploy:** IRM Core Data sprint (Sprint 1-2). Client provides data in specified format;
Deloitte validates, cleanses, and imports.

**⚠️ Client responsibility:** Client reviews, cleanses, and approves all data prior to upload.
Deloitte is not responsible for the accuracy or completeness of client-provided data.

---

## 5. IRM Reporting Templates (~10)

**What it is:** Pre-built ServiceNow report and dashboard configurations for standard IRM
KPIs and operational metrics.

**Templates available:**
- Risk heat map (likelihood × impact by entity)
- Control attestation completion rate by business unit
- Issues by status, severity, and age
- Audit engagement status and finding tracker
- TPRM vendor assessment status and risk score distribution
- Policy compliance posture by framework
- Overdue items dashboard (risks, issues, attestations, assessments)
- Executive IRM summary dashboard
- BCM recovery objective coverage (RTO/RPO by tier)
- IRM program health scorecard (cross-module KPIs)

**When to deploy:** Run phase (hypercare) for baseline; optionally configured during final
Deliver sprints for UAT validation of reporting requirements.

---

## 6. IRM Process Flows (~10)

**What it is:** Deloitte-designed future state IRM workflow diagrams showing the end-to-end
process for each core IRM use case, including roles, decision points, and system actions.

**Process flows available:**
- Risk identification and assessment workflow
- Control attestation and exception workflow
- Issue intake, triage, and remediation workflow
- Audit engagement lifecycle workflow
- Vendor onboarding and assessment workflow
- Policy creation, approval, and publication workflow
- BIA and BCP development workflow
- Privacy impact assessment (DPIA) workflow
- Regulatory change management workflow
- IRM governance and escalation workflow

**When to deploy:** Imagine phase design workshops — use as the "future state straw man"
to accelerate design decisions. Client reacts to the flow rather than building from scratch,
which significantly reduces workshop time.

---

## 7. IRM Data Model Templates (~12)

**What it is:** Pre-built data model diagrams showing the object model and key relationships
for each IRM module and cross-module integration patterns.

**Templates available:**
- IRM Core Data model (entity → risk → control relationships)
- PCM data model (policy → statement → control → attestation)
- Risk Management data model (definition → scoped risk → assessment → response)
- Issues data model (issue → task → remediation plan)
- Audit data model (plan → engagement → task → finding → workpaper)
- TPRM data model (vendor → assessment → risk → issue)
- Privacy data model (data element → DPIA → consent → incident)
- BCM data model (BIA → plan → test → recovery task)
- Cross-module integration map (all modules → entity framework)
- ServiceNow CSDM alignment model
- Reporting and analytics data model
- Integration architecture data model (ServiceNow → external systems)

**When to deploy:** Architecture review sessions during Imagine; Technical Architecture
document development; any cross-module design decision requiring data model reference.

---

## 8. IRM Implementation Design Binder

**What it is:** Consolidated design documentation template that captures all configuration
decisions, design specs, and build guidance for a ServiceNow IRM implementation.

**Contents:**
- Project overview and scope summary
- Entity framework design (hierarchy, classes, tiers)
- Module-by-module configuration design (per module: data model, workflows, notifications, reporting)
- Integration design (for each integration: source, target, field mapping, trigger, frequency)
- Customization log (all non-OOB decisions documented per complexity tier)
- Security and access control design
- Test strategy and UAT guide reference
- Go-live and cutover plan reference

**When to deploy:** Initiated in Imagine; maintained throughout Deliver; finalized as a
deliverable before go-live. This is the primary technical handoff document to the client's
operational team.

---

## 9. IRM Maturity Rating Matrix

**What it is:** A structured assessment tool that rates an organization's IRM program maturity
across key dimensions using a 1-5 scale (Initial → Optimized).

**Dimensions assessed:**
- Risk governance and oversight
- Policy and control framework maturity
- Risk assessment methodology
- Issue and remediation management
- Audit program maturity
- Third-party risk management
- Technology enablement and automation
- Data quality and reporting
- Culture and risk awareness
- Regulatory compliance posture

**When to deploy:**
- Strategize & Advise engagements (current state assessment)
- Beginning of Imagine (baseline the client before implementation)
- End of Run / hypercare (measure improvement from implementation)
- Periodic program assessments post-go-live

---

## 10. OCM Impact Tracker & Adoption Scorecard

**What it is:** Organizational Change Management toolset that tracks the people-side of
the IRM implementation — change impacts, training completion, and user adoption metrics.

**Components:**
- **Change Impact Assessment:** Maps changes by stakeholder group (what changes for each role, magnitude of change, readiness level)
- **Training Needs Analysis:** Role-based training requirements matrix
- **Training Completion Tracker:** By role, module, and business unit
- **Adoption Scorecard:** Post-go-live metrics tracking whether users are actually using the system (login rates, record creation volume, attestation completion, assessment participation)
- **Resistance Log:** Tracks identified resistance points with mitigation actions

**When to deploy:**
- Change impact assessment: Imagine phase
- Training delivery: final Deliver sprints
- Adoption scorecard: Run phase (hypercare and beyond)

---

## 11. Best Practice IRM Strategy & Implementation Roadmap

**What it is:** A templated IRM strategy document and phased implementation roadmap
that presents high, medium, and low complexity implementation options with effort
estimates and timelines.

**When to deploy:**
- Strategize & Advise engagements (delivered as the Wave 3 output)
- Any engagement where the client needs options analysis for scope and investment decisions
- Annual program planning for existing IRM clients

**Roadmap options (standard):**
- **Low:** Core Risk Management + Policy Management, basic reporting, standard workflows, limited integrations ($500K-$700K range)
- **Medium:** Full IRM suite (Risk, Policy, Compliance, Issues, Audit), advanced dashboards, UCF integration, extensive automation, ITSM integration ($800K-$1M range)
- **High:** Complete solution with advanced analytics, custom reporting, full external integrations, comprehensive training, extended support (up to $1.5M)

---

## 12. Deloitte Risk AI Capabilities

**What it is:** Deloitte's internally built Risk AI solution suite, integrated with ServiceNow
IRM architecture and built with modular, future-proof agentic capabilities.

**Suite components:**

| Suite | Capabilities |
|-------|-------------|
| **Process Analyzer & Mapping Suite** | Process modelling, risk & control mapping |
| **RCSA Quality & Automation Suite** | Risk identification, risk statement & rationale uplift, control suite risk mitigation analysis |
| **Control Review & Enhancement Suite** | Control uplift, control rationalization, control automation |
| **Platform Suite for Control Testing** | Test script generation, narrative generation, automated reporting |
| **Issue Management Automation Suite** | Issue capture & systemic root cause, remediation plan generation |

**Technical architecture:**
- AI assets integrated in the risk platform and linked with the risk data foundation
- Modular and upgrade-safe; built with agentic architecture
- KPIs built into the risk platform for continuous improvement measurement
- Full E2E tech stack consideration (experience layer, data integration, AI engine)

**When to position:** Advanced Risk Management or Issues Management scope; clients with
CISO mandate to automate GRC processes; clients with large control or risk libraries
where manual quality review is a bottleneck; board-level reporting requiring AI-generated
narratives.

---

## 13. Accelerator Deployment Guidance

### Accelerator Selection by Engagement Type

| Engagement Type | Priority Accelerators |
|----------------|----------------------|
| Full IRM suite implementation | SDLC methodology, user story library, data import templates, design binder, process flows, data model templates |
| Strategize & Advise only | Maturity rating matrix, implementation roadmap, IRM strategy framework |
| Risk + PCM (mid-size scope) | User story library (filtered), data import templates, reporting templates, design binder |
| Run (managed service) | Reporting templates, adoption scorecard, maturity rating matrix |
| Add-on module (existing client) | User story library (module-specific), data import templates, reporting templates |

### ⚠️ Risk: Treating Accelerators as Final Deliverables
Accelerators are starting points, not finished products. Every accelerator must be reviewed,
tailored, and approved by the client before use. An unmodified user story template does not
reflect the client's actual requirements. An unmodified process flow does not account for
the client's organizational structure and decision rights. Document all tailoring in the design binder.
