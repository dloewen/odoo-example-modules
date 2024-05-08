/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { COLORS, getColor } from "@web/views/graph/colors";
import { ActivityListPopoverItem } from "@mail/core/web/activity_list_popover_item";
import { FloatField } from '@web/views/fields/float/float_field';

// Since pretty much anything in JavaScript is an object,
// and the "patch" function can patch objects,
// the patch function can patch pretty much anything!

// Patch a constant
// ------------------------------------------------------------------------
export const EXTRA_COLORS = ['#333333', '#555555', '#777777'];
patch(COLORS, [...COLORS, ...EXTRA_COLORS]);

// Patch a function
// ------------------------------------------------------------------------
export function myGetColor(index) {
    return COLORS[index % COLORS.length];
}
patch(getColor, myGetColor);

// Patch an OWL component's method
// ------------------------------------------------------------------------
patch(GraphView.prototype, {
    setup() {
        super(...arguments);
        console.log("Hello!")
    }
});

// Patching a list of components inside an OWL component
// ------------------------------------------------------------------------
// The patch function doesn't support static properties inside a class,
// so we have to use Object.assign instead.
Object.assign(ActivityListPopoverItem.components, { FloatField });
