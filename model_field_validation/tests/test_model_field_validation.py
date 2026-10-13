from odoo.exceptions import ValidationError
from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestModelFieldValidation(TransactionCase):
    def test_valid_tax_id(self):
        partner = self.env["res.partner"].create({"name": "Valid", "vat": "something-123"})
        self.assertEqual(partner.vat, "something-123")

    def test_invalid_tax_id(self):
        with self.assertRaises(ValidationError):
            self.env["res.partner"].create({"name": "Invalid", "vat": "123"})

    def test_invalid_tax_id_multiple_records(self):
        partners = self.env["res.partner"].create([{"name": "A"}, {"name": "B"}])
        with self.assertRaises(ValidationError):
            partners.write({"vat": "123"})
