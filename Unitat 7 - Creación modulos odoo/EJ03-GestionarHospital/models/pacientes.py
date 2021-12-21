# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo de las relaciones
class pacientes(models.Model):

    _name = 'pacientes' # Nombre del modelo
    _description = 'Pacientes del hospital' # Descripcion del modelo
    _order = 'apellidos desc, nombre'  # Parametros para ordenar
    _rec_name = 'nombre' # Atributo nombre
    
    nombre = fields.Char('nombre', required=True, index=True) # Nombre del paciente, campo con texto
    apellidos = fields.Char('apellidos', required=True, index=True) # Apellido del paciente, campo con texto
    sintomas = fields.Char('sintomas', required=True, index=True) # Sintomas del paciente, campo con texto