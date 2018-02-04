from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from wit import Wit
from tokenconfig import TOKEN, WIT, CONVERT
import cloudconvert
import logging

#logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

client = Wit(WIT)
updater = Updater(token=TOKEN)
api = cloudconvert.Api()

dispatcher = updater.dispatcher

#Start function
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello, I am a bot! Please talk to me!')
#Start function Commandhandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def convertOgg():
    voice = update.message.voice.file_id

    process = api.convert({
        "inputformat": "ogg",
        "outputformat": "wav",
        "input": "raw",
        "file": voice,
        "filename": "voice.ogg"
    })
    process.wait()
    return process

def overall(bot, update):
    # convert function
    # wit.ai voice to text function

overall_handler = MessageHandler(Filters.voice, overall)
dispatcher.add_handler(overall_handler)

updater.start_polling()
