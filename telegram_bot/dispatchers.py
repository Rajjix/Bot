from telegram.ext import RegexHandler
from telegram.ext import Updater

from .main import PizzaBot

updater = Updater(token="702876825:AAGgkndMF9HswFWczI2M8-F-IPE74n2XMn8")

pizza_bot = {
    'msg': RegexHandler('.*', PizzaBot.handle_msg, pass_user_data=True)
    }
