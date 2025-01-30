from telegram.ext import Application
from .config import BOT_TOKEN
from .commands import get_handlers

async def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    for handler in get_handlers():
        application.add_handler(handler)
        
    await application.run_polling()
    
if __name__ =='__main__':
    import asyncio
    asyncio.run(main())
    