# Copyright (c) 2025, surendhra.erpnext@gmail.com and contributors
# For license information, please see license.txt

import frappe

@frappe.whitelist()
def enrich_single_lead(lead_name):
    # read settings
    settings = frappe.get_single("Apollo Settings")

    if not settings.active:
        frappe.throw("Apollo Integration is disabled in Apollo Settings")

    api_key = settings.apollo_api_key
    base_url = settings.base_url or "https://api.apollo.io/v1"

    # placeholder — REAL API CALL will be done later
    doc = frappe.get_doc("Lead", lead_name)
    doc.apollo_enrichment_status = "Not Attempted"
    doc.save(ignore_permissions=True)

    return {
        "status": "ok",
        "message": f"Triggered enrichment for {lead_name}"
    }
