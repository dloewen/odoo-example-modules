{
    "name": "Odoo 18 Example - View Extensions",
    "summary": "Examples of extending views and templates",
    "description": """
This module demonstrates various methods of extending Odoo views and templates.

Admin Views
-----------
These are used for Odoo admin interface, including list, form, graph, pivot, search views.

Documentation: https://www.odoo.com/documentation/18.0/developer/reference/user_interface/view_records.html#reference-view-records-inheritance

QWeb Templates
--------------
Used for JavaScript widget views and website/customer portal templates.

Documentation: https://www.odoo.com/documentation/18.0/developer/reference/frontend/qweb.html#template-inheritance

QWeb Reports
------------
Used for PDF reports, for example, sale order printouts.

Documentation: https://www.odoo.com/documentation/18.0/th/developer/reference/backend/reports.html
    """,
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "depends": ["web", "mail", "sale"],
    "auto_install": False,
    "data": [
        "reports/sale_order_reports.xml",
        "views/sale_order_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "view_extensions/static/src/**/*",
        ],
    },
}
