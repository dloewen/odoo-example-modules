from odoo import fields, models, _

from logging import getLogger

logger = getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def my_example_method(self):
        """Example of retrieving the setting"""
        # Note that the setting is saved as a string, so it must be converted as necessary.
        my_notification_user_id = self.env["ir.config_parameter"].sudo().get_param("my_notification_user_id")
        if my_notification_user_id:
            user_id = self.env["res.users"].search(["id", "=", int(my_notification_user_id)])
            logger.info(str(user_id))
