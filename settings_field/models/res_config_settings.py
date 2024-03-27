from odoo import fields, models, _

from logging import getLogger

logger = getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    my_notification_user_id = fields.Many2one(
        string="User to notify of new sales",
        comodel_name="res.users",
        config_parameter="my_notification_user_id",
    )
