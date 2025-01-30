from telegram.ext import CommandHandler, MessageHandler, filters
from handlers import start, help, add_stock_conversation, show_stocks_handler

def get_handlers():
    return [
        CommandHandler('start', start),
        CommandHandler('help', help),
        MessageHandler(filters.Regex("📊 show stocks"), show_stocks_handler),
        add_stock_conversation,
    ]