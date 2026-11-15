# Vendor Zero-Data-Retention (ZDR), Patent & IP Contract Checklist

Use this checklist with Legal and Procurement before signing an Enterprise AI Addendum or onboarding a third-party foundation model API.

---

## 1. Zero-Data-Retention (ZDR) & Training Opt-Out
* **No Model Training:** Vendor contractually warrants that Customer Inputs (prompts, fine-tuning datasets, RAG documents) and Customer Outputs are never used to train, fine-tune, or improve foundation models.
* **Zero-Day Log Retention:** For regulated or patent-sensitive workflows, automated abuse-monitoring human review and 30-day prompt logging are disabled via a signed ZDR addendum.
* **Sub-Processor Lock:** Vendor cannot route inference traffic to undisclosed third-party model hosts without prior written notice.

---

## 2. Patent & Copyright Indemnification Clauses
* **Third-Party Patent & Copyright Defense:** Vendor agrees to defend and indemnify Customer against third-party claims alleging that the underlying foundation model, inference architecture, or unmodified model outputs infringe a valid **patent, copyright, or trade secret**.
* **Uncapped or Super-Cap IP Liability:** Patent and copyright infringement indemnification is carved out from standard low fee caps (e.g., 12-month subscription fees).
* **Customer Output Ownership:** Vendor assigns all right, title, and interest in Customer Outputs to Customer and waives any claim over derivative software code, technical designs, or patentable inventions generated using the service.

---

## 3. Patent Novelty & Trade-Secret Protection (Internal Policy Rule)
* **Pre-Filing Patent Bar Warning:** R&D, hardware, and software engineers must never submit unfiled patent disclosures, invention blueprints, or proprietary source code into any AI service lacking an active Enterprise ZDR agreement.
* **Open-Weights License Clearance:** Before deploying open-weights models in commercial products, Legal must verify whether the model license includes a **patent grant** (e.g., Apache 2.0) or restrictive acceptable-use / defensive-termination triggers.

---

## 4. Cross-Border Data Residency & India DPDP Act Compliance
* **Regional Endpoints:** Inference endpoints are pinned to approved cloud regions (`ap-south-1`, `central-india`, or `eu-central-1` / `eu-west-1`).
* **Processor Obligations:** Vendor executes a Data Processing Addendum (DPA) supporting **India DPDP Act** security safeguards and **EU GDPR Standard Contractual Clauses (SCCs)** where personal data is processed.
