# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

class eliminar_empates(http.Controller):
    @http.route('/ligafutbol/equipo/eliminarempates', type='http', auth='none')
    def eliminarEmpates(self):
        # Obtenemos la referencia al modelo de Equipo
        partidos = request.env['liga.partido'].sudo().search([])
        # Variable para contar cuantos partidos vamos a eliminar
        partidosEliminados = 0
        
        for partido in partidos:
            # Si la cantidad de goles es igual
            if partido.goles_casa == partido.goles_fuera:
                # Añadimos +1
                partidosEliminados += 1
                partido.unlink()
        return "" + str(partidosEliminados)
                