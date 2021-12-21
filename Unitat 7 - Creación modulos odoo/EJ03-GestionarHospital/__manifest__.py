# -*- coding: utf-8 -*-
{
    'name': "Gestio d'Hospital",

    'summary': """
    Gestio d'Hospital""",

    'description': """
    Mòdul que conté tot el necesari per a realitzar una gestió de pacients i mèdics
    """,

    'author': "Cassandra Sowa CAndela",
    #'website': "https://apuntesfpinformatica.es",
    
    # Indiquem que el mòdul es una aplicació
    'application': True,

    # En la següent URL s'indica que categories es poden usar
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    'category': 'Productivity',
    'version': '0.1',

    # Indiquem llista de mòduls necesaris per a que aquest funcione correctament
    # En aquest cas, sol depen del mòdulol "base"
    'depends': ['base'],

    # Aquest sempre es carga
    'data': [
        # Política d'accés al mòdul
        'security/ir.model.access.csv',

        # Carguem les vistes i les plantilles
        'views/voluntaris.xml',

    ]
}