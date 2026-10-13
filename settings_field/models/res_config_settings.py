from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Stored in ir.config_parameter upon save, because of the "config_parameter" attribute
    my_notification_user_id = fields.Many2one(
        string="User to notify of new sales",
        comodel_name="res.users",
        config_parameter="my_notification_user_id",
    )

    # Stored in res.company, so it is company-dependent (must *not* have config_parameter set)
    my_company_text = fields.Char(
        related="company_id.my_company_text",
        readonly=False,
    )
