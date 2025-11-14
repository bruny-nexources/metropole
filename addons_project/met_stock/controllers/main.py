from odoo import http
from odoo.http import request


class OrderpointCreatePurchase(http.Controller):
    @http.route(
        "/orderpoint/check_and_create_purchase",
        type="http",
        auth="user",
        website=False,
        csrf=False,
    )
    def action_call_orderpoint(self, **kwargs):
        request.env[
            "stock.warehouse.orderpoint"
        ].sudo().action_check_orderpoint_and_create_purchase()
