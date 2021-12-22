# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definimos el modelo BaseArchive
class BaseArchive(models.AbstractModel):
    _name = 'base.archive' # Nombre del modelo
    _description = 'Fichero abstracto' # Descripcion del modelo

    # Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)
    def archivar(self):
        # Por cada registro del modelo
        for record in self:
            # Activo se cambia a False
            record.activo = not record.activo


# Definimos modelo ciclos
class ciclos(models.Model):
    _name = 'ciclos' # Nombre del modelo
    _description = 'Ciclos del colegio' # Descripcion del modelo
    _inherit = ['base.archive'] # Hereda de "base.archive"
    _order = 'numID desc, nombre' # Parametros para ordenar
    _rec_name = 'nombre' # Atributo para el nombre

    numID = fields.Integer('Número identificador', required=True, index=True)  # ID del ciclo, campo númericoss
    nombre = fields.Char('Nombre', required=True, index=True)  # Nombre del ciclo, campo de texto
    categoria = fields.Selection(
        [('DAM', 'Desarrollo de Aplicaciones Multiplataformas'),
         ('DAW', 'Desarrollo de Aplicaciones Web'),
         ('ASIX', 'Administrador de Sistemas Informáticos y Redes')],
        'Categoria', default="DAM") # Categoria para elegir una opción
    descripcion = fields.Text('Descripción del ciclo' , required=True, index=True)  # Descripción del ciclo, campo de texto
    
    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('numID_uniq', 'UNIQUE (numID)', 'ID ya existe')
    ]