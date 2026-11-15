# Project 03: Third-Party AI and GPAI Vendor Due-Diligence Kit

**Advisory Release Window:** November 2025 – February 2026  
**Primary Frameworks:** EU AI Act (Chapter V GPAI Obligations, Art. 25, Art. 53), NIST AI RMF 1.0 (`GOVERN 6.1`, `MAP 4.1`), ISO/IEC 42001 (Annex A.10 Third-Party Relationships), India DPDP Act (Data Processor Safeguards), and Enterprise Patent / IP Indemnification Standards  
**Target Audience:** Procurement Leads, Legal Counsel, Technical Account Managers (TAMs), and Technology Risk Teams

---

## Problem Addressed

Most mid-sized Indian SaaS companies and GCCs do not train foundation models from scratch. Instead, they build features on top of third-party APIs (OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Google Vertex AI) or self-host open-weights models (Llama, Mistral, Qwen).

When an enterprise customer audits your product, they look straight through you to your upstream model providers. Common deal-blockers include:
* Engineering teams using consumer or default API tiers where prompts are retained or used for model training.
* Unclear **patent and copyright indemnification** if an enterprise customer is sued over model outputs or underlying model architecture patents.
* Loss of **patent novelty or trade secrets** when R&D teams paste proprietary source code or unpublished inventions into external AI tools.

---

## Files in This Folder

| File Name | Format | Purpose |
| :--- | :--- | :--- |
| `01_Third_Party_AI_Vendor_Scorecard.csv` | CSV (GitHub Table) | Structured 7-category vendor due-diligence scorecard with worked evaluations for 5 common AI deployment patterns |
| `01_Third_Party_AI_Vendor_Scorecard.docx` | Word Document | Executive landscape Word scorecard for vendor onboarding and annual risk reviews |
| `02_Vendor_ZDR_IP_and_Patent_Contract_Clauses.md` | Markdown Legal/GRC Aid | Practical contract checklist covering Zero-Data-Retention (ZDR), Patent Indemnification, Training-Data IP, and India DPDP cross-border rules |
