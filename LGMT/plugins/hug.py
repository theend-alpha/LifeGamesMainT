from telethon import events, version, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from telethon.tl.functions.users import GetFullUserRequest
from LGMT import ALF

@ALF.on(events.NewMessage(incoming=True, pattern="/hug"))
async def hug(e):
    if e.sender_id in A_ID:
        start = datetime.now()
        text = "Pong!"
        event = await e.reply(text, parse_mode=None, link_preview=None )
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await event.edit(f"🎉 🇵 🇴 🇳 🇬 !\n\n♡︎ `{ms}` 𝗺𝘀 ♡︎")
