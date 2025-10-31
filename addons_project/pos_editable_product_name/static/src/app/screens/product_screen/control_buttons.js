/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { patch } from "@web/core/utils/patch";
import { ControlButtons } from "@point_of_sale/app/screens/product_screen/control_buttons/control_buttons";
import { OrderlineProductNoteButton } from "./order_line_product_note_button";

patch(ControlButtons, {
    components: { ...ControlButtons.components, OrderlineProductNoteButton },
});
patch(ControlButtons.prototype, {
    productNoteLabel() {
        return _t("Designation");
    }
});
