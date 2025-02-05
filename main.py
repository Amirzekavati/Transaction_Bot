import multiprocessing
from telegram.ext import Application
from config import BOT_TOKEN
from commands import get_handlers
from crawl import run_crawler

def start_bot():
    application = Application.builder().token(BOT_TOKEN).build()

    for handler in get_handlers():
        application.add_handler(handler)

    print("🤖 Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    # start_bot()
    bot_process = multiprocessing.Process(target=start_bot)
    crawler_process = multiprocessing.Process(target=run_crawler)

    bot_process.start()
    crawler_process.start()

    bot_process.join()
    crawler_process.join()

