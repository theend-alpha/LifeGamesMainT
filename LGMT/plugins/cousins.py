from telethon import events
from LGMT import ALF
from Nayantara.inherits import *
from Hexa.Markups import *
from YashviDB.cousins_adb import *
from telethon.utils import get_display_name

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
    i_name = get_display_name(i_id)
    f_name = get_display_name(f_id)  
    i_mention = mentionuser(i_name, i_id)
    f_mention = mentionuser(f_name, f_id)
    await event.client.send_message(event.chat.id, 
