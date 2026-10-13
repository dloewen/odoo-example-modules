{
    "name": "Odoo 18 Example - Patching JavaScript",
    "summary": "An example of various patching methods in JS.",
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "18.0.1.0.0",
    "depends": ["web", "mail"],
    "auto_install": False,
    "assets": {
        "web.assets_backend": [
            "js_patching/static/src/**/*.js",
        ],
    },
}
