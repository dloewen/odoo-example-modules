{
    "name": "Odoo 16 Example - Field Widgets",
    "summary": "Examples of a custom field widgets using the OWL framework",
    "description": """
    See Odoo documentation for more details:
    https://www.odoo.com/documentation/16.0/developer/tutorials/master_odoo_web_framework/01_fields_and_views.html
    """,
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "0.1",
    "depends": ["web"],
    "auto_install": False,
    "assets": {
        "web.assets_backend": [
            "field_widgets/static/src/components/**/*",
        ],
    },
}
