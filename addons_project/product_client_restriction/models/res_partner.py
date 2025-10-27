from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    restricted_product_ids = fields.Many2many(comodel_name="product.product")
