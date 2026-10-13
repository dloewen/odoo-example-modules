{
    "name": "Odoo 20 Example - View Extensions",
    "summary": "Examples of extending views and templates",
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "20.0.1.0.0",
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
