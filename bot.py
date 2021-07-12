from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
import re
import logging
logging.basicConfig(level=logging.WARNING)
import telegram
from BrainyQuotes import getQuotes
import os


def get_quote(query):
    try:
        data = getQuotes(query)
        quote = data["quote"]
    except:
        return 'Invalid Query , Try Others....\n What About "Technology" ,"Nature" ,"Love" 🙂 '
    author = data["author"]
    qt_link = data["quotelink"]
    auth_link = data["authorlink"]
    quoteImage = data["quoteImage"]

    message = f"{quote} \n {author}"
    dataDict = {"message":message,"img":quoteImage}

    return dataDict


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

def quote(update,context):

    chat_id = update.message.chat_id
    if update.message:  # your bot can receive updates without messages
            # Reply to the message
            query = update.message.text
            data = get_quote(query)
            context.bot.send_message(chat_id=update.effective_chat.id,parse_mode=telegram.ParseMode.MARKDOWN, text=str(data["message"]))
            context.bot.sendPhoto(chat_id=update.effective_chat.id,photo=data["img"])



def start(update,context):
    name = "Hello! " + update.message.from_user["first_name"]
    context.bot.send_message(chat_id=update.effective_chat.id,text=name)

    welcome = """
Hi I'm Miyuki Shirogane, ofc the President! 

Send /help for Help 

Made By @featzai

Contact @ftfridaybot for Issues/Bugs etc
"""
    context.bot.send_message(chat_id=update.effective_chat.id,text=
welcome)


def help(update,context):
    helpmessage = '''
Send Me Any Topic or Word to Me 

I'll Send You A Quote based On Your Query

For Example : "love" , "kaguya" , "ishigami"   and Even "Hi" and "Hello"  

Type

/help to Get this Message 

/donate To Donate Me (Still Not Added)

if Any Issues Contact : @featzai 

Report Bugs @ftfridaybot 

'''
    context.bot.send_message(chat_id=update.effective_chat.id,text=helpmessage)

def donate(update,context):
    donate = '''
Donate Feature Haven't Added Yet 

'''
    context.bot.send_message(chat_id=update.effective_chat.id,text=donate )

def main():
    updater = Updater(os.environ.get("BOT_TOKEN", "1898039570:AAEixLvZWEVHp3PLqJ7dF8cTAsUM4cPvqVU"), use_context=True)
    dp = updater.dispatcher
    start_handler = CommandHandler("start",start)
    dp.add_handler(start_handler)

    help_handler = CommandHandler("help",help)
    dp.add_handler(help_handler)

    donate_handler = CommandHandler("donate",donate)
    dp.add_handler(donate_handler)

    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)

    quote_msg = MessageHandler(Filters.text,quote)
    dp.add_handler(quote_msg)

    updater.start_polling()
    updater.idle()
main()
