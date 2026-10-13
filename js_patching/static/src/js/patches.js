/** @odoo-module **/

import { ActivityListPopoverItem } from "@mail/core/web/activity_list_popover_item";
import { patch } from "@web/core/utils/patch";
import { FloatField, floatField } from "@web/views/fields/float/float_field";
import { FormController } from "@web/views/form/form_controller";

// Since pretty much anything in JavaScript is an object,
// and the "patch" function can patch objects,
// the patch function can patch pretty much anything!
// Note: exported functions and constants can't be reassigned (ES module bindings
// are read-only), so patch the object or class that holds them instead.

// Patch a plain object
// Here we patch the float field's registry entry, "super" works like in a class.
// ------------------------------------------------------------------------
patch(floatField, {
    extractProps() {
        const props = super.extractProps(...arguments);
        // Change the props given to every float field here
        return props;
    },
});

// Patch an OWL component's method
// ------------------------------------------------------------------------
patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);
        console.log("Hello from the patched form controller!");
    },
});

// Patch a static property of an OWL component
// Here we add a float component to the existing components
// ------------------------------------------------------------------------
patch(ActivityListPopoverItem, {
    components: { ...ActivityListPopoverItem.components, FloatField },
});
