# -*- coding: utf-8 -*-
{
    'name': "Biblioteca Comics Simple",  # Titulo del módulo
    'summary': "Gestionar comics :) (Version simple)",  # Resumen
    'description': """
Gestor de bibliotecas (Version Simple)
==============
    """,  # Descripción

    'author': "Cassandra Sowa Candela", # Indicamos el autor
    'application': True, # Indicamos que el modulo una aplicación
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    # Siempre se carga
    'data': [
        'security/groups.xml', # Grupo de seguridad basado en rol
        'security/ir.model.access.csv', # Política de acceso al módulo
        # Cargamos la vista y las plantillas
        'views/biblioteca_comic.xml',
        'views/socios.xml',
        'views/prestamos.xml'
    ],
}
