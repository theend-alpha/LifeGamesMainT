from LGMT import ALF as SISTER_TARA
from telethon.tl.functions.users import GetFullUserRequest
from telethon.utils import get_display_name as namertara

def nayantara(name, userid):
    return f"[{name}](tg://user?id={userid})"


def taramention(id):
    tara_entity = await SISTER_TARA.get_entity(id)
    named_by_tara =  namertara(tara_entity)
    mentioned_tara = nayantara(named_by_tara, id)
    return mentioned_tara
