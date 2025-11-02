from odoo import models
from ..utils.description import formatted_description


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    def get_product_description(self):
        return formatted_description(self.name)
