# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo médico
class modulos(models.Model):


    _name = 'modulos' # Nombre del modelo
    _description = 'Módulos del colegio' # Descripcion del modelo
    _order = 'asigID desc, nombre' # Parametros para ordenar
    _rec_name = 'nombre' # Atributo nombre

    asigID = fields.Integer('ID de asignatura', required=True, index=True) # Identificador del móddulo, campo númerico
    nombre = fields.Char('Nombre', required=True, index=True) # nombre del módulo, campo con texto
    departamento = fields.Char('Departamento', required=True, index=True) # departamento del módulo, campo con texto
    ciclo = fields.Many2one('ciclos', required=True, index=True)  # Ciclo, relación entre el ciclo y sus módulos

    # Constraints de SQL del modelo
    # Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('asigID_uniq', 'UNIQUE (asigID)', 'ID ya existe')
    ]


