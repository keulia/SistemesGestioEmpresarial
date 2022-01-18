# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo de Clientes
class clientes(models.Model):


    _name = 'clientes' # Nombre del modelo
    _inherit = ['base.archive'] # Hereda de "base.archive"
    _description = 'clientes' # Descripcion del modelo
    _order = 'nombre' # Parametros para ordenar
    _rec_name = 'dni'

    # ATRIBUTOS
    nombre = fields.Char('Nombre', required=True, index=True) # Nombre del cliente, campo con texto
    apellidos = fields.Char("Apellidos") # Apellidos del cliente, campo con texto
    dni = fields.Char("dni") # DNI del cliente, campo con texto
    telefono = fields.Char("Teléfono") # Teléfono del cliente, campo con texto


    #Constraints de SQL del modelo
    # DNI debe ser único
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (dni)', 'El dni debe ser único.')
    ]
