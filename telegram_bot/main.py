from mainbot.messages import MessageHandler

botmsg = MessageHandler()

class PizzaBot:
    def handle_msg(bot, update, user_data):
        msg = update.message.text
        msg = botmsg.handle_msg(msg)
        bot.send_message(chat_id = update.effective_chat.id, text=msg)
