from LGMT import ALF
from telethon import events, Button
from telethon.tl.custom import button
from YashviDB.genders_adb import add_male, add_female, rmv_male, rmv_female, id_is_male, id_is_female, get_males, get_females

OMFOO = []

def mentionuser(name, userid):
    return f"[{name}](tg://user?id={userid})"

xD = "https://te.legra.ph/file/9a207e6e453a93ab2b165.jpg"

gender_button = [
        [
        Button.inline("Male 👦 ", data="male"),
        Button.inline("Female 👧 ", data="female"),
        ],
        ]

@ALF.on(events.NewMessage(incoming=True, pattern="/mygender"))
async def gender(event):
    global OMFOO
    OMFOO.append(event.sender_id)
    if id_is_male(event.sender_id) is True:
        gender = " 👦 "
    elif id_is_female(event.sender_id) is True:
        gender = " 👧 "
    else:
        gender = " None "
    await event.client.send_file(event.chat.id, xD, caption=f"""Current Status :- {gender} \n\n Specify Your Gender !""", buttons=gender_button)


@ALF.on(events.CallbackQuery(pattern=r"male"))
async def maleback(event):
    if event.query.user_id in OMFOO:
        rmv_male(event.sender_id)
        rmv_female(event.sender_id)
        add_male(event.sender_id)
        await event.edit("your gender is updated to male 👦 ")
        OMFOO.remove(event.query.user_id)
    else:
        await event.answer("This is not for you", cache_time=0, alert=True)

@ALF.on(events.CallbackQuery(pattern=r"female"))
async def maleback(event):
    if event.query.user_id in OMFOO:
        rmv_female(event.sender_id)
        rmv_male(event.sender_id)
        add_female(event.sender_id)
        await event.edit("your gender is updated to female 👧 ")
        OMFOO.remove(event.query.user_id)
    else:
        await event.answer("This is not for you", cache_time=0, alert=True)

@ALF.on(events.NewMessage(pattern="/flee"))
async def flee(event):
    if id_is_male(event.sender_id) is True:
        rmv_male(event.sender_id)
        await event.reply("your gender is updated from male to none")
    elif id_is_female(event.sender_id) is True:
        rmv_female(event.sender_id)
        await event.reply("your gender is updated from female to none")
    else:
        await event.reply("your gender is already none \n\n /mygender to set")

@ALF.on(events.NewMessage(patter="/users"))
async def users(event):
    no_of_males = get_males()
    no_of_females = get_females()
    await event.reply(f""" Bot Users : \n\n Males - {no_of_males}\n Females - {no_of_females}""")
