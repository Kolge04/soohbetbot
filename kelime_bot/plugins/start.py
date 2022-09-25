from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕𝐌ə𝐧𝐢 𝐪𝐫𝐮𝐩𝐚 ə𝐥𝐚𝐯ə 𝐞𝐭➕", url=f"http://t.me/UlviSozBot?startgroup=new")
    ],
    [
        InlineKeyboardButton(" 𝐎𝐰𝐧𝐞𝐫🇦🇿 ", url="t.me/Rahid_2003"),
        InlineKeyboardButton("𝐃𝐢𝐠𝐞𝐫 𝐁𝐨𝐭𝐥𝐚𝐫", url="t.me/Rahid_44"),
    ]
])


START = """
**🔮 Salam👋 bu bot ilə söz tapmaq oyunu oynaya bilərsiniz..**

➤ Məlumat üçün 👉 /help üzərinə klikləyin.  Əmrlər asan və sadədir.
"""

HELP = """
**✌️ Əmrlər menyusuna xoş gəlmisiniz.**


/oyna - Söz tap oyunu başlat.
/kec - Sözü keç.
/reytinq - Oyunçular arasında rəqabət məlumatları.
/dayan - Oyunu dayandırar.
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/fbae3dc2b7e5c3863c1d5.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/fbae3dc2b7e5c3863c1d5.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("oyna")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**❗ Qrupunuzda  oyun artıq davam edir ✍🏻 \n Oyunu dayandırmaq üçün /dayan əmri yaza bilərsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən! \nsöz tapma oyunu başladı .\n\nUğurlar !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund : {oyun[m.chat.id]['round']}/100 
📝 Söz :   <code>{kelime_list}</code>
💰 Qazandığın Xal: 50
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışıq hərflərdən ibarət sözü tapın 
        """
        await c.send_message(m.chat.id, text)
        
