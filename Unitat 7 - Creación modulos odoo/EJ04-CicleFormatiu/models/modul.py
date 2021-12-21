# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class Moduls(models.Model):

    # Nom i descripció del model de dates
    _name = 'moduls'
    _description = "Model de la llista de moduls"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut nom_complet
    _rec_name="nom"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    nom = fields.Char("Nom Complet") # Nom del medic, camp amb text
    cicle_formatiu = fields.Many2one('Cicle Formatiu')
    professor = fields.Many2one('Professor') 
    