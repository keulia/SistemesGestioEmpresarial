# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo empleados
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)

    #Introducice metodo "archivar" que invierte el estado de "activo"
    #Recordamos se recive "self" como el modelo entero y no como un registro,
    #por ese motivo debemos iterar
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo

# Definimos el modelo de empleados
class empleados(models.Model):


    _name = 'empleados'

    _inherit = ['base.archive']

    _description = 'empleados'


    _order = 'nombre'

    _rec_name = 'dni'
    #Atributo nombre
    imagen = fields.Binary("Imagen") # Imagen del empleado, campo binario
    nombre = fields.Char('Nombre', required=True, index=True) # Apellidos del empleado, campo con texto
    apellidos = fields.Char("Apellidos") # Apellidos del empleado, campo con texto
    dni = fields.Char("dni") # DNI del empleado, campo con texto
    carnet = fields.Selection([('n','No tiene carnet'),('c','carnet de ciclomotor'),('f','carnet de furgoneta')],string='Carnet') # Carnet del empleado, campo selection
    telefono = fields.Char("Teléfono") # Teléfono del empleado, campo con texto
    repartosCompletados = fields.One2many("reparto","repartidor") # Repartos hechos por el empleado


    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (dni)', 'El dni debe ser único.')
    ]
