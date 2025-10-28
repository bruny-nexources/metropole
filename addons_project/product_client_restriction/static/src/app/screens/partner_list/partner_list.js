/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { PartnerList } from "@point_of_sale/app/screens/partner_list/partner_list";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(PartnerList.prototype, {
  async clickPartner(partner) {
    const currentOrder = this.pos.get_order();
    for (const orderLine of currentOrder.lines) {
      if (
        partner.restricted_product_ids.find(
          (p) => p.id == orderLine.product_id.id
        )
      ) {
        this.dialog.add(AlertDialog, {
          title: _t("Unsupported product"),
          body: _t(
            "Product %s does not supported by %s.",
            orderLine.product_id.display_name,
            partner.name
          ),
        });
        return;
      }
    }
    await super.clickPartner(partner);
  },
});
