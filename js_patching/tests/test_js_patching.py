from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install")
class TestJsPatching(HttpCase):
    def test_patches_loaded(self):
        self.browser_js(
            "/web",
            "console.log('test successful')",
            "odoo.loader.modules.has('@js_patching/js/patches')",
            login="admin",
        )
