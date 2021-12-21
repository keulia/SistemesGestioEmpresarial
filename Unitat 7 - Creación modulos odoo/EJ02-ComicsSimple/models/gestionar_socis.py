
# -*- coding: utf-8 -*-

from odoo import models, fields, api

# Definim el model de dates
class GestionarSocis(models.Model):

    # Nom i descripció del model de dates
    _name = 'gestionar.socis'
    _description = "Socis"

    # Com no tenim un atribut "name" en el nostre model, indiquem que quan
    # es necessite un nom, s'usara el atribut nom_complet
    _rec_name="nom"

    # Tipos de dates a Odoo
    # https://www.odoo.com/documentation/14.0/developer/reference/addons/orm.html#fields
   
    # Elements de cada fila del model de dates
    nom = fields.Char("Nom") # Nom del soci, camp amb text
    cognom = fields.Char("Cognom") # Cognomom del soci, camp amb text
    identificador = fields.Integer("Identificador") # Identificador del soci, camp numeric
    biblioteca_comic = fields.One2Many("Comic") # Nom del comic, camp amb text
