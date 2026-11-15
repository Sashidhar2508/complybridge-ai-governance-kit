# EU AI Act & NIST AI RMF Classification Decision Guide

Use this 4-step decision workflow whenever a business unit proposes or procures a new AI/ML or Generative AI system.

---

## Step 1: Determine Your Regulatory Role (`Provider` vs. `Deployer`)
* **Provider:** Your organization develops the AI system (or fine-tunes/brands a foundation model) and places it on the market or into service under its own name for customers.
* **Deployer:** Your organization licenses or uses an existing third-party AI tool under its own authority for internal business operations (e.g., HR screening, marketing, code assistance).

---

## Step 2: Screen for Prohibited Practices (EU AI Act Article 5 — In Force Feb 2025)
Immediately flag and halt any system involving:
* Workplace or educational emotion recognition (unless strictly for medical or safety reasons).
* Social scoring or untargeted scraping of facial images to build recognition databases.
* Subliminal manipulation or exploitation of age/disability vulnerabilities.

---

## Step 3: Classify Risk Tier (Article 6, Annex III & Article 50)
1. **High-Risk (Annex III):** Systems used in recruitment/HR evaluation, creditworthiness/credit scoring, biometric categorization, critical infrastructure, education admissions, or essential public services.
   * *Note on FRIA (Article 27):* Private deployers must complete a formal **Fundamental Rights Impact Assessment (FRIA)** specifically when deploying AI for **credit scoring** or **life/health insurance risk pricing** (in addition to public-service deployers). HR deployers should complete a GDPR DPIA, algorithmic bias review, and Article 26 human-oversight controls.
2. **Limited Risk (Transparency Obligations — Article 50):**
   * Direct end-user conversational chatbots (`Art. 50(1)`): Must disclose AI interaction upfront unless obvious from context.
   * Synthetic audio, image, video, or deepfake generation (`Art. 50(2)` & `50(4)`): Providers must embed machine-readable markings; deployers must label deepfakes or unreviewed public-interest synthetic text.
3. **Minimal Risk:** Internal workflow tools (OCR, churn analytics, spam filters, IDE coding assistants). Subject to general **Article 4 AI Literacy** and internal data-security hygiene.

---

## Step 4: Assign NIST AI RMF 1.0 Focus & Review Cadence
* **GOVERN:** Assign an accountable business owner, AI literacy training, and acceptable-use policy.
* **MAP:** Document intended purpose, affected stakeholders, and data lineage (including India DPDP Act consent/notice checks).
* **MEASURE:** Establish accuracy, hallucination, and demographic fairness metrics before production launch.
* **MANAGE:** Implement human-in-the-loop (HITL) override triggers, kill-switches, and semi-annual inventory reviews.
