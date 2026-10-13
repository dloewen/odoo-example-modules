=======================
Adding a Settings field
=======================

This module adds a field to the res.company model. When adding a field like this to a module
that is already installed, upgrade the module from the command line before starting Odoo,
otherwise Odoo will not start::

    ./odoo-bin --config odoo.conf --database=my_db_name --update=my_module_name
