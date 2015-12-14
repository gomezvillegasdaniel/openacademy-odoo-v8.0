# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """ Curso técnico de Odoo 8 """,

    'description': """
    """,

    'author': "Daniel Gómez Villegas",
    'website': "google.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': '',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'installable': True,
    'auto_install': False,
}
