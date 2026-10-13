from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestNotifications(TransactionCase):
    def test_notification_sent(self):
        self.env["res.partner"].create({"name": "Test"}).action_test_notification()
        self.assertIn("simple_notification", str(self.env.cr.precommit.data.get("bus.bus.values")))
