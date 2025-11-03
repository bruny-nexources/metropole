from odoo import models
from ..utils.description import formatted_description


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def get_product_description(self):
        return formatted_description(self.name)
