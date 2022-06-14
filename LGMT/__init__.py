import os
from telethon import TelegramClient, events
import pyrogram as Alpha

API_ID = 14151343
API_HASH = "9330f17086496c4580bdc8f8b24ec364"
BOT_TOKEN = os.getenv("BOT_TOKEN", default=None)

ALF = TelegramClient('ALF', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

MONGO_DB_URI = "mongodb+srv://keshavalpha:keshavalpha@cluster0.p7qz4.mongodb.net/?retryWrites=true&w=majority"
