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
import threading
from time import sleep

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
/stop_type :  stop echo typing on the typewriter\n\
/cancel : stop /meteo, /calendar and /print_picture\n"

white_list_error = "Oops you're not in the whitelist, contact the bot dev if you wanna be in!"

admin_start = "Also, you look like an admin to me, try /admin_help for more stuff!"

unknown_command_error = "Oops, I don't know this command..."

admin_help_text = "Hi my dear Admin, here is a little reminder of what you can do:\n\n\
 /add_id id_number : add the id to the user whitelist (longclick on this since need parameter)\n\
/remove_id id_number : remove the id to the user whitelist(longclick on this since need parameter)\n\
/list_id : display the whitelist list\n\
As a reminder, id manipulation are effective only in a bot session, whitelistedid will be lost on a reboot except if they are part of hardcoded whitelist."

running_service = ""
cancel_action = False

running_service_string = lambda : "Oops the {} service is already running on the typewriter. You can use /cancel to stop it".format(running_service)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher

ECHO_ENABLED = False
PICTURE_NAME = "Telegram_picture.png"

def threaded_callback_service_finished(context, start_chat_id):
    global cancel_action
    while(autoTypewriter.running and cancel_action == False):
        sleep(0.5)
    if cancel_action:
        context.bot.send_message(chat_id=start_chat_id, text="The {} service got canceled!".format(running_service))
        autoTypewriter.press_string("\n")
        cancel_action = False
    else:
        context.bot.send_message(chat_id=start_chat_id, text="The {} service just finished!".format(running_service))

def help_display(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
        if update.effective_chat.id == ADMIN_ID:
            context.bot.send_message(chat_id=update.effective_chat.id, text=admin_start)

def add_id(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if update.effective_chat.id == ADMIN_ID:
            try:
                telegram_id = int(context.args[0])
                TELEGRAM_WHITE_LIST.append(telegram_id)
                context.bot.send_message(chat_id=update.effective_chat.id, text="Id {} added".format(telegram_id))
            except (IndexError, ValueError):
                context.bot.send_message(chat_id=update.effective_chat.id, text="You forgot to put an id or it wasn't a number")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_command_error)

def remove_id(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if update.effective_chat.id == ADMIN_ID:
            try:
                telegram_id = int(context.args[0])
                TELEGRAM_WHITE_LIST.remove(telegram_id)
                context.bot.send_message(chat_id=update.effective_chat.id, text="Id {} removed".format(telegram_id))
            except (IndexError, ValueError):
                context.bot.send_message(chat_id=update.effective_chat.id, text="You forgot to put an id or it wasn't a number")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_command_error)

def list_id(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if update.effective_chat.id == ADMIN_ID:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Here are the current whitelisted id:")
            for telegram_id in TELEGRAM_WHITE_LIST:
                context.bot.send_message(chat_id=update.effective_chat.id, text="- "+str(telegram_id))
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_command_error)

def admin_help_display(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if update.effective_chat.id == ADMIN_ID:
            context.bot.send_message(chat_id=update.effective_chat.id, text=admin_help_text)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_command_error)

def unknown_command(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=unknown_command_error)

def start(update, context):
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
        context.bot.send_message(chat_id=ADMIN_ID, text="New connection from someone not in the whitelist\nID: {} \nFistName: {}\nLastName: {}".format(update.effective_chat.id,update.effective_chat.first_name,update.effective_chat.last_name))
        context.bot.send_message(chat_id=ADMIN_ID, text="add it to the whitelist with :"))
        context.bot.send_message(chat_id=ADMIN_ID, text="/add_id {}".format(update.effective_chat.id))
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=help_text)
        if update.effective_chat.id == ADMIN_ID:
            context.bot.send_message(chat_id=update.effective_chat.id, text=admin_start)

def meteo(update, context):
    global running_service
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if autoTypewriter.running:
            context.bot.send_message(chat_id=update.effective_chat.id, text=running_service_string())
        else:
            running_service = "meteo"
            context.bot.send_message(chat_id=update.effective_chat.id, text="Retrieving meteo Info")
            text = typeMeteoService()
            context.bot.send_message(chat_id=update.effective_chat.id, text="Starting to print the meteo on typewriter!")
            autoTypewriter.threaded_underline_delimiter_press_string(text)
            t = threading.Thread(target=threaded_callback_service_finished, args=(context,update.effective_chat.id))
            t.start()
            context.bot.send_message(chat_id=update.effective_chat.id, text="The meteo has been sent to printer!")

def calendar(update, context):
    global running_service
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if autoTypewriter.running:
            context.bot.send_message(chat_id=update.effective_chat.id, text=running_service_string())
        else:
            running_service = "calendar"
            context.bot.send_message(chat_id=update.effective_chat.id, text="Retrieving calendar Info")
            text = typeAgendaService()
            context.bot.send_message(chat_id=update.effective_chat.id, text="Starting to print the calendar on typewriter!")
            autoTypewriter.threaded_press_string(text)
            t = threading.Thread(target=threaded_callback_service_finished, args=(context,update.effective_chat.id))
            t.start()
            context.bot.send_message(chat_id=update.effective_chat.id, text="The calendar has been sent to printer!")

def print_picture(update, context):
    global running_service
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if autoTypewriter.running:
            context.bot.send_message(chat_id=update.effective_chat.id, text=running_service_string())
        else:
            running_service = "picture printing"
            img = Image.open(PICTURE_NAME)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Converting the last received picture Ascii art")
            ascii_img = convertImageToAscii(img, 45, 0.5, False)
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sending the last received picture to the typewriter!")
            print(ascii_img)
            autoTypewriter.threaded_press_string(ascii_img)
            t = threading.Thread(target=threaded_callback_service_finished, args=(context,update.effective_chat.id))
            t.start()
            context.bot.send_message(chat_id=update.effective_chat.id, text="The picture is printing")

def start_type(update, context):
    global ECHO_ENABLED

    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if autoTypewriter.running:
            context.bot.send_message(chat_id=update.effective_chat.id, text=running_service_string())
        else:
            ECHO_ENABLED = True
            context.bot.send_message(chat_id=update.effective_chat.id, text="Echo typing is enabled on the typewriter")

def stop_type(update, context):
    global ECHO_ENABLED

    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if autoTypewriter.running:
            context.bot.send_message(chat_id=update.effective_chat.id, text=running_service_string())
        else:
            ECHO_ENABLED = False
            context.bot.send_message(chat_id=update.effective_chat.id, text="Echo typing is disabled on the typewriter")

def cancel(update, context):
    global running_service, cancel_action
    if update.effective_user.id not in TELEGRAM_WHITE_LIST:
        context.bot.send_message(chat_id=update.effective_chat.id, text=white_list_error)
    else:
        if autoTypewriter.running:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Cancelling the {} service".format(running_service))
            cancel_action = True
            autoTypewriter.cancel()
        else:
            context.bot.send_message(chat_id=update.effective_chat.id, text="No service do cancel apparently")




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

admin_help_handler = CommandHandler('admin_help', admin_help_display)
dispatcher.add_handler(admin_help_handler)

add_id_handler = CommandHandler('add_id', add_id)
dispatcher.add_handler(add_id_handler)

remove_id_handler = CommandHandler('remove_id', remove_id)
dispatcher.add_handler(remove_id_handler)

list_id_handler = CommandHandler('list_id', list_id)
dispatcher.add_handler(list_id_handler)

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

cancel_handler = CommandHandler('cancel', cancel)
dispatcher.add_handler(cancel_handler)

simple_text_handler = MessageHandler(Filters.text & (~Filters.command), simple_text)
dispatcher.add_handler(simple_text_handler)

unknown_command_handler = MessageHandler(Filters.command, unknown_command)
dispatcher.add_handler(unknown_command_handler)

updater.dispatcher.add_handler(MessageHandler(Filters.photo, image_handler))
updater.start_polling()
updater.idle()