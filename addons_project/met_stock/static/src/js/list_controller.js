/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import { rpc } from "@web/core/network/rpc";

patch(ListController.prototype, {
    setup() {
        super.setup();
        this.rpc = rpc;
    },

    async actionCreatePurchaseManul() {
        await this.rpc("/orderpoint/check_and_create_purchase", {});
    }


});