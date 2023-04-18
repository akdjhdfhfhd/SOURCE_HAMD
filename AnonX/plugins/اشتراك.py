from pyrogram import *
from pyrogram.types import *
from pyrogram.errors import *


me = "1748768168" #ايدي المطور

app = Client(
 "Spd",
 api_id="21468057", #ايبي ايدي
 api_hash="f4a868976632fec2260eb7a7f9d88720", #ايبي هاش
 bot_token="5844861055:AAH3E3zKmSn44T_eYx5EL_utA5ogZDaPJQ8" #توكن بوتك
)

async def check_sub(c:Client,m:Message):
 channel = "@ah07v"  #قناتك
 startMessage = "مرحبا بك صديقي تم التحقق من اشتراكك بقناة البوت"
 try:
  r = await c.get_chat_member(
  chat_id=channel,
  user_id=m.from_user.id)
  if r.status in [
  enums.ChatMemberStatus.BANNED,
  enums.ChatMemberStatus.LEFT]:
   return await m.reply(
   f"◈ اشترك بقناة البوت لتتمكن من استخدامة \n- {channel}")
  return await m.reply(
  startMessage)
 except ChatAdminRequired:
  await m.reply(
  'البوت معطل من قبل المطور')
  await c.send_message(int(me),
  'ارفع البوت ادمن في قناة الاشتراك')
  return
 except UserNotParticipant:
  return await m.reply(
  f"◈ اشترك بقناة البوت لتتمكن من استخدامة \n- {channel}")
 return await m.reply(
 startMessage)
 

#طريقه استخدام الداله بعد الامر 
#await check_sub(c=c,m=m)


@app.on_message(filters.command('start')&filters.private)
async def start(c:Client,m:Message):
 if not m.from_user.id == me:
  await check_sub(c=c,m=m)
  return
 return await m.reply(
 "◍ مرحباا بك مطور البوت 🥂🖤")
