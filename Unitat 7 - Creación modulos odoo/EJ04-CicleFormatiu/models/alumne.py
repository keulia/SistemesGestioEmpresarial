# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class Alumne(models.Model):

    # Nom i descripció del model de dates
    _name = 'alumne'
    _description = "Model de la llista de alumnes"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut nom_complet
    _rec_name="nom"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    nom = fields.Char("Nom") # Nom del medic, camp amb text
    cognom = fields.Char("Cognom") # Cognom del medic camp amb text
    moduls = fields.Many2Many('moduls') # Voluntari, relació per a indicar el voluntari que ha recollit cada producte
    
    