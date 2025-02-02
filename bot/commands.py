from telegram.ext import CommandHandler, MessageHandler, filters
from handlers import start, help, add_stock_conversation, show_stocks_handler, remove_stock_conversation

def get_handlers():
    return [
        CommandHandler('start', start),
        MessageHandler(filters.Regex("ℹ️ Help"), help),
        MessageHandler(filters.Regex("📊 show stocks"), show_stocks_handler),
        add_stock_conversation,
        remove_stock_conversation,
    ]