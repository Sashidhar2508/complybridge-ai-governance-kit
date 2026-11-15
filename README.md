# ComplyBridge AI Governance Kit: Practical AI Risk, IP Protection & Advisory Suite for Indian SaaS and GCCs

**Author & Principal Advisor:** Sashidhar Sripadanna (IAPP AIGP Candidate | OCI Certified AI Associate | 13+ Years Enterprise Cloud and TAM Leadership)  
**Advisory Practice Timeline:** March 2025 – Present  
**Regulatory & IP Scope:** EU AI Act (incl. Regulation (EU) 2026/1744 Digital Omnibus), NIST AI RMF 1.0, ISO/IEC 42001 AIMS, India DPDP Act, India IT Amendment Rules 2026, and Enterprise Patent/IP Indemnification  
**License:** Apache License 2.0 (includes explicit patent and copyright grant; see `LICENSE`)  
*Note: ComplyBridge AI Governance Kit is an independent open-source AI governance and technical account advisory framework for SaaS and GCC teams (distinct from financial services compliance platforms).*

---

## 90-Second Executive Summary

> **New Here?** Start with **[`00_Executive_One_Pager_90_Second_Brief.md`](./00_Executive_One_Pager_90_Second_Brief.md)** (or download **[`00_Executive_One_Pager_90_Second_Brief.pdf`](./00_Executive_One_Pager_90_Second_Brief.pdf)**) for a single-page overview of how ComplyBridge unblocks US/EU enterprise procurement reviews.

**ComplyBridge AI Governance Kit** is an applied, zero-code AI Governance and Technical Account Advisory suite built between **March 2025 and November 2026**. It bridges the operational disconnect between engineering teams, legal/risk counsel, and European or US enterprise procurement buyers.

Every single module in this repository pairs **plug-and-play governance artefacts** with **realistic worked B2B SaaS case studies** and **advisory decision logs** showing how classification edge cases, vendor Zero-Data-Retention (ZDR) gaps, patent/IP risks, Article 50 disclosures, and production AI incidents are resolved in practice.

---

## How a Company Uses ComplyBridge in a Live Enterprise Sales Cycle

When a mid-sized Indian SaaS vendor pitches an AI-enabled product to a European bank or US enterprise buyer, InfoSec and Legal reviews typically stall for 4–6 weeks. ComplyBridge compresses that review into a structured **48-hour response workflow**:

1. **Hour 0–4 — Scope Role & Risk Tier (`Project 01`):** Log the customer-facing AI feature and internal supporting models in the *AI System Inventory Register*, establish whether the company acts as **Provider** or **Deployer**, and screen for Annex III High-Risk or Article 50 transparency triggers.
2. **Hour 4–12 — Verify Upstream Model & IP Hygiene (`Project 03`):** Audit the underlying cloud/LLM API (e.g., Azure OpenAI, AWS Bedrock) using the *Third-Party Vendor Scorecard* to confirm active Enterprise ZDR, regional data residency, and third-party patent/copyright indemnification.
3. **Hour 12–24 — Assemble Model Card & Transparency Proof (`Project 04`):** Attach the system's *Model Card* (documenting accuracy/hallucination benchmarks and license attribution) alongside live UI screenshots proving Article 50(1) upfront bot disclosure.
4. **Hour 24–48 — Deliver Client Evidence Pack & SLA Commitments (`Project 02` & `Project 05`):** Submit the completed *Enterprise Client AI Evidence & Risk Pack* backed by documented human-in-the-loop (HITL) override rules and a 24-hour Sev-1 incident escalation SLA.

---

## Repository Structure

```text
complybridge-ai-governance-kit/
├── README.md                                                     # Suite overview, sales-cycle workflow & roadmap
├── LICENSE                                                       # Apache 2.0 license with explicit patent protection
├── 00_Executive_One_Pager_90_Second_Brief.md                     # 90-second hiring manager & executive brief
├── 00_Executive_One_Pager_90_Second_Brief.pdf                    # Printable 1-page PDF executive brief
├── 00_ComplyBridge_Executive_Overview.docx                       # Detailed Word overview of all five kits
│
├── Project-01-AI-System-Inventory-and-Classifier/                # Release Window: Mar – Jun 2025
│   ├── README.md
│   ├── 01_AI_System_Inventory_Register.csv
│   ├── 01_AI_System_Inventory_Register.docx
│   ├── 02_EU_AI_Act_and_NIST_Classification_Guide.md
│   ├── 03_Case_Study_VeloceFlow_Hyderabad_AI_Inventory.md        # [WORKED CASE STUDY] 185-person B2B SaaS audit
│   └── 04_Advisory_Decision_Log_Project_01.md                    # [DECISION LOG] Classification & FRIA edge cases
│
├── Project-02-Client-AI-Evidence-and-Risk-Pack/                  # Release Window: Jul – Oct 2025
│   ├── README.md
│   ├── 01_Client_AI_Evidence_and_Risk_Pack_Template.docx
│   ├── 02_Worked_Example_HR_Resume_Screener.md
│   ├── 03_Enterprise_Buyer_Evidence_Checklist.md
│   ├── 04_Case_Study_VeloceFlow_EU_Bank_Procurement_Pack.md      # [WORKED CASE STUDY] Frankfurt bank 28-Q review
│   └── 05_Advisory_Decision_Log_Project_02.md                    # [DECISION LOG] ZDR, HITL & DPDP/GDPR trade-offs
│
├── Project-03-Third-Party-AI-and-GPAI-Vendor-Due-Diligence/      # Release Window: Nov 2025 – Feb 2026
│   ├── README.md
│   ├── 01_Third_Party_AI_Vendor_Scorecard.csv
│   ├── 01_Third_Party_AI_Vendor_Scorecard.docx
│   ├── 02_Vendor_ZDR_IP_and_Patent_Contract_Clauses.md
│   ├── 03_Case_Study_VeloceFlow_Vendor_ZDR_and_IP_Audit.md       # [WORKED CASE STUDY] 4-vendor ZDR & IP audit
│   └── 04_Advisory_Decision_Log_Project_03.md                    # [DECISION LOG] Fee caps, open-weights & novelty
│
├── Project-04-Model-Card-and-Article-50-Transparency-Pack/       # Release Window: Mar – Jul 2026
│   ├── README.md
│   ├── 01_Standard_AI_Model_Card_Template.docx
│   ├── 02_Article_50_and_India_IT_Rules_2026_Transparency_Checklist.md
│   ├── 03_Worked_Example_Support_Chatbot_Model_Card.md
│   ├── 04_Case_Study_Multi_Jurisdiction_Art50_and_SGI_Rollout.md # [WORKED CASE STUDY] EU Art. 50 & India IT Rules
│   └── 05_Advisory_Decision_Log_Project_04.md                    # [DECISION LOG] C2PA pipelines & license tracking
│
├── Project-05-Lightweight-AI-GovOps-and-Incident-Playbook/       # Release Window: Aug – Nov 2026
│   ├── README.md
│   ├── 01_AI_GovOps_and_Incident_Response_Playbook.docx
│   ├── 02_AI_System_Change_and_Drift_Review_Log.csv
│   ├── 03_AI_Incident_Escalation_SOP.md
│   ├── 04_Case_Study_Sev1_RAG_Tenant_Isolation_and_Drift_Response.md # [WORKED CASE STUDY] Sev-1 RCA & drift fix
│   └── 05_Advisory_Decision_Log_Project_05.md                    # [DECISION LOG] Quarterly cadence & 24-hr SLAs
│
└── docs/                                                         # GitHub Pages Personal Capability Site
    └── index.html                                                # Live AI Governance & TAM Bridge showcase
```

---

## Advisory Portfolio & Timeline (March 2025 – November 2026)

| Kit / Project | Advisory Window | Core Deliverables & Applied Proof | Regulatory & IP Anchor | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Project 01:** AI System Inventory & Classification Register | **Mar – Jun 2025** | 10-column register, classification guide, **VeloceFlow Hyderabad SaaS Case Study**, & **Decision Log** | EU AI Act **Art. 4, 5, 6, Annex III**; NIST AI RMF; India DPDP Act | **Published** |
| **Project 02:** Enterprise Client AI Evidence & Risk Pack | **Jul – Oct 2025** | Due-diligence pack, worked HR pack, **Frankfurt Bank Procurement Case Study**, & **Decision Log** | EU AI Act **GPAI & Art. 14/26/50**; ISO/IEC 42001; DPDP/GDPR | **Published** |
| **Project 03:** Third-Party AI & GPAI Vendor Due-Diligence Kit | **Nov 2025 – Feb 2026** | Upstream LLM scorecard, ZDR & Patent clauses, **4-Vendor ZDR/IP Audit Case Study**, & **Decision Log** | EU GPAI Chapter V; Patent Novelty & IP Indemnification | **Published** |
| **Project 04:** Model Card & Article 50 Transparency Pack | **Mar – Jul 2026** | Model Card (with Patent/License attribution), **Multi-Jurisdiction Art. 50/SGI Case Study**, & **Decision Log** | EU AI Act **Art. 50** (Aug/Dec 2026); India IT Rules 2026 | **Published** |
| **Project 05:** Lightweight AI GovOps & Incident Playbook | **Aug – Nov 2026** | Post-market monitoring SOP, drift log, **Sev-1 RAG & Drift Response Case Study**, & **Decision Log** | ISO/IEC 42001 Clause 8–10; NIST RMF Manage; Annex III window | **Published** |

---

## Contact & Advisory Background

* **Name:** Sashidhar Sripadanna
* **Focus Areas:** AI Governance & Risk Advisory (EU AI Act, NIST AI RMF, ISO/IEC 42001, India DPDP Act), Technical Account Management (TAM), Enterprise Buyer Due-Diligence & Escalation Bridge
* **LinkedIn:** [linkedin.com/in/sashidhar-s-6a6662186](https://linkedin.com/in/sashidhar-s-6a6662186)
* **GitHub:** [github.com/sashidhar2508](https://github.com/sashidhar2508)
