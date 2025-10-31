from odoo import models
from ..utils.description import formatted_description


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def get_product_description(self):
        return formatted_description(self.name)
