### Lead Enrich

Apollo.io Lead Enrich integration with ERPNext

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app lead_enrich
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/lead_enrich
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### CI

This app can use GitHub Actions for CI. The following workflows are configured:

- CI: Installs this app and runs unit tests on every push to `develop` branch.
- Linters: Runs [Frappe Semgrep Rules](https://github.com/frappe/semgrep-rules) and [pip-audit](https://pypi.org/project/pip-audit/) on every pull request.


### License

gpl-3.0
************************************************************************************************************************************************************
# Lead Enrich App (Apollo.io Integration for ERPNext)

### Overview

The **Lead Enrich** custom app is designed to integrate **Apollo.io** APIs with **ERPNext CRM** (Lead Doctype).  
It enables users to enrich Lead records using Apollo's data — such as job title, LinkedIn profiles, company size, and more — directly inside ERPNext.

This app is built as a separate module (standalone app) so it does not interfere with your existing `realapp` or ERPNext core.

---

## What This App Provides

| Feature | Description |
|--------|-------------|
| Manual Lead Enrichment Button | A button on the Lead form to trigger enrichment for one Lead |
| Bulk Lead Enrichment | Action button in ListView to enrich multiple selected Leads |
| Apollo Settings Doctype | Settings screen for user to enter Apollo API Key |
| Custom Fields in Lead | Stores Apollo-based data (LinkedIn, Apollo Job Title etc) |
| API-based design | Reads settings + triggers Python logic for enrichment |

---

## Technical Building Blocks

| Component | Location | Purpose |
|----------|----------|---------|
| Custom Fields Fixture | `/lead_enrich/lead_enrich/fixtures/custom_field.json` | Adds Apollo fields to Lead |
| Apollo Settings Doctype | `/lead_enrich/lead_enrich/lead_enrich/doctype/apollo_settings/` | Stores Apollo API key |
| Python API logic | `/lead_enrich/lead_enrich/api/apollo_service.py` | Handles enrichment actions |
| Client-side JS | `/lead_enrich/lead_enrich/public/js/*.js` | Buttons and UI triggers |
| hooks.py | root of app | binds JS + fixtures to Lead Doctype |

---

## Flow Summary

```
Lead Created / Existing Lead
       |
User clicks "Enrich via Apollo"
       |
Python function → checks Apollo Settings
       |
Actual API call (future step)
       |
Lead updated with Apollo data fields
```

---

## Why This App Is Designed This Way

| Decision | Reason |
|----------|--------|
| Separate app | better maintainability |
| API key stored in Doctype | editable via UI by admins |
| JS in `public/js` | version control friendly |
| No auto-enrich | avoids token waste |
| Bulk List Action planned | improves efficiency for sales teams |

---

## Next Steps

| Step | Status |
|------|--------|
| Custom Fields | ✅ DONE |
| Apollo Settings Doctype | ✅ DONE |
| Single Lead Button | ✅ DONE |
| Bulk Action Button | ⏳ NEXT |
| Real Apollo API calls | ⏳ after API key provided |

---

## Intended Audience

| User Type | Benefit |
|----------|----------|
| CRM Users | Can enrich any lead on demand |
| Pre-sales | Validate unknown leads faster |
| Developers | Extend Lead scoring / Data models |

---

## Final Notes

- This is a foundation layer for enrichment
- Apollo API calls will be plugged in when API Key is available
- Design is modular → future expansion clean

**This document is suitable for internal teams / project documentation / onboarding new developers into this app**
