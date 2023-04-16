from AnonX.utils.database import is_music_playing, music_off
from strings import get_command
import asyncio
from strings.filters import command
from AnonX import app
from AnonX.core.call import Yukki
from AnonX.utils.database import set_loop
from AnonX.utils.decorators import AdminRightsCheck
from AnonX.utils.database import is_muted, mute_on
from AnonX.utils.database import is_muted, mute_off
from AnonX.utils.database import is_music_playing, music_on
from datetime import datetime
from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL, lyrical, START_IMG_URL, MONGO_DB_URI, OWNER_ID
from AnonX.utils import bot_sys_stats
from AnonX.utils.decorators.language import language
import random
import config
import re
from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
import string
import lyricsgenius as lg
from pyrogram.types import (InlineKeyboardButton,
                            InlineKeyboardMarkup, Message)
from pyrogram import Client, filters
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from typing import Union
import sys
from os import getenv
from dotenv import load_dotenv

load_dotenv()

BOT_USERNAME = getenv("BOT_USERNAME")

START_IMG_URL = getenv("START_IMG_URL")

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")

# Commands
STOP_COMMAND = get_command("STOP_COMMAND")
PAUSE_COMMAND = get_command("PAUSE_COMMAND")
MUTE_COMMAND = get_command("MUTE_COMMAND")
UNMUTE_COMMAND = get_command("UNMUTE_COMMAND")
RESUME_COMMAND = get_command("RESUME_COMMAND")
PING_COMMAND = get_command("PING_COMMAND")
LYRICS_COMMAND = get_command("LYRICS_COMMAND")

api_key = "Vd9FvPMOKWfsKJNG9RbZnItaTNIRFzVyyXFdrGHONVsGqHcHBoj3AI3sIlNuqzuf0ZNG8uLcF9wAd5DXBBnUzA"
y = lg.Genius(
    api_key,
    skip_non_songs=True,
    excluded_terms=["(Remix)", "(Live)"],
    remove_section_headers=True,
)
y.verbose = False


    
@app.on_message(
    command(["قول"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["قول"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
    command(["قول"])
    & filters.channel
    & ~filters.edited
)
def echo(client, msg):
    text = msg.text.split(None, 1)[1]
    msg.reply(text)

@app.on_message(
    command(["انا منو"])
    & filters.group
    & ~filters.edited
)
@app.on_message(
    command(["انا منو"])
    & filters.private
    & ~filters.edited
)
@app.on_message(
    command(["انا منو"])
    & filters.channel
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(message.from_user.id)
    name = usr.first_name
    async for photo in client.iter_profile_photos(message.from_user.id, limit=1):
                    await message.reply_text( 
                    f"""انت {message.from_user.mention} روح قلبي .""",
        reply_markup=InlineKeyboardMarkup(
                ]
            ]
        ),
    )

@app.on_message(
     command(["يوزري","معرفي"])
    & filters.private
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d1f75386af9cf775c0c52.jpg",
        caption=f""" 🐉 | يـوزرڪ : [ @{user} ] \n✓ """,
        reply_markup=InlineKeyboardMarkup(
            [
                [  
