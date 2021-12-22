# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


#Definimos el modelo alumnos
class alumnos(models.Model):

    _name = 'alumnos' # Nombre del modelo
    _description = 'Alumnos del ciclo' # Descripcion del modelo
    _order = 'aluID desc, nombre' # Parametros para ordenar
    _rec_name = 'nombre' # Atributo nombre


    aluID = fields.Integer('ID de alumno', required=True, index=True) # ID del alumno, campo con número
    nombre = fields.Char('nombre', required=True, index=True) # Nombre del alumno, campo con texto
    apellidos = fields.Char('apellidos', required=True, index=True) # Apellidos del alumno, campo con texto
    profesor = fields.Many2one('profesores', required=True, index=True) # Profesor, relación para indicar el profesor

    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('aluID_uniq', 'UNIQUE (aluID)', 'ID ya existe.')
    ]