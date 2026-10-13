from odoo import api, models
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains("vat")
    def _my_check_tax_id(self):
        for partner in self:
            if partner.vat and "something" not in partner.vat:
                raise ValidationError(self.env._("The tax ID is invalid."))
