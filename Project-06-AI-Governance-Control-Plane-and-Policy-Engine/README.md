# Project 06: Enterprise AI Governance Control Plane & Policy-as-Code Engine

**Live Interactive Control Plane (Zero Localhost — Hosted 24/7):** **[https://sashidhar2508.github.io/website/control-plane.html](https://sashidhar2508.github.io/website/control-plane.html)**  
**Advisory Release Window:** November 2026 – Present  
**Regulatory Baseline:** EU AI Act (`Regulation (EU) 2024/1689` + `Digital Omnibus Regulation (EU) 2026/1744`), DORA (`Regulation (EU) 2022/2554` / Central Bank of Ireland supervision), GDPR (`Irish DPC 6-Step DPIA` & `Art. 22`), ISO/IEC 42001 AIMS, NIST AI RMF 1.0, and India DPDP Act.

---

## Why This Exists (The Governance-Engineering Bridge)

Enterprise AI deployments rarely fail because engineers cannot call an LLM API. They fail audits, lose multi-million-euro enterprise deals, and trigger regulatory investigations because **infrastructure drift and product shortcuts collide with overlapping statutory deadlines**:
- **EU AI Act Article 50(1)** interactive transparency has been **legally enforceable since 2 August 2026**, while the **Article 50(2)** synthetic content marking grace period expires on **2 December 2026** (fines up to **€15M / 3% global turnover**).
- **EU AI Act Annex III High-Risk obligations** (credit scoring under `5(b)`, HR recruitment under `4(a)`) hit on **2 December 2027**, requiring **Article 14 human oversight**, **Article 12 logging**, and **Article 27 FRIAs** to be architected into pipelines now.
- **DORA (`Regulation (EU) 2022/2554`)** is **actively enforced** by the **Central Bank of Ireland**, requiring **Article 28 xBRL-CSV Register of Information** filings, **Article 30 audit/exit clauses**, and **4-hour major ICT incident reporting**.

This repository demonstrates how **Policy-as-Code (OPA / Rego + CI/CD Release Gates)** prevents those failures before code reaches production.

---

## Repository Architecture (No Localhost Required)

| Folder / File | Purpose |
| :--- | :--- |
| **[Live Web Control Plane](https://sashidhar2508.github.io/website/control-plane.html)** | Interactive **Regulatory Blast-Radius & Audit Failure Simulator** across 4 production AI systems (`SYS-01` to `SYS-04`) — zero setup required |
| `RELEASE_AUDIT_EVIDENCE.md` | Auto-generated CI/CD audit dossier verifying all 4 systems + 3 adversarial chaos drift tests |
| `policies/eu_ai_act.rego` | Open Policy Agent (OPA) Rego rules enforcing EU AI Act Art. 5, Art. 50(1)/(2), Art. 10, Art. 14 & Art. 27 |
| `policies/dora_resilience.rego` | OPA Rego rules enforcing DORA Art. 19, Art. 28(3) xBRL-CSV RoI, Art. 28(8) exit plans & Art. 30 CBI audit rights |
| `policies/gdpr_dpdp_privacy.rego` | OPA Rego rules enforcing Zero-Data-Retention (ZDR), EEA residency (`eu-west-1`/`eu-central-1`), GDPR Art. 22 & Art. 35 DPIA |
| `manifests/*.json` | Machine-readable governance manifests for 4 enterprise AI systems (`Dublin IFSC Credit`, `HR Talent Screener`, `B2B Support RAG`, `M&A Synthetic Memo`) |
| `controls/Cross_Framework_Control_Traceability_Matrix.csv` | Cross-framework traceability matrix mapping technical controls to EU AI Act, DORA, GDPR, ISO 42001, NIST RMF & India DPDP |
| `.github/workflows/ai-governance-gate.yml` | Live GitHub Actions CI/CD workflow running `opa check`, `opa eval`, and `engine/validate_governance_gates.py` on every push |
