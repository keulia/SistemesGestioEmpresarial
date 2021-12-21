# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class Medics(models.Model):

    # Nom i descripció del model de dates
    _name = 'medics'
    _description = "Model de la llista de medics"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut nom_complet
    _rec_name="nom"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    nom = fields.Char("nom") # Nom del medic, camp amb text

    