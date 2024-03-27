from odoo import fields, models, _

from logging import getLogger

logger = getLogger(__name__)


class ResCompany(models.Model):
    _inherit = "res.company"

    my_company_text = fields.Char(string="My Text")
