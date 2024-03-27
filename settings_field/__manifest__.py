{
    "name": "Odoo 16 Example - Adding a Settings field",
    "summary": "An example of how to add a field to the Settings app.",
    "description": """
    Important: before running Odoo, please note that this module adds a field
    to the res.company model, which requires a module upgrade via command line,
    using odoo-bin with the -u flag, for example:
    ./odoo-bin --config odoo.conf --database=my_db_name --update=my_module_name
    Otherwise, Odoo will not start.
    """,
    "author": "Derek Loewen",
    "website": "https://myles.consulting",
    "category": "Customizations",
    "license": "AGPL-3",
    "version": "0.1",
    "depends": ["sale"],
    "auto_install": False,
    "data": [
        "views/res_config_settings.xml"
    ],
}
