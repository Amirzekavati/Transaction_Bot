from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import CallbackContext
from config import ALLOWED_USERS_ID, OWNER_ID

USER_OPTIONS = [["📈 View Stock", "📉 Sell Stock"], ["📊 Portfolio", "ℹ️ Help"]]
# ADMIN_OPTIONS = [["📢 Manage Channel", "🔍 Analyze Trends"], ["⚙️ Settings", "📊 Portfolio"], ["ℹ️ Help"]]

async def start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    
    print(f"{user_id} attempting to join")
    if user_id in ALLOWED_USERS_ID:
        
        # if user_id == OWNER_ID:
        #     keyboard = ADMIN_OPTIONS
        # else:
        keyboard = USER_OPTIONS
            
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        
        await update.message.reply_text(
            "Welcome, you're authorized to use this bot!",
            reply_markup=reply_markup
        )

    else:
        await update.message.reply_text("Sorry, you're not authorized to use this bot.")
        
async def help(update: Update, context: CallbackContext):
    await update.message.reply_text("This bot is for help to buying and selling stock.\n \
                                Here are the available commands: /start, /addStock, /volume")