import random
import os
import logging
import asyncio
from telethon import Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from kelime_bot.mesaj import salam, necesen, getdim, geldim, sesizKOLGE, ban, emoji1, emoji2, fed, niye, ne, hay, mal, 

logging.basicConfig(can, balam, xos, hara, gel, gordum, taım, pp
from kelime_bot.bot import yeni_user, start, info
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)




api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
xaos = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)



# aykhan026 | aykhan_s | @sesizKOLGE
# əsası aykhan026 
# dəyişiklər @sesizKOLGE
# 0-dan yığılıb sənöl
# öz adına çıxaran papa de


xaos_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@xaos.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}",
                      buttons=(
			    
		              [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Chatbot?startgroup=a')],
			      [Button.url("👨‍💻 OWNER", "https://t.me/sesizKOLGE")],
			      [Button.inline("ℹ İNFO", data="info")],
                    ),
                    link_preview=False
		   )
                      
 
@xaos.on(events.callbackquery.CallbackQuery(data="start"))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}",
                      buttons=(
			    
		              [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Chatbot?startgroup=a')],
			      [Button.url("👨‍💻 OWNER", "https://t.me/sesizKOLGE")],
			      [Button.inline("ℹ İNFO", data="info")],
                    ),
                    link_preview=False
		   )
#info
@xaos.on(events.callbackquery.CallbackQuery(data="info"))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(info)}",
		      buttons=(
			    
		              [Button.url('➕ ℚℝ𝕌ℙ𝔸 𝔼𝕃𝔸𝕍𝔼 𝔼𝕋 ➕', 'https://t.me/XAOS_Chatbot?startgroup=a')],
			      [Button.url('👨‍💻 OWNER', 'https://t.me/sesizKOOGE')],
			      [Button.inline("◀️ GERİ", data="start")],
                    ),
                    link_preview=False
		   )



# Yeni istifadəçi mesajı
@xaos.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")
        
# Chatbot
 

isleyen = []

@xaos.on(events.NewMessage(pattern="^/chatbot ?(.*)"))
async def chatbot(event):
    global isleyen
    emr = event.pattern_match.group(1)
    qrup = event.chat_id
    if emr == "ON" or emr == "on" or emr == "On":
        if qrup not in isleyen:
            isleyen.append(qrup)
            aktiv_olundu = "✅ **ChatBot Qrupda Aktiv Olundu !**"
            await event.reply(aktiv_olundu)
            return
        await event.reply("⚠️ **ChatBot Hal-hazırda Qrupda Aktivdir !**")
        return
    elif emr == "OFF" or emr == "off" or emr == "Off":
        if qrup in isleyen:
            isleyen.remove(qrup)
            await event.reply("⛔️ **ChatBot Qrupda Deaktiv Olundu !**")
            return # aykhan026 | aykhan_s
        await event.reply("⚠️ **ChatBot Hal-Hazırda Deaktivdir !**")
        return
    
    else:
        await event.reply("🤖 Chatbot u Aktiv Edmək Üçün On və  Off yazın")


@xaos.on(events.NewMessage)
async def chatbot(event):
    global isleyen
    mesaj = str(event.raw_text)
    qrup = event.chat_id
    if qrup not in isleyen:
        return
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
    if "Salam" in mesaj or "salam" in mesaj:
        await event.reply(f"{random.choice(salam)}")
    if "necesen" in mesaj or "necəsən" in mesaj or "netersen" in mesaj or "nətərsən" in mesaj or "Netersen" in mesaj:
        await event.reply(f"{random.choice(necesen)}")
    if "xos" in mesaj or "Xos" in mesaj:
        await event.reply(f"{random.choice(xos)}")
	
	
	
	
	
	
	
        
xaos_run = xaos_start.decode("utf8")
print(">> Chat bot uğurla işləyir ♿ <<")
print(f"{xaos_run}")
xaos.run_until_disconnected()
