from telethon import events
from LGMT import ALF
from NayanTara.inherits import *
from Hexa.Markups import *
from Hexa.Texts import *
from YashviDB.cousins_adb import *
from YashviDB.genders_adb import id_is_male, id_is_female
from telethon.utils import get_display_name

f_id = None
i_mention = None
f_mention = None
i_id = None

@ALF.on(events.NewMessage(incoming="True", pattern="/cousin"))
async def csn(event):
    global f_id
    global i_mention
    global f_mention
    global i_id
    i_id = event.sender_id
    hehe = event.text[8:]
    if event.reply_to_msg_id is not None:
        msg = await event.get_reply_message()
        f_id = msg.sender_id
    elif hehe is not None:
        if not hehe.isnumeric():
            await event.reply("Try: /cousin <user_id> or reply to an user")
        f_id = hehe
    if not hehe.isnumeric():
        return
    elif are_cousins(i_id, f_id) is False:
        if id_is_male(i_id) is True:
            gender = "his"
        elif id_is_female(i_id) is True:
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
    
@Yashu.on_message(filters.command(["cousin", "cousin@nothehe_bot"]) & ~filters.edited & filters.group & ~filters.via_bot)
async def ofmn(_, m: YashuBaby):
    global i_mention
    global f_mention
    init_id = m.from_user.id
    final_id = m.reply_to_message.from_user.id
    i_mention = m.from_user.mention
    f_mention = (await _.get_users(final_id)).mention
