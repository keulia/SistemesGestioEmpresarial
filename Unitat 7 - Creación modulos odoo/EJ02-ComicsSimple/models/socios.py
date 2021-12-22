# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo médico
class socios(models.Model):

    _name = 'socios' # Nombre del modelo
    _description = 'Socios de biblioteca' # Descripcion del modelo

    _order = 'apellidos desc, nombre' # Parametros para ordenar

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    _rec_name = 'nombre' # Atributo nombre
    nombre = fields.Char('Nombre', required=True, index=True) # Nombre del socio, campo con texto
    apellidos = fields.Char('Apellidos', required=True, index=True) # apellidos del socio, campo con texto
    identificador = fields.Char('Identificador', required=True, index=True) # Identificador, campo con texto

    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('identificador_uniq', 'UNIQUE (identificador)', 'El identificador del socio debe ser único.')
    ]


