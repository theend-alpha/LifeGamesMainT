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

a = None
b = None

@ALF.on(events.NewMessage(incoming=True, patter="/cousin"))
async def acsn(event):
    global a
    global b 
    a = event.sender_id
    if event.sender_id:
        if event.text.spilt(None, 1)[1]:
            if event.text.split(None, 1)[1][0] == "@":
                try:
                    b = await ALF.get_entity(event.text.split(None, 1)[1]).id
                except:
                    pass
            else:
                return
        else:
            b = await get_user(event)
    else:
        return
    cousins = await are_cousins(a, b)
    if cousins:
        return
    female = await is_female(a)
    a_fn = await ALF.get_entity(a).get_display_name
    b_fn = await ALF.get_entity(b).get_display_name
    a_m = nayantara(a_fn, a)
    b_m = nayantara(b_fn, b)
    ladki = " 👧 "
    ladka = " 👦 "
    await event.send_message(event.chat_id, f"{ladki if female else ladka} {a_m} **wants** {b_m} **as {"her" if female else "his"} cousin**", buttons=cousin_markup)

@ALF.on(events.CallbackQuery(pattern=r"csnaccept"))
async def csna(event):
    if b != event.query.user_id:
        return await event.answer()
    await add_cousin(a, b)
    await add_cousin(b, a)
    await event.edit(f"{b_m} **accepted** {a_m} **as their cousin**")
         
        
