# -*- coding: utf-8 -*-

from odoo import models, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    @api.model
    def get_stock_by_location(self, product_id):
        product = self.browse(product_id)
        if not product.exists():
            return []

        # We will get all quants for this product in internal locations
        quants = self.env['stock.quant'].search([
            ('product_id', '=', product_id),
            ('location_id.usage', '=', 'internal')
        ])

        stock_by_warehouse = {}
        for quant in quants:
            wh = quant.location_id.warehouse_id
            # Group by warehouse if available, else by location
            key = f"wh_{wh.id}" if wh else f"loc_{quant.location_id.id}"
            name = wh.name if wh else quant.location_id.display_name
            
            if key not in stock_by_warehouse:
                stock_by_warehouse[key] = {
                    'name': name,
                    'quantity': 0.0,
                    'uom': product.uom_name,
                }
            stock_by_warehouse[key]['quantity'] += quant.quantity

        # Format and sort results
        result = list(stock_by_warehouse.values())
        result.sort(key=lambda x: x['name'])
        
        return result
