from telegram.ext import CommandHandler
from handlers import start, help, add_stock_conversation

def get_handlers():
    return [
        CommandHandler('start', start),
        CommandHandler('help', help),
        add_stock_conversation,
    ]