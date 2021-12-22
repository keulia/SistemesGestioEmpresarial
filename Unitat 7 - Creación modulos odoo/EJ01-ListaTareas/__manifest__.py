# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas", # Titulo del módulo

    'summary': """
    Sencilla Lista de tareas""", # Resumen

    'description': """
    Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos
    """, # Descripción

    'author': "Cassandra Sowa Candela", # Indicamos el autor
    'application': True,  # Indicamos que el modulo una aplicación

    # En la siguiente URL se indica que categorias pueden usarse
    # https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # Vamos a utilizar la categoria Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Depende del modulo base
    'depends': ['base'],

    # Siempre se carga
    'data': [

        'security/ir.model.access.csv', # Grupo de seguridad basado en rol
        'views/views.xml', # Cargamos las vistas y las plantillas
    ]
}
