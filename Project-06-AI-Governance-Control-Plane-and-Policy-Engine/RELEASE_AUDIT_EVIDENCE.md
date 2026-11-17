# Enterprise AI Governance Control Plane — Automated CI/CD Audit Dossier

- **Evaluation Timestamp:** `2026-11-17 05:22:30 UTC`
- **Policy Engine:** `ComplyBridge OPA/Rego + Python Gate Evaluator v3.0`
- **Regulatory Baseline:** EU AI Act (`Reg. (EU) 2024/1689` + `Digital Omnibus Reg. (EU) 2026/1744`), DORA (`Reg. (EU) 2022/2554`), GDPR / Irish DPC, ISO/IEC 42001, NIST AI RMF 1.0, India DPDP
- **Overall Release Gate Verdict:** **`APPROVED — ALL 4 PRODUCTION SYSTEMS & CHAOS GATES VERIFIED`**

---

## 1. Multi-System Production Governance Inventory

| System ID | System Name | Regulatory Tier & Active Deadlines | Residency & ZDR | Manifest SHA-256 | Gate Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`SYS-01` (`FF-06`)** | EmeraldPay Dublin IFSC SME Credit & Fraud Triage Engine | High-Risk AI System (EU AI Act Annex III Point 5(b) — Creditworthiness) | `eu-west-1, eu-central-1` / ZDR=`True` | `31B30E613D986745` | **PASS (0 Violations)** |
| **`SYS-02` (`HR-04`)** | Enterprise Talent Resume & Structured Interview Scoring Copilot | High-Risk AI System (EU AI Act Annex III Point 4(a) — Recruitment & Selection) | `eu-west-1, eu-central-1` / ZDR=`True` | `C5A87EB3492FC15E` | **PASS (0 Violations)** |
| **`SYS-03` (`VF-02`)** | VeloceFlow Multi-Tenant B2B Customer Support RAG Assistant | Limited Risk (EU AI Act Art. 50(1) Transparency — Enforced since 2 Aug 2026) | `eu-west-1, eu-central-1, ap-south-1` / ZDR=`True` | `B1DAE87B6A6F3A55` | **PASS (0 Violations)** |
| **`SYS-04` (`LG-09`)** | M&A Due-Diligence & Synthetic Executive Briefing Generator | Limited Risk — Synthetic Content Marking (EU AI Act Art. 50(2) Cliff: 2 Dec 2026) | `eu-central-1` / ZDR=`True` | `FD1B8FE2830797DA` | **PASS (0 Violations)** |

---

## 2. Adversarial Policy-Drift & Chaos Verification (Proving Gate Enforcement)

Before approving clean manifests, the CI/CD engine injects simulated DevOps and product-drift faults to verify that non-compliant releases are deterministically blocked (`exit 1`):

| Simulated Governance / DevOps Failure | Gate Behavior | Verification Detail |
| :--- | :--- | :--- |
| **Chaos Test 1: Non-ZDR & Non-EEA Region Drift (us-east-1)** | **VERIFIED BLOCK** | Blocked with 2 statutory violations |
| **Chaos Test 2: Autonomous Credit Decline Enabled** | **VERIFIED BLOCK** | Blocked with 2 EU AI Act Art. 14 / GDPR Art. 22 violations |
| **Chaos Test 3: DORA Art. 28/30 CBI Audit & Exit Breach** | **VERIFIED BLOCK** | Blocked with 2 DORA violations |

---

## 3. Audit & Supervisory Sign-Off Note

This dossier is auto-generated on every pull request and release build via `.github/workflows/ai-governance-gate.yml`. It pairs machine-enforceable **Open Policy Agent (OPA / Rego)** rules (`policies/*.rego`) with the interactive **ComplyBridge AI Governance Control Plane** (`https://sashidhar2508.github.io/website/control-plane.html`).
