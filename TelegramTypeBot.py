from telegram.ext import Updater
import logging
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from AutoTypewriter import AutoTypewriter
from KeyDictionnary import correct_string
from AsciiGenerator import convertImageToAscii
from PIL import Image
from TelegramData import *
from TypeMeteoService import typeMeteoService
from TypeAgendaService import typeAgendaService

autoTypewriter = AutoTypewriter()

help_text =    "Welcome to the E-type bot by helixbyte!\n\n\n \
With this bot you can interact with the automatic typwriter \
made by helixbyte. \n\n \
A few commands are implemented : \n \
/help : will display this message\n\
/meteo : will print the meteo of Sion on the typewriter\n\
/calendar : will print your current week on google calendar\n\
/print_picture : will print the last sent picture in ascii art\n\
/start_type : start echo typing on the typewriter\n\
/stop_type :  stop echo typing on the typewriter\n"

white_list_error = "Oops you're not in the whitelist, contact the bot dev if you wanna be in!"


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher

ECHO_ENABLED = False
PICTURE_NAME = "Telegram_picture.png"

def help_display(update, context):    
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
 
def start(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
        context.bot.send_message(chat_id=ADMIN_ID, text="New connection from someone not in the whitelist\nID: {} \nFistName: {}\nLastName: {}".format(update.effective_chat.id,update.effective_chat.first_name,update.effective_chat.last_name)) 
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_text) 
    
def meteo(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Retrieving meteo Info")
        text = typeMeteoService()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Starting to print the meteo on typewriter!")
        autoTypewriter.underline_delimiter_press_string(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text="The meteo has been printed!")
    
def calendar(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Retrieving calendar Info")
        text = typeAgendaService()
        context.bot.send_message(chat_id=update.effective_chat.id, text="Starting to print the calendar on typewriter!")
        autoTypewriter.press_string(text)
        context.bot.send_message(chat_id=update.effective_chat.id, text="The calendar has been printed!")

def print_picture(update, context):  
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:   
        img = Image.open(PICTURE_NAME)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Converting the last received picture Ascii art")
        ascii_img = convertImageToAscii(img, 45, 0.5, False)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Sending the last received picture to the typewriter!")
        print(ascii_img)
        autoTypewriter.press_string(ascii_img)
        context.bot.send_message(chat_id=update.effective_chat.id, text="Picture Printed")

def start_type(update, context):
    global ECHO_ENABLED
    
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        ECHO_ENABLED = True
        context.bot.send_message(chat_id=update.effective_chat.id, text="Echo typing is enabled on the typewriter")

def stop_type(update, context):
    global ECHO_ENABLED
    
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        ECHO_ENABLED = False
        context.bot.send_message(chat_id=update.effective_chat.id, text="Echo typing is disabled on the typewriter")

def image_handler(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        file = context.bot.getFile(update.message.photo[-1].file_id)
        print ("file_id: " + str(update.message.photo[-1].file_id))
        file.download(PICTURE_NAME)
        context.bot.send_message(chat_id=update.effective_chat.id, text="The picture has been saved! Wanna print it? /print_picture if so!")
 
def simple_text(update, context):
    global ECHO_ENABLED
    
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error) 
    else:
        if ECHO_ENABLED:
            text = correct_string(update.message.text)+"\n"
            autoTypewriter.press_string(text)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Are you looking for help? /help might be what you're searching for")

help_handler = CommandHandler('help', help_display)
dispatcher.add_handler(help_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

meteo_handler = CommandHandler('meteo', meteo)
dispatcher.add_handler(meteo_handler)

calendar_handler = CommandHandler('calendar', calendar)
dispatcher.add_handler(calendar_handler)

start_type_handler = CommandHandler('start_type', start_type)
dispatcher.add_handler(start_type_handler)

stop_type_handler = CommandHandler('stop_type', stop_type)
dispatcher.add_handler(stop_type_handler)

print_picture_handler = CommandHandler('print_picture', print_picture)
dispatcher.add_handler(print_picture_handler)

simple_text_handler = MessageHandler(Filters.text & (~Filters.command), simple_text)
dispatcher.add_handler(simple_text_handler)

updater.dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))
updater.start_polling()
updater.idle()