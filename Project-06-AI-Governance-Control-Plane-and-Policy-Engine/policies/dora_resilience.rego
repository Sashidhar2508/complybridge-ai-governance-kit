package complybridge.dora

import rego.v1

# Digital Operational Resilience Act — DORA Regulation (EU) 2022/2554 (In force since 17 Jan 2025)
# Supervised by Central Bank of Ireland (CBI) & European Supervisory Authorities (ESAs)

default allow := false

allow if {
    count(deny) == 0
}

deny contains msg if {
    input.sector_profile.is_eu_financial_entity == true
    input.dora_controls.art28_roi_xbrl_csv_registered != true
    msg := "BLOCK [DORA Art. 28(3) — Central Bank of Ireland Portal]: AI/ICT third-party arrangement missing from xBRL-CSV Register of Information."
}

deny contains msg if {
    input.sector_profile.is_eu_financial_entity == true
    input.dora_controls.art30_cbi_audit_addendum_signed != true
    msg := "BLOCK [DORA Art. 30(2)(e)]: Missing mandatory contractual audit, inspection, and access rights for Central Bank of Ireland."
}

deny contains msg if {
    input.sector_profile.is_eu_financial_entity == true
    input.dora_controls.vendor_incident_sla_hours > 2
    msg := "BLOCK [DORA Art. 19 Major ICT Incident Reporting]: Vendor notification SLA exceeds 2 hours (jeopardizes 4-hour CBI initial notification window)."
}

deny contains msg if {
    input.sector_profile.is_eu_financial_entity == true
    input.dora_controls.art28_8_exit_plan_tested != true
    msg := "BLOCK [DORA Art. 28(8) Concentration & Exit Risk]: Tested deterministic fallback and 30-day model portability exit strategy not verified."
}
