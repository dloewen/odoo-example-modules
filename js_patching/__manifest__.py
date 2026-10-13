{
    "name": "Odoo 17 Example - Patching JavaScript",
    "summary": "An example of various patching methods in JS.",
    "description": """
    See Odoo documentation for more details:
    https://www.odoo.com/documentation/17.0/developer/reference/frontend/patching_code.html
    """,
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    "depends": ["web", "mail"],
    "auto_install": False,
    "assets": {
        "web.assets_backend": [
            "js_patching/static/src/**/*.js",
        ],
    },
}
