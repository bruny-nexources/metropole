/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { PosOrderline } from "@point_of_sale/app/models/pos_order_line";

patch(PosOrderline.prototype, {
    getProductNote() {
        return this.product_note || this.get_full_product_name();
    },
    setProductNote(productNote) {
        this.setDirty();
        this.product_note = productNote;
    },
    getDisplayData() {
        const res = super.getDisplayData()
        res.product_note = this.getProductNote();
        return res;
    }
});
