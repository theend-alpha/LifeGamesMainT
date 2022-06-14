from telethon import events
from LGMT import ALF
from Nayantara.inherits import *
from Hexa.Markups import *
from YashviDB.cousins_adb import *

@ALF.on(events.NewMessage(incoming="True", pattern=["/cousin", "/cousin@nothehe_bot"]))
async def csn(event):
    i_id = event.sender_id
    hehe = event.text[8:]
    if event.reply_to_msg_id is not None:
        msg = await event.get_reply_message()
        f_id = msg.sender_id
    elif hehe is not None:
        if not hehe.isnumeric():
            await event.reply("Try: /cousin <user_id> ")
        f_id = hehe
        
        
