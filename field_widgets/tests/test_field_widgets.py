from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestFieldWidgets(HttpCase):
    def test_widget_registered(self):
        self.browser_js(
            "/web",
            "console.log('test successful')",
            "!!odoo.loader.modules.get('@web/core/registry')?.registry.category('fields').contains('my_increment')",
            login="admin",
        )
