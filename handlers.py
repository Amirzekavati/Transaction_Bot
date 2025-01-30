from telegram import Update
from telegram.ext import CallbackContext
from .config import ALLOWD_USERS_ID

def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    if user_id in ALLOWD_USERS_ID:
        update.message.reply_text("Welcome, you're authorized to use this bot!")
    else:
        update.message.reply_text("Sorry, you're not authorized to use this bot.")
        
def help(update: Update, context: CallbackContext):
    update.message.reply_text("This bot is for help to buying and selling stock.\n \
                                Here are the available commands: /start, /addStock, /volume")