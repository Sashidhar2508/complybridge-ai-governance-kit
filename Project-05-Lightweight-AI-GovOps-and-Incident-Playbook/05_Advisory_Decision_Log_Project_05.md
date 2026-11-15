# Advisory Decision Log: Project 05 (Lightweight AI GovOps & Incident Playbook)

This log explains the operational design choices behind `Project 05`.

---

## Decision 01: Empowering On-Call Engineering & TAMs with Unilateral Kill-Switch Authority
* **Context:** In many organizations, disabling a customer-facing AI feature requires multi-level executive approval, stretching containment from minutes to days.
* **Decision:** Granted unilateral **1-hour kill-switch / deterministic-fallback authority** to on-call engineering and product owners for any suspected Sev-1 privacy, IP, or bias incident.
* **Reasoning:** Drawing directly from 13+ years of enterprise production escalation management, rapid containment caps blast radius immediately while preserving client trust.

## Decision 02: Using a Quarterly Review Cadence Instead of Heavy Continuous Governance Meetings
* **Context:** Mid-sized Indian SaaS teams rarely have dedicated 10-person AI ethics committees. Weekly governance meetings quickly get skipped.
* **Decision:** Anchored post-market monitoring around **three event-driven triggers** (model swap, scope expansion, new PII/IP data ingestion) plus **one structured quarterly review**.
* **Reasoning:** Lightweight, predictable checkpoints align with ISO/IEC 42001 Clause 9 performance evaluation without creating bureaucratic drag on engineering sprints.

## Decision 03: Committing to a 24-Hour Factual Client Advisory SLA on Sev-1 AI Incidents
* **Context:** Vendors often delay notifying enterprise clients for days while waiting for a complete technical root cause, triggering breach-of-trust escalations.
* **Decision:** Separated **24-hour factual containment notification** (what happened, confirmation of pause/rollback, scope of exposure) from the **5-business-day formal 5-Whys RCA**.
* **Reasoning:** Enterprise DPOs and procurement leads need immediate factual confirmation to satisfy their own regulatory clocks (e.g., 72-hour GDPR breach assessment), even while deep technical remediation continues.
