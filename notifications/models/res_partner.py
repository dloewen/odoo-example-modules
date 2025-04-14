from odoo import api, models, _

from logging import getLogger

logger = getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def test_notification(self, arg):
        self.env.user._bus_send('simple_notification', {
            'type': 'danger',
            'title': _("Warning"),
            'message': _('Watch out!'),
        })
