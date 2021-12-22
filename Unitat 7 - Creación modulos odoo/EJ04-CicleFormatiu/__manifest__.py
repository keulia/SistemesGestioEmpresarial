# -*- coding: utf-8 -*-
{
    'name': "Ciclo Formativo",  # Titulo del módulo
    'summary': "Gestión de un ciclo formativo",  # Resumen
    'description': """
Colegio
==============
    """,  # Descripción

    'application': True, # Indicamos que el modulo una aplicación
    'author': "Cassandra Sowa Candela", # Indicamos el autor
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    # Siempre se carga
    'data': [
        'security/groups.xml',  # Grupo de seguridad basado en rol
        'security/ir.model.access.csv', # Política de acceso al módulo
        # Cargamos la vista y las plantillas
        'views/ciclos.xml',
        'views/modulos.xml',
        'views/profesores.xml',
        'views/alumnos.xml'
    ],
}
