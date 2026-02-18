/** @odoo-module **/

import { CategoryButton } from "@point_of_sale/app/screens/product_screen/category_button/category_button";
import { patch } from "@web/core/utils/patch";
import { session } from "@web/session";

patch(CategoryButton.prototype, {
    setup() {
        super.setup();
        this.colors = session.colorlist_customizer || {};
    },
    
    getCategoryColor(colorIndex) {
        if (colorIndex === undefined || colorIndex === null) return null;
        const colorKey = `colorlist_${colorIndex}`;
        return this.colors[colorKey] || null;
    }
});
