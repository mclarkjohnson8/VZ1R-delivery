# Policy & Compliance Management (PCM) Reference

## Table of Contents
1. Module Overview
2. PCM Data Model
3. Policy Hierarchy Design
4. Control Framework Design
5. Attestation Configuration
6. Regulatory Framework Mapping
7. Common Configuration Decisions
8. Anti-Patterns

---

## 1. Module Overview

PCM operationalizes the policy lifecycle (create, publish, attest, review, retire) and control
management (define controls, map to policies/regulations, assess effectiveness, track attestations).

**Primary Use Cases:**
- Enterprise Policy Management
- Control Library Management
- Regulatory Compliance Mapping (NIST, ISO 27001, COBIT, PCI-DSS, HIPAA, SOX, state privacy laws)
- Control Attestation and Self-Assessment
- Compliance Posture Reporting

---

## 2. PCM Data Model

### Core Tables
- `sn_compliance_policy` — Policy document record
- `sn_compliance_policy_statement` — Individual policy statements within a policy
- `sn_compliance_control` — Control definition (the "what we do to comply")
- `sn_compliance_control_objective` — Higher-level grouping of related controls
- `sn_compliance_attestation` — Attestation record (did this control pass/fail for this entity?)
- `sn_compliance_citation` — Regulatory citation (maps controls to external standards)

### Hierarchy
```
Regulatory Framework / Standard (e.g., NIST CSF)
└── Policy (e.g., Information Security Policy)
    └── Policy Statement (e.g., "All data at rest must be encrypted")
        └── Control Objective (e.g., Data Protection)
            └── Control (e.g., AES-256 encryption on all databases)
                └── Attestation (entity-specific: did Business Unit A comply?)
```

---

## 3. Policy Hierarchy Design

### Policy Structure Principles
- Policies should be technology-agnostic; procedures contain implementation specifics
- Each policy should map to one primary domain (security, privacy, operational, etc.)
- Policy statements are the unit of compliance mapping — not the policy itself
- Keep policy statements specific enough to attest (yes/no or maturity-scored)

### Policy Lifecycle States (OOB)
Draft → Review → Approved → Published → Under Review → Retired

### Policy Ownership Model
- **Policy Owner:** Accountable for policy content and annual review (executive level)
- **Policy Author:** Responsible for drafting and maintaining (operational level)
- **Control Owner:** Accountable for implementing and evidencing the control
- **Control Tester:** Performs effectiveness testing or attestation

---

## 4. Control Framework Design

### Control Library Principles
- Rationalize before building — clients often have controls in spreadsheets, GRC tools, and audit trackers that overlap significantly. Deduplicate before loading into ServiceNow.
- One control, many mappings — a single control can map to multiple policy statements and multiple regulatory citations
- Control granularity: Controls should be specific enough to test. "Manage access" is not a control. "Quarterly user access reviews are performed and evidenced by department managers" is a control.

### Control Attributes to Configure

| Attribute | Description |
|-----------|-------------|
| Control ID | Unique identifier; use client's existing numbering if they have one |
| Control Name | Short descriptive label |
| Control Description | Full specification of what the control requires |
| Control Type | Preventive / Detective / Corrective / Deterrent |
| Control Category | Administrative / Technical / Physical |
| Frequency | Continuous / Daily / Weekly / Monthly / Quarterly / Annual / Ad hoc |
| Owner | Named individual or role |
| Testing Method | Self-attestation / Manager attestation / Independent testing |
| Applicable Entities | Which entity classes/tiers this control applies to |
| Regulatory Mappings | External standards this control satisfies |

### Control Taxonomy (Recommended Top-Level Categories)
- Access Control
- Data Protection & Encryption
- Vulnerability & Patch Management
- Change Management
- Incident Management
- Business Continuity
- Third Party Management
- Privacy & Data Handling
- Audit & Logging
- Physical Security
- HR & Training
- Legal & Regulatory

---

## 5. Attestation Configuration

### Attestation Design Decisions

**Attestation Type:**
- **Yes/No (Binary):** Control is in place or it is not. Simplest; lowest adoption friction.
- **Maturity-Scored:** Rate control maturity on a 1-5 scale (Initial → Optimized). More nuanced; more training required.
- **Evidence-Required:** Attestor must attach evidence. Strongest; highest effort.

**Recommendation:** Start with Yes/No + comments field for Phase 1. Add evidence requirements and
maturity scoring in Phase 2 once adoption is established.

**Attestation Scheduling:**
- Driven by control frequency attribute (monthly, quarterly, annual)
- Entity tier determines which entities attest — Tier 1/2 before Tier 3/4
- Cascade scheduling: start attestation cycles 30 days before due date

**Escalation Configuration:**
- Reminder notifications at: 14 days, 7 days, 2 days before due
- Escalation to manager at: 1 day after due date
- Escalation to workstream lead at: 5 days after due date
- Failed attestation → auto-create Issue (configure severity mapping)

### ⚠️ Risk: Attestation Fatigue
Overloading attestors (>20 attestations per quarter) drives rubber-stamping and false positives.
Scope attestations by entity tier and control criticality. Reserve high-frequency attestation
for Tier 1 entities and high-risk controls only.

---

## 6. Regulatory Framework Mapping

### Supported Citation Frameworks (OOB + Common)
- NIST Cybersecurity Framework (CSF) 2.0
- NIST SP 800-53
- ISO/IEC 27001:2022
- COBIT 2019
- PCI-DSS v4.0
- HIPAA Security Rule
- SOX ITGC
- GDPR / CPRA / State Privacy Laws
- FFIEC CAT
- FedRAMP

### Mapping Approach
1. Import citation library (ServiceNow provides OOB citation content for major frameworks)
2. Map client controls to citations (many-to-many relationship)
3. Map citations to policy statements
4. Validate coverage — identify gaps where regulatory requirements have no corresponding control
5. Gap register: document unmapped citations as compliance gaps with remediation plans

### ⚠️ Risk: Framework Proliferation
Clients want to map to every framework simultaneously. Scope framework mapping carefully —
each additional framework multiplies the attestation and maintenance burden. Prioritize by
regulatory obligation and risk exposure.

---

## 7. Common Configuration Decisions

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Control library source | Import from client's existing spreadsheet | Build fresh in ServiceNow | Import and rationalize — never build from scratch if a library exists |
| Attestation method | Self-attestation by control owner | Manager attestation | Self-attestation with manager escalation workflow |
| Policy storage | Full policy text in ServiceNow | Linked to external policy repository | Link to authoritative source (SharePoint, intranet); maintain metadata in ServiceNow — do not recommend third-party policy management tools unless the client has an existing investment and explicit requirement to integrate |
| Citation mapping | Pre-built OOB citation content | Custom citations | Use OOB where available; custom only for proprietary frameworks |
| Control testing integration | PCM only | PCM + Audit module integration | Integrate with Audit for independent testing; PCM for self-attestation |

---

## 8. Anti-Patterns

**Anti-Pattern: Uploading Policy PDFs as Attachments and Calling It Done**
Attaching PDFs gives you a document repository, not a compliance program. Policy statements must
be parsed into discrete, attestable items in the platform.

**Anti-Pattern: One Attestation Per Policy**
Attestors end up rubber-stamping an entire policy as "compliant" without evaluating individual
controls. Break attestations down to the control level.

**Anti-Pattern: Building the Control Library During Sprints Without Pre-Rationalization**
Trying to rationalize 2,000 spreadsheet controls during sprint configuration is a delivery killer.
Control rationalization is a Imagine phase activity. It must be complete before PCM build starts.

**Anti-Pattern: No Control Owner Assignment at Launch**
Controls without named owners have no accountability. Before go-live, every in-scope control must
have a named owner. Use entity owner as the fallback only temporarily.

**Anti-Pattern: Recommending a Third-Party Policy Management Tool**
ServiceNow's native PCM module covers the full policy lifecycle (authoring, approval, publication, attestation, review, retirement) out of the box. Do not recommend external policy management platforms (e.g., dedicated GRC or policy authoring tools) unless the client has an existing license, an active integration requirement, or an explicit business need that OOB PCM cannot satisfy. The default position is to leverage native ServiceNow capabilities first.
