# AI Incident Escalation Standard Operating Procedure (SOP)

**Purpose:** Provide a clear, non-bureaucratic response sequence when an AI system produces a severe privacy leak, IP/patent exposure, discriminatory outcome, or safety failure.

---

## Phase 1: Detect & Contain (0 – 60 Minutes)
1. **Trigger Kill-Switch / Fallback:** On-call engineering or product owner disables the AI feature flag and routes traffic to deterministic rules or human support queues.
2. **Preserve Evidence:** Capture prompt/response logs, model version ID, and retrieval document IDs in a restricted forensic bucket (do not delete audit trails).

---

## Phase 2: Triage & Classify Severity (1 – 4 Hours)
* **Sev-1 (Critical):** Unauthorized exposure of customer PII, confidential R&D/patent data, severe demographic bias in HR/credit decisions, or regulatory breach.
* **Sev-2 (High):** Broken Article 50 transparency disclosure, stripped synthetic-content watermark, or repeatable hallucination affecting customer workflows.

---

## Phase 3: Client & Stakeholder Communication (Within 24 Hours for Sev-1)
* **Technical Account Manager (TAM) / Risk Lead** issues a concise factual advisory to affected enterprise clients covering:
  1. What happened and which system ID was affected.
  2. Confirmation that the system has been paused or rolled back.
  3. Whether customer data or intellectual property was exposed.
  4. Target timestamp for the full Root Cause Analysis (RCA).

---

## Phase 4: Root Cause Analysis & Control Closure (Within 5 Business Days)
* Complete a structured **5-Whys RCA** identifying whether the failure stemmed from prompt design, retrieval data, upstream model drift, or missing human oversight.
* Update the `AI System Inventory Register`, `Model Card`, and `Change & Drift Review Log` before re-enabling production traffic.
