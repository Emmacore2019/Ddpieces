# -*- coding: utf-8 -*-
{
    'name': "gss_sale_order",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale_crm','purchase_stock','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'templates/report.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/crm_lead_views.xml',
        # 'views/product_views.xml',
        'views/purchase_view.xml',
        'templates/gss_header_footer.xml',
        'templates/invoices_template.xml',
        'templates/sale_template.xml',
       
       
    ],
    "assets": {
        "web.assets_backend": [
            "/gss_sale_order/templates/style.scss",
        ],
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'license': 'LGPL-3',
}
