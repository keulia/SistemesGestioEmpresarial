# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo médico
class medicos(models.Model):
    _name = 'medicos'  # Nombre del modelo
    _description = 'Médicos de Hospital'  # Descripcion del modelo


    _order = 'apellidos desc, nombre' # Parametros para ordenar
    _rec_name = 'nombre' # Atributo nombre
    nombre = fields.Char('Nombre', required=True, index=True) # Nombre del médico, campo con texto
    apellidos = fields.Char('Apellidos', required=True, index=True) # Apellido del médico, campo con texto
    numColegiado = fields.Integer('Número de colegiado', required=True, index=True)  # Número de colegiado del médico, campo con número


