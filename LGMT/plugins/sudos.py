from LGMT import ALF
from YashviDB.sudousers_adb import *
from telethon import events
from NayanTara.inherits import *
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_display_name as goddess_tara

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

@ALF.on(events.NewMessage(incoming=True, pattern="/addsudo"))
async def addsudo(event):
    if event.sender_id in ALPHA_ID:
        id = await get_user(event)
        tara_entity = await ALF.get_entity(id)
        namertara = goddess_tara(tara_entity)
        id_mention = nayantara(namertara, id)
        if is_sudo(id) is False:
            add_sudo(id)
            await event.reply(f"{id_mention} is added as sudo user")
        else:
            await event.reply(f"{id_mention} is already a sudo user")
    else:
        await event.reply("Only Alpha can use this")
        
@ALF.on(events.NewMessage(incoming=True, pattern="/delsudo"))       
async def delsudo(event):
    if event.sender_id in ALPHA_ID:
        id = await get_user(event)
        tara_entity = await ALF.get_entity(id)
        namertara = goddess_tara(tara_entity)
        id_mention = nayantara(namertara, id)
        if is_sudo(id) is True:
            del_sudo(id)
            await event.reply(f"{id_mention} has been removed from sudo users")
        else:
            await event.reply(f"{id_mention} is not a sudo user")
    else:
        await event.reply("Only Alpha can use this")

@ALF.on(events.NewMessage(incoming=True, pattern="/sudos"))
async def sudos(event):
    if event.sender_id in ALPHA_ID:
        sudousers = list_sudo()
        msg = """"""
        for user in sudousers:
            tara_entity = await ALF.get_entity(user)
            namertara = goddess_tara(tara_entity)
            id_mention = nayantara(namertara, id)
            omfoo = str(user)
            msg += f"\n • {id_mention} ({omfoo})"
        try:
            await event.reply(msg)
        except:
            await event.reply("No sudo users")
