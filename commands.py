from telegram.ext import CommandHandler
from .handlers import start, help

def get_handlers():
    return [
        CommandHandler('start', start),
        CommandHandler('help', help),
    ]