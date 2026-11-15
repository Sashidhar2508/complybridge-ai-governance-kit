# Worked Case Study: Upstream AI Vendor ZDR & Patent Indemnity Audit — VeloceFlow Technologies

**Engagement Profile:** VeloceFlow Technologies (185-person Hyderabad B2B FinTech SaaS selling to European banks)  
**Trigger:** During an annual enterprise vendor review, a German banking client demanded contractual proof that VeloceFlow's upstream foundation model vendors (1) enforce Zero-Data-Retention (ZDR), (2) keep inference inside EU/India approved cloud regions, and (3) provide third-party patent and copyright indemnification.  
**Outcome:** Audited 4 upstream AI vendors in 4 days, blocked an unvetted CRM AI sub-processor, consolidated LLM traffic onto enterprise ZDR endpoints, and eliminated a major IP/patent exposure gap.

---

## 1. Upstream Vendor Audit Results

| Vendor / Tool Evaluated | Initial Setup Discovered | Critical Risk / IP Finding | Remediation Executed |
| :--- | :--- | :--- | :--- |
| **1. Direct OpenAI API (Pay-As-You-Go)** | Used by Support Chatbot (`VF-02`) on default US endpoint | 30-day abuse/diagnostic retention active; standard self-serve terms lacked signed ZDR addendum and super-cap patent indemnity | Migrated inference to **AWS Bedrock (`eu-central-1` / `ap-south-1`)** with default zero-logging and AWS Service Terms AI IP/patent indemnity |
| **2. Self-Hosted Llama 3.1 (GPU Node)** | Deployed by R&D for internal log summarization on OCI | Low data-egress risk, but Engineering assumed an open-weights download carried vendor patent protection | Documented that organization assumes upstream patent/IP risk; verified commercial license compliance and restricted usage to internal non-customer logs |
| **3. Cloud CRM "AI Deal Summarizer" Add-On** | Enabled via admin toggle by Revenue Ops without InfoSec review | Vendor's legacy MSA allowed sub-processor model improvement unless explicitly opted out; sub-processor regions undisclosed | **Disabled feature immediately** until vendor executed an AI Addendum confirming ZDR, EU/India DPA coverage, and IP indemnity |
| **4. Developer IDE Code Assistant** | 22 engineers expensing individual public-tier accounts | Engineers pasted proprietary credit-scoring logic into non-ZDR accounts, risking trade-secret loss and pre-filing **patent novelty bar** | Consolidated all seats under an Enterprise Tenant with ZDR enforced and issued an R&D policy prohibiting unfiled patent disclosures in prompts |

---

## 2. Commercial & Legal Impact
* **Audit Closure:** Delivered completed vendor scorecards and signed DPA/ZDR extracts to the German bank's TPRM team, passing third-party sub-processor review with zero open findings.
* **IP Protection:** Prevented potential loss of patent novelty on two pending merchant-risk scoring algorithms under development in Hyderabad.
