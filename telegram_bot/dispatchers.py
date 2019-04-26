from telegram.ext import RegexHandler
from telegram.ext import Updater

from .main import PizzaBot

updater = Updater(token="XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX-X-XXXXXXXXXXX")

pizza_bot = {
    'msg': RegexHandler('.*', PizzaBot.handle_msg, pass_user_data=True)
    }
