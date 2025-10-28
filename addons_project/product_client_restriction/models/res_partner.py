from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    restricted_product_ids = fields.Many2many(comodel_name="product.product")

    @api.model
    def _load_pos_data_fields(self, config_id):
        return super()._load_pos_data_fields(config_id) + ["restricted_product_ids"]
