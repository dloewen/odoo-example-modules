# Odoo Example Modules

Small, self-contained examples of common Odoo customizations. Each Odoo version lives on its own branch (`17.0`,
`18.0`, `19.0`, `20.0`).

| Module                   | Example                                                       |
| ------------------------ | ------------------------------------------------------------- |
| `add_pivot`              | Add a pivot view to an existing model and action              |
| `field_widgets`          | A custom OWL field widget                                     |
| `js_patching`            | Patching objects, component methods and static properties     |
| `model_field_validation` | Validate a field with `@api.constrains`                       |
| `notifications`          | Send a real-time notification to the user                     |
| `settings_field`         | Add fields to the Settings app (config parameter and company) |
| `view_extensions`        | Extend a form view, an OWL template (chatter) and a report    |
| `wizard_file_upload`     | Upload a file through a wizard                                |

## Development

```bash
pip install -r requirements.txt
pre-commit install
pre-commit run --all-files
```

## Testing

Each module has a `tests/` folder. Run them with odoo-bin, for example:

```bash
odoo-bin -c odoo.conf -d test_db -i add_pivot,field_widgets,js_patching,model_field_validation,notifications,settings_field,view_extensions,wizard_file_upload \
  --test-enable --test-tags=/add_pivot,/field_widgets,/js_patching,/model_field_validation,/notifications,/settings_field,/view_extensions,/wizard_file_upload \
  --stop-after-init
```

Browser tests (`HttpCase`) need Google Chrome or Chromium and the `websocket-client` Python package, otherwise they
are skipped.
