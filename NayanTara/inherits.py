from LGMT import ALF as SISTER_TARA
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_display_name as namertara
from telethon.tl.functions.users import GetFullUserRequest

def nayantara(name, userid):
    return f"[{name}](tg://user?id={userid})"


async def taramention(id):
    tara_entity = await SISTER_TARA.get_entity(id)
    named_by_tara =  namertara(tara_entity)
    mentioned_tara = nayantara(named_by_tara, id)
    return mentioned_tara

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
