package complybridge.eu_ai_act

import rego.v1

# EU AI Act (Regulation (EU) 2024/1689 as amended by Digital Omnibus Reg. (EU) 2026/1744)
# Enforceable Milestones Checked:
#   - Art. 5 Prohibited Practices (in force 2 Feb 2025; expanded 2 Dec 2026) -> Max Fine: EUR 35M / 7%
#   - Art. 50(1) Interactive AI Transparency (in force 2 Aug 2026) -> Max Fine: EUR 15M / 3%
#   - Art. 50(2) Machine-Readable Synthetic Content Marking (2 Dec 2026 cliff) -> Max Fine: EUR 15M / 3%
#   - Annex III High-Risk Controls (Art. 10, 12, 14, 27 FRIA ahead of 2 Dec 2027) -> Max Fine: EUR 15M / 3%

default allow := false

allow if {
    count(deny) == 0
}

deny contains msg if {
    input.regulatory_classification.article_5_prohibited_check != "PASSED"
    msg := "CRITICAL [EU AI Act Art. 5 | Fine up to EUR 35M or 7%]: System has not cleared Article 5 prohibited-practice screening."
}

deny contains msg if {
    input.runtime_controls.art50_1_upfront_disclosure != true
    msg := "BLOCK [EU AI Act Art. 50(1) — Enforced since 2 Aug 2026 | Fine up to EUR 15M or 3%]: Upfront human-facing AI interaction notice is disabled."
}

deny contains msg if {
    input.capabilities.generates_synthetic_content == true
    input.runtime_controls.art50_2_c2pa_watermarking != true
    msg := "BLOCK [EU AI Act Art. 50(2) — 2 Dec 2026 Grace Period Cliff | Fine up to EUR 15M or 3%]: Machine-readable synthetic content marking (C2PA / watermark) missing."
}

deny contains msg if {
    input.regulatory_classification.is_annex_iii_high_risk == true
    input.runtime_controls.art14_human_oversight_hard_stop != true
    msg := "BLOCK [EU AI Act Annex III & Art. 14 | Fine up to EUR 15M or 3%]: High-risk system lacks mandatory Human-in-the-Loop hard stop on adverse decisions."
}

deny contains msg if {
    input.regulatory_classification.is_annex_iii_high_risk == true
    input.governance_artifacts.art27_fria_completed != true
    msg := "BLOCK [EU AI Act Art. 27 FRIA]: Fundamental Rights Impact Assessment not signed off prior to high-risk deployment."
}

deny contains msg if {
    input.regulatory_classification.is_annex_iii_high_risk == true
    input.runtime_controls.protected_proxy_filtering != true
    msg := "BLOCK [EU AI Act Art. 10(2)(f) Data Governance]: Protected demographic and geographic proxy filters (e.g. Eircode, nationality, gender) are not enforced."
}
