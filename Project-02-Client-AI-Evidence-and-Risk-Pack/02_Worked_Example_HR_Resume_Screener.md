# Worked Example: Enterprise AI Due-Diligence & Evidence Pack (`AI-001`)

**Prepared for:** Enterprise Buyer Security & Procurement Review (Sample Illustration)  
**Date:** October 2025  
**Prepared by:** ComplyBridge Advisory Practice (Template Demonstration)  
**System Covered:** `AI-001` – Candidate Resume Screening & Shortlisting Assistant

---

## 1. AI System Overview & Regulatory Role
* **System Name & Inventory ID:** Candidate Resume Screening Tool (`AI-001`)
* **Business Purpose:** Assists internal Talent Acquisition specialists in parsing incoming CVs and matching skills against approved job descriptions.
* **Regulatory Role under EU AI Act:** **Deployer** (licensed enterprise SaaS module configured with internal hiring rubrics).
* **Consequential Decision Impact:** **Yes** — supports candidate shortlisting in recruitment (Annex III, Section 4(a) employment/recruitment systems).

---

## 2. Risk Classification & Framework Mapping
* **EU AI Act Risk Tier:** **High-Risk (Annex III, Point 4(a))**
* **Classification Rationale:** AI systems intended to be used for recruitment or selection of natural persons—specifically filtering applications and evaluating candidates—are classified as High-Risk under Annex III. As a private deployer, the organization enforces **Article 26 deployer obligations** alongside a **GDPR DPIA** and **India DPDP Act** candidate privacy notice.
* **NIST AI RMF & ISO/IEC 42001 Alignment:** `GOVERN 1.2` (Accountability), `MAP 2.3` (Stakeholder Impact), `MEASURE 2.11` (Fairness & Bias Evaluation), `MANAGE 2.2` (Human Oversight).

---

## 3. Transparency & User Disclosure Controls
* **Candidate Notice:** Every career portal application page displays an explicit upfront notice informing applicants that automated resume-parsing assistance is used alongside human recruiter review, with a link to request manual-only accommodation.
* **Evidence Reference:** `DOC-HR-TRN-01` (Career Portal Disclosure Screenshot & Candidate Privacy Notice v2.4).

---

## 4. Human Oversight & Override Accountability
* **Mandatory Human-in-the-Loop (HITL) Gate:** The system is strictly prohibited from auto-rejecting any candidate. It surfaces a structured skills-match summary, and a trained Talent Acquisition specialist must review and approve every advancement or rejection decision.
* **Override Capability:** Recruiters can override or disregard model relevance scores with a single click; override rates are logged monthly.
* **Accountable Owner:** Head of Talent Acquisition & HR Compliance Lead.

---

## 5. Data Governance, DPDP / GDPR & Third-Party GPAI Controls
* **Model Training Opt-Out:** **No** candidate CVs or personal data are ever used to train or fine-tune foundation models.
* **Upstream Provider Controls:** Hosted via Azure OpenAI (`eu-west` / `central-india` isolated tenant) under an executed Enterprise DPA with **Zero-Data-Retention (ZDR)** enabled and abuse-monitoring exemption approved.
* **Data Retention & Encryption:** TLS 1.3 in transit, AES-256 at rest; rejected candidate records purged after 180 days in accordance with GDPR storage limitation and India DPDP Act retention rules.

---

## 6. Risk Management, Bias Testing & Incident Response
* **Key Risks Identified:** Proxy bias (university prestige, career gaps, gender/regional naming signals) and hallucinated skill extraction.
* **Active Controls:** Blinded demographic attributes during scoring; pre-deployment and semi-annual adverse-impact parity testing across gender and geographic cohorts; structured JSON schema validation preventing ungrounded skill claims.
* **Incident Escalation SLA:** Any suspected discriminatory drift or data-privacy anomaly triggers immediate system pause within 2 hours and formal client/DPO notification within 24 hours.
