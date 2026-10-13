from logging import getLogger

from odoo import models

logger = getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def my_example_method(self):
        """Example of retrieving the settings"""

        # ir.config_parameter has a getter for each type: get_str, get_int, get_float and get_bool.
        my_notification_user_id = self.env["ir.config_parameter"].sudo().get_int("my_notification_user_id")
        if my_notification_user_id:
            user = self.env["res.users"].browse(my_notification_user_id)
            logger.info("my_notification_user_id: %s", user)

        # Company-related field
        for order in self:
            logger.info("my_company_text: %s", order.company_id.my_company_text)
