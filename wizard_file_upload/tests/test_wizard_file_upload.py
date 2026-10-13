import base64

from odoo.tests import TransactionCase, new_test_user, tagged


@tagged("post_install", "-at_install")
class TestWizardFileUpload(TransactionCase):
    def test_import_csv(self):
        user = new_test_user(self.env, login="wizard_user", groups="base.group_user")
        wizard = (
            self.env["my.import.wizard"]
            .with_user(user)
            .create({"csv_file": base64.b64encode(b"name\nfoo\n"), "file_name": "items.csv"})
        )
        with self.assertLogs("odoo.addons.wizard_file_upload.wizard.my_import_wizard") as logs:
            wizard.import_csv()
        self.assertIn("items.csv (9 bytes)", logs.output[0])
