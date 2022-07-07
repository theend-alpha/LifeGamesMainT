from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from LGMT import ALF
from NayanTara.inherits import *
from Hexa.Markups import *
from Hexa.Texts import *
from YashuAlpha.cousins import *
from YashuAlpha.genders import *
from telethon.utils import get_display_name

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

@ALF.on(events.NewMessage(incoming=True, patter="/cousin"))
async def acsn(event):
    a = event.sender_id
    if event.sender_id:
        if event.text.spilt(None, 1)[1]:
            if event.text.split(None, 1)[1][0] == "@":
                try:
                    b = await ALF.get_entity(event.text.split(None, 1)[1])
                except:
                    pass
            else:
                return
        else:
            b = await get_user(event)
    else:
        return
