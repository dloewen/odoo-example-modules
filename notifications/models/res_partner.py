from odoo import _, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def action_test_notification(self):
        self.env["bus.bus"]._sendone(
            self.env.user.partner_id,
            "simple_notification",
            {
                "type": "danger",
                "title": _("Warning"),
                "message": _("Watch out!"),
            },
        )
