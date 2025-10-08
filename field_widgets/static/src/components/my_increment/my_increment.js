import { registry } from '@web/core/registry';
import { Component } from "@odoo/owl";

/**
 * Increment widget integer/float fields
 *
 * @extends Component
 */

export class MyIncrementWidget extends Component {
    static template = "field_widgets.MyIncrementWidget";
    static supportedTypes = ["integer", "float"];
    setup() {
        super.setup(...arguments);
    }

    addQuantity(quantity, ev) {
        ev.preventDefault();
        const originalQty = this.props.value;
        let newQty = this.props.value + quantity;
        this.props.update(newQty >= 0 ? newQty : originalQty);
    }
}

registry.category("fields").add("my_increment", MyIncrementWidget);
