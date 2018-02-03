from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from wit import Wit
from tokenconfig import TOKEN, WIT
import cloudconvert
import logging

#logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = Wit(WIT)
updater = Updater(token=TOKEN)

dispatcher = updater.dispatcher

#Start function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello, I am a bot! Please talk to me!')
#Start function Commandhandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
