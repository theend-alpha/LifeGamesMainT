from decouple import config 
from telethon import TelegramClient, events

API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)

ALF = TelegramClient('ALF', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
