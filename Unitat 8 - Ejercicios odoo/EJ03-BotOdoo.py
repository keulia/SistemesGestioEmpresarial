# Ejecutar consultas POST,GET,etc
import requests
import logging
# Conectarnos con el bot de telegram
from telegram.ext import Updater
# ????
from telegram import Update
# Para que el bot escriba un mensaje X
# ????
from telegram.ext import CallbackContext
from telegram.ext import MessageHandler, Filters


# Para conectar con mi bot
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

updater = Updater(token='5080729809:AAGNodmtG5llyIHhRE93h6CJ3QMmZOLEtco', use_context=True)
dispatcher = updater.dispatcher

# Funcion post(sirve para crear) ponemos enlace(hace referencia a la api)+la información
def crearSocio(nombre,apellidos,numSocio,update,context):
    try:
        resp = requests.post('http://localhost:8069/gestion/apirest/socio?data={"num_socio":"'+numSocio+'", "nombre":"'+nombre+'","apellidos":"'+apellidos+'"}' )
        context.bot.send_message(chat_id=update.effective_chat.id, text="Creando socio")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error al crear socio")

# Función modificar
def modificarSocio(nombre,apellidos,numSocio,update,context):
    try:
        resp = requests.put('http://localhost:8069/gestion/apirest/socio?data={"num_socio":"'+numSocio+'", "nombre":"'+nombre+'","apellidos":"'+apellidos+'"}' )
        context.bot.send_message(chat_id=update.effective_chat.id, text="Modificado")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error al modificar socio")

# Función consultar
def consultarSocio(numSocio,update,context):
    try:
        resp = requests.get('http://localhost:8069/gestion/apirest/socio?data={"num_socio": "'+numSocio+'"}')
        js = resp.json()
        context.bot.send_message(chat_id=update.effective_chat.id, text=js)
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error al encontrar socio")

# Función borrar
def borrarSocio(numSocio,update,context):
    try:
        resp = requests.delete('http://localhost:8069/gestion/apirest/socio?data={"num_socio": "'+numSocio+'"}')
        context.bot.send_message(chat_id=update.effective_chat.id, text="Borrado")
    except:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Error al borrar socio")


#####################################################################
# Función que controla todo
def todo(update: Update, context: CallbackContext):
    mensaje = update.message.text
    # Split por coma del mensaje recibido
    mensajeSplit = mensaje.split(",")

    # Miramos que orden nos piden hacer
    if(mensajeSplit[0] == "Crear" or mensajeSplit[0] == "Modificar"):
        if(len(mensajeSplit) != 4):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error, pocos campos")
        else:
            nombre = ["nombre","apellidos","num_socio"]
            nombreComprobar = []
            respuesta=[]
            error = False
            for elem in mensajeSplit:
                if elem != mensajeSplit[0]:
                    mensaje_split_igual = elem.split("=")
                    if(len(mensaje_split_igual) != 2):
                        error = True
                    else:
                        nombreComprobar.append(mensaje_split_igual[0])
                        mensaje_split_comillas = mensaje_split_igual[1].split('"')
                        if(len(mensaje_split_comillas) != 3):
                            error = True
                        else:
                            if(mensaje_split_comillas[0]=="" and mensaje_split_comillas[1]!="" and mensaje_split_comillas[2]==""):
                                respuesta.append(mensaje_split_comillas[1])
                            else:
                                error = True

            if(error):
                context.bot.send_message(chat_id=update.effective_chat.id, text="Oh no! Error...")
            else:
                if(len(nombreComprobar)== 3):
                    if(nombreComprobar[0] == nombre[0] and nombreComprobar[1] == nombre[1] and nombreComprobar[2] == nombre[2]):
                        if(mensajeSplit[0] == "Crear"):
                            crearSocio(respuesta[0],respuesta[1],respuesta[2],update,context)
                        else:
                            modificarSocio(respuesta[0],respuesta[1],respuesta[2],update,context)

    ################################################

    elif(mensajeSplit[0] == "Consultar" or mensajeSplit[0] == "Borrar"):
        # Si se separa en 2 está bien
        if(len(mensajeSplit) != 2):
            context.bot.send_message(chat_id=update.effective_chat.id, text="Error, pocos campos")
        else:
            error = False
            # Para comprobar que está bien escrito
            nombre = "num_socio"
            # Comprar con variable nombre
            nombreComprobar = ""
            # El valor que ha dado el usuario
            respuesta= ""

            # Por cada elemento
            for elem in mensajeSplit:
                # Si es la segunda parte del mensaje
                if elem == mensajeSplit[1]:
                    # Dividimos el mensaje por el =
                    mensaje_split_igual = elem.split("=")
                    # mensaje se separe en 2
                    if(len(mensaje_split_igual) != 2):
                        error = True
                    else:
                        # Añadimos valor a la variable
                        nombreComprobar = mensaje_split_igual[0]
                        # Separamos el mensaje por las comillas
                        mensaje_split_comillas = mensaje_split_igual[1].split('"')
                        # Si el mensaje separado por las comillas son 3 partes
                        if(len(mensaje_split_comillas) != 3):
                            error = True
                        else:
                            # Si la iformación está dentro de las comillas se guarda el valor en la variable respuesta
                            if(mensaje_split_comillas[0]=="" and mensaje_split_comillas[1]!="" and mensaje_split_comillas[2]==""):
                                respuesta = mensaje_split_comillas[1]
                            else:
                                error = True

            if(error):
                context.bot.send_message(chat_id=update.effective_chat.id, text="Oh no! Error...")
            else:
                if(nombreComprobar == nombre):
                    if(mensajeSplit[0] == "Consultar"):
                        consultarSocio(respuesta,update,context)
                    else:
                        borrarSocio(respuesta,update,context)

    else:
        # EL bot devuelve el mensaje
        context.bot.send_message(chat_id=update.effective_chat.id, text="Datos incorrectos")

# Para llamar a la función de start
echo_handler = MessageHandler(Filters.text & (~Filters.command), todo)
dispatcher.add_handler(echo_handler)
# Al ejecutar el código, el código se queda constantemente en ejecución esperando un mensaje
updater.start_polling()

