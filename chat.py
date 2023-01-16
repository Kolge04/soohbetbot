import random
import os
import logging
import asyncio
from telethon import Button
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon import TelegramClient, events
from kelime_bot.mesaj import taım, azz, enn, trrr, russ, fra
from kelime_bot.bot import yeni_user, ınfom

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)




api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
xaos = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)





# Yeni istifadəçi mesajı
@xaos.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")
#start
        
xaos_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@xaos.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}")
  
#info

@xaos.on(events.NewMessage(pattern='(?i)/xaosinfo+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(info)}")

 #oyunlar   
    
@xaos.on(events.NewMessage(pattern='(?i)/oyunlar+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(oyun)}")
 

@xaos.on(events.NewMessage(pattern='(?i)/zer+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(zer)}")
 
@xaos.on(events.NewMessage(pattern='(?i)/ox+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ox)}")
 
@xaos.on(events.NewMessage(pattern='(?i)/carx+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(carx)}")
 
@xaos.on(events.NewMessage(pattern='(?i)/ftop+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ftop)}")
 
@xaos.on(events.NewMessage(pattern='(?i)/btop+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(btop)}")
 
@xaos.on(events.NewMessage(pattern='(?i)/boling+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(bol)}")
 




@xaos.on(events.NewMessage(pattern='(?i)salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@xaos.on(events.NewMessage(pattern='(?i)necəsən+'))
@xaos.on(events.NewMessage(pattern='(?i)necesen+'))
@xaos.on(events.NewMessage(pattern='(?i)nətərsən+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@xaos.on(events.NewMessage(pattern='(?i)sağol+'))
@xaos.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@xaos.on(events.NewMessage(pattern='(?i)getdim+'))
@xaos.on(events.NewMessage(pattern='(?i)gedim+'))
@xaos.on(events.NewMessage(pattern='(?i)gedirəm+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@xaos.on(events.NewMessage(pattern='(?i)gəldim+'))
@xaos.on(events.NewMessage(pattern='(?i)geldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@xaos.on(events.NewMessage(pattern='(?i)@sesizKOLGE+'))
@xaos.on(events.NewMessage(pattern='(?i)@MR_K4BUS_13+'))
@xaos.on(events.NewMessage(pattern='(?i)@Modelhs+'))
@xaos.on(events.NewMessage(pattern='(?i)@sanane_lann+'))
@xaos.on(events.NewMessage(pattern='(?i)@adsizm1_2+'))
@xaos.on(events.NewMessage(pattern='(?i)@NaraHva+'))
@xaos.on(events.NewMessage(pattern='(?i)@DAGLI_R_17+'))
@xaos.on(events.NewMessage(pattern='(?i)@lezgididee+'))
@xaos.on(events.NewMessage(pattern='(?i)@mmmdtly+'))
@xaos.on(events.NewMessage(pattern='(?i)@Cavkaa+'))
@xaos.on(events.NewMessage(pattern='(?i)KOLGE+'))
@xaos.on(events.NewMessage(pattern='(?i)KOLGƏ+'))
@xaos.on(events.NewMessage(pattern='(?i)kabus+'))
@xaos.on(events.NewMessage(pattern='(?i)niko+'))
@xaos.on(events.NewMessage(pattern='(?i)nara+'))
@xaos.on(events.NewMessage(pattern='(?i)@Geldim000+'))
@xaos.on(events.NewMessage(pattern='(?i)Emin+'))
@xaos.on(events.NewMessage(pattern='(?i)emın+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sesizKOLGE)}")

@xaos.on(events.NewMessage(pattern='(?i)ban+'))
@xaos.on(events.NewMessage(pattern='(?i)kick+'))
@xaos.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")
    
@xaos.on(events.NewMessage(pattern='(?i)🙄+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji1)}")

@xaos.on(events.NewMessage(pattern='(?i)😂+'))
@xaos.on(events.NewMessage(pattern='(?i)🤣+'))
@xaos.on(events.NewMessage(pattern='(?i)😅+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji2)}")

@xaos.on(events.NewMessage(pattern='(?i)xaos+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(fed)}")
 
@xaos.on(events.NewMessage(pattern='(?i)niye+'))
@xaos.on(events.NewMessage(pattern='(?i)nıye+'))
@xaos.on(events.NewMessage(pattern='(?i)niyə+'))
@xaos.on(events.NewMessage(pattern='(?i)nıyə+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(niye)}")

    
@xaos.on(events.NewMessage(pattern='(?i)ne+'))
@xaos.on(events.NewMessage(pattern='(?i)nə+'))
@xaos.on(events.NewMessage(pattern='(?i)what+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ne)}")
   
@xaos.on(events.NewMessage(pattern='(?i)hay+'))
@xaos.on(events.NewMessage(pattern='(?i)hiy+'))
@xaos.on(events.NewMessage(pattern='(?i)hııy+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hay)}")
    
@xaos.on(events.NewMessage(pattern='(?i)mal+'))
@xaos.on(events.NewMessage(pattern='(?i)maal+'))
@xaos.on(events.NewMessage(pattern='(?i)qoyun+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(mal)}")
    
    
@xaos.on(events.NewMessage(pattern='(?i)can+'))
@xaos.on(events.NewMessage(pattern='(?i)haycan+'))
@xaos.on(events.NewMessage(pattern='(?i)uşş+'))
@xaos.on(events.NewMessage(pattern='(?i)uss+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(can)}")
    
    
@xaos.on(events.NewMessage(pattern='(?i)balam+'))
@xaos.on(events.NewMessage(pattern='(?i)quzum+'))
@xaos.on(events.NewMessage(pattern='(?i)❤+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(balam)}")
   
@xaos.on(events.NewMessage(pattern='(?i)xoş+'))
@xaos.on(events.NewMessage(pattern='(?i)xos+'))
@xaos.on(events.NewMessage(pattern='(?i)gününə+'))
@xaos.on(events.NewMessage(pattern='(?i)gününe+'))
@xaos.on(events.NewMessage(pattern='(?i)gunune+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(xos)}")
     
@xaos.on(events.NewMessage(pattern='(?i)hara+'))
@xaos.on(events.NewMessage(pattern='(?i)havaq+'))
@xaos.on(events.NewMessage(pattern='(?i)hansı+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hara)}")
    
@xaos.on(events.NewMessage(pattern='(?i)gel+'))
@xaos.on(events.NewMessage(pattern='(?i)gəl+'))
@xaos.on(events.NewMessage(pattern='(?i)gelde+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gel)}")
    
@xaos.on(events.NewMessage(pattern='(?i)gordum+'))
@xaos.on(events.NewMessage(pattern='(?i)gördüm+'))
@xaos.on(events.NewMessage(pattern='(?i)gördün+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gordum)}")
         
@xaos.on(events.NewMessage(pattern='(?i)tema+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(taım)}")

        
        
        
        
xaos_run = xaos_start.decode("utf8")
print(">> Chat bot uğurla işləyir ♿ <<")
print(f"{xaos_run}")
xaos.run_until_disconnected()
