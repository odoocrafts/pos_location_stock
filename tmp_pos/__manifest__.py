# -*- coding: utf-8 -*-
{
    'name': 'POS Location Stock',
    'version': '1.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Check product stock across other stores/warehouses from POS',
    'description': """
POS Location Stock
==================
Adds a "Check Other Locations" button to the POS Product Details screen, allowing cashiers to quickly see real-time stock levels of a product across all configured warehouses.
    """,
    'author': 'Odoocrafts Innovations',
    'website': 'https://odoocrafts.com',
    'price': 25.0,
    'currency': 'EUR',
    'license': 'OPL-1',
    'images': ['static/description/banner.png'],
    'depends': ['point_of_sale', 'stock'],
    'data': [],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_location_stock/static/src/app/location_stock_popup.xml',
            'pos_location_stock/static/src/app/location_stock_popup.js',
            'pos_location_stock/static/src/app/location_stock_button.xml',
            'pos_location_stock/static/src/app/location_stock_button.js',
        ],
    },
    'installable': True,
    'application': False,
}
