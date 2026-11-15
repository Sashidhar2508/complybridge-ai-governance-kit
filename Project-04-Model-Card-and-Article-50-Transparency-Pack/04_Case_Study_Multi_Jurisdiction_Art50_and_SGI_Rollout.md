# Worked Case Study: Multi-Jurisdiction Transparency Rollout (EU AI Act Art. 50 & India IT Rules 2026)

**Engagement Profile:** Mid-sized Bengaluru SaaS & Digital Engagement Platform (serving Indian enterprise portals and EU B2B customers)  
**Trigger:** Following the February 2026 enforcement of **India's IT Amendment Rules, 2026** and ahead of the **2 August 2026 EU AI Act Article 50** enforcement date, the company needed to audit two customer-facing generative features: (1) an AI Helpdesk Chatbot and (2) an AI Campaign Banner & Voiceover Generator.  
**Outcome:** Completed standardized Model Cards with patent/license attribution, deployed Article 50(1) disclosures across web/mobile SDKs, and fixed an image-compression bug that was stripping C2PA provenance metadata.

---

## 1. Technical & Regulatory Gaps Uncovered

| Feature Audited | Applicable Rules | Gap Found During Audit | Fix Implemented |
| :--- | :--- | :--- | :--- |
| **AI Helpdesk Chatbot** | EU AI Act **Art. 50(1)** (Conversational AI notice) | Chat widget opened with *"Hi! How can I help you today?"*—failing to inform users they were interacting with an AI system; no clear button to reach a human agent | Added persistent header disclosure (*"AI Assistant — Powered by AI over official docs"*) and a one-click **`Talk to Human Agent`** button |
| **AI Campaign Banner & Voiceover Generator** | EU AI Act **Art. 50(2)** (Machine-readable marking) & **India IT Rules 2026** (SGI labelling) | Upstream image generator embedded **C2PA Content Credentials**, but the SaaS platform's thumbnail resizer stripped EXIF/XMP/C2PA headers before download/export | Reconfigured media processing pipeline (`sharp` / CDN rules) to preserve C2PA manifest chunks intact and added a visible *"AI-Generated"* badge toggle for Indian intermediary uploads |
| **Model Documentation & IP Clarity** | ISO/IEC 42001 & Enterprise Buyer Procurement | Sales teams had no single document explaining accuracy benchmarks, hallucination guardrails, or commercial license/patent rights for the generated banners | Published signed **Model Cards** (`01_Standard_AI_Model_Card_Template.docx`) documenting benchmark faithfulness (96.4%), commercial usage rights, and upstream vendor patent indemnity |

---

## 2. Business & Compliance Outcome
* **Zero Retroactive Rework:** Met the **2 August 2026** EU AI Act Article 50 live date and positioned all legacy assets well ahead of the **2 December 2026** legacy marking deadline.
* **Sales Enablement:** Enterprise buyers in Frankfurt and Mumbai accepted the published Model Cards as standalone transparency proof during Q3 2026 security reviews.
