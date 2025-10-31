from odoo import models, fields, api


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    product_note = fields.Char(
        compute="_compute_product_note", store=True, readonly=False
    )

    @api.depends("product_id")
    def _compute_product_note(self):
        for line in self:
            line.product_note = line.product_id.name

    @api.model
    def _load_pos_data_fields(self, config_id):
        data_fields = super()._load_pos_data_fields(config_id)
        return data_fields + ["product_note"]
