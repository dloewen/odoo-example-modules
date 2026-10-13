/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

/**
 * Increment widget for integer/float fields, limited to values between 0 and 10
 *
 * Usage in a view: <field name="my_integer_field" widget="my_increment"/>
 */
export class MyIncrementWidget extends Component {
    static template = "field_widgets.MyIncrementWidget";
    static props = { ...standardFieldProps };

    get value() {
        return this.props.record.data[this.props.name];
    }

    addQuantity(quantity, ev) {
        ev.preventDefault();
        const newQty = this.value + quantity;
        if (newQty >= 0 && newQty <= 10) {
            this.props.record.update({ [this.props.name]: newQty });
        }
    }
}

registry.category("fields").add("my_increment", {
    component: MyIncrementWidget,
    supportedTypes: ["integer", "float"],
});
