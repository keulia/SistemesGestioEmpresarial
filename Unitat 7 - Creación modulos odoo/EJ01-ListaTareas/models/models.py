# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime

# Definimos el modelo de las relaciones
class lista_tareas(models.Model):
    _name = 'lista_tareas.lista' # Nombre del modelo
    _description = 'Modelo de la lista de tareas' # Descripcion del modelo
    _rec_name="tarea" # Atributo nombre

    #Elementos de cada fila del modelo de datos
    #Los tipos de datos a usar en el ORM son 
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    tarea = fields.Char() # Nombre de la tarea, campo con texto
    prioridad = fields.Integer() # Prioridad de la tarea, campo con número
    urgente = fields.Boolean(compute="_value_urgente", store=True) # Urgencia de la tarea, campo booleano
    realizada = fields.Boolean() # Tarea realizada, campo booleano
    fecha = fields.Date(string='Fecha de creación', default=datetime.today()) # fecha de la entrega de la tarea, campo fecha


    @api.depends('prioridad')
    def _value_urgente(self):
        for record in self:
            if record.prioridad>10:
                record.urgente = True
            else:
                record.urgente = False
