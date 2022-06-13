from telethon import events, Button
from telethon.tl.custom import button
from LGMT import ALF


@ALF.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("Hey! Am alive")
