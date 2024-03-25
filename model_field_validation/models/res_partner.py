from odoo import api, models, _
from odoo.exceptions import ValidationError

from logging import getLogger

logger = getLogger(__name__)


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains("vat")
    def _my_check_tax_id(self):
        if self.vat and "something" not in self.vat:
            raise ValidationError(_("The tax ID is invalid."))
