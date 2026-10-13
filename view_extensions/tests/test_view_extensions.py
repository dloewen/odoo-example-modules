from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestViewExtensions(HttpCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        partner = cls.env["res.partner"].create({"name": "Test Customer"})
        cls.order = cls.env["sale.order"].create({"partner_id": partner.id})

    def test_form_view(self):
        arch = self.env["sale.order"].get_views([(False, "form")])["views"]["form"]["arch"]
        self.assertIn('name="my_tab"', arch)
        self.assertIn('string="Customer PO"', arch)

    def test_report(self):
        html = self.env["ir.actions.report"]._render_qweb_html("sale.action_report_saleorder", self.order.ids)[0]
        self.assertIn(b"My Info", html)

    def test_chatter_button(self):
        self.browser_js(
            f"/odoo/sale.order/{self.order.id}",
            "console.log('test successful')",
            "!!document.querySelector('.o-mail-Chatter-myButton')",
            login="admin",
        )
