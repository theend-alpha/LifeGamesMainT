from LGMT import ALF
from telethon import events, Button
from telethon.tl.custom import button
from YashuAlpha.genders import *
from Hexa import *
from NayanTara.inherits import *
from telethon.utils import get_display_name as rupali

sed = "https://te.legra.ph/file/7d3cf74eba54fc4559909.jpg"

@ALF.on(events.NewMessage(incoming=True, pattern="/mygender"))
async def smexy(event):
    a = event.sender_id
    alpha_entity = await ALF.get_entity(a)
    a_fn = rupali(alpha_entitiy)
    is_male = await is_male(a)
    is_female = await is_female(a)
    await event.client.send_file(event.chat_id, sed, caption=GENDER_TXT.format(a_fn, " 👧 " if is_female else " 👦 "), buttons=gender_markup)

    
