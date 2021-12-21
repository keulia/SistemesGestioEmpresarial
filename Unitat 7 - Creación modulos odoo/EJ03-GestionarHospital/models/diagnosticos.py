# -*- coding: utf-8 -*-
from datetime import timedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definimos el modelo de las relaciones
class BaseArchive(models.AbstractModel):

    _name = 'base.archive' # Nombre del modelo
    _description = 'Fichero abstracto' # Descripcion del modelo

    activo = fields.Boolean(default=True)
    def archivar(self):
        # Por cada registro del modelo
        for record in self:
            # Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


# Definimos modelo diagnosticos
class diagnosticos(models.Model):

    _name = 'diagnosticos' # Nombre del modelo
    _inherit = ['base.archive']
    _description = 'Diagnósticos del hospital' # Descripcion del modelo
    _order = 'medico desc, paciente'     # Parametros para ordenar
    _rec_name = 'diagnostico'

    # Elementos de cada fila del modelo
    medico = fields.Many2one('medicos', required=True, index=True) # Médico, relación para indicar el médico
    paciente = fields.Many2one('pacientes', required=True, index=True) # Paciente, relación para indicar el paciente
    diagnostico = fields.Text('Diagnóstico de la consulta' , required=True, index=True) # Diagnostico relación para indicar el diagnostico