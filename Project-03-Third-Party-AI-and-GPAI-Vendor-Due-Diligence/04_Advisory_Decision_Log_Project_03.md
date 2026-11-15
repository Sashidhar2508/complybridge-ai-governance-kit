# Advisory Decision Log: Project 03 (Third-Party AI & GPAI Vendor Due-Diligence)

This log documents the legal, procurement, and IP reasoning behind key evaluation criteria in `Project 03`.

---

## Decision 01: Carving Patent & Copyright Indemnity Out of Standard 12-Month Fee Caps
* **Context:** Most SaaS Master Services Agreements cap total vendor liability at 12 months of fees paid. In an AI procurement review, an enterprise buyer's patent/IP litigation exposure can easily exceed millions of euros.
* **Decision:** Required upstream foundation model providers (or cloud hosts like Azure/AWS) to provide explicit third-party **patent and copyright indemnification** carved out from low standard fee caps.
* **Reasoning:** If a downstream enterprise customer is sued over patent infringement embedded in an upstream model's architecture or unmodified outputs, a 12-month API fee cap leaves the Indian SaaS vendor absorbing catastrophic legal defense costs.

## Decision 02: Treating Open-Weights Models as "Self-Insured" for Patent/IP Risk
* **Context:** Engineering teams frequently view open-weights models (Llama, Mistral, Qwen) as "free and risk-free" because they run inside the company's own VPC.
* **Decision:** Scored self-hosted open-weights models as **Medium Risk** on IP/Patent Indemnity in `01_Third_Party_AI_Vendor_Scorecard.csv` and required Legal license review before commercial product deployment.
* **Reasoning:** While VPC hosting solves data egress and ZDR completely, open-weights releases rarely include upstream vendor patent indemnification—meaning the deploying SaaS company assumes direct IP clearance responsibility.

## Decision 03: Enforcing a Pre-Filing Patent Novelty Boundary on R&D AI Tools
* **Context:** R&D teams routinely paste code snippets, circuit architectures, and algorithm specs into coding assistants.
* **Decision:** Made active Enterprise ZDR + zero-human-review mandatory before any R&D engineer can use an external AI tool.
* **Reasoning:** Under patent law in India, the EU, and the US, non-confidential disclosure of an invention prior to patent filing can destroy novelty. Treating non-ZDR prompts as external disclosures protects future patent filings.
