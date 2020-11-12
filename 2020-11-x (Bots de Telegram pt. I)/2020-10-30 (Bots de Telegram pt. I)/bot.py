import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent, \
    InlineQueryResultVideo, ParseMode, InlineKeyboardMarkup, InlineKeyboardButton
from uuid import uuid4
import traceback
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from enum import Enum, unique


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


@unique
class Operacion(Enum):
    SUMA = "1"
    RESTA = "2"
    MULTIPLICACION = "3"
    COEF_BINOMIAL = "4"
    POTENCIA = "5"


def teclado(update: telegram.Update, context):
    texto = update.message.text  # /teclado n m
    texto = texto[len('/teclado')+1:]
    texto = texto.split(" ")
    if len(texto) != 2:
        update.message.reply_text("Digite parámetros n y m válidos. Separados por un espacio.")
    else:
        n, m = int(texto[0]), int(texto[1])
        options = [
            [
                InlineKeyboardButton("Sumar", callback_data=f"{Operacion.SUMA.value} {n} {m}"),
                InlineKeyboardButton("Restar", callback_data=f"{Operacion.RESTA.value} {n} {m}"),
            ],
            [InlineKeyboardButton("Multiplicar", callback_data=f"{Operacion.MULTIPLICACION.value} {n} {m}"),
             InlineKeyboardButton("Potencia", callback_data=f"{Operacion.POTENCIA.value} {n} {m}"),
             InlineKeyboardButton("C(n, k)", callback_data=f"{Operacion.COEF_BINOMIAL.value} {n} {m}")]
        ]

        reply_markup = InlineKeyboardMarkup(options)

        update.message.reply_text('Elija una opción:', reply_markup=reply_markup)


def opcion(update, context):
    query = update.callback_query
    query.answer()
    data = query.data
    selected, n, m = tuple(data.split(" "))
    n, m = int(n), int(m)

    if selected == Operacion.SUMA.value:
        p = n + m
        query.message.reply_text(f"La suma de {n} y {m} es {p}")
    elif selected == Operacion.RESTA.value:
        p = n - m
        query.message.reply_text(f"La resta de {n} y {m} es {p}")
    elif selected == Operacion.MULTIPLICACION.value:
        p = n * m
        query.message.reply_text(f"La multiplicación de {n} y {m} es {p}")
    elif selected == Operacion.COEF_BINOMIAL.value:
        p = comb(n, m, exact=True)
        query.message.reply_text(f"C({n},{m}) es {p}")

    elif selected == Operacion.POTENCIA.value:
        p = n ** m
        query.message.reply_text(f"{n} elevado a la {m} es {p}")

