# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Definimos el modelo profesor
class profesores(models.Model):

    _name = 'profesores'# Nombre del modul
    _description = 'Profesores del colegio'# Descripcion del modelo
    _order = 'profID desc, nombre' # Parametros para ordenar
    _rec_name = 'nombre'  # Atributo nombre
 
    profID = fields.Integer('ID de profesor', required=True, index=True) # Identificador del profesor, campo númerico
    nombre = fields.Char('nombre', required=True, index=True)# nombre del prfesor, campo con textos
    apellidos = fields.Char('apellidos', required=True, index=True) # Apellidos del profesor, campo con texto
    asignatura = fields.Many2one('modulos', required=True, index=True)  # Asignatura, relación entre el ciclo y los profesoresz
    # Constraints de SQL del modelo
    # Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('profID_uniq', 'UNIQUE (profID)', 'ID ya existe')
    ]