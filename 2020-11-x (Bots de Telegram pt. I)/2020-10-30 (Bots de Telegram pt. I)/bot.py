from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultVideo, ParseMode
from uuid import uuid4
import traceback
import numpy as np
import matplotlib.pyplot as plt


def start(update, context):
    update.message.reply_text("Bienvenido al bot.")


def mi_nombre(update, context):
    nombre = update.message.from_user.name
    update.message.reply_text(f"Su nombre es: {nombre}")


def invertir(update, context):
    texto = update.message.text
    texto = texto[len("/invertir") + 1:]
    texto = texto[::-1]
    update.message.reply_text(f"Usted escribió:\n{texto}")


def sumar(update, context):
    texto = update.message.text
    texto = texto[len("/sumar") + 1:]
    numeros = texto.split(" ")
    if len(numeros) >= 2:
        suma = 0
        for numero in numeros:
            suma += int(numero)

        update.message.reply_text(f"La suma de los {len(numeros)} números es {suma}.")
    else:
        update.message.reply_text("Por favor digite al menos dos números. Use el formato /sumar a b c [...].")


def imagen(update, context):
    # archivo
    img = open('./multimedia/imagen1.jpg', 'rb')
    chat_id = update.message.chat.id
    context.bot.send_photo(chat_id, photo=img)


def histograma(update, context):
    chat_id = update.message.chat.id
    numeros = update.message.text[len('/histograma')+1:].split(" ")
    n, m = int(numeros[0]), int(numeros[1])
    random_numbers = np.random.randint(0, n, m, dtype=np.int64)
    # Creamos la figura
    fig = plt.figure(figsize=(6, 6))
    plt.title("Histograma", fontsize=18)
    plt.xlabel("Número", fontsize=12)
    plt.ylabel("Conteo", fontsize=12)
    plt.hist(random_numbers)
    plt.savefig("histograma.png")
    context.bot.send_photo(chat_id, open("histograma.png", "rb"))


def inline_query(update, context):
    # opciones a desplegar
    results = [
        InlineQueryResultArticle(
            id=uuid4(),  # SE REQUIERE
            title="Prueba",
            input_message_content=InputTextMessageContent("Esta es una posible opción en la inline query."),
            description="Test."
        ),
        InlineQueryResultArticle(
            id=uuid4(),  # SE REQUIERE
            title="Prueba2",
            input_message_content=InputTextMessageContent("Esta otra posible opción."),
            description="Test2."
        )
    ]

    # enviar resultado
    try:
        update.inline_query.answer(results, cache_time=2)
    except Exception as e:
        traceback.print_stack()
        print(e)

