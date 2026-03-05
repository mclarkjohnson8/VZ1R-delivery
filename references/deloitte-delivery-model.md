# Deloitte Delivery Model Reference

## Table of Contents
1. Ready / Set / Go — Engagement Launch Approach
2. Governance Model
3. PMO Setup & Operating Rhythm
4. Deloitte Risk Panel
5. Stakeholder Communication Approach
6. Engagement Environment Strategy

---

## 1. Ready / Set / Go — Engagement Launch Approach

Deloitte's standard engagement launch model. The goal is to "hit the ground running" — PMO stood up,
governance model established, and stakeholders engaged on Day 1.

### READY — Pre-Kickoff (Deloitte-led preparation)
- Identify stakeholders and develop communication plan
- Develop weekly status report template and meeting cadence
- Finalize project plan and stakeholder communication materials
- Engage ServiceNow partners and client architects
- Determine ServiceNow environment strategy
- Align with client's ServiceNow governance and operating rhythms
- Establish Steering Committee composition and Deloitte Risk Panel

### SET — Kickoff Execution (Week 1)
- Issue communications to stakeholders and schedule standing working sessions
- Prepare baseline design workflows, wireframes, and functional demos
- Develop project management routines and templates
- Conduct Ways of Working session
- Stand up project governance (Steering Committee meeting 1)
- Deliver project kickoff presentation

### GO — Active Delivery
- Rapid, inclusive, and iterative design sessions per module (up to 5 client employees per use case)
- Reach key design decisions through facilitated demos and analysis
- Walk through design documentation and workflows for core team feedback
- Document material changes and open decisions
- Develop target state object model and core data model
- Apply configuration/integration standards with ongoing quality reviews
- Change analysis and user adoption planning
- Role-based training design

---

## 2. Governance Model

### Governance Structure

| Body | Composition | Cadence | Purpose |
|------|-------------|---------|---------|
| **Steering Committee** | Client executive sponsor + program leads; Deloitte engagement partner + program manager | Bi-weekly | Milestone review, escalation resolution, strategic decisions, budget and scope oversight |
| **Deloitte Risk Panel** | Deloitte senior leaders; internal quality and risk oversight | As needed (at major milestones) | Internal Deloitte governance; quality assurance; escalation support; delivery risk review |
| **Project Status Meeting** | PMs (client + Deloitte), workstream leads | Weekly | RAID review, milestone tracking, blocker resolution, sprint status |
| **Design / Working Sessions** | SMEs, workstream leads, Deloitte functional team | Per module (Imagine) | Requirements, design decisions, sign-off |
| **Sprint Ceremonies** | Delivery team | Per sprint cadence | Planning, standup, demo, retro |

### Decision Rights

| Decision Type | Who Decides | Who Approves | Who is Informed |
|--------------|-------------|--------------|-----------------|
| Scope change | PM (client) | Executive Sponsor | Steering Committee |
| Configuration design | Workstream Lead (Deloitte) | Functional Lead | PM |
| Customization approval (High/Very High) | Solution Architect + Client IT | Program Manager + Executive Sponsor | Steering Committee |
| Go-live authorization | PM (client) + PM (Deloitte) | Executive Sponsor | All stakeholders |
| Key design decisions (framework, platform) | Deloitte guidance + client leadership | Executive Sponsor | Steering Committee |
| Sprint commitment | Scrum team | Product Owner | PM |

### Escalation Path
1. Team level — resolve within sprint
2. Workstream Lead — resolve within 2 business days
3. Program Manager — resolve within 3 business days
4. Steering Committee — next scheduled session or emergency session
5. Deloitte Risk Panel — escalated by Deloitte engagement leadership for delivery risk issues

---

## 3. PMO Setup & Operating Rhythm

### PMO Standup at Engagement Launch
The PMO is operational before client kickoff. At minimum, the following must be in place on Day 1:
- Project plan baselined in agreed project tracking tool
- RAID log template distributed and populated with known items
- Status report template agreed with client PM
- All standing meeting invites sent and accepted
- Communication plan approved
- Document repository structure set up (SharePoint, Confluence, or agreed platform)

### Weekly Status Report Distribution
- Prepared by Deloitte PM; reviewed by engagement lead before distribution
- Distributed 24 hours before weekly status meeting
- Recipients: all Steering Committee members + workstream leads
- Contains: executive summary, health dashboard, accomplishments, next week plan, RAID highlights, decisions needed

### RAID Log Operating Rules
- Reviewed at every weekly status meeting — not quarterly, not ad hoc
- Every risk with High Impact + High Probability: documented mitigation AND contingency
- Issues open >5 business days without progress: escalate to Steering Committee agenda
- Assumptions violated: convert to Issues immediately; do not leave in Assumptions category

### Document Management Standards
- All deliverables version-controlled with date and version number in filename
- Draft documents distributed with clear "DRAFT — NOT FOR DISTRIBUTION" watermark
- Final documents require client sign-off before baseline; signed copy retained
- Configuration workbook maintained in real-time — not updated retrospectively

---

## 4. Deloitte Risk Panel

The Risk Panel is Deloitte's internal governance mechanism for engagement oversight. It is not a
client-facing body but its findings directly influence engagement delivery decisions.

### Risk Panel Triggers (when to convene)
- End of Imagine phase — before Deliver kickoff
- Significant scope change request
- At-risk delivery status sustained for >2 consecutive reporting periods
- Major technical architecture decision
- Go-live authorization
- Any event that could materially affect Deloitte's delivery quality or client relationship

### Risk Panel Inputs
- Current project status report
- RAID log
- Open key design decisions
- Budget and schedule variance analysis
- Technical architecture summary
- Client satisfaction signals

### Risk Panel Outputs
- Guidance on delivery approach adjustments
- Escalation decisions (when to involve Deloitte executive leadership with client)
- Quality review directives (when to conduct independent configuration review)

---

## 5. Stakeholder Communication Approach

### Communication Planning (Imagine Phase Activity)

**Stakeholder analysis dimensions:**
- Influence (High / Medium / Low) — ability to affect the project
- Interest (High / Medium / Low) — degree of impact from the project outcome
- Current sentiment (Champion / Supporter / Neutral / Skeptic / Blocker)
- Target sentiment (what we need them to be by go-live)

**Engagement strategies by profile:**
- High influence + High interest: Collaborate — active participants in design sessions and governance
- High influence + Low interest: Consult — keep informed; seek input on key decisions
- Low influence + High interest: Inform — regular status updates; include in demos
- Low influence + Low interest: Monitor — minimal engagement; ensure they have access to updates

### Communication Channels and Standards
| Channel | Purpose | Cadence | Owner |
|---------|---------|---------|-------|
| Weekly Status Report | Overall project health | Weekly | Deloitte PM |
| Steering Committee Deck | Executive milestone and decision updates | Bi-weekly | Deloitte PM + Engagement Lead |
| Sprint Demo | Working software showcase | Every 2 weeks | Workstream Lead |
| Design Workshop Outputs | Decision log and open items | Post each workshop | Functional Lead |
| RAID Log | Living risk and issue register | Continuous; reviewed weekly | Deloitte PM |
| Ad Hoc Escalation | Urgent issues requiring immediate action | As needed | PM or Engagement Lead |

---

## 6. Engagement Environment Strategy

### Standard Instance Configuration
The environment strategy is confirmed during the Ways of Working session and locked before Sprint 1.

| Environment | Purpose | Managed By | Refresh Cadence |
|------------|---------|-----------|-----------------|
| DEV | Active development and unit testing | Deloitte (with client IT) | As needed |
| TEST / QA | SIT and UAT | Client IT | Pre-SIT, pre-UAT |
| PROD | Live environment | Client IT | Post go-live authorization only |
| TRAINING (optional) | End-user training post-UAT | Client IT | Post-UAT |

### Instance Governance Rules
- All development in DEV only — no direct TEST or PROD modifications
- Update Sets: one per sprint per module; committed and exported at sprint close
- No admin accounts used for day-to-day development — scoped developer accounts only
- PROD access for Deloitte team: time-bounded, documented, revoked at engagement close
- ServiceNow release: minimum Zurich; Xanadu or current preferred

### ServiceNow Workspaces UI
Deloitte's standard is to use the Workspaces UI across all ServiceNow IRM modules. Classic UI
is not the delivery target. Confirm Workspaces availability in the client's ServiceNow instance
during the Ways of Working session.
