from LGMT import ALF
from telethon import events, Button
from telethon.tl.custom import button
from YashviDB.genders_adb import add_male, add_female, rmv_male, rmv_female, id_is_male, id_is_female, get_males, get_females

def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"

xD = "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

gender_button = [
        [
        Button.inline("Male 👦 ", data="male")
        Button.inline("Female 👧 ", data="female")
        ]
        ]

@ALF.on(events.NewMessage(incoming=True, pattern="/gender"))
async def gender(event):
    await event.client.send_file(event.chat.id, xD
