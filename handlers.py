from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler, MessageHandler, filters
from config import ALLOWED_USERS_ID, db

STOCK_NAME, STOCK_AMOUNT = range(2)

USER_OPTIONS = [["📈 add Stock", "📉 remove Stock"], ["📊 show stocks", "ℹ️ Help"]]
# ADMIN_OPTIONS = [["📢 Manage Channel", "🔍 Analyze Trends"], ["⚙️ Settings", "📊 Portfolio"], ["ℹ️ Help"]]

async def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    
    print(f"{user_id} attempting to join")
    if user_id in ALLOWED_USERS_ID:
        keyboard = USER_OPTIONS
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        
        await update.message.reply_text(
            "Welcome, you're authorized to use this bot!",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text("Sorry, you're not authorized to use this bot.")
        
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("This bot is for help to buying and selling stock.")
    
async def start_add_stock(update: Update, context: CallbackContext):
    """Starts the conversation for adding a stock."""
    await update.message.reply_text("Please send the name of the stock you'd like to add.")
    return STOCK_NAME

async def stock_name_received(update: Update, context: CallbackContext):
    """Receives the stock name and asks for the amount."""
    context.user_data["stock_name"] = update.message.text
    await update.message.reply_text("How many units of this stock do you want to add?")
    return STOCK_AMOUNT

async def stock_amount_received(update: Update, context: CallbackContext):
    """Receives the stock amount, stores it in the database, and confirms."""
    stock_name = context.user_data["stock_name"]
    stock_amount = int(update.message.text)
    user_id = update.message.from_user.id

    message = {
        "UserID": user_id,
        "StockName": stock_name,
        "StockAmount": stock_amount,
    }
    
    # Store in the database
    db.upsert(message)

    await update.message.reply_text(f"Stock {stock_name} (Amount: {stock_amount}) has been added to your stocks!")
    return ConversationHandler.END

async def cancel(update: Update, context: CallbackContext):
    """Handles cancellation of stock addition."""
    await update.message.reply_text("Operation cancelled.")
    return ConversationHandler.END

add_stock_conversation = ConversationHandler(
    entry_points=[MessageHandler(filters.Regex("📈 add Stock"), start_add_stock)],
    states={
        STOCK_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, stock_name_received)],
        STOCK_AMOUNT: [MessageHandler(filters.TEXT & filters.Regex("^[0-9]+$"), stock_amount_received)],
    },
    fallbacks=[CommandHandler("cancel", cancel)],
)

