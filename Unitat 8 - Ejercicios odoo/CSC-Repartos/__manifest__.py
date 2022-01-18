# -*- coding: utf-8 -*-
{
    'name': "Empresa de repartidors",  # Titulo del módulo
    'summary': "Empresa de repartidors",  # Resumen de la funcionaliadad
    'description': """ 
Empresa de repartidors
==============
    """,  # Descripción

    #Indicamos que es una aplicación
    'application': True,
    'author': "Cassandra Sowa Candela", # Autora
    'category': 'Tools', # Categoría
    'version': '0.1', # Versión
    'depends': ['base'],

    'data': [
        'security/groups.xml', # grupo de seguridad basado en rol
        'security/ir.model.access.csv', # politica de acceso del modelo
        #Cargamos las vistas
        'views/empleados.xml',
        'views/clientes.xml',
        'views/reparto.xml',
        'views/vehiculos.xml',
        'wizard/reparto_wizard.xml',
        'report/pendienteSalida.xml'
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
