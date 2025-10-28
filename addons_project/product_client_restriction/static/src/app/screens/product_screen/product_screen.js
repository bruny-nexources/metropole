/** @odoo-module **/

import { _t } from "@web/core/l10n/translation";
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { patch } from "@web/core/utils/patch";
import { AlertDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(ProductScreen.prototype, {
  async addProductToOrder(product) {
    const currentOrder = this.pos.get_order();
    const currentPartner = currentOrder.get_partner();
    let restrictedProductIds = currentPartner.restricted_product_ids.find(
      (p) => p.id === product.id
    );
    if (restrictedProductIds) {
      this.dialog.add(AlertDialog, {
        title: _t("Unsupported product"),
        body: _t(
          "Product %s does not supported by %s.",
          product.display_name,
          currentPartner.name
        ),
      });
      return;
    }

    await super.addProductToOrder(product);
  },
});
