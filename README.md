# Odoo CRM & UTM Integration (Week 1 Assignment)

A custom Odoo module and external web form integration designed to capture student admission enquiries directly into Odoo CRM with dynamic UTM tracking.

## Features
* **Custom Odoo Addon (`odoo_crm_assignment`):** Exposes a public HTTP controller route at `/api/external-enquiry` to receive JSON/form posts.
* **Lead Generation:** Creates leads under the `New Enquiry` stage in `crm.lead`.
* **UTM & Source Tracking:** Captures `utm_source`, `utm_medium`, `utm_campaign`, and `landing_page_url` dynamically from the form URL and stores them in the lead description.
* **5-Stage Pipeline Support:** Configured for `New Enquiry` -> `Contacted` -> `Counselling` -> `Application` -> `Admitted`.

## Project Structure
```text
.
├── custom_addons/
│   └── odoo_crm_assignment/    # Custom Odoo module
│       ├── __init__.py
│       ├── __manifest__.py
│       └── controllers.py       # Public HTTP API Controller
├── docker-compose.yml           # Local Odoo 17 setup
├── enquiry.html                 # External HTML enquiry form with UTM JS
└── .gitignore
