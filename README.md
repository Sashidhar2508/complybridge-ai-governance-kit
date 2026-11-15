# ComplyBridge: Practical AI Governance, IP Protection & Advisory Suite for Indian SaaS and GCCs

**Author and Principal Advisor:** Sashidhar Sripadanna (IAPP AIGP Candidate | OCI Certified AI Associate | 13+ Years Enterprise Cloud and TAM Leadership)  
**Advisory Practice Timeline:** March 2025 – Present  
**Regulatory and IP Alignment:** EU AI Act (including Regulation (EU) 2026/1744 Digital Omnibus), NIST AI RMF 1.0, ISO/IEC 42001 AIMS, India DPDP Act, India IT Amendment Rules 2026, and Enterprise Patent/IP Indemnification Standards  
**License:** Apache License 2.0 (includes explicit patent and copyright grant; see `LICENSE`)

---

## Purpose

**ComplyBridge** is a practical, zero-code governance suite developed between **March 2025 and November 2026**. It is built for mid-sized Indian software companies and Global Capability Centers (GCCs) that sell AI-enabled products or delivery services to European and US enterprise buyers.

In real enterprise sales and audit cycles, deals rarely stall over model accuracy alone. They stall when Legal, Procurement, and Information Security teams ask:
1. Which AI systems are in production, and are you acting as a **Provider** or **Deployer** under the EU AI Act?
2. Can you document Article 50 transparency notices, human-in-the-loop (HITL) override rules, and Zero-Data-Retention (ZDR) terms?
3. How do you protect proprietary **patents, trade secrets, and client intellectual property** when calling third-party foundation models, and what patent indemnification do your upstream vendors provide?

ComplyBridge gives risk, legal, and technical account teams ready-to-use registers, vendor scorecards, model cards, and operational SOPs so they can answer these questions clearly without hiring a Big 4 consultancy.

---

## Repository Structure

```text
complybridge-ai-governance-kit/
├── README.md                                                     # Suite overview, timeline and regulatory mapping
├── LICENSE                                                       # Apache 2.0 license with explicit patent protection
├── 00_ComplyBridge_Executive_Overview.docx                       # Executive summary covering all five published kits
│
├── Project-01-AI-System-Inventory-and-Classifier/                # Release Window: Mar – Jun 2025
│   ├── README.md
│   ├── 01_AI_System_Inventory_Register.csv
│   ├── 01_AI_System_Inventory_Register.docx
│   └── 02_EU_AI_Act_and_NIST_Classification_Guide.md
│
├── Project-02-Client-AI-Evidence-and-Risk-Pack/                  # Release Window: Jul – Oct 2025
│   ├── README.md
│   ├── 01_Client_AI_Evidence_and_Risk_Pack_Template.docx
│   ├── 02_Worked_Example_HR_Resume_Screener.md
│   └── 03_Enterprise_Buyer_Evidence_Checklist.md
│
├── Project-03-Third-Party-AI-and-GPAI-Vendor-Due-Diligence/      # Release Window: Nov 2025 – Feb 2026
│   ├── README.md
│   ├── 01_Third_Party_AI_Vendor_Scorecard.csv
│   ├── 01_Third_Party_AI_Vendor_Scorecard.docx
│   └── 02_Vendor_ZDR_IP_and_Patent_Contract_Clauses.md
│
├── Project-04-Model-Card-and-Article-50-Transparency-Pack/       # Release Window: Mar – Jul 2026
│   ├── README.md
│   ├── 01_Standard_AI_Model_Card_Template.docx
│   ├── 02_Article_50_and_India_IT_Rules_2026_Transparency_Checklist.md
│   └── 03_Worked_Example_Support_Chatbot_Model_Card.md
│
└── Project-05-Lightweight-AI-GovOps-and-Incident-Playbook/       # Release Window: Aug – Nov 2026
    ├── README.md
    ├── 01_AI_GovOps_and_Incident_Response_Playbook.docx
    ├── 02_AI_System_Change_and_Drift_Review_Log.csv
    └── 03_AI_Incident_Escalation_SOP.md
```

---

## Advisory Portfolio and Timeline (March 2025 – November 2026)

Each kit in this repository corresponds to a specific regulatory milestone and enterprise buyer requirement:

| Kit / Project | Advisory Window | Core Deliverables | Regulatory and IP Trigger Addressed | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Project 01:** AI System Inventory and Classification Register | **Mar – Jun 2025** | 10-column baseline AI register (8 worked SaaS/GCC systems), Provider vs. Deployer scoping, and EU AI Act / NIST AI RMF decision rules | EU AI Act **Art. 4** (AI Literacy) and **Art. 5** (Prohibited Practices) application (Feb 2025) | **Published** |
| **Project 02:** Enterprise Client AI Evidence and Risk Pack | **Jul – Oct 2025** | Fillable enterprise buyer due-diligence response pack, pre-submission checklist, and worked HR screening assessment | EU AI Act **GPAI Governance** rules (Aug 2025) and **India DPDP Act** processor safeguards | **Published** |
| **Project 03:** Third-Party AI and GPAI Vendor Due-Diligence Kit | **Nov 2025 – Feb 2026** | Upstream LLM/API vendor risk scorecard, Zero-Data-Retention (ZDR) checks, and **Patent / Copyright Indemnification** contract clauses | Cross-border processor governance, trade-secret / patent novelty preservation, and upstream GPAI risk | **Published** |
| **Project 04:** Model Card and Article 50 Transparency Pack | **Mar – Jul 2026** | Standardized Model Card (including **Patent and Model License Attribution**), Article 50 UI notices, and C2PA provenance checklist | EU AI Act **Art. 50** enforcement (Aug 2026 / Dec 2026 marking deadline) and **India IT Amendment Rules 2026** | **Published** |
| **Project 05:** Lightweight AI GovOps and Incident Playbook | **Aug – Nov 2026** | Post-market monitoring SOP, AI change and drift review log, and 24-hour client incident escalation runbook | Post-Aug 2026 enforcement and Digital Omnibus **Annex III** readiness window (through Dec 2027) | **Published** |

---

## Intellectual Property and Patent Governance

Enterprise AI adoption introduces two distinct patent and IP risks that standard IT security questionnaires miss:
1. **Loss of Patent Novelty via Prompt Leakage:** If engineers or R&D staff paste unpatented algorithms, circuit designs, or product architectures into a third-party AI tool lacking Zero-Data-Retention (ZDR), that disclosure can compromise patentability. Project 03 and Project 05 enforce strict ZDR and confidential-input boundaries.
2. **Third-Party Patent and Copyright Infringement Claims:** SaaS companies building on commercial or open-weights foundation models need explicit contractual patent/copyright indemnification and clear open-source license tracking. Project 03 provides ready-to-use vendor contract clauses, and Project 04 embeds patent and license attribution directly into every Model Card.

---

## How to Use This Repository

* **In Browser (GitHub):** Open any project folder to read the `.md` playbooks and inspect the `.csv` registers directly in GitHub's table viewer.
* **For Client Reviews and Internal Audits:** Download the `.docx` files inside each folder for clean, formatted templates ready for Word or Google Docs.

---

## Author Contact

* **Name:** Sashidhar Sripadanna
* **Domain:** AI Governance and Risk Advisory (EU AI Act, NIST AI RMF, ISO/IEC 42001, India DPDP Act), Technical Account Management (TAM)
* **LinkedIn:** [linkedin.com/in/sashidhar-s-6a6662186](https://linkedin.com/in/sashidhar-s-6a6662186)
* **GitHub:** [github.com/sashidhar2508](https://github.com/sashidhar2508)
