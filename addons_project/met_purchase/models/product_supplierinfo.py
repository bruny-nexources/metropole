from odoo import models, fields


class ProductSupplierInfo(models.Model):
    _inherit = "product.supplierinfo"

    product_code = fields.Char(
        string="CIP",
        help="This vendor's product code will be used when printing a request for quotation. Keep empty to use the internal one.",
    )
