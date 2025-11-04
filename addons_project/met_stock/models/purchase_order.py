# -*- coding: utf-8 -*-

from odoo import models, fields


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    is_orderpoint = fields.Boolean(string="Orderpoint")
