import os
from telethon import TelegramClient, events

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH", default=None)
BOT_TOKEN = os.getenv("BOT_TOKEN", default=None)

ALF = TelegramClient('ALF', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

MONGO_DB_URI = "mongodb+srv://keshavalpha:keshavalpha@cluster0.p7qz4.mongodb.net/?retryWrites=true&w=majority"