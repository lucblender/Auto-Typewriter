from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

help_text =    "Welcome to the E-type bot by helixbyte!\n\n\n \
With this bot you can interact with the automatic typwriter \
made by helixbyte. \n\n \
A few commands are implemented : \n \
/help : will display this message\n\
/meteo : will print the meteo of Sion on the typewriter\n\
/calendar : will print your current week on google calendar\n\
/print_picture : will print the last sent picture in ascii art"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token='', use_context=True)

dispatcher = updater.dispatcher

def help_display(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
 
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=help_text) 
    
def meteo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="calm down, still need to implement this")
    
def calendar(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="calm down, still need to implement this")

def print_picture(update, context):     
    context.bot.send_message(chat_id=update.effective_chat.id, text="calm down, still need to implement this")
 
def simple_text(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Are you looking for help? /help might be what you're searching for")

def image_handler(update, context):
    file = context.bot.getFile(update.message.photo[-1].file_id)
    print ("file_id: " + str(update.message.photo[-1].file_id))
    file.download('image.jpg')
    context.bot.send_message(chat_id=update.effective_chat.id, text="The picture has been saved! Wanna print it? /print_picture if so!")

help_handler = CommandHandler('help', help_display)
dispatcher.add_handler(help_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

meteo_handler = CommandHandler('meteo', meteo)
dispatcher.add_handler(meteo_handler)

calendar_handler = CommandHandler('calendar', calendar)
dispatcher.add_handler(calendar_handler)

print_picture_handler = CommandHandler('print_picture', print_picture)
dispatcher.add_handler(print_picture_handler)

simple_text_handler = MessageHandler(Filters.text & (~Filters.command), simple_text)
dispatcher.add_handler(simple_text_handler)

updater.dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))
updater.start_polling()
updater.idle()