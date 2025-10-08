{
    "name": "Odoo 18 Example - Field Widgets",
    "summary": "Examples of a custom field widgets using the OWL framework",
    "description": """
    See Odoo documentation for more details:
    https://www.odoo.com/documentation/18.0/developer/howtos/javascript_field.html
    """,
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "depends": ["web"],
    "auto_install": False,
    "assets": {
        "web.assets_backend": [
            "field_widgets/static/src/components/**/*",
        ],
    },
}
