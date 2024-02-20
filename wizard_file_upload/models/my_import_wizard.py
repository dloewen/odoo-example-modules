from odoo import api, fields, models, _
from odoo.exceptions import ValidationError
import base64

from logging import getLogger
logger = getLogger(__name__)


class MyImportWizard(models.TransientModel):
    _name = 'my.import.wizard'
    _description = 'File Import Wizard'

    csv_file = fields.Binary('CSV File', required=True)
    file_name = fields.Char('File Name')

    # Optional: uncomment the following block to require certain file extensions
    # @api.constrains('file_name')
    # def _check_file_extension(self):
    #     allowed_extensions = ['.pdf', '.zip']
    #     if self.file_name:
    #         extension = os.path.splitext(self.file_name)[1].lower()
    #         if extension not in allowed_extensions:
    #             raise ValidationError(f"File type not allowed. Please upload files with one of the following extensions: {', '.join(allowed_extensions)}")

    def import_csv(self):
        """Handle file import"""
        self.ensure_one()
        if self.csv_file:
            file_content = base64.b64decode(self.csv_file)
            # Do processing of the file contents here
