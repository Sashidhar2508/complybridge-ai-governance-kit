# Worked Case Study: Unblocking a Frankfurt Bank Procurement Review — VeloceFlow Technologies

**Client Context:** VeloceFlow Technologies (Hyderabad B2B SaaS) selling its merchant onboarding suite to a regulated German financial institution  
**Trigger:** The buyer's Third-Party Risk Management (TPRM) team issued a 28-question AI & Data Governance questionnaire and paused contract renewal pending evidence.  
**Deliverable:** Completed `Enterprise AI Due-Diligence & Evidence Pack` delivered in 48 hours, clearing InfoSec and Legal review without external Big 4 consulting spend.

---

## 1. Key Buyer Questions & Evidence Provided

| Buyer TPRM Question | VeloceFlow Initial Posture (Blocked) | Remediated Control & Evidence Submitted (Approved) |
| :--- | :--- | :--- |
| **Q1. Are customer or merchant records used to train foundation models?** | Unverified; engineering used a standard API key. | Migrated to enterprise cloud endpoint (`eu-central-1`) with signed **Zero-Data-Retention (ZDR)** addendum; attached DPA extract (`DOC-ZDR-02`). |
| **Q2. How are end-users notified when interacting with AI (`Art. 50`)?** | No UI label on the merchant support chat widget. | Deployed persistent header banner: *"AI Support Assistant — Responses generated from official product docs. Type 'agent' for human support."* Attached screenshot (`DOC-TRN-01`). |
| **Q3. Can the AI autonomously reject a merchant or alter credit limits?** | Unclear escalation boundary in product docs. | Documented mandatory **Human-in-the-Loop (HITL)** gate: model outputs a risk score and reason codes only; certified credit analysts approve/reject every limit (`DOC-HITL-03`). |
| **Q4. How is personal data governed across India and EU teams (`DPDP / GDPR`)?** | Production support logs accessible to Hyderabad engineers with raw PII. | Implemented automated PII redaction prior to inference logging and role-based access controls aligned with **GDPR SCCs** and **India DPDP Act** security safeguards. |
| **Q5. What is your SLA if the AI hallucinates policy terms or leaks data?** | Covered only under generic IT uptime SLAs. | Issued AI Incident Escalation SOP committing to **1-hour kill-switch containment** and **24-hour buyer DPO notification** for any Sev-1 AI incident. |

---

## 2. Commercial & Governance Outcome
* **Deal Impact:** Cleared the buyer's TPRM security gate within **5 business days**, securing the €240,000 renewal.
* **Reusable Asset:** The completed pack became VeloceFlow's standard presales attachment for all subsequent European banking prospects.
