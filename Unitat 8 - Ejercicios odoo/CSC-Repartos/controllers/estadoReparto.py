# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

# Nos mostrará al entrar a la url el estado del reparto que pongamos
class estadoReparto(http.Controller):
    @http.route('/estadoReparto/<id>', auth='public', cors='*', type='http')
    def estadoReparto(self, id, **kw):
        reparto = request.env['reparto'].search([])
        existe = False
    
        for i in reparto:
            if (str(i.codigoNumerico) == str(id)):
                existe = True
                if(str(i.estadoEntrega) == "c"):
                    return '<div> De camino... <div>'
                elif(str(i.estadoEntrega) == "e"):
                    return '<div> Entregado! <div>'
                elif(str(i.estadoEntrega) == "n"):
                    return '<div> No ha salido aún... <div>'
            
        if(existe == False):
            return '<div>No existe</div>'