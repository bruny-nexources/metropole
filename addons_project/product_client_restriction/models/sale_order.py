from markupsafe import Markup

from odoo import models, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange("partner_id")
    def _onchange_partner_id_restricted(self):
        for line in self.order_line:
            if line.product_id in self.partner_id.mapped("restricted_product_ids"):
                raise UserError(
                    Markup(
                        _(
                            "Product %s not supported by %s.",
                            line.product_id.display_name,
                            self.partner_id.name,
                        )
                    )
                )
