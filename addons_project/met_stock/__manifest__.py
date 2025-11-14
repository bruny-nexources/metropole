# -*- coding: utf-8 -*-
{
    "name": "MET - Stock",
    "summary": "Short (1 phrase/line) summary of the module's purpose",
    "author": "Nexources",
    "website": "https://www.nexources.com",
    "category": "Uncategorized",
    "version": "0.1",
    "depends": ["met_base", "stock", "purchase", "product"],
    "data": [
        "data/ir_cron.xml",
        "views/product_template_views.xml",
        "views/purchase_order_views.xml",
        "views/stock_warehouse_orderpoint_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "met_stock/static/src/js/list_controller.js",
            "met_stock/static/src/xml/list_controller.xml",
        ],
    },
}
