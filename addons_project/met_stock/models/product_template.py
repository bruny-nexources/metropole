# -*- coding: utf-8 -*-

from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    no_orderpoint = fields.Boolean(string="No orderpoint")
