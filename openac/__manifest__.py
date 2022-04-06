# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """
        Мой первый модкль Открытая акадения""",

    'description': """
        Мой первый модкль Открытая акадения
    """,

    'author': "My Company",
    'website': "https://www.a4.com.ua",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizard/session_create_wizard_views.xml',
        'views/partners_views.xml',
        'views/course_views.xml',
        'views/sessions_views.xml',
        'views/templates.xml',
        'report/report_sessions.xml',
        'report/dashboard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
