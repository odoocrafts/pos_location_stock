/** @odoo-module */

import { Dialog } from "@web/core/dialog/dialog";
import { Component } from "@odoo/owl";

export class LocationStockPopup extends Component {
    static template = "pos_location_stock.LocationStockPopup";
    static components = { Dialog };
    static props = {
        title: { type: String },
        stockData: { type: Array },
        close: { type: Function },
        "*": true,
    };
}
