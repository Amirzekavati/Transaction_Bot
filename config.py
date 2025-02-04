import os
from dotenv import load_dotenv
from database import AgentDataBase

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_PREFIX = os.getenv("BOT_PREFIX", "/")

OWNER_ID = int(os.getenv("OWNER_ID"))

ALLOWED_USERS_ID = os.getenv("ALLOWED_USERS_ID")
print(ALLOWED_USERS_ID)
if ALLOWED_USERS_ID:
    ALLOWED_USERS_ID = [int(user_id.strip()) for user_id in ALLOWED_USERS_ID.split(",")]
else:
    ALLOWED_USERS_ID = []


DB_URL = os.getenv("DATABASE_URL")

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"
if DEBUG_MODE:
    print("Bot is running in debug mode.")
else:
    print("Bot is running in production mode.")

MAX_MESSAGES_PER_HOUR = int(os.getenv("MAX_MESSAGES_PER_HOUR", "200"))
MESSAGE_DELAY = int(os.getenv("MESSAGE_DELAY", "1"))

USE_HTTPS = os.getenv("USE_HTTPS", "True").lower() == "true" 

required_vars = ["BOT_TOKEN", "OWNER_ID"]
for var in required_vars:
    if not globals()[var]:
        raise ValueError(f"Missing required environment variable: {var}")
    
database = AgentDataBase()
database.check_connection()

print(f"✅ Config Loaded: Prefix={BOT_PREFIX}, Debug={DEBUG_MODE}")
