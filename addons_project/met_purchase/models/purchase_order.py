from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # Champ pour stocker le code fournisseur de la ligne principale
    supplier_product_code = fields.Char(
        string="CIP",
        compute="_compute_supplier_product_code",
        store=True,
    )

    @api.depends("order_line.supplier_product_code")
    def _compute_supplier_product_code(self):
        for order in self:
            # On prend le premier code fournisseur trouvé sur les lignes
            codes = order.order_line.mapped("supplier_product_code")
            order.supplier_product_code = codes[0] if codes else False
