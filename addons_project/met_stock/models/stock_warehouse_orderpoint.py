# -*- coding: utf-8 -*-

from odoo import models, Command, fields, api


class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    no_orderpoint = fields.Boolean(
        related="product_id.product_tmpl_id.no_orderpoint",
        store=True,
        string="No orderpoint",
    )
    qty_to_purchase_order = fields.Float(
        string="To purchase order",
        compute="_compute_qty_to_purchase_order",
        store=True,
    )

    @api.depends("product_max_qty", "qty_on_hand")
    def _compute_qty_to_purchase_order(self):
        for orderpoint in self:
            qty = orderpoint.product_max_qty - orderpoint.qty_on_hand
            orderpoint.qty_to_purchase_order = qty if qty > 0 else 0

    def action_check_orderpoint_and_create_purchase(self):
        orderpoints = self.search(
            [
                ("route_id", "=", 5),
                ("trigger", "=", "auto"),
                ("no_orderpoint", "=", False),
            ]
        )
        orderpoints = orderpoints.filtered(lambda o: o.qty_on_hand < o.product_min_qty)
        vals = {}
        for order in orderpoints:
            domain = [("product_tmpl_id", "=", order.product_id.product_tmpl_id.id)]
            pricelist_id = self.env["product.supplierinfo"].search(
                domain, order="price asc", limit=1
            )
            if pricelist_id.partner_id:
                if pricelist_id.partner_id not in vals:
                    vals[pricelist_id.partner_id] = [
                        Command.create(
                            {
                                "product_id": order.product_id.id,
                                "product_qty": order.qty_to_purchase_order,
                            }
                        )
                    ]
                else:
                    vals[pricelist_id.partner_id].append(
                        Command.create(
                            {
                                "product_id": order.product_id.id,
                                "product_qty": order.qty_to_purchase_order,
                            }
                        )
                    )
        for key, value in vals.items():
            purchase_vals = {
                "partner_id": key.id,
                "is_orderpoint": True,
                "order_line": value,
            }
            self.env["purchase.order"].create(purchase_vals)
