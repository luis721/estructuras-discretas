# El punto de entrada

from config import TOKEN

import bot
from telegram.ext import Updater, CommandHandler


def main():
    # se asigna el token
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    # se añaden los métodos que controlan cada comando

    # mensajes de texto
    dispatcher.add_handler(CommandHandler('start', bot.start))
    dispatcher.add_handler(CommandHandler('saludo', bot.saludo))

    # contenido multimedia
    dispatcher.add_handler(CommandHandler('foto', bot.foto))

    # iniciar bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
