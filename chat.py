import base64
from mesajlar.mesaj import salam, necesen, sagol, getdim, geldim, sesizKOLGE, ban, emoji1, emoji2, fed, niye, ne, hay, mal, can, balam, xos, hara, gel, gordum, taım
from mesajlar.bot import yeni_user, start, info, oyun, zer, bol, ftop, btop, carx, ox
from telethon import events, Button
import random


# Yeni istifadəçi mesajı
@bot.on(events.ChatAction)
async def handler(event):
    if event.user_joined:
        await event.reply(f"{random.choice(yeni_user)}")
#start
        
nermin_start = b"\x42\x6F\x74\x20\x42\x61\xC5\x9F\x6C\x61\x64\xC4\xB1\x6C\x64\xC4\xB1\x2E\x2E\x2E\x0A\x4F\x77\x6E\x65\x72\x3A\x20\x61\x79\x6B\x68\x61\x6E\x5F\x73\x20\x7C\x20\x61\x79\x6B\x68\x61\x6E\x30\x32\x36\x0A\x74\x2E\x6D\x65\x2F\x52\x6F\x42\x6F\x74\x6C\x61\x72\x69\x6D\x54\x67"
@Nermin.on(events.NewMessage(pattern='(?i)/start+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(start)}")
  
#info

@Nermin.on(events.NewMessage(pattern='(?i)/xaosinfo+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(info)}")

 #oyunlar   
    
@Nermin.on(events.NewMessage(pattern='(?i)/oyunlar+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(oyun)}")
 

@Nermin.on(events.NewMessage(pattern='(?i)/zer+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(zer)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/ox+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ox)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/carx+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(carx)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/ftop+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ftop)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/btop+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(btop)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)/boling+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(bol)}")
 




@Nermin.on(events.NewMessage(pattern='(?i)salam+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(salam)}")

@Nermin.on(events.NewMessage(pattern='(?i)necəsən+'))
@Nermin.on(events.NewMessage(pattern='(?i)necesen+'))
@Nermin.on(events.NewMessage(pattern='(?i)nətərsən+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(necesen)}")

@Nermin.on(events.NewMessage(pattern='(?i)sağol+'))
@Nermin.on(events.NewMessage(pattern='(?i)sagol+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sagol)}")

@Nermin.on(events.NewMessage(pattern='(?i)getdim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gedim+'))
@Nermin.on(events.NewMessage(pattern='(?i)gedirəm+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(getdim)}")

@Nermin.on(events.NewMessage(pattern='(?i)gəldim+'))
@Nermin.on(events.NewMessage(pattern='(?i)geldim+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(geldim)}")

@Nermin.on(events.NewMessage(pattern='(?i)@sesizKOLGE+'))
@Nermin.on(events.NewMessage(pattern='(?i)@MR_K4BUS_13+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Modelhs+'))
@Nermin.on(events.NewMessage(pattern='(?i)@sanane_lann+'))
@Nermin.on(events.NewMessage(pattern='(?i)@adsizm1_2+'))
@Nermin.on(events.NewMessage(pattern='(?i)@NaraHva+'))
@Nermin.on(events.NewMessage(pattern='(?i)@DAGLI_R_17+'))
@Nermin.on(events.NewMessage(pattern='(?i)@lezgididee+'))
@Nermin.on(events.NewMessage(pattern='(?i)@mmmdtly+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Cavkaa+'))
@Nermin.on(events.NewMessage(pattern='(?i)KOLGE+'))
@Nermin.on(events.NewMessage(pattern='(?i)KOLGƏ+'))
@Nermin.on(events.NewMessage(pattern='(?i)kabus+'))
@Nermin.on(events.NewMessage(pattern='(?i)niko+'))
@Nermin.on(events.NewMessage(pattern='(?i)nara+'))
@Nermin.on(events.NewMessage(pattern='(?i)@Geldim000+'))
@Nermin.on(events.NewMessage(pattern='(?i)Emin+'))
@Nermin.on(events.NewMessage(pattern='(?i)emın+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(sesizKOLGE)}")

@Nermin.on(events.NewMessage(pattern='(?i)ban+'))
@Nermin.on(events.NewMessage(pattern='(?i)kick+'))
@Nermin.on(events.NewMessage(pattern='(?i)mute+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ban)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)🙄+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji1)}")

@Nermin.on(events.NewMessage(pattern='(?i)😂+'))
@Nermin.on(events.NewMessage(pattern='(?i)🤣+'))
@Nermin.on(events.NewMessage(pattern='(?i)😅+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(emoji2)}")

@Nermin.on(events.NewMessage(pattern='(?i)xaos+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(fed)}")
 
@Nermin.on(events.NewMessage(pattern='(?i)niye+'))
@Nermin.on(events.NewMessage(pattern='(?i)nıye+'))
@Nermin.on(events.NewMessage(pattern='(?i)niyə+'))
@Nermin.on(events.NewMessage(pattern='(?i)nıyə+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(niye)}")

    
@Nermin.on(events.NewMessage(pattern='(?i)ne+'))
@Nermin.on(events.NewMessage(pattern='(?i)nə+'))
@Nermin.on(events.NewMessage(pattern='(?i)what+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(ne)}")
   
@Nermin.on(events.NewMessage(pattern='(?i)hay+'))
@Nermin.on(events.NewMessage(pattern='(?i)hiy+'))
@Nermin.on(events.NewMessage(pattern='(?i)hııy+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hay)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)mal+'))
@Nermin.on(events.NewMessage(pattern='(?i)maal+'))
@Nermin.on(events.NewMessage(pattern='(?i)qoyun+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(mal)}")
    
    
@Nermin.on(events.NewMessage(pattern='(?i)can+'))
@Nermin.on(events.NewMessage(pattern='(?i)haycan+'))
@Nermin.on(events.NewMessage(pattern='(?i)uşş+'))
@Nermin.on(events.NewMessage(pattern='(?i)uss+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(can)}")
    
    
@Nermin.on(events.NewMessage(pattern='(?i)balam+'))
@Nermin.on(events.NewMessage(pattern='(?i)quzum+'))
@Nermin.on(events.NewMessage(pattern='(?i)❤+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(balam)}")
   
@Nermin.on(events.NewMessage(pattern='(?i)xoş+'))
@Nermin.on(events.NewMessage(pattern='(?i)xos+'))
@Nermin.on(events.NewMessage(pattern='(?i)gününə+'))
@Nermin.on(events.NewMessage(pattern='(?i)gününe+'))
@Nermin.on(events.NewMessage(pattern='(?i)gunune+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(xos)}")
     
@Nermin.on(events.NewMessage(pattern='(?i)hara+'))
@Nermin.on(events.NewMessage(pattern='(?i)havaq+'))
@Nermin.on(events.NewMessage(pattern='(?i)hansı+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(hara)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)gel+'))
@Nermin.on(events.NewMessage(pattern='(?i)gəl+'))
@Nermin.on(events.NewMessage(pattern='(?i)gelde+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gel)}")
    
@Nermin.on(events.NewMessage(pattern='(?i)gordum+'))
@Nermin.on(events.NewMessage(pattern='(?i)gördüm+'))
@Nermin.on(events.NewMessage(pattern='(?i)gördün+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(gordum)}")
         
@Nermin.on(events.NewMessage(pattern='(?i)tema+'))
async def yeni_mesaj(event: events.NewMessage.Event):
    await event.reply(f"{random.choice(taım)}")

        
        
        
        
nermin_run = nermin_start.decode("utf8")
print(">> Chat bot uğurla işləyir ♿ <<")
print(f"{nermin_run}")
Nermin.run_until_disconnected()
