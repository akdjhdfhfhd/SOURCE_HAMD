import asyncio
import config
from pyrogram import Client, filters
from pyrogram import filters
from strings import get_command
from strings.filters import command
from AnonX import app
from config import OWNER_ID
from AnonX.misc import SUDOERS
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,InlineKeyboardMarkup, Message)
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX.misc import SUDOERS

@app.on_message(command(["ابراج","غادر حمد"]))
async def bra(client: Client, message: Message):
       usr = await client.get_users(message.from_user.id)
       user_id = message.from_user.id
       ch = message.chat.username
       chat_id = message.chat.id
       gti = message.chat.title
       user_ab = message.from_user.username
       user_name = message.from_user.first_name
       await app.leave_chat(chat_id)
       await app.send_message(-1001420714100, f"- قام {message.from_user.mention} \n\n- بطرد البوت .\n- ايديه {user_id}`\n- معرفه @{user_ab}\n- ايدي القروب `{chat_id} - {gti}\n- @{ch}")
