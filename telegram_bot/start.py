from dispatchers import updater, pizza_bot
import logging

logging.basicConfig(format='%(asctime)s - %(name)s = %(levelname)s - %(message)s',
                    level=logging.INFO)

dispatcher = updater.dispatcher.add_handler

if __name__ == '__main__':
    dispatcher(pizza_bot['msg'])
    updater.start_polling()
