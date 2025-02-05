import asyncio
import pytse_client as tse
from telegram import Bot
from database import AgentDataBase
from config import BOT_TOKEN

# Initialize database and bot
database = AgentDataBase()
bot = Bot(token=BOT_TOKEN)

async def check_stock_volumes():
    while True:
        all_users = database.get_all_users()
        for user_id in all_users:
            stocks = database.get_user_stocks(user_id)

            for stock in stocks:
                stock_name = stock["StockName"]
                user_stock_amount = stock["StockAmount"]

                try:
                    tse.download(symbols=stock_name)
                    ticker = tse.Ticker(stock_name)
                    market_volume = ticker.volume

                    if user_stock_amount <= market_volume:
                        message = (
                            f"⚠️ Alert:   '{stock_name}' ({market_volume}) "
                        )
                        await bot.send_message(chat_id=user_id, text=message)
                        print(f"✅ Alert sent to {user_id} about stock {stock_name}.")

                except Exception as e:
                    print(f"⚠️ Error checking stock {stock_name}: {e}")

        await asyncio.sleep(10)
