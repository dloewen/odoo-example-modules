/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { COLORS, getColor } from "@web/views/graph/colors";

// Since pretty much anything in JavaScript is an object,
// and the "patch" function can patch objects,
// the patch function can patch pretty much anything!

// Patch a constant
// ------------------------------------------------------------------------
export const EXTRA_COLORS = ['#333333', '#555555', '#777777'];
patch(COLORS, "js_patching.patches", [...COLORS, ...EXTRA_COLORS]);

// Patch a function
// ------------------------------------------------------------------------
export function myGetColor(index) {
    return COLORS[index % COLORS.length];
}
patch(getColor, "js_patching.patches", myGetColor);

// Patch an OWL component's method
// ------------------------------------------------------------------------
patch(GraphView.prototype, "js_patching.patches", {
    setup() {
        this._super(...arguments);
        console.log("Hello!")
    }
})