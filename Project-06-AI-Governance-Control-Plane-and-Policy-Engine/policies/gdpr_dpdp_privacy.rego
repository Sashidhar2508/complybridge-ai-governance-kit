package complybridge.privacy_and_residency

import rego.v1

# GDPR (Regulation (EU) 2016/679 — Irish DPC Standard) & India DPDP Act 2023

default allow := false

approved_eea_regions := {"eu-west-1", "eu-central-1"}
approved_global_regions := {"eu-west-1", "eu-central-1", "ap-south-1"}

allow if {
    count(deny) == 0
}

deny contains msg if {
    input.model_supply_chain.zero_data_retention_zdr != true
    msg := "CRITICAL [GDPR Art. 28 & India DPDP | Fine up to EUR 20M or 4%]: Upstream foundation model endpoint does not enforce Zero-Data-Retention (ZDR)."
}

deny contains msg if {
    input.sector_profile.strict_eea_residency == true
    some region in input.model_supply_chain.active_regions
    not region in approved_eea_regions
    msg := sprintf("CRITICAL [GDPR Art. 44 Cross-Border Transfer]: Unapproved non-EEA inference region '%s' detected for EU regulated workload.", [region])
}

deny contains msg if {
    input.sector_profile.strict_eea_residency != true
    some region in input.model_supply_chain.active_regions
    not region in approved_global_regions
    msg := sprintf("BLOCK [Data Residency Drift]: Unapproved inference region '%s' outside governance boundary.", [region])
}

deny contains msg if {
    input.governance_artifacts.dpia_completed != true
    msg := "BLOCK [GDPR Art. 35 / Irish DPC 6-Step DPIA]: Data Protection Impact Assessment missing or unsigned."
}

deny contains msg if {
    input.runtime_controls.automated_adverse_decision_prohibited != true
    msg := "CRITICAL [GDPR Art. 22]: Solely automated adverse decisions affecting natural persons are not blocked."
}
