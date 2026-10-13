import base64
from logging import getLogger

from odoo import fields, models

logger = getLogger(__name__)


class MyImportWizard(models.TransientModel):
    _name = "my.import.wizard"
    _description = "File Import Wizard"

    csv_file = fields.Binary("CSV File", required=True)
    file_name = fields.Char()

    # Optional: uncomment the following block (and import os, api, _ and ValidationError)
    # to require certain file extensions
    # @api.constrains("file_name")
    # def _check_file_extension(self):
    #     allowed_extensions = [".pdf", ".zip"]
    #     for wizard in self:
    #         extension = os.path.splitext(wizard.file_name or "")[1].lower()
    #         if extension not in allowed_extensions:
    #             raise ValidationError(
    #                 _("File type not allowed. Allowed extensions: %s", ", ".join(allowed_extensions))
    #             )

    def import_csv(self):
        """Handle file import"""
        self.ensure_one()
        file_content = base64.b64decode(self.csv_file)
        # Do processing of the file contents here
        logger.info("Importing %s (%d bytes)", self.file_name, len(file_content))
