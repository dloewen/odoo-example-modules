from odoo.tests import TransactionCase, tagged


@tagged("post_install", "-at_install")
class TestAddPivot(TransactionCase):
    def test_pivot_view_added_to_action(self):
        action = self.env.ref("sale.product_template_action")
        self.assertIn("pivot", action.view_mode.split(","))

        views = self.env["product.template"].get_views([(False, "pivot")])
        self.assertEqual(views["views"]["pivot"]["id"], self.env.ref("add_pivot.product_template_pivot_view").id)
