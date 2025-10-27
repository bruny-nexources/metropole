from markupsafe import Markup

from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange("product_id")
    def _onchange_product_id_restricted(self):
        if self.product_id in self.order_partner_id.mapped("restricted_product_ids"):
            raise UserError(
                Markup(
                    _(
                        "Product %s not supported by %s.",
                        self.product_id.display_name,
                        self.order_partner_id.name,
                    )
                )
            )
