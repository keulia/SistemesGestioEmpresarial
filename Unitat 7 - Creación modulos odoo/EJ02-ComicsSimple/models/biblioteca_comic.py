# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

# Definimos el modelo de BaseArchive
class BaseArchive(models.AbstractModel):

    _name = 'base.archive' # Nombre del modelo
    _description = 'Fichero abstracto' # Descripcion del modelo

    activo = fields.Boolean(default=True)


    def archivar(self):
        # Por cada registro del modelo
        for record in self:
            # Cambiamos activo a False
            record.activo = not record.activo


# Definimos el modelo Biblioteca comic
class BibliotecaComic(models.Model):

    _name = 'biblioteca.comic' # Nombre del modelo
    _description = 'Comic de biblioteca' # Descripcion del modelo
    _inherit = ['base.archive'] # Hereda de "base.archive"
    
    # Parametros para ordenar
    _order = 'fecha_publicacion desc, nombre'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Indicamos que atributo sera el que se usara para mostrar nombre.
    #Por defecto es "name", pero si no hay un atributo que se llama name, aqui lo indicamos
    #Aqui indicamos que se use el atributo "nombre"
    _rec_name = 'nombre' # Atributo nombre
    nombre = fields.Char('Titulo', required=True, index=True) # nombre, es un campo de texto
    estado = fields.Selection(
        [('borrador', 'No disponible'),
         ('disponible', 'Disponible'),
         ('perdido', 'Perdido')],
        'Estado', default="borrador") # Estado, seleccionar entre las distintas opciones
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False) # Descripción, es un campo HTML
    portada = fields.Binary('Portada Comic') # Portada, campo binario
    fecha_publicacion = fields.Date('Fecha publicación') # fecha, campo de fecha
    precio = fields.Float('Precio') # precio, campo float
    paginas = fields.Integer('Numero de páginas',
        groups='base.group_user',
        estados={'perdido': [('readonly', True)]},
        help='Total numero de paginas',
        company_dependent=False)
    valoracion_lector = fields.Float(
        'Valoración media lectores',
        digits=(14, 4),  
    )
    # de Odoo (Es un elemento que puede ser empresa o individuo)
    # https://stackoverflow.com/questions/22927605/what-is-res-partner
    autor_ids = fields.Many2many('res.partner', string='Autores')

    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El titulo Comic debe ser único.'),
        ('positive_page', 'CHECK(paginas>0)', 'El comic debe tener al menos una página')
    ]

    #Indicamos que esta funcion es una "Constraints" de ese atributos
    #Dicho de otra forma, cada vez que se cambie ese atributo, se lanzara esta funcion
    #Y si la funcion detecta un cambio inadecuado, cambiara una instruccion
    #Util cuando la constraint no se puede definir con sintaxis SQL y debe indicar en una funcion
    @api.constrains('fecha_publicacion')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:
            if record.fecha_publicacion and record.fecha_publicacion > fields.Date.today():
                raise models.ValidationError('La fecha de lanzamiento debe haber sido antes a hoy')


