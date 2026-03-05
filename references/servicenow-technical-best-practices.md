# ServiceNow Technical Best Practices

## Certified Master Architect & Certified Technical Architect Reference

---

## Table of Contents

1. Platform Architecture & Instance Strategy
2. Data Model Design
3. Access Control & Security Model
4. Scripting Standards & Development Practices
5. Integration Architecture
6. Performance Engineering
7. Upgrade & Release Management
8. UI/UX & Portal Development
9. Reporting, Analytics & Performance Analytics
10. Flow Designer & Process Automation
11. CMDB & Asset Management
12. Platform Administration & Governance
13. Testing Strategy & Quality Assurance
14. DevOps, Source Control & Deployment
15. AI/ML & Now Intelligence
16. IRM/GRC Technical Architecture & Configuration

---

## 1. Platform Architecture & Instance Strategy

### Instance Topology
The standard enterprise topology is three instances: Development (DEV) → Test/UAT → Production. For large or regulated environments, extend to four: DEV → SIT → UAT → Production. Avoid "golden" or persistent sandbox instances that accumulate unmanaged changes — they become unreliable baselines and create upgrade risk.

**Multi-instance vs. single instance:**
- Single instance with scoped applications is strongly preferred over separate instances per business unit. Cross-application reporting, shared data models, and unified CMDB are significantly harder to achieve across instances.
- Separate instances are justified when: data sovereignty requirements prohibit co-mingling (e.g., EU data residency mandates), or when organizational separation is absolute (e.g., divested subsidiary).
- Sub-production instances should mirror production infrastructure as closely as possible — same plugins, same patches, same node count (or proportionally scaled). Environments that diverge from production in plugin set or customization level produce misleading test results.

### Scoped vs. Global Application Development
Always develop in a scoped application, not the global scope. This is non-negotiable for new development regardless of perceived simplicity.

**Reasons:**
- Scoped apps enforce namespace isolation — no accidental collisions with platform or other app artifacts
- Update sets respect scope boundaries; global scope changes bleed across everything
- App Repository and Source Control require scoped applications
- Upgrade safety: platform upgrades are less likely to conflict with scoped artifacts

**Exceptions for global scope:**
- Business rules, script includes, or UI actions that genuinely must operate cross-scope (e.g., intercepting a platform-level process)
- Even then, minimize global scope footprint and document every artifact placed there

### Node Architecture & Clustering
- Production instances run on multiple nodes behind a load balancer. Understand which node type handles what: application nodes process transactions; background nodes handle scheduled jobs and async processing.
- Do not schedule resource-intensive jobs during peak transaction hours. Use the `sys_trigger` table and job scheduling windows intentionally.
- Memory-intensive operations (large imports, complex reports, PA data collection) should be scheduled during low-traffic windows with awareness of other scheduled processes competing for the same node resources.

### Plugin Management
- Activate plugins in DEV first; validate behavior; promote through the pipeline before activating in Production.
- Review plugin dependencies before activation — some plugins activate additional plugins automatically. Understand the full activation footprint.
- Once activated, most plugins cannot be deactivated. Treat plugin activation as a permanent change.
- ⚠️ Activating plugins in Production without prior DEV/UAT validation is a change management risk that has caused production outages.

---

## 2. Data Model Design

### Table Design Principles
ServiceNow uses single-table inheritance. All records in an extended table are stored in the parent table (`sys_db_object`). This has significant implications:

- **Extend sparingly.** Creating deeply nested table hierarchies (Task → Incident → Custom Incident Subtype → Further Subtype) bloats the base table and degrades query performance.
- **Prefer extending Task** for work-item-style records. Task provides assignment, state, priority, SLA, and workflow integration out of the box. Do not create custom work tables that duplicate Task functionality.
- **Maximum recommended extension depth:** 3-4 levels from the root table. Beyond this, query performance degrades measurably and the data model becomes difficult to reason about.

### Field Design
- Use the most specific field type for the data being stored. Using a String(255) for a date, a boolean, or a reference wastes index space and eliminates type-specific query optimizations.
- Reference fields create a foreign key relationship and display as a typeahead lookup. Do not use a string field to store a sys_id manually — use a Reference field.
- **Choice fields** (dropdown lists) are appropriate for small, stable value sets. For large or changing value sets, use a reference field to a configuration table.
- Avoid creating fields on base tables (Task, CMDB CI, etc.) that are only used by one application. Use the scoped table extension or a related table to hold application-specific attributes.
- **Field naming:** prefix custom fields with the application scope prefix. This prevents naming collisions and makes origin identification straightforward during upgrades.

### Dictionary Overrides
When behavior on an extended table must differ from the parent (e.g., a field that is mandatory in Incident but not in Task), use a dictionary override rather than duplicating the field or using client scripts to enforce it. Dictionary overrides are upgrade-safe; client script enforcement of mandatory fields is fragile.

### Database Indexes
- ServiceNow automatically indexes Reference fields, the primary key (`sys_id`), and fields used in table relationships.
- Request custom indexes through the platform team (via `sys_db_index`) for fields used heavily in list filters, reports, or queries on large tables.
- Over-indexing degrades write performance. Index fields that appear in `WHERE` clauses of frequent queries — not every field.
- For IRM/GRC tables with large record volumes (risk assessments, attestation records), audit the query patterns before go-live and request indexes proactively.

### Import Sets and Data Transformation
- Never import directly into production tables from external sources without a staging table (Import Set table). Always use Transform Maps.
- Transform Maps should include field-level coalesce keys to prevent duplicates on re-import.
- Validate transform output in DEV with a representative data sample before running in Production.
- Large imports (>50,000 records) should use chunked processing via scheduled jobs, not a single synchronous import.

---

## 3. Access Control & Security Model

### ACL Architecture
Access Control Lists (ACLs) are the authoritative security mechanism for record-level, field-level, and operation-level access control. Never rely solely on UI-layer hiding (form views, client scripts) to enforce security — always back it up with ACLs.

**ACL evaluation order:**
1. Record-level ACL is evaluated first
2. If the record ACL passes, field-level ACLs are evaluated per field
3. Operation-level ACLs (read, write, create, delete) are evaluated per operation

**Best practices:**
- Keep ACL conditions as simple as possible. Complex ACL scripts (scripted conditions) execute on every record access — inefficient ACLs are a top source of platform performance degradation on large tables.
- Use roles as the primary ACL condition, not user attributes. Role-based access is cacheable; attribute-based conditions are evaluated at runtime.
- Avoid hardcoding user sys_ids or group sys_ids in ACL conditions. Reference roles or dynamic group membership instead.
- Test ACL coverage with an impersonation test matrix: cover every role combination relevant to the application before go-live.

### Role Design
- Design roles around job functions, not individual users. Users are assigned to roles; ACLs reference roles.
- Use role inheritance to compose complex permission sets from simple building blocks. A `sn_risk.manager` role might include `sn_risk.writer` and `sn_risk.reader` as contained roles.
- Avoid the `admin` role in ACL conditions except for administrative configuration tables. Admin bypass of all ACLs means any admin-level account can access everything.
- `security_admin` is required to create and modify ACLs. This role should be held by a very limited number of accounts and should not be a standing assignment.
- Regularly audit role assignments. Role bloat (users accumulating roles over time without removal) is a consistent audit finding in GRC implementations.

### Data Classification and Field-Level Security
For sensitive fields (SSN, PHI, financial data, executive compensation), implement field-level ACLs in addition to record-level ACLs. Sensitive fields visible at the record level but unprotected at the field level are a common vulnerability.

For IRM implementations: Risk scores, audit findings, and executive-level risk summaries may need field-level restrictions to prevent premature visibility before formal review processes complete.

### User Criteria vs. ACLs
User Criteria (used in Knowledge, Service Catalog, and some portal components) is a separate access control mechanism from ACLs. Do not confuse them:
- ACLs control read/write access to records and fields
- User Criteria controls visibility of catalog items, knowledge articles, and portal widgets
- Both layers may be needed for a fully secured implementation

### Elevated Privilege Scripts (gs.hasRole, gs.getUser)
When writing scripts that make security decisions, use `gs.hasRole()` for role checks rather than parsing user attributes. `gs.hasRole()` respects role inheritance; manual attribute parsing does not.

---

## 4. Scripting Standards & Development Practices

### Script Type Selection Guide

| Script Type | Runs | Use For |
|-------------|------|---------|
| Business Rule | Server (sync or async) | Data validation, field updates, record creation, cross-table operations |
| Client Script | Browser | Real-time UI feedback, form field interaction, conditional field visibility |
| UI Policy | Browser | Simple show/hide/mandatory rules with no conditional logic |
| Script Include | Server (called by other scripts) | Reusable server-side logic; never runs standalone |
| Flow Designer Action | Server | Reusable integration or logic steps within flows |
| Scheduled Job | Server (timed) | Periodic batch operations, data maintenance, report generation |
| Event / Event Queue | Server (async) | Decoupled processing; fire-and-forget notifications; heavy processing without blocking the transaction |

### Business Rule Design
- **Prefer async business rules** for operations that do not need to complete before the user's transaction returns (notifications, downstream record creation, logging). Synchronous rules block the transaction and degrade perceived performance.
- **Avoid querying in loops inside business rules.** A business rule that queries a table once per iteration of a 500-record import will execute 500 queries. Collect all needed data before the loop; process in bulk.
- **Prevent infinite loops:** Always check `current.isNewRecord()` and `current.operation()` before taking action. A business rule that triggers itself creates an infinite loop that will bring down a node.
- Use `previous` object to compare field changes: `current.state.changedTo('resolved')` is cleaner and more reliable than `current.state != previous.state && current.state == 'resolved'`.
- Business rules modifying fields on `current` should use `current.field.setValue()` rather than direct assignment when running after insert/update — direct assignment after database commit has no effect.

### Script Include Best Practices
- Script Includes are the correct place for reusable server-side logic. Any logic used in more than one Business Rule, Flow Action, or REST API handler belongs in a Script Include.
- Use class-based Script Includes (prototype pattern) rather than function-only includes. This enables inheritance, namespace organization, and unit testing.
- Script Includes set to `Client-callable` are accessible from client scripts and GlideAjax. Only expose Script Includes to the client when necessary — each client-callable Script Include is a potential attack surface if not properly secured.

### GlideRecord Best Practices
GlideRecord is the primary server-side API for querying and manipulating records.

```javascript
// CORRECT: Scoped query with field selection
var gr = new GlideRecord('sn_risk_definition');
gr.addQuery('active', true);
gr.addQuery('category', 'cyber');
gr.setLimit(500); // Always set a limit on unbounded queries
gr.query();
while (gr.next()) {
    // Process each record
}

// WRONG: No limit, no field scoping on large table
var gr = new GlideRecord('sn_risk');
gr.query(); // Will attempt to load entire table
```

- Always call `setLimit()` on queries where the result set could be large.
- Use `addEncodedQuery()` for complex filter conditions sourced from list views or report filters — it is more readable and directly mirrors what the platform generates.
- Use `getRefRecord()` to traverse a reference field to the related record rather than creating a second GlideRecord query.
- Never use GlideRecord in client scripts. Client-side GlideRecord calls trigger a synchronous server round-trip for every execution — use GlideAjax (Script Include) or REST API instead.

### Client Script Best Practices
- **Minimize DOM manipulation.** Use ServiceNow's supported APIs (`g_form`, `g_list`, `g_user`) rather than direct jQuery or DOM access. Direct DOM manipulation breaks in UI16+, mobile, and Service Portal.
- **Catalog client scripts use `g_form` as well** — the API is consistent with standard forms.
- **`onLoad` scripts should be fast.** Expensive operations in `onLoad` delay form rendering. If data must be fetched, use a GlideAjax call rather than a synchronous server round-trip.
- Use `g_form.setDisplay()` to show/hide fields; use UI Policies for simple display rules rather than client scripts — UI Policies are declarative and more performant.
- Avoid `setTimeout()` hacks to work around race conditions. If a race condition exists, fix the underlying sequencing problem.

### JavaScript Coding Standards
- Use `strict mode` declarations in Script Includes and complex Business Rules.
- Prefer `var` declarations at the top of function scope — ServiceNow's Rhino engine (pre-ES6 on older instances) does not support `let`/`const`. On Tokyo+ (V8 engine), `let`/`const` are available but verify instance engine version.
- Handle null/undefined explicitly. `gr.getValue('field')` returns null if the field is empty; code that doesn't handle null will throw errors silently swallowed by the platform.
- Log thoughtfully: `gs.log()`, `gs.info()`, `gs.warn()`, `gs.error()` all write to the application log. Excessive logging in high-frequency business rules creates log table bloat and is itself a performance issue.

---

## 5. Integration Architecture

### Integration Pattern Selection

| Pattern | When to Use | ServiceNow Mechanism |
|---------|-------------|---------------------|
| REST Inbound | External system pushes data to ServiceNow | Scripted REST API or Table API |
| REST Outbound | ServiceNow pushes or queries external system | REST Message + Flow Action or Business Rule |
| SOAP Inbound | Legacy systems with WSDL-based interfaces | Web Service Import Set or SOAP Scripted API |
| SOAP Outbound | Calling legacy external SOAP services | SOAP Message |
| MID Server | Outbound to on-premise or firewalled systems | MID Server with IntegrationHub |
| Event-Driven | Async processing; decoupled publish/subscribe | ServiceNow Event Queue or outbound webhook |
| File-Based | Batch data exchange (nightly imports) | Import Sets via FTP, SFTP, email attachment |
| Integration Hub Spokes | Certified connectors to SaaS platforms | IntegrationHub (licensed) |

### REST API Design (Inbound)
- Use **Scripted REST APIs** rather than the Table API for any integration requiring business logic, response shaping, or security beyond what the Table API provides. The Table API exposes raw table data — use it only for simple, trusted internal integrations.
- Version your Scripted REST API paths (`/api/scope/v1/endpoint`). Breaking changes require a new version; old versions stay active during client migration.
- Implement proper HTTP status code handling: 200 for success, 201 for created, 400 for bad request (invalid input), 401 for unauthorized, 404 for not found, 500 for server error. Return meaningful error messages in the response body.
- All inbound REST APIs should validate input before processing. Never pass user-supplied values directly into a GlideRecord query without sanitization.
- Rate limiting: use ServiceNow's REST API rate limiting policies for externally-exposed APIs.

### Outbound Integration Best Practices
- Store credentials in **Connection Aliases** (or MID Server credentials), never hardcoded in scripts or REST Message records.
- Implement retry logic for transient failures. Use the Event Queue to fire outbound calls asynchronously — a failed outbound call should not fail the user's transaction.
- Log integration payloads (request and response) to a custom log table for the first 90 days of any new integration. Debugging integration issues without payload history is significantly harder.
- Use **IntegrationHub** for SaaS-to-SaaS integrations where a certified spoke exists — spokes are maintained by ServiceNow and handle authentication lifecycle, versioning, and error handling in a standardized way.

### MID Server Architecture
- MID Servers should be deployed in HA pairs (two MID Servers per cluster) for any production integration that cannot tolerate downtime.
- Place MID Servers in the network zone where they need connectivity — a MID Server integrating with on-premise Active Directory should be in the on-premise network, not in a DMZ.
- MID Servers run as Windows Service or Linux daemon. Keep the underlying OS patched; MID Server security vulnerabilities are a common finding in security audits.
- Test MID Server connectivity from the platform UI (`Validate`) before configuring integrations that depend on it.

### CMDB Integrations
- Discovery, SCCM imports, cloud integrations, and manual imports all feed the CMDB. Conflicting data from multiple authoritative sources creates CI data quality problems.
- Use **Identification and Reconciliation Engine (IRE)** to define which source is authoritative per attribute per CI class. Without IRE configuration, last-write-wins — which produces unpredictable data.
- All CMDB population should go through the IRE pipeline, not direct GlideRecord inserts.

### Integration Governance
- Maintain an integration registry: every integration should be documented with source, target, protocol, frequency, data elements, owning team, and review date.
- Integrations should be reviewed annually for relevance, security posture, and performance impact.

---

## 6. Performance Engineering

### Query Performance
Query performance is the most common source of platform slowdowns. The root causes are almost always: missing indexes, unoptimized ACLs, or unbounded GlideRecord queries.

**Diagnosis tools:**
- **Stats.do** (`instance.service-now.com/stats.do`): Real-time node statistics; transaction rates; slow transaction log.
- **Transaction Log** (`syslog_transaction`): Records every transaction with execution time. Filter for transactions over 2 seconds to identify slow queries.
- **SQL Debug plugin** (DEV only): Exposes the SQL generated by GlideRecord queries. Use this to identify full table scans.
- **Performance Analytics Diagnostics:** PA-specific performance visibility.

**Optimization techniques:**
- Add indexes for fields used in frequent WHERE clauses on large tables.
- Rewrite ACL conditions that query related tables — each related-table query in an ACL condition executes for every record access.
- Use `setWorkflow(false)` in bulk update scripts where business rule re-execution is not needed (e.g., data migration).
- Use `autoSysFields(false)` in bulk inserts to prevent unnecessary sys field updates.
- For large data volumes, use `GlideRecordUtil` or `GlideMultipleInsert` for bulk operations.

### Scheduled Job Optimization
- Audit the scheduled job roster on Production quarterly. Disabled or orphaned jobs still consume scheduler overhead.
- Jobs that run frequently (every 5 minutes) on large tables without narrow filters are a consistent performance issue.
- Stagger high-intensity jobs. Avoid scheduling multiple heavy jobs at the same clock time (e.g., all jobs at midnight).
- Monitor job execution duration in `sys_trigger`. A job whose duration approaches its recurrence interval is effectively running continuously.

### UI Performance
- **Service Portal:** Widget server-side scripts execute for every portal page load. Uncached GlideRecord queries in widget controllers are a primary source of portal slowness. Use `$sp.getCatalogItem()` and platform caching APIs where available.
- **Form performance:** Excessive client scripts (particularly `onLoad` scripts with GlideAjax calls), large reference field sets, and deeply embedded related lists all degrade form load time.
- **List performance:** Lists with complex column configurations (many reference fields, many encoded conditions) are slower than simple column sets. Export/report-heavy list configurations should use dedicated report views.

### Instance Sizing and Capacity
- Work with ServiceNow support to review HI (Hosted Instance) metrics if experiencing consistent performance issues. Metrics include: CPU utilization, memory pressure, active threads, and database query volume.
- Large data growth (millions of records in core tables) eventually requires archiving or purging strategies. Define data retention policies before go-live for high-volume tables (audit logs, email logs, event queue history).

---

## 7. Upgrade & Release Management

### Upgrade Preparation
ServiceNow releases two major versions annually (Q1 and Q3). Patch releases occur approximately every 6 weeks. Proactive upgrade management is the single most important factor in maintaining a healthy instance.

**Pre-upgrade checklist:**
1. Review the upgrade release notes and known issues list for the target version
2. Run the **Upgrade Preview** tool on a sub-production clone — this identifies skipped or modified platform records before you upgrade
3. Review the **Skipped Changes** and **Customizations** report from Upgrade Preview — any customized OOB artifact needs a decision: accept platform version, retain customization, or merge
4. Review deprecated APIs and features in the target release. Deprecation warnings in current scripts become runtime errors in future releases.
5. Test all critical integrations and automations in the upgraded instance before production promotion
6. Schedule production upgrade during a low-traffic window with a tested rollback plan

### Upgrade Strategy for Customized Instances
- **Minimize OOB customizations.** Every modified platform artifact is a potential upgrade conflict. The fewer OOB customizations, the smoother upgrades become. This is the core argument for OOTB-first delivery methodology.
- When customization is unavoidable, document it in a customization registry with the business justification and planned review date.
- After each upgrade, remediate skipped changes within 90 days. Carrying forward unreviewed skipped changes across multiple upgrades compounds technical debt rapidly.

### Update Set Management
Update Sets capture configuration changes for promotion through the pipeline. They are the primary mechanism for moving changes from DEV to TEST to Production.

**Best practices:**
- One update set per story or change. Avoid bundling unrelated changes in one update set.
- Name update sets descriptively: `[AppName] - [Story/Change ID] - [Brief Description]`.
- Complete (close) update sets in DEV before retrieving in TEST. Incomplete update sets can be modified after retrieval, which creates promotion inconsistency.
- Retrieve → Preview → Commit in each environment. Always review Preview warnings before committing. Preview errors (dependency missing, collision) must be resolved before commit.
- Never manually edit records in TEST or Production that were configured in DEV. Manual edits outside update sets create configuration drift and break traceable promotion.

### Cloning Strategy
- Clone Production to sub-production environments on a regular cycle (monthly for active development; quarterly for stable instances).
- Use clone data preservers to protect sub-production-specific configuration (integration endpoints, email override rules, MID Server assignments) from being overwritten by the clone.
- Clone jobs are time-consuming (hours for large instances). Schedule clones during weekends and communicate blackout periods to development teams.

---

## 8. UI/UX & Portal Development

### Next Experience (UI Builder) vs. Service Portal
ServiceNow has two primary portal frameworks:

| Framework | Built With | Best For |
|-----------|-----------|---------|
| **Service Portal** | AngularJS, Bootstrap | Established; large widget library; most current implementations |
| **Next Experience (Workspace / UI Builder)** | React-based | New implementations; CMS; Agent Workspace; Configurable Workspace |

For new implementations on Washington DC+, Next Experience and UI Builder are the strategic direction. Service Portal remains fully supported but is not receiving major feature investment.

### Service Portal Development
- Build custom widgets in a scoped application, not the global scope.
- Widget HTML, CSS, Client Controller, and Server Script must all be considered when assessing performance. Server Script runs on every widget render.
- Use `sp-model` for two-way data binding; avoid jQuery DOM manipulation inside widget controllers.
- Service Portal pages are composed of containers, rows, columns, and widgets. Plan the page layout before building widgets — retrofitting layout after widget development is expensive.
- Test all portal pages in mobile viewport as well as desktop. Service Portal is responsive by default but custom widgets frequently break mobile layout.

### Workspace / Next Experience
- Configurable Workspaces are built on the Workspace framework and are the preferred UI for process owners and agents in modern ServiceNow implementations (CSM, ITSM, IRM).
- Use **UI Builder** to configure workspace experiences without custom code where possible — declarative configuration is upgrade-safe; coded overrides are not.
- Workspace list and form layouts are managed through Workspace configuration, not Form Designer. Understand the distinction — changes in Form Designer do not automatically propagate to Workspace views.

### Form Design
- Use **Views** to present different field subsets to different user populations. A technician view, a manager view, and a requester view can all reference the same form with different field visibility.
- Minimize required fields on initial submission forms. Every additional required field on submission reduces completion rates.
- Use **Form Sections** to logically group related fields. Sections can be collapsed, reducing cognitive load on complex forms.
- Place high-urgency fields (priority, assignment group, state) in the first section — visible without scrolling.

---

## 9. Reporting, Analytics & Performance Analytics

### Report Builder vs. Performance Analytics vs. Dashboards

| Tool | Purpose | Audience |
|------|---------|---------|
| **Report Builder** | Point-in-time reports from table data; exported or embedded | Operational users; analysts |
| **Dashboards** | Collections of reports and widgets; configurable per audience | Managers; executives |
| **Performance Analytics (PA)** | Time-series trending; KPIs; scores tracked over time | Program managers; executives |
| **Reporting API** | Programmatic report generation and delivery | Automated distribution; integration |

### Performance Analytics Design
PA Indicators are the core data structure. Each Indicator tracks a single metric over time by running a data collection job on a defined schedule.

**Design principles:**
- Define Indicators from the business question backward — "What does the stakeholder need to know?" → KPI definition → Indicator configuration.
- PA Scores are historical and immutable. Once a score is collected, it represents that moment in time. Design collection schedules to match the reporting cadence needed.
- **Breakdowns** slice Indicator scores by a dimension (assignment group, category, entity tier). Plan breakdowns during design — adding a new breakdown does not retroactively populate historical data.
- PA dashboards are built from Widgets, not Report Builder reports. The two systems use different rendering engines — mixing them in the same dashboard is possible but layout inconsistency is common.

### Report Governance
- Large or complex reports with full table scans on Production tables should be scheduled for off-hours delivery rather than rendered on-demand.
- Reports shared broadly should be owned by a service account, not an individual user. When users leave, their reports become orphaned.
- Report data is subject to ACLs — a report showing all incidents will only show incidents the running user can see. This is expected behavior, but must be communicated to report consumers.

---

## 10. Flow Designer & Process Automation

### Flow Designer vs. Workflow Editor
Workflow Editor (legacy) is still functional but is deprecated in favor of Flow Designer. All new automation should be built in Flow Designer.

| Capability | Flow Designer | Workflow Editor |
|------------|-------------|----------------|
| Low-code UI | Yes | Partial |
| Subflows (reuse) | Yes | No |
| Action library | Yes | No |
| IntegrationHub | Yes | Limited |
| Debugging | Execution Detail | Limited |
| Status | Strategic | Deprecated |

### Flow Design Best Practices
- Use **Subflows** for reusable logic — approval steps, notification sequences, SLA calculations. Build once; reference from multiple flows.
- Use **Actions** for integration steps. Action records are version-controlled, reusable, and testable independently of the parent flow.
- Keep flows readable. A flow with 40+ steps in a single sequence is a maintenance problem. Break complex processes into subflows with clear names.
- Flow execution is asynchronous by default. If synchronous execution is required (e.g., a flow that must return a value to a calling script), use flow execution context `synchronous` mode — but understand this blocks the calling thread.
- Always define **Error Handling** in flows that call external systems. An uncaught error in an outbound REST action will fail the entire flow silently.
- Test flows using **Flow Designer Test Mode** before activating in production. Test mode traces every step with input/output visibility.

### Approval Design
- Use the **Approval — User** or **Approval — Group** flow actions rather than building custom approval scripts. Platform-native approvals integrate with the Approval Workbench, notification framework, and Mobile Approvals.
- Set timeout/escalation rules on all approvals. An approval with no timeout can stall indefinitely if the approver is unavailable.
- For multi-stage approvals, use sequential subflows — Stage 1 → Stage 2 → Stage 3 — rather than embedding all approval steps in a flat flow. This makes individual stage modification possible without touching the parent flow.

### SLA Management
- SLAs are driven by **SLA Definitions** that evaluate conditions at record state changes. The SLA engine is a background process; near-real-time SLA tracking requires a short evaluation interval.
- Use **Task SLA** records to track individual SLA instances per record. These are what appear on forms and in reports.
- SLA breach thresholds (50%, 75%, 100%) drive notifications. Configure breach notifications for each stage — waiting for 100% breach to notify is operationally too late.
- Pause conditions (e.g., waiting on third party, business hours restriction) must be tested explicitly. Incorrectly configured pause conditions are a common source of SLA inaccuracy.

---

## 11. CMDB & Asset Management

### CMDB Foundations
The CMDB is the source of truth for IT assets, services, and their relationships. Every product suite that relies on CI data (ITSM, IRM, ITOM, BCM) depends on CMDB accuracy.

**Common CI Classes used in IRM/GRC context:**
- `cmdb_ci_appl` — Application CIs (business applications in scope for IRM assessments)
- `cmdb_ci_service` — Business Services (service entities)
- `cmdb_ci_server` — Server infrastructure
- `cmdb_ci_database` — Databases
- `cmdb_ci_hardware` — Physical hardware assets

### CMDB Health Score
ServiceNow provides a CMDB Health dashboard scoring the CMDB on completeness, compliance (attribute population), correctness (duplicates, stale records), and relationships. Target CMDB Health Score > 80% before using CMDB as a data source for IRM assessments or BCM dependency mapping.

A CMDB with a health score below 50% will produce unreliable BIA dependency data and risk assessment scope.

### Discovery
ServiceNow Discovery (licensed) automates CI population from the network. It uses MID Servers to probe, classify, and import CIs.

**Key principles:**
- Discovery should be the authoritative source for infrastructure CIs. Manual management of infrastructure CIs is not scalable.
- Configure Discovery schedules to run during off-hours to minimize network impact.
- Define the Discovery scope (IP ranges, CI classes, credentials) carefully before running in Production. Overly broad Discovery in complex networks can produce thousands of unmanaged CIs.

### Service Mapping
Service Mapping extends Discovery by identifying application-to-infrastructure dependencies, producing Business Service Maps. These maps are directly usable as BCM dependency data.

**IRM/BCM integration:** Service Maps from Service Mapping should be the source for application-to-infrastructure dependency data in the BCM BIA. Manual dependency collection in BIA workshops should be validated against Service Mapping outputs, not replace them.

### Asset vs. CI
Asset Management (Hardware Asset, Software Asset) and CMDB serve related but distinct purposes:
- **Asset record:** Tracks the financial and lifecycle state of a physical or software asset (procurement, cost, contract, disposal)
- **CI record:** Tracks the operational and relationship state of an IT configuration item (state, owner, connections to services and processes)

Most hardware assets have both an Asset record and a CI record linked. They should remain synchronized — a decommissioned CI should trigger asset retirement.

---

## 12. Platform Administration & Governance

### Instance Governance Model
Every ServiceNow instance should have a defined governance structure:

- **Platform Owner:** Executive accountable for the ServiceNow program; budget, strategic direction
- **Platform Architect:** Technical authority; approves architectural decisions; owns upgrade strategy
- **Application Owners:** Per product suite (ITSM, IRM, HR, etc.); accountable for their module's configuration
- **Change Advisory Board (CAB):** Reviews and approves production changes; includes Platform Architect and affected Application Owners
- **ServiceNow CoE (Center of Excellence):** Cross-functional team for standards, reuse, and platform health

Without governance, ServiceNow instances accumulate technical debt rapidly — competing configurations, duplicated automations, inconsistent data models.

### Configuration Management Database for ServiceNow (Meta-CMDB)
Maintain a registry of all custom artifacts: Business Rules, Script Includes, ACLs, Integrations, Flows, Scheduled Jobs. Each entry should include: purpose, owning application, author, last review date, and dependency map.

This registry is essential for upgrade impact analysis and for onboarding new platform team members.

### Email Configuration
- Configure email notification exclusions carefully. A misconfigured notification with no send condition on a high-volume table (e.g., Incident) can flood users with emails.
- All outbound email goes through the email log (`sys_email`). Review the email log in DEV before enabling production email to validate notification content and recipients.
- Configure notification digest intervals for high-frequency events. Real-time notification for every record update creates notification fatigue.

### Security Hardening
- Remove unused plugins. Each active plugin expands the attack surface.
- Disable the `demo` and default admin accounts before production go-live.
- Configure session timeout (recommend 8 hours maximum for standard users; 2 hours for admin accounts).
- Enable MFA for all administrative accounts.
- Review and restrict IP allowlists for API access if the platform supports it.
- Audit `sys_properties` for exposed credentials or sensitive configuration values.

### Instance Health Maintenance
- Monitor the **Upgrade Monitor** page to track your instance against ServiceNow's supported version window. Running an unsupported version (>2 versions behind current) means loss of Tier 1 support.
- Review the **Instance Security Center** monthly for flagged vulnerabilities and configuration drift.
- Run **Database Rotation** and **Log Purge** policies to prevent storage bloat. The default log table retention in ServiceNow is 90 days for most log tables — validate this against your compliance requirements.

---

## 13. Testing Strategy & Quality Assurance

### Test Architecture
A complete testing strategy for ServiceNow includes five layers:

| Layer | What It Tests | Tool |
|-------|-------------|------|
| Unit | Individual scripts, Script Includes | ATF (Automated Test Framework) |
| Integration | End-to-end flows, integrations, cross-table behavior | ATF + manual |
| Regression | That existing functionality wasn't broken by a change | ATF suite run on every deployment |
| UAT | Business process validation from end-user perspective | Manual; business stakeholders |
| Performance | System behavior under load | Synthetic load testing; transaction monitoring |

### Automated Test Framework (ATF)
ATF is ServiceNow's native test automation framework. All platform teams should maintain a regression test suite.

**ATF best practices:**
- Write tests for every custom Business Rule, Flow, and integration endpoint — not just happy paths.
- Tests should be idempotent: running the same test twice should produce the same result. Use test data cleanup steps to reset state.
- ATF tests run in a test transaction that is rolled back after completion — they do not pollute production data if configured correctly.
- Include negative test cases: test that a user without the required role cannot access a restricted record; test that invalid input returns the expected error.
- Run the full ATF regression suite in the promoted-to environment (TEST, UAT) before every production deployment.

### UAT Management
- UAT scripts should map directly to business process steps, not to technical configurations. Testers should validate that the system does what the business needs — not that the configuration matches a spec.
- Track UAT defects in ServiceNow itself (Defect or Enhancement records in SDLC or custom table). This provides a complete audit trail of test outcomes.
- Define a **UAT exit criteria** before testing begins: what pass rate (% of test cases passing) is required before go-live approval? For IRM implementations, target 100% on critical-path test cases.
- Separate UAT from SIT. System Integration Testing validates that technical components work together; UAT validates business requirements. Running both simultaneously degrades the quality of both.

---

## 14. DevOps, Source Control & Deployment

### Source Control Integration
ServiceNow supports Git-based source control (GitHub, GitLab, Azure DevOps Repos) for scoped application development via the **App Engine Studio** and **Studio IDE**.

**Source control workflow:**
1. Developer creates a feature branch from `main`
2. Configuration is captured in the scoped app as source files (XML/JSON)
3. Pull request review triggers automated ATF runs
4. Merge to `main` triggers pipeline promotion (DEV → TEST → UAT → PROD)

This flow requires the **App Engine** license tier. For non-App Engine environments, Update Sets remain the primary promotion mechanism.

### CI/CD with ServiceNow
- **ServiceNow DevOps** (licensed) integrates with external CI/CD tools (Jenkins, Azure DevOps, GitHub Actions) to trigger ATF test runs, enforce change gates, and log pipeline events in the ServiceNow Change module.
- For teams without ServiceNow DevOps, a manual CI/CD discipline using Update Sets with defined review checkpoints at each pipeline stage achieves similar outcomes.

### Change Management Integration
All production changes should go through the ServiceNow Change module — including platform configuration changes made by the platform team itself. This is frequently skipped in practice and is consistently cited in audit findings.

- Automate emergency change tracking — even if a change was deployed in an emergency, log it as an emergency change with post-deployment documentation.
- Use Change Tasks to break complex changes into individual steps with owners, making rollback planning explicit.

---

## 15. AI/ML & Now Intelligence

### Now Intelligence Capabilities
ServiceNow's AI/ML capabilities are embedded across product suites. Understand what is available before recommending custom ML development.

| Capability | Description | Applicable Products |
|------------|-------------|---------------------|
| **Predictive Intelligence** | Classification, similarity, clustering on record data | ITSM, CSM, HR, IRM |
| **Virtual Agent** | NLU-based conversational AI; ticket deflection | ITSM, HR, CSM |
| **AI Search** | Semantic search across Knowledge, Catalog, and records | All |
| **Now Assist (GenAI)** | Generative AI: case summarization, field suggestions, resolution drafts | ITSM, CSM, HR (licensed) |
| **Document Intelligence** | AI-based document field extraction | HR, Finance, Procurement |
| **Process Mining** | Process analysis from historical event data | Cross-suite |

### Predictive Intelligence for IRM
Predictive Intelligence can be applied in IRM contexts:
- **Risk classification:** Classify incoming risk records by category/subcategory based on description text
- **Issue routing:** Predict assignment group for issues based on historical routing patterns
- **Attestation anomaly:** Flag anomalous attestation responses (e.g., a control consistently attested as passing that has historically failed)

**Caution:** ML models require sufficient training data (minimum 400-800 labeled records per class) to produce reliable predictions. Do not activate Predictive Intelligence on tables with insufficient historical data — the model will produce low-confidence, unreliable classifications.

### Now Assist (Generative AI)
Now Assist (built on large language models) is available as a licensed add-on. Current capabilities include:
- Case and incident summarization
- Resolution note generation
- Search result augmentation

For IRM use cases: risk register summarization, audit finding narrative drafts, and compliance posture summaries are candidate use cases as Now Assist coverage expands to IRM modules.

⚠️ Now Assist requires careful data governance review before activation. Ensure that data sent to the LLM backend complies with the organization's data classification and residency requirements.

---

## 16. IRM/GRC Technical Architecture & Configuration

This section translates platform-level best practices into IRM-specific guidance. Cross-reference with the module-specific reference files for full configuration detail.

### IRM Data Model Overview

IRM is built on the ServiceNow platform's scoped application model. All IRM tables extend from platform base tables, inheriting their behaviors, ACLs, and workflow capabilities.

**Core IRM table relationships:**

```
sn_grc_item (Base GRC Item)
├── sn_risk_definition (Risk Definition — reusable risk type)
│   └── sn_risk (Scoped Risk — risk instance per entity)
│       └── sn_risk_assessment (Point-in-time assessment)
├── sn_compliance_control (Control)
│   └── sn_compliance_attestation (Attestation per entity)
├── sn_audit_engagement (Audit Engagement)
│   └── sn_audit_task (Audit Workpaper/Test)
│       └── sn_audit_finding (Finding)
└── sn_issue_m2m_issue (Issue)
    └── sn_issue_task (Remediation Task)

sn_grc_profile (Entity Profile — extends Entity record)
└── Links risk, control, audit, and issue records to a specific entity
```

### Entity Framework as the Technical Foundation
Every IRM module operates against entities. The entity hierarchy must be technically correct before any module configuration begins.

**Technical entity configuration checklist:**
- Entity type records defined in `sn_grc_entity_class` with correct parent-child hierarchy
- Entity class profile type mapping: which profile type (risk, compliance, audit) applies to which entity class
- Entity tier assignment: tier field populated or derived via business rule from entity attributes
- Profile auto-creation: configure whether entity profiles are created automatically on entity activation or require manual creation
- Relationship types: define allowed parent-child relationship types to enforce hierarchy integrity

**⚠️ Technical risk:** Changing entity class hierarchy after risk and control records have been created requires data migration. Entity class is a key attribute on scoped risks and attestation records. Validate entity design in a data model design document before Sprint 1 begins.

### ACL Architecture for IRM
IRM ships with a layered role model. Understand the hierarchy before customizing:

| Role Pattern | Example | Scope |
|-------------|---------|-------|
| `sn_risk.admin` | Risk module admin | Full read/write on all risk records |
| `sn_risk.manager` | Risk manager | Read/write on assigned entity risks |
| `sn_risk.analyst` | Risk analyst | Create/update assessments; limited risk definition access |
| `sn_risk.reader` | Read-only consumer | Read access to risk records |
| `sn_grc.user` | Cross-module base | Base read access across IRM modules |

**IRM-specific ACL considerations:**
- Executive risk summaries and residual scores may need field-level ACLs if the client has sensitivity around pre-approved risk data visibility.
- Attestation records should restrict write access to the assigned attestor and their manager. Configure attestation-specific ACLs on `sn_compliance_attestation` to prevent unauthorized attestation responses.
- Audit findings should be restricted from unrestricted read access until formally issued. Configure draft finding ACLs separately from issued finding ACLs.

### IRM Business Rule Patterns
Common business rule patterns in IRM implementations:

**Auto-issue creation on risk threshold breach:**
```javascript
// Business Rule: After Update, async
// Table: sn_risk (Scoped Risk)
// Condition: current.residual_score.changedValue() && current.residual_score > risk_appetite_threshold

(function executeRule(current, previous) {
    if (current.residual_score > gs.getProperty('risk.appetite.threshold', 15)) {
        var issue = new GlideRecord('sn_issue_m2m_issue');
        issue.initialize();
        issue.short_description = 'Risk threshold breach: ' + current.name;
        issue.risk = current.sys_id;
        issue.profile = current.profile;
        issue.priority = mapRiskScoreToPriority(current.residual_score);
        issue.insert();
    }
})(current, previous);
```

**BIA criticality tier auto-assignment:**
```javascript
// Business Rule: Before Insert/Update, sync
// Table: sn_bcm_bia
(function executeRule(current, previous) {
    var maxImpact = Math.max(
        parseInt(current.impact_1hr) || 0,
        parseInt(current.impact_4hr) || 0
    );
    if (maxImpact >= 4) current.criticality_tier = '1';
    else if (maxImpact >= 3) current.criticality_tier = '2';
    else if (maxImpact >= 2) current.criticality_tier = '3';
    else current.criticality_tier = '4';
})(current, previous);
```

### Performance Considerations Specific to IRM
IRM tables with the highest record volumes and therefore highest performance sensitivity:

| Table | Volume Driver | Optimization |
|-------|-------------|-------------|
| `sn_compliance_attestation` | One per control per entity per period | Index on `profile`, `control`, `state`, `due_date` |
| `sn_risk_assessment` | One per scoped risk per assessment cycle | Index on `risk`, `state`, `assessment_date` |
| `sn_audit_task` | One per test step per engagement | Index on `engagement`, `state`, `assigned_to` |
| `sn_grc_profile` | One per entity (can be large for broad entity scope) | Index on `entity_class`, `tier`, `active` |

For clients with large entity scopes (500+ entities, multiple IRM modules active), attestation campaigns can generate tens of thousands of records simultaneously. Test attestation campaign creation performance in an environment with production-representative data before go-live.

### IRM Integration Patterns

**GRC API:** ServiceNow exposes a GRC REST API for external systems to create, read, and update GRC records. Use this for:
- Feeding risk events from external monitoring systems (SIEM → IRM Issue or Risk record)
- Syncing control attestation status to a third-party audit tool
- Publishing risk register data to executive dashboards built outside ServiceNow

**Integration Hub for IRM:**
- **Vulnerability Response integration:** VR findings can auto-create Issues in IRM for compliance gap tracking
- **CMDB-to-Entity sync:** Application CIs from CMDB can auto-create or update IRM entity records — ensuring IRM scope remains aligned with the actual IT landscape
- **Third-party data feeds:** TPRM continuous monitoring can be fed by external vendor risk data sources via Integration Hub spokes or custom REST integrations

### IRM Upgrade Considerations
IRM is a highly customized domain. Specific upgrade risk areas:

- **Scoring methodology changes:** Platform-delivered changes to risk scoring logic can affect existing residual scores. Review risk-related release notes before every upgrade.
- **ACL changes in OOB IRM roles:** Platform updates occasionally modify OOB role definitions. After upgrading, validate that customized ACLs still produce the expected access outcomes.
- **Flow Designer changes:** IRM ships with OOB flows for notifications, approvals, and record lifecycle. If any OOB flow has been customized, it will appear as a skipped change on upgrade. Review all IRM flows in the upgrade preview report.
- **PA Indicator changes:** If ServiceNow modifies an OOB PA Indicator that has been customized, historical scores may become inconsistent. Review all customized PA Indicators post-upgrade.

### IRM-Specific Performance Analytics Design
Key IRM KPIs that should be tracked as PA Indicators (not just report counts):

| KPI | Table | Indicator Type |
|-----|-------|---------------|
| Critical risks by entity tier | `sn_risk` | Count — filtered |
| Residual risk score trend | `sn_risk_assessment` | Average score — trending |
| Control attestation pass rate | `sn_compliance_attestation` | % passed — trending |
| Overdue attestations | `sn_compliance_attestation` | Count — filtered |
| Open audit findings by age | `sn_audit_finding` | Count — breakdowns by age bucket |
| Issue mean time to remediation | `sn_issue_m2m_issue` | Average duration — trending |
| BIA completion rate | `sn_bcm_bia` | % complete — filtered |
| Open exercise findings | `sn_bcm_test` linked to Issues | Count — filtered |

All KPIs should have configured Targets and Thresholds in PA so that visual indicators (green/yellow/red) display on dashboards without requiring interpretation.

### IRM Technical Deployment Checklist
Before go-live on any IRM module:

- [ ] Entity hierarchy finalized and approved; all entities loaded with correct tier and class
- [ ] Role assignments tested end-to-end for each persona (admin, manager, analyst, reader, attestor)
- [ ] ACL coverage validated via impersonation testing matrix
- [ ] All OOB flows reviewed; customizations documented
- [ ] ATF regression suite created and passing for all custom scripts and flows
- [ ] PA Indicators configured with targets, thresholds, and collection schedule
- [ ] Notification templates tested with realistic data (not just "Test" buttons)
- [ ] SLA definitions tested with pause/resume scenarios
- [ ] Data volumes in TEST environment representative of production at 12-month scale
- [ ] Index requests submitted for high-volume tables
- [ ] Integration endpoints tested with production-equivalent credentials and data
- [ ] Upgrade Preview run and all skipped changes reviewed
- [ ] Admin account security hardened (MFA, session timeout, no shared credentials)
- [ ] Post-go-live monitoring plan defined (who reviews slow transaction log, PA alert thresholds)
