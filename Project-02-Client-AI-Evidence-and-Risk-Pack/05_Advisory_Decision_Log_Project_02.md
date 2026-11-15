# Advisory Decision Log: Project 02 (Client Evidence & Risk Pack)

This log explains key design choices in the `Enterprise AI Due-Diligence & Evidence Pack`.

---

## Decision 01: Attaching Concrete Artefact IDs Instead of Narrative Promises
* **Context:** Vendors frequently answer buyer questionnaires with vague statements like *"We take AI ethics seriously and follow best practices."* Enterprise TPRM reviewers reject unsubstantiated prose.
* **Decision:** Structured every section of `Project 02` around verifiable **Evidence References** (`UI screenshot IDs`, `DPA ZDR clauses`, `HITL SOP references`, and `24-hour incident SLAs`).
* **Reasoning:** Procurement reviewers score vendors on auditability. Pointing to a specific document ID reduces follow-up clarification rounds by 60–70%.

## Decision 02: Dual-Mapping EU Regulations (GDPR / EU AI Act) with India DPDP Act Safeguards
* **Context:** Indian SaaS companies and GCCs operate engineering/support teams in India while serving EU/US customers.
* **Decision:** Embedded both **EU GDPR / EU AI Act** and **India DPDP Act** data-processing and retention checks into Section 5 of the Evidence Pack.
* **Reasoning:** Cross-border enterprise buyers explicitly audit how Indian delivery centers handle personal data during support, debugging, and model evaluation. Addressing both jurisdictions proactively demonstrates operational maturity.

## Decision 03: Separating Pre-Submission Legal/Risk Sign-Off (`03_Enterprise_Buyer_Evidence_Checklist.md`)
* **Context:** Sales and account teams under quarter-end pressure often over-promise capabilities on security questionnaires.
* **Decision:** Created a mandatory 6-point pre-submission checklist requiring Risk/Legal verification of ZDR status and named human accountability before external release.
* **Reasoning:** Preventing inaccurate representations on buyer security questionnaires protects the company from contractual breach and regulatory misrepresentation claims.
