import asyncio
import time

from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch

import config
from config import BANNED_USERS
from config import OWNER_ID
from strings import get_command, get_string
from AnonX import Telegram, YouTube, app
from AnonX.misc import SUDOERS, _boot_
from AnonX.plugins.playlist import del_plist_msg
from AnonX.plugins.sudoers import sudoers_list
from AnonX.utils.database import (add_served_chat,
                                       add_served_user,
                                       get_served_chats,
                                       get_served_users,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from AnonX.utils.decorators.language import LanguageStart
from AnonX.utils.formatters import get_readable_time
from AnonX.utils.inline import (help_pannel, private_panel,
                                     start_pannel)

loop = asyncio.get_running_loop()

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
