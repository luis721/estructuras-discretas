import traceback

# Las diferentes funciones del bot

def start(update, context):
    update.message.reply_text("Ha iniciado conversación con el bot.")


def saludo(update, context):
    primer_nombre = update.message.chat.first_name
    apellidos = update.message.chat.last_name
    update.message.reply_text(f"Hola {primer_nombre} {apellidos}.")


def foto(update, context):
    # Obtener la ID del chat
    chat_id = update.message.chat.id
    # archivo
    img = open('./multimedia/imagen1.jpg', 'rb')
    # Enviar imagen
    context.bot.send_photo(chat_id, photo=img)
