# -*- coding: utf-8 -*-
{
    'name': "validations",

    'summary': """
        Application for managini different task""",

    'description': """
        In this aplication can hadd different tasks to do it Also tou can modigy different things!
    """,

    'author': "Ricardo Zoel Molina gandia",
    'website': "http://www.RicardoZ.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/students_views.xml',
        'views/modules_views.xml',
        'views/validation_views.xml',
        'views/course_views.xml',
        'views/menu.xml',
    #    'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}
