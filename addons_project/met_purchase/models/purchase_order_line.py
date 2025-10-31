from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    supplier_product_code = fields.Char(
        string="CIP",
        compute="_compute_supplier_product_code",
        store=True,
    )

    @api.depends("product_id", "order_id.partner_id", "product_id.seller_ids")
    def _compute_supplier_product_code(self):
        for line in self:
            code = False
            seller = line.product_id.seller_ids.filtered(
                lambda s: s.partner_id == line.order_id.partner_id
            )
            if seller:
                code = seller[0].product_code
            line.supplier_product_code = code
