# Business Continuity Management (BCM) Reference

## Table of Contents
1. Module Overview & Scope
2. Regulatory & Standards Landscape
3. Business Impact Analysis (BIA)
4. BCP/DRP Documentation Standards
5. Exercise & Testing Program
6. Crisis Management & Incident Response Integration
7. Supply Chain & Third-Party Resilience
8. Recovery Task Management During Active Events
9. ServiceNow BCM Configuration — Full Scope
10. Program Governance & Maturity
11. Common Design Decisions
12. Anti-Patterns

---

## 1. Module Overview & Scope

ServiceNow BCM operationalizes the full business continuity lifecycle: Business Impact Analysis,
BCP/DRP documentation, exercise and testing management, crisis response, and recovery task execution.

BCM sits at the intersection of risk, operations, and IT — and is frequently scoped to Phase 2
because of its data intensity (BIA requires significant business input) and dependency on a mature
entity framework. When scoped to Phase 1, BIA requirements gathering should begin in Imagine
concurrently with other modules.

**BCM is foundational to:**
- IT Disaster Recovery (DR) planning for applications and infrastructure
- Operational resilience for regulatory requirements (DORA, FFIEC, OCC, ISO 22301, state insurance)
- Third-party resilience validation (TPRM dependency)
- Risk module alignment (BIA results inform operational risk assessments)

**Key integration dependencies:**
- Entity Framework must be complete before BIA scoping (BCM operates at process and application entity level)
- Risk module should be active before BCM — BIA findings surface as operational risks
- Issues module required for exercise findings and gap remediation tracking
- TPRM integration needed for third-party dependency visibility in BIA

**BCM vs. DR vs. Crisis Management — Scope Clarity:**

| Discipline | Focus | Owner | Activation Trigger |
|------------|-------|-------|-------------------|
| **BCM** | Maintaining critical business operations during any disruption | BCM Program Manager / COO | Any event threatening continuity |
| **IT Disaster Recovery** | Recovering IT systems and infrastructure | CTO / IT DR Lead | System/infrastructure failure or loss |
| **Crisis Management** | Leadership decision-making, communications, and external response | Executive (CEO/COO) | High-severity events requiring executive action |
| **Security Incident Response** | Detect, contain, eradicate cyber threats | CISO / Security team | Confirmed or suspected security event |

---

## 2. Regulatory & Standards Landscape

BCM program design should align with the regulatory and standards environment applicable to the client.
Confirm regulatory obligations in the Imagine phase before BIA scoping begins.

### ISO 22301 — Business Continuity Management Systems
The primary international standard for BCM. Defines requirements for a documented BCMS including:
- Context of the organization and interested parties
- Leadership commitment and BCM policy
- BIA and risk assessment process
- BCP/DRP documentation requirements
- Competence, awareness, and training
- Exercise and testing requirements
- Monitoring, measurement, and continual improvement

**ServiceNow mapping:** ISO 22301 certification requires documented evidence at each stage. ServiceNow BCM records (BIA, plans, exercise results, issues) serve as the audit trail. Where clients are pursuing ISO 22301 certification, configure record retention, approval workflows, and plan versioning accordingly.

### ISO 22317 — Business Impact Analysis Guidelines
Provides detailed guidance on BIA methodology aligned to ISO 22301. Key principles that should inform BIA design:
- BIA is a process for analyzing business functions and the effect that a disruption would have on them
- Output: prioritized list of activities, recovery time objectives, resource requirements
- BIA findings must be reviewed and approved at an appropriate level of authority

### ISO 22313 — Guidance for ISO 22301
Implementation guidance. Particularly useful for clients new to BCM who need prescriptive guidance alongside the standard itself.

### NIST SP 800-34 — Contingency Planning Guide for Federal Information Systems
Applicable primarily to federal agencies and regulated entities requiring NIST alignment:
- Defines contingency plan development for information systems
- Establishes BIA process with impact levels (low/medium/high) per FIPS 199
- Recovery strategy development, plan testing, and maintenance requirements

**ServiceNow mapping:** NIST 800-34 system categorization maps to entity criticality tiering in ServiceNow BCM. BIA records should capture FIPS impact levels where applicable.

### DORA — Digital Operational Resilience Act (EU)
Applicable to EU financial entities (banks, insurers, investment firms) and their critical ICT third-party providers:
- ICT risk management framework requirement
- Business continuity policy, crisis communication, recovery plans required
- ICT-related incident classification and reporting obligations
- Digital operational resilience testing (TLPT for significant entities)
- Third-party ICT risk management with contractual requirements

**ServiceNow mapping:** DORA compliance documentation can be built within BCM (plans, tests) and TPRM (third-party ICT contracts, assessments). Issues module captures ICT incident reporting. ⚠️ Risk: DORA has specific regulatory reporting timelines (initial notification: 4 hours; intermediate: 72 hours; final: 1 month) — configure notification workflows with these SLAs explicitly.

### FFIEC Business Continuity Management Booklet
Applies to US financial institutions regulated by FFIEC member agencies:
- Requires enterprise-wide BCM program with board oversight
- BIA and risk assessment as foundational activities
- Business continuity planning covering critical operations and services
- Testing requirements: annual tabletop minimum; periodic full-scale tests
- Third-party resilience requirements

### OCC Guidance (12 CFR Part 30)
Applicable to national banks and federal savings associations. Aligns with FFIEC guidance; emphasizes:
- Recovery time objectives that meet customer service commitments
- Testing programs that validate recovery capabilities
- Pandemic/widespread disruption scenarios

### Healthcare Regulatory Considerations
- **CMS Conditions of Participation (CoP):** Require hospitals to maintain emergency operations plans covering alternate care sites, resource management, communication, and staff roles
- **The Joint Commission:** Emergency Management chapter (EM) requires a hazard vulnerability analysis (HVA) that maps directly to BIA methodology; four phases of emergency management (mitigation, preparedness, response, recovery)
- **HIPAA:** Emergency access provisions and contingency planning requirements (data backup, disaster recovery, emergency mode operations, testing, applications criticality analysis)
- **HHS HPP / ASPR:** Hospital preparedness program requirements for healthcare coalitions and resource sharing

⚠️ For healthcare clients, BIA scope must include clinical operations and patient care processes — not just IT systems. Recovery objectives for clinical processes may be measured in minutes, not hours.

---

## 3. Business Impact Analysis (BIA)

### BIA Purpose
The BIA identifies which business processes and supporting systems are critical, quantifies the impact
of disruption over time, and establishes the recovery objectives that drive BCP/DRP design.

### Core Recovery Metrics

| Metric | Definition | How Used |
|--------|------------|----------|
| **RTO** (Recovery Time Objective) | Maximum acceptable time to restore a process/system after disruption | Drives DR architecture and recovery procedure design |
| **RPO** (Recovery Point Objective) | Maximum acceptable data loss measured in time | Drives backup frequency and replication strategy |
| **MTPD** (Maximum Tolerable Period of Disruption) | Point beyond which the organization cannot recover — existential threshold | Sets the outer boundary; RTO must always be less than MTPD |
| **WRT** (Work Recovery Time) | Time to restore normal operations after systems are recovered | RTO (total) = RTO (technical) + WRT |
| **MBCO** (Minimum Business Continuity Objective) | Minimum level of service acceptable during recovery | Informs degraded mode operating procedures |
| **RLO** (Recovery Level Objective) | Minimum level of functionality required at restoration | Relevant for phased system recovery |

### BIA Scoping Approach
Conduct BIA at the **process** and **application** entity level — not at the business unit level.
Business units are too broad; process and application-level BIA produces actionable recovery objectives.

**BIA scope determination steps:**
1. Identify all in-scope processes and supporting applications (source from entity hierarchy)
2. Group by business domain and assign BIA facilitators
3. Tier processes by initial criticality estimate to prioritize facilitation effort
4. Conduct facilitated BIA sessions per domain (see workshop structure below)
5. Validate outputs with IT to confirm technical feasibility of stated RTOs/RPOs
6. Produce recovery gap analysis — delta between stated objectives and current capability
7. Obtain business and executive sign-off on finalized BIA outputs

### BIA Data Model — Key Attributes per Process/Application

| Attribute | Description |
|-----------|-------------|
| Process / Application Name | Entity record reference |
| Business Owner | Named individual accountable for this process |
| Process Description | What the process does and what it enables |
| Peak Periods | Times of highest operational dependency (e.g., month-end close, holiday season, regulatory deadlines) |
| Regulatory / Contractual Obligations | Any regulatory SLAs or contractual commitments tied to this process |
| Dependencies — Upstream | Processes/systems this process depends on to function |
| Dependencies — Downstream | Processes/systems that depend on this process |
| Third-Party Dependencies | Critical vendors/suppliers in the dependency chain |
| Staff Dependencies | Number of staff required; named alternates; minimum staffing for degraded mode |
| Physical Dependencies | Facilities, equipment, utilities required |
| Impact at 1 hour | Financial, operational, reputational, regulatory |
| Impact at 4 hours | Same dimensions |
| Impact at 24 hours | Same dimensions |
| Impact at 72 hours | Same dimensions |
| Impact at 1 week | Same dimensions |
| RTO (business-stated) | Maximum downtime tolerable per business owner |
| RPO (business-stated) | Maximum data loss tolerable per business owner |
| MTPD | Absolute recovery deadline |
| MBCO | Minimum operational level acceptable during recovery |
| Current Recovery Capability | What exists today (manual workaround, hot standby, cold backup, none) |
| Current RTO Capability | What recovery time the current architecture actually achieves |
| Recovery Gap | Delta between stated RTO and current capability |
| Criticality Tier | Critical / High / Medium / Low (derived from impact ratings) |
| Manual Workaround | Whether a viable manual workaround exists; description if yes |
| Workaround Duration Limit | How long the manual workaround can be sustained |

### Criticality Scoring Framework

| Score | Criticality | RTO Target | Definition |
|-------|-------------|-----------|------------|
| 1 — Critical | Tier 1 | ≤ 1 hour | Disruption causes unacceptable impact within 1 hour; no viable manual workaround; regulatory or patient-safety implications possible |
| 2 — High | Tier 2 | ≤ 4 hours | Disruption causes significant impact within 4 hours; limited workaround available |
| 3 — Medium | Tier 3 | ≤ 24 hours | Disruption causes moderate impact; effective workaround exists |
| 4 — Low | Tier 4 | > 24 hours | Disruption tolerable for more than 24 hours; full manual workaround available |

### Impact Assessment Dimensions

For each process at each time horizon, assess impact across all relevant dimensions:

| Dimension | Description | Example Indicators |
|-----------|-------------|-------------------|
| **Financial** | Direct revenue loss, cost of workaround, regulatory fines | Revenue per hour, contractual penalty amounts |
| **Operational** | Ability to deliver products/services | Customer SLA breaches, production stoppage |
| **Regulatory / Legal** | Compliance obligations, reporting timelines | Regulatory breach notifications, consent order risk |
| **Reputational** | Customer confidence, brand, media exposure | Customer churn risk, media attention level |
| **Safety / Patient Care** | Risk to human life or patient outcomes | Clinical pathway disruption, medication management impact |
| **Data Integrity** | Corruption, loss, or unavailability of critical data | Transactions lost, patient record gaps |

### Dependency Mapping
Dependency mapping is the most analytically intensive BIA activity and the one most commonly
under-resourced. Single points of failure and cascading failure chains only become visible through
systematic dependency mapping.

**Required dependency artifacts:**
- Process-to-process dependency matrix
- Process-to-application dependency matrix
- Application-to-infrastructure dependency (source from CMDB where available)
- Third-party/vendor dependency map
- Facility dependency map

**Dependency analysis outputs:**
- Single points of failure (one process/system whose loss cascades broadly)
- Shared dependencies (one infrastructure component supporting multiple critical processes)
- Third-party critical path items requiring TPRM alignment

**⚠️ Risk: BIA Without Dependency Mapping Produces Misleading RTOs**
A process owner may state an RTO of 4 hours, not realizing their process depends on an application
with a current recovery capability of 72 hours. Dependencies must be validated before RTOs are finalized.

### Hazard Vulnerability Analysis (HVA)
For healthcare clients (Joint Commission requirement) and any client with significant physical risk exposure, conduct an HVA alongside the BIA. The HVA assesses:
- Natural hazards (flooding, earthquake, hurricane, winter storm)
- Technological hazards (utility failure, cyber incident, system outage)
- Human/community hazards (civil unrest, pandemic, active shooter)

HVA outputs feed directly into BIA scenario design and exercise scenario selection. Joint Commission requires annual HVA review.

### BIA Workshop Structure (per Business Domain, ~3 hours)
1. BIA overview and methodology briefing (20 min)
2. Process inventory validation — confirm all processes in scope (20 min)
3. Impact assessment per process — work through dimensions at each time horizon (60 min)
4. Recovery objective elicitation — RTO, RPO, MTPD, MBCO per process (30 min)
5. Dependency identification — upstream/downstream processes, applications, third parties, facilities (30 min)
6. Manual workaround review — what exists, how long it can be sustained (15 min)
7. Open items and next steps (5 min)

**Post-workshop:** BIA coordinator consolidates outputs, validates against IT capability, presents
recovery gap analysis within 5 business days. Gap analysis must show:
- Processes where current capability meets stated RTO (no gap)
- Processes where current capability falls short (gap = quantified delta)
- Investment implications of closing each gap

---

## 4. BCP/DRP Documentation Standards

### Plan Types

| Plan Type | Scope | Primary Audience | Owner |
|-----------|-------|-----------------|-------|
| **Business Continuity Plan (BCP)** | How critical business processes continue during disruption | Business process owners, operational teams | BCM Program Manager |
| **Disaster Recovery Plan (DRP)** | How IT systems and infrastructure are recovered | IT operations, infrastructure teams | CTO / IT DR Lead |
| **Crisis Management Plan (CMP)** | How leadership responds, communicates, and makes decisions during a crisis | Executive leadership, communications, legal | COO / CEO |
| **Business Recovery Plan (BRP)** | How normal operations are restored after systems are recovered | Business unit leads | Business owners |
| **Occupant Emergency Plan (OEP)** | Physical safety and evacuation procedures | Facilities, all employees | Facilities Manager |
| **Pandemic / Widespread Disruption Plan** | Operations under mass absenteeism or remote-only conditions | HR, Operations | COO / HR Lead |

### BCP Document Structure (Standard Template)

**Section 1: Plan Overview**
- Purpose, scope, and applicability
- Activation criteria — specific, unambiguous thresholds that trigger this plan
- Plan owner, version, and review/approval history
- Relationship to other plans (DRP, CMP) — how they interact and sequence
- Distribution and access — where the plan is stored; who has access offline

**Section 2: Roles and Responsibilities**
- Crisis Management Team (CMT) composition and decision authority matrix
- Business Continuity Team roles per process/function
- Named primary and alternate for every role (every role must have a trained alternate)
- Escalation decision authority (who can activate the plan; who cannot)
- Contact directory — name, role, cell, alternate cell, personal email; updated quarterly minimum

**Section 3: Recovery Strategies**
Per critical process:
- Degraded mode operating procedure (how the process operates at minimum viable capacity)
- Manual workaround procedures (step-by-step; must be usable without system access)
- Alternate site / remote work procedures (where staff go; how connectivity is established)
- Critical resource requirements (minimum staffing numbers, equipment, third-party access, data)
- Time-horizon actions (what changes at T+1hr, T+4hr, T+24hr, T+72hr, T+1 week)

**Section 4: Recovery Procedures**
- Step-by-step recovery actions per critical process, sequenced by priority
- Decision tree: criteria for activating degraded mode vs. full recovery vs. alternate site
- Time-sequenced checklist with owner for each step
- IT recovery handoff point — when IT declares system restored, what does the business do to validate and resume?
- Validation criteria — how the team confirms recovery is sufficient to resume normal operations

**Section 5: Communication Templates**
- Internal staff communications (by audience: all staff, management, board)
- Customer communications — general service disruption; specific commitments
- Regulatory notification templates with applicable SLA timelines pre-populated
- Media holding statement — approved by legal and communications
- Supplier/vendor notifications where applicable

**Section 6: Plan Maintenance**
- Annual review cycle — month in which full plan review occurs
- Trigger-based review criteria (material system change, org restructure, post-exercise gaps, regulatory requirement change)
- Change management process for plan updates (who drafts, who approves, how distribution is managed)
- Training and awareness requirements — who must be trained; frequency; how competency is validated

### DRP Document Structure (Standard Template)

**Section 1: DR Overview**
- Scope — which systems and applications are covered
- Recovery architecture overview (hot standby, warm standby, cold standby, cloud failover)
- RTO/RPO targets by system criticality tier
- DR site location(s) — primary and secondary
- Assumptions and dependencies

**Section 2: System Inventory and Tier Classification**

| System / Application | Criticality Tier | RTO | RPO | Recovery Architecture | Primary DR Site | Secondary DR Site |
|----------------------|-----------------|-----|-----|-----------------------|-----------------|------------------|

**Section 3: Pre-Incident Preparation**
- Backup schedules and validation procedures
- Replication health monitoring
- DR environment maintenance (patching, credentials, periodic validation)
- Run book location — physical and digital copies; offline access plan

**Section 4: Activation Decision and Notification**
- Declaration criteria — who declares; what observable thresholds trigger DR activation
- Escalation path — from monitoring alert to DR declaration
- Notification sequence — who is notified, in what order, by whom
- Mobilization procedure — how DR team assembles

**Section 5: DR Runbooks (per system/application)**
- Pre-failover checklist (confirm replication is current; confirm DR environment is healthy)
- Failover execution steps with named owner per step and validation checkpoint
- Post-failover validation (user acceptance; data integrity; connectivity; monitoring restored)
- Failback procedure — how to return to primary environment
- Known issues and workarounds during DR operation
- Rollback triggers — conditions under which failover is abandoned

**Section 6: DR Testing Results**
- Last test date, scope, test type, outcome
- RTO/RPO achieved vs. targets
- Deficiencies identified and remediation status

---

## 5. Exercise & Testing Program

### Exercise Types

| Type | Description | Frequency | Resources Required |
|------|-------------|-----------|-------------------|
| **Tabletop Exercise** | Discussion-based scenario walkthrough; no system activation | Annual minimum for all Tier 1/2 plans | Facilitator + participants (half day) |
| **Walkthrough / Plan Review** | Team reads through plan together; validates accuracy | Annual at minimum; any time after material changes | Plan owners + key personnel (2-3 hours) |
| **Functional Exercise** | Activates specific response functions without full system recovery | Annual for high-criticality processes | Response team + logistics (full day) |
| **Simulation / Parallel Test** | Systems brought up in DR environment while production continues | Annual for Tier 1 IT systems | IT DR team + business validators (full day) |
| **Full-Scale / Cutover Test** | Production fails over to DR environment for a defined window | Bi-annual for highest-criticality systems; required by some regulators | All teams; significant overhead |
| **Unannounced Exercise** | Scenario activated without advance notice | After program maturity is established; not Year 1 | Requires executive sponsorship and no-fault culture |

### Exercise Program Governance
- Annual exercise calendar published at program launch; incorporated into BCM governance calendar
- Exercise plan (scope, scenario, objectives, participants) approved 6 weeks in advance
- After-Action Report (AAR) completed within 1 week of exercise; approved within 2 weeks
- All identified gaps converted to Issues in ServiceNow with owners and due dates

### Exercise Design Principles
- **Scenario-based:** Realistic scenarios relevant to the client's risk environment — ransomware, data center outage, key supplier failure, natural disaster, pandemic/mass absenteeism, regulatory notification event
- **Objective-driven:** Define 3-5 measurable exercise objectives before the exercise; evaluate against them in the AAR
- **No-fault culture:** Exercises surface gaps; requires explicit executive framing before the exercise
- **Inject design:** Build 2-3 injects (unexpected mid-exercise developments) to test adaptability
- **Escalating complexity:** New programs start with tabletops; add complexity annually
- **Include third parties:** Critical vendors should participate in exercises where they are on the dependency path — include this as a contractual requirement for critical providers

### Tabletop Exercise — Full Planning and Execution

**8 weeks prior:** Define scenario type, exercise scope, objectives, facilitator, and observers.

**6 weeks prior:** Draft scenario and inject sequence. Identify and notify all participants. Distribute pre-read: current BCP/DRP, scenario overview, participant roles.

**2 weeks prior:** Final scenario distributed to facilitators only (not participants). Logistics confirmed.

**Exercise Day:**
1. Welcome, objectives, and ground rules — no-fault framing (15 min)
2. Scenario presentation — initial situation (15 min)
3. Facilitated walkthrough with injects (2-3 hours)
4. Hot debrief — immediate participant observations (30 min)

**Within 1 week post-exercise:**
- After-Action Report drafted and circulated
- Gaps converted to Issues in ServiceNow
- Plan updates triggered where procedures proved incorrect or incomplete

### After-Action Report (AAR) Structure
1. Exercise Overview — date, scope, participants, scenario summary
2. Objectives Assessment — each objective rated (Met / Partially Met / Not Met) with evidence
3. Strengths — specific behaviors and decisions that were effective
4. Areas for Improvement — what didn't work; root cause per gap
5. Issues and Corrective Actions — tabular list: gap, recommended action, owner, due date
6. Plan Update Requirements — specific plan sections to update, by whom, by when

### Exercise Findings to Issues Integration
Any gap requiring a plan or capability change creates an Issue record:
- Issue source: BCM Exercise
- Issue type: Corrective Action (plan update) or Capability Gap (investment required)
- Priority: Tier 1 gaps = High; Tier 2 gaps = Medium
- Owner = plan owner or process owner
- Due date aligned to next exercise cycle or regulatory deadline

---

## 6. Crisis Management & Incident Response Integration

### Crisis Management Plan Activation Criteria
Define specific, unambiguous thresholds — vague criteria lead to under- or over-activation. Examples:
- Unplanned outage of a Tier 1 system that has reached or exceeded the defined RTO threshold
- Confirmed ransomware, data breach, or cyber incident requiring business impact assessment
- Physical security incident affecting primary site operations
- Loss of key personnel — sudden unavailability of more than [X%] of critical operational roles
- Regulatory notification required within 24 hours or less
- Media/reputational incident requiring executive response or legal involvement
- Vendor/supplier failure that materially impacts a critical business process

### Crisis Management Team (CMT) Structure

| Role | Responsibility | Has Activation Authority |
|------|---------------|--------------------------|
| Crisis Commander (CMC) | Overall incident command; final decision authority; interface to board | Yes |
| Deputy Crisis Commander | CMC alternate; assumes full authority when CMC unavailable | Yes |
| Operations Lead | Coordinates operational response across business functions | Yes (when CMC/Deputy unavailable) |
| IT/DR Lead | Coordinates technical recovery; executes and reports on DRP | No |
| Communications Lead | Internal and external communications; media management | No |
| Legal/Compliance Lead | Regulatory notifications, legal exposure, privilege | No |
| HR Lead | Staff welfare, personnel communications, staffing decisions | No |
| Finance Lead | Financial impact tracking, insurance activation, cost authorization | No |
| BCM Coordinator | Administrative support; maintains situation log; tracks tasks | No |

**⚠️ Every role must have a named, trained alternate who has participated in at least one exercise.**

### Situation Log Requirements
During any CMT activation, maintain a real-time situation log:
- Timestamp of all decisions and who made them
- Timestamp of all notifications sent (regulatory, customer, staff, media)
- Timestamp of all key events (plan activation, system recovery milestones, staff notifications)
- All external commitments — to regulators, customers, media
- Action items with owner and due time

This is a legal and regulatory record. It must be accurate and complete.

### Integration with Security Incident Response (IR)

**Integration sequence during a cyber event:**
1. IR detects and classifies the incident
2. If BCM activation criteria are met → CMT activated in parallel (not after IR resolves)
3. IR Lead joins CMT calls; provides technical status and timeline to business recovery
4. CMT makes operational decisions (shutdowns, customer communications, regulatory notification) while IR executes containment
5. ServiceNow BCM recovery tasks track operational restoration; IR tracks technical remediation

**⚠️ Risk: Sequential Activation Delays Response**
Do not wait for IR to finish before activating BCM. Configure CMT criteria to explicitly include cyber incidents meeting defined severity thresholds.

### Regulatory Notification Requirements During Active Events

| Regulation | Notification Trigger | Required Timeline | Recipient |
|------------|---------------------|------------------|-----------|
| DORA (EU) | Significant ICT incident | Initial: 4 hrs; Intermediate: 72 hrs; Final: 1 month | Competent authority |
| HIPAA Breach (US) | PHI breach | 60 days from discovery | HHS OCR; affected individuals |
| NY SHIELD / State Laws | Personal data breach | 30-72 hours (varies by state) | State AG; individuals |
| PCI-DSS | Suspected cardholder data breach | Immediately | Payment brands; acquiring bank |
| SEC (public companies) | Material cybersecurity incident | 4 business days from materiality determination | SEC Form 8-K |
| CMS (healthcare) | Emergency declaration | Per CMS emergency program requirements | CMS regional office |

⚠️ Configure notification SLA tracking in ServiceNow Issues/BCM triggered from incident activation time.

### Crisis Communication Templates
Pre-build and store in ServiceNow BCM (accessible offline):
- Internal all-staff notification: incident confirmed; employee instructions; social media policy
- Executive/board notification: situation summary; business impact; actions taken; next update time
- Customer notification: service disruption or breach; what it means for them; steps being taken
- Regulatory notification: per applicable regulatory template with fixed fields pre-populated
- Media holding statement: minimal information, never speculative — "we are investigating"

---

## 7. Supply Chain & Third-Party Resilience

### Third-Party Dependencies in BCM
Third-party failure is consistently among the top causes of continuity events. BCM and TPRM must be formally integrated — BIA dependency mapping identifies which vendors are critical path, and TPRM validates whether those vendors have adequate BCM programs.

### Third-Party Criticality Tiers for BCM

| Tier | Definition | BCM Requirement |
|------|------------|----------------|
| **Tier 1 — Critical** | Vendor failure would trigger CMT activation or Tier 1/2 process disruption | Contractual BCM requirements; annual BCP evidence review; exercise participation where possible |
| **Tier 2 — Important** | Vendor failure causes significant but non-critical impact; workaround exists | Contractual BCM requirements; biennial BCP evidence review |
| **Tier 3 — Standard** | Vendor failure causes limited impact; easily substituted | Standard due diligence; no BCM-specific contractual requirement |

### Contractual BCM Requirements for Critical Vendors
Every Tier 1/2 vendor contract should include:
- Obligation to maintain a BCP and DRP covering services provided
- Annual testing evidence (tabletop minimum; full-scale for highest-criticality)
- Notification obligation: vendor notifies client within [X hours] of any event affecting service delivery
- Right to audit: client can review vendor BCM documentation upon request
- Alternate sourcing provisions: what happens if the vendor cannot recover within RTO

### Supply Chain Concentration Risk
Document situations where a single vendor or geographic region represents a dependency across multiple Tier 1 processes. Surface as operational risk records and ensure executive awareness.

### Integration with ServiceNow TPRM
- BIA third-party dependency data referenced in TPRM vendor profiles
- TPRM assessment questionnaires for Tier 1 vendors include BCM-specific sections (BCP existence, last test date, RTO/RPO for contracted services)
- TPRM monitoring triggers include vendor-disclosed incidents that may affect continuity

---

## 8. Recovery Task Management During Active Events

### ServiceNow BCM — Active Event Use
During an actual disruption, ServiceNow BCM's recovery task management provides real-time
coordination, task tracking, and complete documentation of the response.

### Active Event Record Structure
Each activated BCM event creates:
- **Event Record:** Tied to BCP/DRP; captures activation time, commander, scope, activation criteria met
- **Recovery Tasks:** Individual plan actions assigned to named owners with target completion times
- **Status Tracking:** Real-time task completion vs. plan timeline
- **Communications Log:** All crisis communications timestamped against the event record
- **Regulatory Notification Tracker:** Notification SLAs tracked against actual notification times
- **Issue Escalation:** Blocked tasks escalate to Issues for CMT decision

### Recovery Task Schema

| Field | Description |
|-------|-------------|
| Task ID | Linked to BCP/DRP step reference |
| Task Title | From plan procedure |
| Task Type | Technical / Operational / Communication / Regulatory |
| Owner | Named individual (not team) |
| Target Completion | Time from activation (e.g., T+2hrs) |
| Status | Not Started / In Progress / Complete / Blocked |
| Blockers | What is preventing completion; escalation flag |
| Actual Completion | Timestamp when marked complete |
| Notes | Real-time status updates |

### Post-Event Documentation
Every activation (including partial activations and near-misses) requires a post-event report:
- Activation timeline: detection, activation decision, CMT assembly
- Milestone achievement: when each RTO milestone was reached vs. target
- Regulatory notification log: when each required notification was sent
- CMT decisions log with rationale
- Actual RTO/RPO achieved vs. targets — and why gaps existed
- Gaps in procedures discovered during recovery
- Lessons learned → Issues → Plan updates with due dates

**⚠️ The post-event report is a regulatory artifact in regulated industries. It must be accurate, complete, and approved by the Crisis Commander.**

---

## 9. ServiceNow BCM Configuration — Full Scope

### Core Tables

| Table | Purpose |
|-------|---------|
| `sn_bcm_plan` | BCP/DRP/CMP plan record; linked to entity and plan type |
| `sn_bcm_bia` | BIA record per process or application entity |
| `sn_bcm_test` | Exercise/test record with schedule, scope, outcome |
| `sn_bcm_recovery_task` | Recovery task during active event |
| `sn_bcm_task_template` | Reusable task templates linked to plan procedures |
| `sn_bcm_event` | Active event record (activated plan instance) |
| `sn_bcm_dependency` | Dependency records linking processes/applications |

### Phase 1 — Minimum Viable Configuration

**Entity Framework prerequisites (must be complete before BCM configuration begins):**
- Process and application entities defined and classified
- Entity criticality tiering applied
- Business owners assigned to entities

**BIA configuration:**
- BIA record form with all required attributes (see Section 3 data model)
- Impact scoring at each time horizon (1hr, 4hr, 24hr, 72hr, 1 week) across all impact dimensions
- Recovery objective fields: RTO, RPO, MTPD, MBCO — both business-stated and technically validated
- Recovery gap field: delta between stated RTO and current capability
- Criticality tier assignment with scoring logic
- BIA review/approval workflow (Draft → Review → Approved)
- BIA status dashboard: coverage by entity, completion rate, RTOs by tier

**Plan configuration:**
- Plan record: type, scope, owner, version, review date, activation criteria
- Plan-to-entity linkage
- Plan document link field (authoritative document in SharePoint/intranet; metadata in ServiceNow)
- Plan approval and version control workflow
- Automated review schedule notification (60/30/7 days before review due)

**Exercise configuration:**
- Exercise record: type, scope, scenario, date, participants, objectives
- Exercise outcome capture: objectives met/partially met/not met
- AAR linkage
- Gap/issue creation workflow from exercise findings

**Phase 1 reporting minimum:**
- Critical process inventory with RTO/RPO coverage
- BIA completion rate by business domain
- Recovery gap analysis: processes where current capability ≠ stated RTO
- Plan coverage: which critical processes have approved plans
- Exercise status: scheduled, completed, overdue by plan
- Open issues from exercises by age and priority

### Phase 2 Enhancements

**Workflow automation:**
- Automated BIA scheduling and notification workflows by entity tier and review cycle
- BIA expiration alerts (flag records approaching 12-month threshold)
- Plan review automation — notifications to owners at 60/30/7 days before review due

**Crisis notification automation:**
- Integration with client's mass notification platform (API-driven from CMT activation record)
- Pre-built notification templates launched from event record
- Regulatory notification workflow with SLA tracking and escalation

**Recovery task automation:**
- Full workflow during active events: auto-assignment from plan, task progression, escalation triggers
- Real-time CMT dashboard: task status, blockers, milestone tracking vs. RTO
- Situation log automation: timestamped record of all updates and communications

**Integration enhancements:**
- CMDB integration: auto-populate application-to-infrastructure dependencies
- TPRM integration: vendor BCP status and third-party incident notifications surfaced into BCM
- Risk module: BIA criticality feeds entity risk profile; recovery gaps auto-create risk records
- SIR (Security Incident Response): cyber incident severity triggers BCM activation check

---

## 10. Program Governance & Maturity

### BCM Program Governance Structure
- **Executive Sponsor** (COO or equivalent): Program accountability; chairs annual program review
- **BCM Program Manager**: Day-to-day program ownership; plan maintenance; exercise calendar
- **Business Continuity Coordinators**: Per business domain; BIA facilitation; plan maintenance for their area
- **IT DR Lead**: DRP ownership; DR testing program; CMDB dependency maintenance
- **CMT (Crisis Management Team)**: As defined in CMP; activated only during events

### Program Review Cadence
- **Monthly:** BCM coordinator review — open issues, exercise schedule, BIA completeness
- **Quarterly:** BCM Program Manager review — plan currency, exercise status, KPI review
- **Annual:** Executive sponsor review — full program assessment, HVA refresh, BIA refresh, risk appetite alignment, investment decisions

### BCM KPIs / Dashboard Metrics

| KPI | Definition | Target |
|-----|------------|--------|
| BIA Coverage | % of Tier 1/2 critical processes with current BIA (< 12 months) | 100% |
| Plan Coverage | % of Tier 1/2 critical processes with approved, current BCP | 100% |
| Plan Currency | % of plans reviewed within required review cycle | > 95% |
| Exercise Completion Rate | % of planned exercises completed on schedule | > 90% |
| Open Exercise Issues (Overdue) | Count of open exercise issues overdue > 90 days | Zero |
| RTO Gap Coverage | % of Tier 1/2 processes with documented recovery gap analysis | 100% |
| Recovery Gap Remediation | % of Tier 1 recovery gaps with active remediation plan | 100% |
| Third-Party BCP Evidence | % of Tier 1 vendors with current BCP evidence on file | 100% |

### BCM Maturity Model

| Level | Description | Indicators |
|-------|-------------|------------|
| **1 — Initial** | Ad hoc, reactive; plans informal or nonexistent | No formal BCP; recovery by heroics; no BIA |
| **2 — Developing** | Some plans documented; BIA informal; limited testing | Plans in SharePoint; no formal exercise program; stale BIA |
| **3 — Defined** | Formal BCM program; BIA complete; plans documented and tested | Annual tabletops; plans reviewed; ServiceNow BCM configured |
| **4 — Managed** | Metrics-driven; integrated with Risk and TPRM; regular testing | KPI dashboard active; exercise findings drive improvement; TPRM integrated |
| **5 — Optimizing** | Continuous improvement; automated monitoring; regulatory benchmark | Automated BIA refresh; full CMDB integration; regulatory audit-ready |

---

## 11. Common Design Decisions

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| BIA unit of analysis | Business unit level | Process + application level | Process + application — business unit is too broad for actionable RTOs |
| Plan storage | Full plan text in ServiceNow | Metadata in ServiceNow; document in SharePoint/intranet | Metadata + key procedures in ServiceNow; full document linked from authoritative source |
| RTO capture | Business-stated only | Business-stated + technically validated + gap field | Capture all three; the gap is the most actionable output |
| BIA refresh cycle | Manual | Automated annual trigger | Automated — programs without automated refresh go stale |
| Exercise scheduling | Ad hoc | Calendar-driven with automated reminders | Calendar-driven; embed in BCM governance calendar at go-live |
| Crisis notification | Manual phone tree | Automated mass notification (client-selected, API-integrated) | Manual for Phase 1; integrate client's chosen platform in Phase 2 |
| Third-party resilience | Assessed separately in TPRM | Integrated into BIA dependency mapping | Integrate — BIA dependencies should surface TPRM gaps automatically |
| Active event management | External tool | ServiceNow BCM recovery task management | Native ServiceNow BCM (OOB-first); defer external integration to Phase 2 |
| DR architecture decision | During BCM/BIA phase | Prior to BCM engagement | Validate DR architecture before BIA — stated RTOs must be technically achievable |

---

## 12. Anti-Patterns

**Anti-Pattern: BIA as a One-Time Documentation Exercise**
BIA data becomes stale within 12-18 months without a structured refresh cycle. Configure automated annual BIA review triggers at program go-live, and require trigger-based reviews after major org or system changes.

**Anti-Pattern: RTOs Set by IT Without Business Input**
IT teams often set RTOs based on what is technically feasible, not what the business requires. Always start with business-stated RTOs, then validate against technical capability. The gap drives the investment case for DR improvements.

**Anti-Pattern: Plans That Live Only in SharePoint**
A BCP in a SharePoint folder nobody can access during an outage is not a BCP. Store critical procedure checklists and contact directories in a location accessible without primary systems — printed binders, offline copies, mobile-accessible platforms.

**Anti-Pattern: Testing Only the Best-Case Scenario**
Exercises designed to always succeed give false confidence. Design scenarios that expose gaps — partial system recovery, unavailability of key personnel, simultaneous failures, third-party supplier failure mid-exercise.

**Anti-Pattern: No Named Alternates for Crisis Roles**
Every named role in the CMP must have at least one trained alternate who has participated in an exercise. Single-person roles are a single point of failure in the response team itself.

**Anti-Pattern: BCM and IR Running in Parallel Without Coordination**
IR and BCM teams operating in silos during an event create conflicting instructions and slow recovery. CMT activation criteria must address cyber incidents, and IR and BCM leads should rehearse joint response at least annually.

**Anti-Pattern: Recovery Gap Analysis Without Investment Decisions**
Identifying that a Tier 1 process has a 72-hour recovery capability against a 4-hour RTO is only useful if the gap drives a decision. Document gaps in ServiceNow, surface as operational risks, and ensure executive ownership of the decision to invest or formally accept the risk.

**Anti-Pattern: No Plan Version Control**
Plans updated informally — overwritten without versioning — create situations where teams work from different versions during an event. Every plan update requires an approval step and a distribution record.

**Anti-Pattern: Skipping Third-Party Dependency Mapping**
Organizations consistently underestimate third-party dependencies. BIA facilitation must explicitly probe for vendor and supplier dependencies — processes whose stated RTO cannot be met if a critical vendor fails are incomplete.

**Anti-Pattern: Vague Activation Criteria**
Plans with criteria like "a significant disruption occurs" are not actionable. CMT members will hesitate to activate when uncertain, wasting critical response time. Write activation criteria as specific, observable thresholds with no room for interpretation.
