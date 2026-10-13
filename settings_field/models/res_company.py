from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    my_company_text = fields.Char(string="My Text")
