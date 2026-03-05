# ServiceNow Technical Best Practices Reference
## Verizon OneRisk TPRM | Deloitte | ServiceNow IRM (Zurich)

---

## Overview

This document captures the ServiceNow technical best practices that govern all configuration and development work on the Verizon OneRisk engagement. These standards align with Deloitte's ServiceNow Center of Excellence (CoE) guidelines, ServiceNow's Now Create methodology, and the Global Elite partnership standards.

---

## Platform Architecture Principles

### 1. Scoped Application Always

All customization must be in a **scoped application**. Global scope is last resort and requires explicit justification.

- **Why**: Scoped apps are upgrade-safe, portable, and isolate custom logic from platform updates
- **Verizon**: All IRM customizations are in the `x_deloitte_onerisk` scoped application
- **Never**: Create custom tables, scripts, or fields in global scope without ARB approval

### 2. Standard Instance Topology

```
DEV → TEST/UAT → PROD
```

- Sub-production instances must mirror PROD in plugin set and patch level
- No exceptions: if PROD has a plugin, TEST and DEV must have it
- Patch level sync: coordinate with Verizon IT for quarterly patch windows

### 3. MID Server Standards

- Production integrations require MID Server **HA pairs** (high availability)
- MID Servers must be domain-joined where required by the target system
- MID Server version must match or be within one release of the ServiceNow instance
- Health monitoring via OOB MID Server health dashboard

---

## Integration Standards

### Scripted REST APIs (Inbound)

For any inbound integration requiring business logic:

```javascript
// Example: Avetta data ingestion endpoint
(function process(/*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {
    var body = request.body.data;
    // Validate input
    if (!body || !body.vendor_id) {
        response.setStatus(400);
        response.setBody({ error: 'Missing required field: vendor_id' });
        return;
    }
    // Business logic
    // ...
    response.setStatus(200);
    response.setBody({ status: 'success' });
})(request, response);
```

**Standards:**
- Always validate input (required fields, data types, format)
- Return meaningful HTTP status codes (200, 201, 400, 401, 403, 404, 500)
- Log all inbound requests for first 90 days in production
- Credentials in Connection Aliases — never hardcoded

### Outbound REST Integrations

```javascript
// Example: REST message call pattern
var sm = new sn_ws.RESTMessageV2('Avetta_API', 'get_vendor_data');
sm.setStringParameterNoEscape('vendor_id', vendorId);
sm.setMutualAuth('Avetta_MutualAuth'); // Use stored credential
var response = sm.execute();
var httpStatus = response.getStatusCode();
```

**Standards:**
- Use REST Message records (not hardcoded URLs)
- Credentials in Connection Aliases or MID Server credential records
- Implement retry logic for transient failures (max 3 retries with exponential backoff)
- Log request/response for first 90 days
- Timeout: 30s default; 120s max for large payloads

---

## Scripting Standards

### Business Rules

| Principle | Standard |
|-----------|---------|
| **When to run** | Use "after" not "before" unless field changes require real-time validation |
| **Conditions** | Always use the "Filter Conditions" builder — not a script condition — unless complex logic requires it |
| **Scope** | Limit to table-specific logic; never cross-table queries in before Business Rules |
| **Performance** | No unbounded GlideRecord queries; always use setLimit() |

```javascript
// BAD: Unbounded query
var gr = new GlideRecord('sn_risk_risk');
gr.query(); // Will scan entire table

// GOOD: Scoped query with limit
var gr = new GlideRecord('sn_risk_risk');
gr.addQuery('active', true);
gr.addQuery('risk_owner', current.assigned_to);
gr.setLimit(100); // Explicit limit
gr.query();
```

### Script Includes

- One class per Script Include
- Document public methods with JSDoc
- Use `gs.log()` sparingly; use `gs.debug()` for verbose logging (auto-filtered in PROD)
- No hard-coded sys_ids — use reference lookups or configuration records

### Client Scripts

- Keep client-side logic minimal — validate on server
- Use `g_form.getControl()` sparingly; prefer `g_form.getValue()`
- No GlideAjax calls in `onLoad` without UX justification (impacts form load performance)

---

## Performance Standards

### Common Performance Issues

| Issue | Cause | Solution |
|-------|-------|---------|
| Slow list views | Missing indexes on large tables | Request custom index via ServiceNow support |
| Slow ACL evaluation | Complex ACL conditions with subqueries | Simplify conditions; use role-based ACLs |
| Slow form load | Multiple client script GlideAjax calls | Batch server calls; defer non-critical loads |
| Integration timeouts | Large payloads without pagination | Implement pagination in integration design |

### Index Requests

Request custom indexes proactively for:
- TPRM tables with >100,000 records
- Any table queried frequently with non-indexed fields
- Integration tables (staging tables for BitSight, Avetta, Ariba)

---

## Update Set Standards

### Naming Convention
```
[Sprint]-[Story/Change ID]-[Short Description]
Example: S12-VZ-0042-BitSight-C2-Issue-Generation-Fix
```

### Rules
1. One Update Set per story or atomic change
2. Update Set must be **Completed** in DEV before retrieval in TEST
3. Never manually edit records in TEST or PROD outside Update Set promotion
4. Document all records in the Update Set (what changed and why) in the Description field
5. Merge conflicts: manual merge using Update Set Compare tool; document resolution

---

## Security Standards

### Credential Management
- All credentials in Connection Aliases (ServiceNow native) or MID Server records
- No credentials in script code, properties, or system parameters
- Credential rotation: review and rotate every 90 days
- Service accounts: least-privilege; dedicated per integration

### ACL Design
- OOB roles where possible
- Avoid "Admin-only" patterns — breaks delegation
- Row-level ACLs for sensitive data (risk scores, vendor financials)
- Test ACLs with non-admin users before go-live

### Encryption
- Field-level encryption: use ServiceNow Edge Encryption for highly sensitive fields
- Integration transport: TLS 1.2 minimum; TLS 1.3 preferred
- Data at rest: ServiceNow encryption at rest (instance-level)

---

## Upgrade Management

### Pre-Upgrade Assessment Checklist
- [ ] Review upgrade impact analysis (ServiceNow provides for major releases)
- [ ] Test all custom scripts and Business Rules in upgrade sandbox
- [ ] Verify scoped app compatibility with target release
- [ ] Integration regression test (BitSight, Avetta, Ariba)
- [ ] User acceptance test of critical TPRM workflows
- [ ] Update upgrade test scripts if needed

### Post-Upgrade Validation
- [ ] Login and access validation
- [ ] Integration smoke tests
- [ ] Custom scripts execution validation
- [ ] Dashboard and report rendering
- [ ] Notification delivery

---

*Reference document. Technical standards apply to all configuration and development work on the Verizon OneRisk engagement. Escalate technical design decisions to Vidhya Sagar (primary) and Tony Scott (escalation).*
