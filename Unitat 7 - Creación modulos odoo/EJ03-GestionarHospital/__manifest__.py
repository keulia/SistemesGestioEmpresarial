# -*- coding: utf-8 -*-
{
    'name': "Gestión Hospital",  # Titulo del módulo
    'summary': "Gestión de Hospital",  # Resumen
    'description': """ 
 Gestión de un hospital
==============
    """,  # Descripción

    'author': "Cassandra Sowa Candela", # Indicamos el autor
    'application': True,     # Indicamos que el modulo una aplicación
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    # Siempre se carga
    'data': [
        'security/groups.xml',         # Grupo de seguridad basado en rol
        'security/ir.model.access.csv', # Política de acceso al módulo
        #Cargamos la vista y las plantillas
        'views/pacientes.xml',
        'views/medicos.xml',
        'views/diagnosticos.xml'
    ],

}
