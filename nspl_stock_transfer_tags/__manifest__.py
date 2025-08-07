{
    'name': 'Stock Picking Tag',
    'version': '16.0.1.0.0',
    'summary': 'Add tag field to stock picking (Receipts)',
    'description': """
Stock Picking Tag
==================
This module adds a 'Tag' selection field to Stock Picking records, specifically visible in the Inventory → Receipts view.

Key Features:
-------------
- Classify incoming shipments as:
  - Consignment
  - Import
  - Spare Part
- Simple dropdown for clear categorization
- Helps with reporting and warehouse operations
    """,
    'category': 'Inventory',
    'website': 'https://www.namahsoftech.com',
    'author': 'Namah Softech Private Limited',
    'company': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech Private Limited',
    'contributors': [
        'Mohit Nare',
    ],
    'price': 9.99,
    'currency': 'USD',
    'license': 'LGPL-3',
    'depends': ['stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_tag_view.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
