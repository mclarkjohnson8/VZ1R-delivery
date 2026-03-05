# Recommended Next Steps
## Verizon OneRisk TPRM | AI-Generated Strategic Recommendations

> **Note:** This file is AI-generated and updated by the delivery agent after
> `context/engagement-history.md` has been populated with the full engagement history.
>
> **Current status:** Pre-populated with Sprint 12 / Go-Live context only.
> Once Clark populates `engagement-history.md`, the agent will produce richer,
> more historically-grounded recommendations.
>
> **How this file is updated:** After dropping new meeting notes into
> `updates/meeting-notes/`, the parser will propose updates to this file
> as part of its recommendations output.

---

## Immediate Actions (Next 72 Hours — as of 2026-03-05)

| Priority | Action | Owner | Deadline | Status |
|----------|--------|-------|----------|--------|
| P1 | BitSight Component 2: confirm scope decision (include or defer) | Tony Scott / Heidi | 2026-03-09 | Open |
| P1 | Avetta: validate production connectivity; root cause Avetta-side server error | Alec Barone / Gary Vick | 2026-03-06 | In Progress |
| P1 | Ariba: obtain fix ETA from Ariba team; validate staging | TBD | 2026-03-06 | In Progress |
| P1 | IRQ: complete stakeholder UAT (targeted 3/5) | Heidi | 2026-03-05 | In Progress |
| P2 | VCS Outbound API: capture volume, frequency, and pull strategy requirements | Arav / Tony | 2026-03-06 | New |
| P2 | EHS integration: confirm 3/10 training readiness | Team | 2026-03-07 | Open |

---

## This Sprint (Sprint 12 — Through 2026-03-13)

### Must-Complete for Go-Live
- [ ] IRQ UAT sign-off
- [ ] BitSight Component 1 UAT sign-off
- [ ] BitSight Component 2 scope decision (go/defer)
- [ ] Avetta integration validated (staging or production)
- [ ] Ariba integration validated
- [ ] All training sessions complete (7 sessions through 3/17)
- [ ] Go/No-Go gate cleared (2026-03-09)
- [ ] Cutover plan confirmed and communicated

### Recommended Sequencing
1. **3/5**: Complete IRQ UAT with stakeholders
2. **3/6**: Resolve Avetta and Ariba blockers
3. **3/7–3/8**: Final UAT regression sweep
4. **3/9**: Go/No-Go decision with full issue status
5. **3/10–3/12**: Final UAT completion and sign-off
6. **3/13**: Go-Live execution

---

## Go/No-Go Readiness Assessment (as of 2026-03-05)

### Decision Gate: 2026-03-09

| Criterion | Status | Risk | Notes |
|-----------|--------|------|-------|
| IRQ UAT | YELLOW | Medium | Functional testing ✓; stakeholder UAT 3/5 |
| BitSight C1 UAT | YELLOW | Medium | UAT underway |
| BitSight C2 | RED | High | GRC issue generation defect; scope decision required |
| Avetta UAT | RED | High | Staging blocked; production validation in progress |
| Ariba UAT | RED | High | Stage environment blocked |
| Training | GREEN | Low | Sessions on track through 3/17 |
| Transition Plan | GREEN | Low | Window active; vendor freeze enforced |
| Cutover Readiness | YELLOW | Medium | Pending UAT completion |

### Go/No-Go Recommendation (Agent)
> ⚠️ **Current trajectory: conditional go.** BitSight C2, Avetta, and Ariba are all active blockers as of 3/5.
> For a 3/13 go-live to be viable, Avetta and Ariba must be resolved by 3/6, and BitSight C2 scope must
> be decided by 3/9. If BitSight C2 defers to post-go-live, confirm defect has no impact on C1 functionality.
>
> *Update this section after 3/9 Go/No-Go gate decision.*

---

## Post Go-Live Watchlist (Hypercare: 2026-03-13 → 2026-03-27)

### High-Priority Watch Items
| Item | Risk | Owner | Action |
|------|------|-------|--------|
| BitSight C2 (if deferred) | Medium | Heidi / Vidhya | Schedule fix for hypercare sprint |
| Avetta production stability | Medium | Gary Vick | Monitor daily for first 5 business days |
| IRQ scoring accuracy | Medium | Heidi | Validate with live data post-go-live |
| VCS Outbound API | Medium | Tony / Arav | Architecture sprint post-go-live |
| User adoption / help desk volume | Medium | Clark | Track support tickets; escalate anomalies |
| Notification volume | Low | Heidi | Confirm 50%+ reduction holds with live data |

### Transition to BAU (Target: 2026-03-27)
- [ ] Hypercare sprint retrospective
- [ ] Managed service handoff checklist complete
- [ ] Documentation finalized (admin guide, user guide, integration runbook)
- [ ] Support model activated
- [ ] VCS Outbound API scoped for next release

---

## Open Architecture Decisions

### ISS-005: VCS Outbound API
**Context:** Business request (CSG-supported) for outbound read API exposing full TPRM dataset.
**North Star:** GCP push architecture.
**Near-term:** Read-only pull API acceptable per Arav.
**Pending inputs from business:** volume, frequency (daily vs delta), pull strategy.

**Recommended approach:**
1. Confirm requirements with CSG business owners this week
2. Design read-only REST API scoped to TPRM entities (TPR records, engagements, IRQs, DDQs, attachments, contacts, risks)
3. Rate limit and authentication aligned with ServiceNow REST API standards
4. Schedule architecture review with Arav before end of sprint

---

*This file is maintained by the VZ1R Delivery Agent. Last updated: 2026-03-05.*
*Source: engagement-state.json + system-instructions.md. Populate engagement-history.md for richer recommendations.*
