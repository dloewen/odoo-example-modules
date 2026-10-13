from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestSettingsField(TransactionCase):
    def test_settings_saved(self):
        user = self.env.ref("base.user_admin")
        self.env["res.config.settings"].create(
            {"my_notification_user_id": user.id, "my_company_text": "Hello"}
        ).execute()

        self.assertEqual(self.env["ir.config_parameter"].sudo().get_int("my_notification_user_id"), user.id)
        self.assertEqual(self.env.company.my_company_text, "Hello")

    def test_settings_view(self):
        arch = self.env["res.config.settings"].get_views([(False, "form")])["views"]["form"]["arch"]
        self.assertIn('name="my_notification_user_id"', arch)
        self.assertIn('name="my_company_text"', arch)

    def test_example_method(self):
        user = self.env.ref("base.user_admin")
        self.env["ir.config_parameter"].sudo().set_int("my_notification_user_id", user.id)
        self.env.company.my_company_text = "Hello"
        order = self.env["sale.order"].create({"partner_id": self.env["res.partner"].create({"name": "C"}).id})

        with self.assertLogs("odoo.addons.settings_field.models.sale_order") as logs:
            order.my_example_method()
        self.assertIn(f"res.users({user.id},)", logs.output[0])
        self.assertIn("Hello", logs.output[1])
