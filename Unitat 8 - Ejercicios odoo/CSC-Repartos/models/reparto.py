# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from odoo.http import request

# Definimos el modelo de Reparto
class reparto(models.Model):


    _name = 'reparto' # Nombre del modelo
    _inherit = ['base.archive'] # Hereda de "base.archive"
    _description = 'reparto' # Descripcion del modelo
    _order = 'fechaEntrega, urgencia' # Parametros para ordenar
    _rec_name = 'codigoNumerico'
    
    #Atributo nombre
    codigoNumerico = fields.Integer(string="ID", default=lambda self: self.env['ir.sequence'].next_by_code('codigoAutomatico')) # ID del reparto
    fechaInicio = fields.Datetime("Fecha y hora devolver") # Fecha de inicio
    fechaDevolver = fields.Datetime("Fecha y hora devolver") # Fecha de devolver
    fechaEntrega = fields.Datetime("Fecha y hora de la entrega") # Fecha de Entrega
    repartidor = fields.Many2one('empleados')  # Repartidor
    vehiculo = fields.Many2one('vehiculos') # Vehiculo
    kilometros = fields.Float("Kilometros")  # Kilometros de distancia
    peso = fields.Float("Peso") # Peso del pedido
    volumen = fields.Float("Volumen") # Volumen
    observacions = fields.Html('Observaciones', sanitize=True, strip_style=False) # Observaciones
    estadoEntrega = fields.Selection([('n','No ha salido'),('c','de camino'),('e','entregado')],string='Estado de la entrega') # Estado de la entrega
    clienteEmissor = fields.Many2one('clientes')  # Cliente emisor
    clienteReceptor = fields.Many2one('clientes') # Cliente receptor
    urgencia = fields.Selection([('0','organos humanos'),('1','alimentos congelados'),('2','alimentos'),('3','prioridad alta'),('4','prioridad baja')],string='Urgencia')  # Urgencia

    #Constraints de SQL del modelo
    # El DNI debe ser único
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (dni)', 'El dni debe ser único.')
    ]
    
    # Función para dar error en caso de que el repartidor 
    #   no tenga carnet y quiera usar un vehículo el cual requiere carnet
    @api.constrains('repartidor')
    def viajeCarnet(self):
        # Recorremos el modelo
        for record in self:            
            #si no tiene carnet SI puede ir en bici
            if ((record.repartidor.carnet == "n" and record.vehiculo.tipo == "f") or(record.repartidor.carnet == "n" and record.vehiculo.tipo == "c")) :
                raise models.ValidationError("No tiene carnet")
                # Si tiene el carnet de ciclomotor no puede ir en furgoneta
            elif record.repartidor.carnet == "c" and record.vehiculo.tipo == "f":
                raise models.ValidationError("No tiene furgoneta")
                # Si tiene el carnet de furgoneta no puede ir en ciclomotor
            elif record.repartidor.carnet == "f"and record.vehiculo.tipo == "c":
                raise models.ValidationError("No tiene ciclomotor")

    # Función para comprobar si el repartidor está de viaje
    @api.constrains('repartidor')
    def estanViaje(self):
        # Recorremos el modelo
        for record in self:
            reparto = request.env['reparto'].search([])

            for i in reparto:
               if i.id != record.id:
                   # Si el repartidor o vehiculo seleccionado no se encuentran disponibles
                   if ((i.repartidor == record.repartidor) or (record.vehiculo == i.vehiculo) and i.estadoEntrega == "c"):
                        raise models.ValidationError("El repartidor/vehiculo no se encuentran disponibles")

    # Función para en el caso de que el viaje sea más largo de 10km, el repartidor no puede
    #   ir en bicicleta        
    @api.constrains('repartidor')
    def menos10km(self):
        # Recorremos el modelo
        for record in self:
            if record.vehiculo.tipo == "b" and record.kilometros > 10:
                raise models.ValidationError("El viaje es demasiado largo, no se puede usar bicicleta")

    # Función para en el caso de que el viaje sea más corto de 1km, el repartidor no puede
    #   ir en furgoneta  
    @api.constrains('repartidor')
    def menos10km(self):
        # Recorremos el modelo
        for record in self:
            if record.vehiculo.tipo == "f" and record.kilometros < 1:
                raise models.ValidationError("El viaje es demasiado corto, no se puede usar furgoneta")
