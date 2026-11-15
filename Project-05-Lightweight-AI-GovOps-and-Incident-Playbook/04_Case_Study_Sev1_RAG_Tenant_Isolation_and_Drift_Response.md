# Worked Case Study: Sev-1 RAG Tenant-Isolation Incident & Quarterly Drift Response

**Engagement Profile:** Post-launch Governance Operations (GovOps) for a B2B SaaS platform serving 35 European and Indian enterprise clients  
**Scenario A (Sev-1 Production Incident):** Following a routine vector-database index migration, an engineering hotfix inadvertently omitted a `tenant_id` metadata filter on a non-default search route—causing one enterprise user's support query to surface a snippet from another tenant's knowledge base.  
**Scenario B (Quarterly Annex III Drift Check):** Scheduled Q4 2026 review detected score calibration drift in a thin-file merchant credit segment.

---

## 1. Execution Timeline (Scenario A — Sev-1 Incident SOP in Action)

| Elapsed Time | Phase | Action Executed | Owner |
| :--- | :--- | :--- | :--- |
| **T + 18 Mins** | **Phase 1: Contain** | Triggered feature-flag **kill-switch** on the RAG retrieval service, falling back gracefully to deterministic keyword search + human support queue | On-Call SRE / Product Lead |
| **T + 45 Mins** | **Phase 1: Preserve** | Snapshotted vector query logs and trace IDs into an access-controlled forensic bucket for audit verification | Security Engineering |
| **T + 2 Hours** | **Phase 2: Triage** | Classified as **Sev-1 (Cross-Tenant Data Exposure)**; confirmed via trace logs that only 1 query across 2 tenants was affected and zero external LLM training occurred (ZDR active) | Risk Lead + TAM |
| **T + 14 Hours** | **Phase 3: Client Notice** | Issued factual written advisory to both affected enterprise DPOs within the **24-hour SLA**, detailing containment, exact scope, and RCA delivery date | Technical Account Manager |
| **T + 4 Days** | **Phase 4: 5-Whys RCA** | Added automated CI/CD tenant-isolation integration tests, updated `02_AI_System_Change_and_Drift_Review_Log.csv`, and delivered signed RCA to clients | Engineering + Risk Lead |

---

## 2. Quarterly Drift & Bias Governance (Scenario B)
* During the Q4 2026 review (`GOV-2026-05`), thin-file merchant credit scores drifted by 6.2% following seasonal onboarding volume changes.
* Because human credit analysts still reviewed every recommendation (`Article 14` HITL gate), zero automated wrongful rejections occurred; Risk and Credit Ops recalibrated thresholds and logged the update for ISO/IEC 42001 audit traceability.
* **Client Retention Result:** Both enterprise accounts praised the 14-hour transparent disclosure and renewed their annual contracts without SLA penalties.
