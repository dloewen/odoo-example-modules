/** @odoo-module **/

import { registry } from '@web/core/registry';

const { Component } = owl;

/**
 * Increment widget integer/float fields
 *
 * @extends Component
 */

export class MyIncrementWidget extends Component {
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

MyIncrementWidget.template = "field_widgets.MyIncrementWidget";
MyIncrementWidget.supportedTypes = ["integer", "float"];

registry.category('fields').add('my_increment', MyIncrementWidget);
