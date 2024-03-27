from odoo import fields, models, _

from logging import getLogger

logger = getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # This field will be stored in the ir.config_parameter upon save, because of the "config_parameter" attribute
    my_notification_user_id = fields.Many2one(
        string="User to notify of new sales",
        comodel_name="res.users",
        config_parameter="my_notification_user_id",
    )

    # This field will be stored in res.company, it is company-dependant (must *not* have config_parameter set)
    my_company_text = fields.Char(
        related="company_id.my_company_text",
        readonly=False,
    )
