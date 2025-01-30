from telegram.ext import Application
from config import BOT_TOKEN
from commands import get_handlers
import asyncio

if __name__ == "__main__":
    application = Application.builder().token(BOT_TOKEN).build()
    
    for handler in get_handlers():
        application.add_handler(handler)
        
    print("🤖 Bot is starting...")
    application.run_polling()
    