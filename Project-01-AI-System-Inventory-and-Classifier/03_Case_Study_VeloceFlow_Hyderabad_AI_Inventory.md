# Worked Case Study: Baseline AI Inventory & Risk Triage — VeloceFlow Technologies (Hyderabad)

**Engagement Profile:** Mid-sized B2B SaaS & FinTech Workflow Platform (185 employees, Hyderabad Delivery Center, selling to EU and UK mid-market banks)  
**Advisory Trigger:** A Tier-2 bank in Frankfurt requested a complete AI inventory and EU AI Act risk classification prior to signing a €240,000 annual SaaS renewal.  
**Outcome:** Delivered a validated 6-system inventory, quarantined two unapproved internal tools, and closed buyer classification sign-off within 5 business days.

---

## 1. Initial Discovery Findings (What Was Broken)
Before this assessment, VeloceFlow's VP of Engineering believed the company operated *"only one AI feature"* (its customer-facing support chatbot). Cross-functional interviews with Product, HR, Finance, and Sales Ops uncovered **six active AI/GenAI systems**, three of which had never been reviewed by Legal or InfoSec:

| ID | System Discovered | Team | Underlying Setup | Role | EU AI Act Tier | Critical Gap Flagged |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VF-01** | Merchant Onboarding & Credit Limit Scorer | Product (Core SaaS) | Gradient-boosted model + bureau APIs | **Provider** | **High-Risk (Annex III)** | Sold to EU banks for SMB creditworthiness; lacked formal risk management file & adverse-action logs |
| **VF-02** | In-App Merchant Support Chatbot | Customer Success | RAG over help docs via direct OpenAI API | **Provider** | **Limited Risk (Art. 50)** | Missing upfront AI disclosure banner; using pay-as-you-go API without signed Zero-Data-Retention (ZDR) |
| **VF-03** | Engineering Resume Shortlisting Filter | Talent Acquisition | Third-party ATS AI scoring plug-in | **Deployer** | **High-Risk (Annex III)** | Configured to auto-reject applicants below 65% match score with zero human recruiter review |
| **VF-04** | Sales Call Tone & Emotion Scorer | Revenue Ops | Third-party call-recording sentiment tool | **Deployer** | **Prohibited (Art. 5(1)(f))** | Used to score internal SDR emotional tone during coaching reviews—violating workplace emotion ban |
| **VF-05** | Vendor Invoice OCR Extractor | Finance Ops | SaaS accounting OCR module | **Deployer** | **Minimal Risk** | Low risk; needed basic vendor SLA documentation and quarterly accuracy spot-check |
| **VF-06** | R&D Code Copilot | Engineering | Individual developer accounts on public tier | **Deployer** | **Minimal Risk (High IP Risk)** | Engineers pasting proprietary scoring algorithms into non-ZDR accounts, risking trade-secret/patent loss |

---

## 2. Remediation Roadmap Executed
1. **Immediate Containment (48 Hours):**
   * Disabled the employee emotion-scoring module in `VF-04` immediately to eliminate **Article 5(1)(f)** prohibited-practice exposure.
   * Turned off auto-rejection in `VF-03` (ATS screener) and instituted a mandatory human recruiter review gate (`Article 26` deployer control).
2. **Contractual & Technical Safeguards (Days 3–5):**
   * Migrated `VF-02` (Support Chatbot) from a standard pay-as-you-go API key to an enterprise cloud endpoint with **Zero-Data-Retention (ZDR)** and added an upfront `"AI Assistant"` disclosure header (`Article 50(1)`).
   * Consolidated `VF-06` (Code Copilot) onto an enterprise license with ZDR enabled and issued an R&D rule banning unfiled patent/algorithm prompts.
   * Scoped a phased conformity roadmap for `VF-01` (SMB Credit Scorer) ahead of the Annex III enforcement window, providing the Frankfurt bank with interim explainability and human-override documentation.
