#!/usr/bin/env python3
"""
ComplyBridge Enterprise AI Governance Policy Engine (Project 06)
Evaluates all 4 enterprise AI system manifests against EU AI Act (Reg. (EU) 2024/1689 +
Digital Omnibus Reg. (EU) 2026/1744), DORA (Reg. (EU) 2022/2554 / Central Bank of Ireland),
GDPR (Irish DPC 6-Step DPIA), ISO/IEC 42001, NIST AI RMF 1.0, and India DPDP rules.
Generates RELEASE_AUDIT_EVIDENCE.md for CI/CD release sign-off.
"""

import glob
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_DIR = os.path.join(BASE_DIR, "manifests")
REPORT_PATH = os.path.join(BASE_DIR, "RELEASE_AUDIT_EVIDENCE.md")

APPROVED_EEA_REGIONS = {"eu-west-1", "eu-central-1"}
APPROVED_GLOBAL_REGIONS = {"eu-west-1", "eu-central-1", "ap-south-1"}


def evaluate_manifest(m: dict) -> list[str]:
    violations = []

    # 1. EU AI Act Art. 5 & Art. 50
    if m["regulatory_classification"].get("article_5_prohibited_check") != "PASSED":
        violations.append("CRITICAL [EU AI Act Art. 5 | EUR 35M / 7%]: Prohibited practice check failed.")

    if not m["runtime_controls"].get("art50_1_upfront_disclosure"):
        violations.append("BLOCK [EU AI Act Art. 50(1) — Live since 2 Aug 2026 | EUR 15M / 3%]: Upfront AI interaction notice disabled.")

    if m["capabilities"].get("generates_synthetic_content") and not m["runtime_controls"].get("art50_2_c2pa_watermarking"):
        violations.append("BLOCK [EU AI Act Art. 50(2) — 2 Dec 2026 Cliff | EUR 15M / 3%]: Missing machine-readable synthetic content marking.")

    # 2. EU AI Act Annex III High-Risk Controls
    if m["regulatory_classification"].get("is_annex_iii_high_risk"):
        if not m["runtime_controls"].get("art14_human_oversight_hard_stop"):
            violations.append("BLOCK [EU AI Act Annex III & Art. 14]: Missing Human-in-the-Loop hard stop.")
        if not m["governance_artifacts"].get("art27_fria_completed"):
            violations.append("BLOCK [EU AI Act Art. 27]: Fundamental Rights Impact Assessment (FRIA) missing.")
        if not m["runtime_controls"].get("protected_proxy_filtering"):
            violations.append("BLOCK [EU AI Act Art. 10(2)(f)]: Protected attribute / Eircode proxy filtering disabled.")

    # 3. GDPR & India DPDP Privacy / Residency / ZDR
    if not m["model_supply_chain"].get("zero_data_retention_zdr"):
        violations.append("CRITICAL [GDPR Art. 28 & India DPDP | EUR 20M / 4%]: Zero-Data-Retention (ZDR) not enforced.")

    allowed = APPROVED_EEA_REGIONS if m["sector_profile"].get("strict_eea_residency") else APPROVED_GLOBAL_REGIONS
    for reg in m["model_supply_chain"].get("active_regions", []):
        if reg not in allowed:
            violations.append(f"CRITICAL [GDPR Art. 44 Data Residency]: Unapproved region '{reg}' detected.")

    if not m["governance_artifacts"].get("dpia_completed"):
        violations.append("BLOCK [GDPR Art. 35 / Irish DPC DPIA]: DPIA sign-off missing.")

    if not m["runtime_controls"].get("automated_adverse_decision_prohibited"):
        violations.append("CRITICAL [GDPR Art. 22]: Solely automated adverse decisions not prohibited.")

    # 4. DORA Reg. (EU) 2022/2554 (EU Financial Entities)
    if m["sector_profile"].get("is_eu_financial_entity"):
        dora = m.get("dora_controls", {})
        if not dora.get("art28_roi_xbrl_csv_registered"):
            violations.append("BLOCK [DORA Art. 28(3) CBI Portal]: Missing from xBRL-CSV Register of Information.")
        if not dora.get("art30_cbi_audit_addendum_signed"):
            violations.append("BLOCK [DORA Art. 30(2)(e)]: Missing Central Bank of Ireland audit/inspection addendum.")
        if dora.get("vendor_incident_sla_hours", 99) > 2:
            violations.append("BLOCK [DORA Art. 19]: Vendor incident notification SLA > 2h (jeopardizes 4h CBI reporting window).")
        if not dora.get("art28_8_exit_plan_tested"):
            violations.append("BLOCK [DORA Art. 28(8)]: Tested deterministic fallback & 30-day exit strategy unverified.")

    # 5. Faithfulness Threshold
    if m["runtime_controls"].get("measured_faithfulness_score", 0.0) < m["runtime_controls"].get("min_faithfulness_score", 0.90):
        violations.append("BLOCK [NIST AI RMF MEASURE]: Grounded faithfulness score below minimum release threshold.")

    return violations


def run_chaos_self_tests(base_manifest: dict) -> list[tuple[str, bool, str]]:
    """Verifies that the Policy Engine actually catches real DevOps/Governance drift faults."""
    tests = []

    # Fault 1: DevOps swaps endpoint to non-ZDR us-east-1
    f1 = json.loads(json.dumps(base_manifest))
    f1["model_supply_chain"]["zero_data_retention_zdr"] = False
    f1["model_supply_chain"]["active_regions"] = ["us-east-1"]
    v1 = evaluate_manifest(f1)
    tests.append(("Chaos Test 1: Non-ZDR & Non-EEA Region Drift (us-east-1)", len(v1) >= 2, f"Blocked with {len(v1)} statutory violations"))

    # Fault 2: Product team enables autonomous credit rejection
    f2 = json.loads(json.dumps(base_manifest))
    f2["runtime_controls"]["art14_human_oversight_hard_stop"] = False
    f2["runtime_controls"]["automated_adverse_decision_prohibited"] = False
    v2 = evaluate_manifest(f2)
    tests.append(("Chaos Test 2: Autonomous Credit Decline Enabled", len(v2) >= 2, f"Blocked with {len(v2)} EU AI Act Art. 14 / GDPR Art. 22 violations"))

    # Fault 3: Upstream vendor lacks DORA Art. 30 CBI audit clause & exit plan
    f3 = json.loads(json.dumps(base_manifest))
    f3["dora_controls"]["art30_cbi_audit_addendum_signed"] = False
    f3["dora_controls"]["art28_8_exit_plan_tested"] = False
    v3 = evaluate_manifest(f3)
    tests.append(("Chaos Test 3: DORA Art. 28/30 CBI Audit & Exit Breach", len(v3) >= 2, f"Blocked with {len(v3)} DORA violations"))

    return tests


def main() -> int:
    manifest_files = sorted(glob.glob(os.path.join(MANIFEST_DIR, "*.json")))
    if not manifest_files:
        print("ERROR: No system manifests found.")
        return 1

    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    system_summaries = []
    total_violations = 0
    sys01_manifest = None

    for mf in manifest_files:
        with open(mf, "rb") as raw_f:
            sha = hashlib.sha256(raw_f.read()).hexdigest()[:16].upper()
        with open(mf, "r", encoding="utf-8") as f:
            m = json.load(f)
        if m["system_id"] == "SYS-01":
            sys01_manifest = m
        violations = evaluate_manifest(m)
        total_violations += len(violations)
        system_summaries.append((m, sha, violations))

    chaos_results = run_chaos_self_tests(sys01_manifest) if sys01_manifest else []
    chaos_ok = all(passed for _, passed, _ in chaos_results)
    all_clear = (total_violations == 0) and chaos_ok
    verdict = "APPROVED — ALL 4 PRODUCTION SYSTEMS & CHAOS GATES VERIFIED" if all_clear else "RELEASE BLOCKED — GOVERNANCE VIOLATION"

    lines = [
        "# Enterprise AI Governance Control Plane — Automated CI/CD Audit Dossier",
        "",
        f"- **Evaluation Timestamp:** `{now_utc}`",
        f"- **Policy Engine:** `ComplyBridge OPA/Rego + Python Gate Evaluator v3.0`",
        f"- **Regulatory Baseline:** EU AI Act (`Reg. (EU) 2024/1689` + `Digital Omnibus Reg. (EU) 2026/1744`), DORA (`Reg. (EU) 2022/2554`), GDPR / Irish DPC, ISO/IEC 42001, NIST AI RMF 1.0, India DPDP",
        f"- **Overall Release Gate Verdict:** **`{verdict}`**",
        "",
        "---",
        "",
        "## 1. Multi-System Production Governance Inventory",
        "",
        "| System ID | System Name | Regulatory Tier & Active Deadlines | Residency & ZDR | Manifest SHA-256 | Gate Verdict |",
        "| :--- | :--- | :--- | :--- | :--- | :--- |"
    ]

    for m, sha, violations in system_summaries:
        status = "PASS (0 Violations)" if not violations else f"FAIL ({len(violations)} Violations)"
        regions = ", ".join(m["model_supply_chain"]["active_regions"])
        lines.append(
            f"| **`{m['system_id']}` (`{m['code_name']}`)** | {m['system_name']} | {m['regulatory_classification']['risk_tier']} | `{regions}` / ZDR=`{m['model_supply_chain']['zero_data_retention_zdr']}` | `{sha}` | **{status}** |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## 2. Adversarial Policy-Drift & Chaos Verification (Proving Gate Enforcement)",
        "",
        "Before approving clean manifests, the CI/CD engine injects simulated DevOps and product-drift faults to verify that non-compliant releases are deterministically blocked (`exit 1`):",
        "",
        "| Simulated Governance / DevOps Failure | Gate Behavior | Verification Detail |",
        "| :--- | :--- | :--- |"
    ])

    for name, passed, detail in chaos_results:
        lines.append(f"| **{name}** | **{'VERIFIED BLOCK' if passed else 'FAILED TO BLOCK'}** | {detail} |")

    lines.extend([
        "",
        "---",
        "",
        "## 3. Audit & Supervisory Sign-Off Note",
        "",
        "This dossier is auto-generated on every pull request and release build via `.github/workflows/ai-governance-gate.yml`. "
        "It pairs machine-enforceable **Open Policy Agent (OPA / Rego)** rules (`policies/*.rego`) with the interactive **ComplyBridge AI Governance Control Plane** (`https://sashidhar2508.github.io/website/control-plane.html`)."
    ])

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("=" * 80)
    print(f"COMPLYBRIDGE ENTERPRISE POLICY ENGINE  |  {verdict}")
    print("=" * 80)
    for m, sha, violations in system_summaries:
        print(f"[{'PASS' if not violations else 'FAIL'}] {m['system_id']} ({m['code_name']}) — {m['system_name']} [SHA: {sha}]")
    for name, passed, detail in chaos_results:
        print(f"[{'PASS' if passed else 'FAIL'}] {name} -> {detail}")
    print("=" * 80)

    return 0 if all_clear else 1


if __name__ == "__main__":
    sys.exit(main())
