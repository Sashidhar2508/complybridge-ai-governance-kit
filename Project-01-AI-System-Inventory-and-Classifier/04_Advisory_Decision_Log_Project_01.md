# Advisory Decision Log: Project 01 (AI System Inventory & Classification)

This log documents the regulatory reasoning behind key classification decisions in `Project 01` so risk reviewers and hiring managers can inspect the judgment behind the register.

---

## Decision 01: Separating `Provider` vs. `Deployer` Duties on the Same Register
* **Context:** Many mid-sized SaaS companies lump internal productivity tools (HR screeners, coding assistants) together with customer-facing AI product features.
* **Decision:** Added an explicit `EU AI Act Role (Provider / Deployer)` column to the master register.
* **Reasoning:** Under the EU AI Act, a **Provider** placing an Annex III system on the market bears heavy pre-market conformity, technical documentation, and quality-management obligations (`Articles 9–17`), whereas a **Deployer** using an off-the-shelf HR tool bears targeted operational duties (`Article 26`: human oversight, input-data relevance, and worker notice). Conflating the two leads to either massive over-engineering on internal tools or dangerous under-compliance on commercial features.

## Decision 02: Restricting Article 27 FRIA to Credit Scoring (`AI-007`) Rather Than Private HR Screening (`AI-001`)
* **Context:** Many generic governance checklists tell every private company using an AI resume screener to conduct a Fundamental Rights Impact Assessment (FRIA).
* **Decision:** Assigned an **Article 27 FRIA** to `AI-007` (Automated Credit Limit Decision Tool) while assigning a **GDPR DPIA, algorithmic bias audit, and Article 26 human-oversight controls** to `AI-001` (Candidate Resume Screening Tool).
* **Reasoning:** Under EU AI Act Article 27(1), mandatory FRIAs apply to bodies governed by public law, private entities providing public services, and private deployers specifically deploying Annex III systems for **creditworthiness evaluation/credit scoring** (Point 5(b)) or **life/health insurance risk pricing** (Point 5(c)). Applying statutory precision builds immediate credibility with legal counsel.

## Decision 03: Treating Unmanaged Coding Assistants (`VF-06`) as an IP/Patent Priority Despite Minimal EU AI Act Risk
* **Context:** Under the EU AI Act, an internal IDE coding assistant is **Minimal Risk**.
* **Decision:** Flagged unmanaged public-tier usage for immediate remediation under **IP and Patent Hygiene**.
* **Reasoning:** Even when statutory AI risk is minimal, engineers pasting proprietary algorithms or unpatented product logic into non-ZDR services create irreversible trade-secret exposure and potential loss of patent novelty.
