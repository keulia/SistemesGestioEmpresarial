# -*- coding: utf-8 -*-
from odoo import models, fields


#crea un modelo, pero es temporal y no hace permanente sus datos en la base de datos.
#Se utiliza para "mientras dura el Wizard"
class RepartoWizard(models.TransientModel):
    _name = 'reparto.wizard'
    #Campos del modelo que usaremos en el Wizard
    codigoNumerico = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code('codigoAutomatico'))
    fechaInicio = fields.Datetime("Fecha y hora devolver")
    fechaDevolver = fields.Datetime("Fecha y hora devolver")
    fechaEntrega = fields.Datetime("Fecha y hora de la entrega")
    repartidor = fields.Many2one('empleados')
    vehiculo = fields.Many2one('vehiculos')
    kilometros = fields.Float("Kilometros")
    peso = fields.Float("Peso")
    volumen = fields.Float("Volumen")
    observacions = fields.Html('Observaciones', sanitize=True, strip_style=False)
    estadoEntrega = fields.Selection([('n','No ha salido'),('c','de camino'),('e','entregado')],string='Estado de la entrega')
    clienteEmissor = fields.Many2one('clientes')
    clienteReceptor = fields.Many2one('clientes')
    urgencia = fields.Selection([('0','organos humanos'),('1','alimentos congelados'),('2','alimenntos'),('3','prioridad alta'),('4','prioridad baja')],string='Urgencia')

    #Funcion que se llamara desde el Wizard, para utilizar este modelo temporal
    #y así poder crear un nuevo registro en el modelo destino(reparto)
    def add_reparto(self):
        #Obtenemos referencia al modelo destino(reparto)
        repartoModel = self.env['reparto']
        #Tenemos que recorrer porque recordamos self referencia a todo el modelo
        for wiz in self:
            #Por cada elemento
            #Creamos un registro en "reparto"
            repartoModel.create({
                'codigoNumerico': wiz.codigoNumerico,
                'fechaInicio': wiz.fechaInicio,
                'fechaDevolver': wiz.fechaDevolver,
                'fechaEntrega': wiz.fechaEntrega,
                'repartidor': wiz.repartidor.id,
                'vehiculo': wiz.vehiculo.id,
                'kilometros': wiz.kilometros,
                'peso': wiz.peso,
                'volumen': wiz.volumen,
                'observacions': wiz.observacions,
                'estadoEntrega': wiz.estadoEntrega,
                'clienteEmissor': wiz.clienteEmissor.id,
                'clienteReceptor': wiz.clienteReceptor.id,
                'urgencia': wiz.urgencia               
            })