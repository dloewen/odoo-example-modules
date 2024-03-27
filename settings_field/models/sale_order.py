from odoo import fields, models, _

from logging import getLogger

logger = getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def my_example_method(self):
        """Example of retrieving the settings"""

        # Note that ir.config_parameter fields are saved as a string, so they must be converted to other types.
        my_notification_user_id = self.env["ir.config_parameter"].sudo().get_param("my_notification_user_id")
        if my_notification_user_id:
            user_id = self.env["res.users"].search(["id", "=", int(my_notification_user_id)])
            logger.info("my_notification_user_id: %s", user_id)

        # Company-related field
        my_company_text = self.company_id.my_company_text
        logger.info("my_company_text: %s", my_company_text)
