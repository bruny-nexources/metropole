# -*- coding: utf-8 -*-

from odoo import models, Command


class StockWarehouseOrderpoint(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    def action_check_orderpoint_and_create_purchase(self):
        orderpoints = self.search(
            [
                ("route_id", "=", 5),
                ("trigger", "=", "auto"),
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
                                "product_qty": order.qty_to_order,
                            }
                        )
                    ]
                else:
                    vals[pricelist_id.partner_id].append(
                        Command.create(
                            {
                                "product_id": order.product_id.id,
                                "product_qty": order.qty_to_order,
                            }
                        )
                    )
        for key, value in vals.items():
            purchase_vals = {"partner_id": key.id, "order_line": value}
            self.env["purchase.order"].create(purchase_vals)
