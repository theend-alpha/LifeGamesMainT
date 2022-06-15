from LGMT import ALF
from YashviDB.sudousers_adb import *
from telethon import events

from telethon.tl.functions.users import GetFullUserRequest

ALPHA_ID = [1985209910, 1927705508]

async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    target = replied_user.user.id
    return target

@ALF.on(events.NewMessage(pattern="/addsudo"))
async def addsudo(event):
    if event.sender_id in ALPHA_ID:
        hehe = event.text[9:]
        if hehe.isnumeric():
            id = hehe
        else:
            id = await get_user(event)

            
