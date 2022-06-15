from LGMT import ALF
from YashviDB.sudousers_adb import *
from telethon import events

ALPHA_ID = [1985209910, 1927705508]

@ALF.on(events.NewMessage(pattern="/addsudo")
async def addsudo(event):
    if event.sender_id in ALPHA_ID:
        hehe = event.text[9:]
