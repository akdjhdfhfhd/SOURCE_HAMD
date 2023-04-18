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

@app.on_message(command(["نداء"]))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"بقلنا ساعه مستنينك فينك 😾 {random_member_mention}",
        f"• يـا قمـري ❤️‍🔥 {random_member_mention}",
        f"حبيبي لي م بتتكلم معنا 🤔 {random_member_mention}",
        f"• يـا تفاحه 🍏 فينك {random_member_mention}",
        f"• هو انت لي قمر كده 🌚♥ {random_member_mention}"
    ])
    client.send_message(chat_id, random_message, parse_mode='markdown')

print("The code work new lits gooo.⚡")
app.run()
