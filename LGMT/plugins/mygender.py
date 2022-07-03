from LGMT import ALF
from telethon import events, Button
from telethon.tl.custom import button
from YashuAlpha.genders import *
from Hexa import *
from NayanTara.inherits import *
from telethon.utils import get_display_name as rupali

@ALF.on(events.NewMessage(incoming=True, pattern="/mygender"))
async def smexy(event):
    a = event.sender_id
    alpha_entity = await ALF.get_entity(a)
    a_fn = rupali(alpha_entitiy)
