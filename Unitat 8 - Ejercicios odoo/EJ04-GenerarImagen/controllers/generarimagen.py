# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#N ecesario para trabajar con base64
import base64

# Biblioteca para guardar la imagen en memoria antes de pasarla a base64
import io
# Nos permite interactuar y conseguir información del sistema operativo
import os
# Necesario para trabajar PIL
from PIL import Image



# Clase del controlador web
class GenerarImagen(http.Controller):
    '''
    LLamada web para generar una imagen random.
    Se puede probar accediendo a http://localhost:8069/generador/300/400
    Y nos devolvera via web una imagen generada

    '''
    @http.route('/generador/<anchura>/<altura>', auth='public', cors='*', type='http')
    # Creamos la imagen
    def crearImagen(self, anchura, altura, **kw):
        
        # Converetimos la anchura y altura en int
        tamanio = (int(anchura), int(altura))
        # Pasamos la anchura y altura al crear la imagen
        img = Image.new("RGB", tamanio)

        def gen():
            # "urandom" genera más casos aleatorios que "random". 
            return os.urandom(int(anchura)*int(altura))
        
        # usamos zip para meter la información en una tupla y devolverla
        pixels = zip(gen(),gen(),gen())
        # "putdata" copia la información de los pixeles a la imagen que hemos puesto "img"
        img.putdata(list(pixels))


        # Guardar la imagen como un texto para mostrar en base64
        with io.BytesIO() as output:
            img.save(output, format="JPEG")
            contents = output.getvalue()
        # Pasamos el flujo de bytes y lo codificamos en base 64
        img_str = str(base64.b64encode(contents).decode("utf-8"))
        # Devolvemos el HTML que muestra la imagen generada, pasada como base64
        return '<div><img src="data:image/jpeg;base64,'+img_str+'"/></div>'

