import asyncio
import pytse_client as tse
from telegram import Bot
from database import AgentDataBase
from config import BOT_TOKEN

# Initialize database and bot
database = AgentDataBase()
bot = Bot(token=BOT_TOKEN)

async def check_stock_volumes():
    """Continuously checks stock volumes and notifies users if needed."""
    while True:
        all_users = database.get_all_users()  # Get all users who own stocks
        for user_id in all_users:
            stocks = database.get_user_stocks(user_id)  # Get stocks for each user

            for stock in stocks:
                stock_name = stock["StockName"]
                user_stock_amount = stock["StockAmount"]

                try:
                    tse.download(symbols=stock_name)  # Fetch the latest stock data
                    ticker = tse.Ticker(stock_name)
                    market_volume = ticker.volume  # Get the latest stock volume

                    # If user stock amount is greater than or equal to market volume, send alert
                    if user_stock_amount <= market_volume:
                        message = (
                            f"⚠️ Alert:   '{stock_name}' ({user_stock_amount}) "
                        )
                        await bot.send_message(chat_id=user_id, text=message)
                        print(f"✅ Alert sent to {user_id} about stock {stock_name}.")

                except Exception as e:
                    print(f"⚠️ Error checking stock {stock_name}: {e}")

        await asyncio.sleep(60)  # Wait 60 seconds before checking again
