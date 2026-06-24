/** @odoo-module */

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/hooks/pos_hook";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { patch } from "@web/core/utils/patch";
import { LocationStockPopup } from "./location_stock_popup";
import { useService } from "@web/core/utils/hooks";

export class LocationStockButton extends Component {
    static template = "pos_location_stock.LocationStockButton";
    static props = {
        class: { type: String, optional: true },
    };

    setup() {
        this.pos = usePos();
        this.orm = useService("orm");
        this.dialog = useService("dialog");
    }

    async onClick() {
        const order = this.pos.getOrder();
        if (!order) {
            return;
        }
        const selectedLine = order.getSelectedOrderline();
        if (!selectedLine) {
            return;
        }

        const product = selectedLine.product_id;

        try {
            const stockData = await this.orm.call(
                "product.template",
                "get_stock_by_location",
                [product.product_tmpl_id.id] // Accessing the template id
            );
            this.dialog.add(LocationStockPopup, {
                title: `Stock across locations for ${product.display_name}`,
                stockData: stockData,
            });
        } catch (error) {
            console.error("Could not fetch location stock", error);
        }
    }
}

// Add the component so it can be used in the ControlButtons template
patch(ControlButtons, {
    components: {
        ...ControlButtons.components,
        LocationStockButton,
    },
});
