from config import TOKEN
from telegram.ext import Updater, CommandHandler, InlineQueryHandler, CallbackQueryHandler
import bot


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # COMANDOS

    # Crea un comando llamado start
    # que es manejado por la función start
    dispatcher.add_handler(CommandHandler("start", bot.start))
    dispatcher.add_handler(CommandHandler("mi_nombre", bot.mi_nombre))
    dispatcher.add_handler(CommandHandler("invertir", bot.invertir))
    dispatcher.add_handler(CommandHandler("sumar", bot.sumar))
    dispatcher.add_handler(CommandHandler("imagen", bot.imagen))
    dispatcher.add_handler(CommandHandler("histograma", bot.histograma))
    # inline keyboard
    dispatcher.add_handler(CommandHandler('teclado', bot.teclado))
    dispatcher.add_handler(CallbackQueryHandler(bot.opcion))

    # inline queries
    """
    Para poder permitir las inline queries en el bot
    es necesario activarlas primero en Bot Father.
    """
    dispatcher.add_handler(InlineQueryHandler(bot.inline_query))

    # INICIAR EL BOT
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
