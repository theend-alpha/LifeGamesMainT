from telethon import events
from telethon.tl.functions.users import GetFullUserRequest
from LGMT import ALF
from NayanTara.inherits import *
from Hexa.Markups import *
from Hexa.Texts import *
from YashviDB.cousins_adb import *
from YashviDB.genders_adb import id_is_male, id_is_female
from telethon.utils import get_display_name
from pyrogram import Client as Yashu, filters
from pyrogram.types import Message as YashuBaby

f_id = None
i_mention = None
f_mention = None
i_id = None

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

@ALF.on(events.NewMessage(incoming="True", pattern="/cousin"))
async def csn(event):
    global f_id
    global i_id
    global i_mention
    global f_mention
    i_id = event.sender_id
    f_id = await get_user(event)
    entity_i = await ALF.get_entity(i_id)
    entity_f = await ALF.get_entity(f_id)
    i_mention = mentionuser(get_display_name(entity_i), i_id)
    f_mention = mentionuser(get_display_name(entity_f), f_id)
    if are_cousins(i_id, f_id) is False:
        if id_is_female(i_id) is True:
            gender = "her"
        else: 
            gender = "his"
        await event.client.send_message(event.chat.id, COUSIN_REQ_TXT.format(i_mention, f_mention, gender), buttons=cousin_markup)      
    else:
        await event.reply("Your both are already cousins 👦👧")

@ALF.on(events.CallbackQuery(pattern=r"csnaccept"))
async def csna(event):
    if event.query.user_id == f_id:
        if id_is_male(f_id) is True:
            gender = "his"
        elif id_is_female(f_id) is True:
            gender = "her"
        else:
            gender = "his"
        add_cousin(i_id, f_id)
        add_cousin(f_id, i_id)
        await event.edit(f"{f_mention} accepted {i_mention} as {gender} cousin...")
    else:
        await event.answer("this is not for you", cache_time=0, alert=True)

@ALF.on(events.CallbackQuery(pattern=r"csnreject"))
async def csnr(event):
    if event.query.user_id == f_id:
        await event.edit("rejected ! Sed xD")
    else:
        await event.answer("this is not for you", cache_time=0, alert=True)
    
