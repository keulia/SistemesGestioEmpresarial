# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo de Clientes
class vehiculos(models.Model):

    _name = 'vehiculos' # Nombre del modelo

    _description = 'vehiculos' # Descripcion del modelo

    _order = 'matricula' # Parametros para ordenar
    _rec_name = 'matricula'
    
    #Atributo nombre
    imagen = fields.Binary("Imagen") # Imagen vehiculo
    tipo = fields.Selection([('c','ciclomotor'),('f','furgoneta'),('b','bicicleta')],string='Tipo') # Tipo de vehiculo
    matricula = fields.Char("Matricula", required=True) # Matricula del vehiculo
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False) # Descripción, es un campo HTML
    
    # Matricula es un campo obligatorio
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (matricula)', 'La matricula debe ser única.')
    ]
