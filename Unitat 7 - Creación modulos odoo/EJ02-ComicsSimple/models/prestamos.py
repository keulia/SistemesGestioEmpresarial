# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


#Definimos el módelo Biblioteca comic
class prestamos(models.Model):
    
    _name = 'prestamos' # Nombre del modelo
    _description = 'Préstamos de biblioteca'  # Descripcion del modelo
    _order = 'inicioprestamo desc, finalprestamo' # Parametros para ordenar

    _rec_name = 'prestadoa' # Atributo nombre
    comic = fields.Many2one('biblioteca.comic', required=True, index=True) # Comic, relación para indicar el comic
    prestadoa = fields.Many2one('socios', required=True, index=True) # Prestado, relación para indicar el prestamo
    inicioprestamo = fields.Date('Inicio del préstamo', required=True, index=True) # Nombre del médico, campo con texto
    finalprestamo = fields.Date('Final del préstamo', required=True, index=True) # Nombre del médico, campo con texto

    @api.constrains('inicioprestamo')
    def _check_inicioprestamo(self):
        # Recorremos el modelo
        for prest in self:
        # Si hay fecha_publicacion y > la fecha de hoy
            if prest.inicioprestamo and prest.inicioprestamo > fields.Date.today():
                raise models.ValidationError('La fecha no puede ser tan alta!')

    @api.constrains('finalprestamo')
    def _check_finalprestamo(self):
        # Recorremos el modelo
        for prest in self:
        # Si hay fecha_publicacion y < la fecha de hoy
            if prest.finalprestamo and prest.finalprestamo < fields.Date.today():
                raise models.ValidationError('La fecha de devolución tiene que ser en el futuro!')