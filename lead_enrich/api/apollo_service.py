# Copyright (c) 2025, surendhra.erpnext@gmail.com and contributors
# For license information, please see license.txt
import frappe
import requests

@frappe.whitelist()
def enrich_single_lead(lead_name):
    lead = frappe.get_doc("Lead", lead_name)

    # get settings
    settings = frappe.get_single("Apollo Settings")
    api_key = settings.get_password("apollo_api_key")
    base_url = settings.base_url.rstrip("/")

    if not api_key:
        frappe.throw("Apollo API Key missing in Apollo Settings")

    # build URL
    url = f"{base_url}/people/match"

    params = {
        "email": lead.email_id or "",
        "first_name": lead.lead_name.split(" ")[0] if lead.lead_name else "",
        "last_name": lead.lead_name.split(" ")[-1] if lead.lead_name else "",
        "reveal_personal_emails": "false",
        "reveal_phone_number": "false"
    }

    headers = {
        "accept": "application/json",
        "Cache-Control": "no-cache",
        "Content-Type": "application/json",
        "x-api-key": api_key
    }

    try:
        r = requests.post(url, headers=headers, params=params)
        r.raise_for_status()
    except Exception:
        frappe.db.set_value("Lead", lead_name, "apollo_enrichment_status", "Error")
        frappe.db.commit()
        return {"status": "error"}

    data = r.json()
    person = data.get("person")

    if not person:
        frappe.db.set_value("Lead", lead_name, "apollo_enrichment_status", "Not Found")
        frappe.db.commit()
        return {"status": "not_found"}

    # map fields
    frappe.db.set_value("Lead", lead_name, "apollo_person_id", person.get("id"))
    frappe.db.set_value("Lead", lead_name, "linkedin_profile_url", person.get("linkedin_url"))
    frappe.db.set_value("Lead", lead_name, "apollo_job_title", person.get("headline"))

    # industry
    industry = person.get("organization", {}).get("industry")
    frappe.db.set_value("Lead", lead_name, "apollo_industry", industry)

    # company size
    company_size = person.get("organization", {}).get("estimated_num_employees")
    frappe.db.set_value("Lead", lead_name, "company_size", company_size)

    # status
    frappe.db.set_value("Lead", lead_name, "apollo_enrichment_status", "Found")
    frappe.db.commit()

    return {"status": "found", "apollo_person_id": person.get("id")}
    return {"status": apollo_status, "message": "Apollo enrichment completed"}
    return {"status": "ok"}

