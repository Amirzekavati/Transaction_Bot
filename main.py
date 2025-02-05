import asyncio
from telegram.ext import Application
from config import BOT_TOKEN
from commands import get_handlers
from monitor import check_stock_volumes

async def main():
    application = Application.builder().token(BOT_TOKEN).build()

    for handler in get_handlers():
        application.add_handler(handler)

    await asyncio.create_task(check_stock_volumes())

    print("🤖 Bot is starting...")
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
