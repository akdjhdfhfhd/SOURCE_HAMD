import asyncio
import os
from pyrogram.types import CallbackQuery
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
import requests
import pyrogram
from pyrogram import Client, emoji 
from config import *
from pyrogram import filters
from strings.filters import command
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from pyrogram.errors import MessageNotModified



@app.on_message(
    command("الاوامر")
)
async def cr_source(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/e40829180343a484855a9.jpg",
        caption=f"""**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**\nمرحبا بك عزيزي {message.from_user.mention}\nهذا قسم الاوامر الخاص بسورس حمد \nلمعرفة الاوامر اختار ما تريد👇\n ◉︙اوامر المجموعات ↫ /gr \n ◉︙اوامر القنوات ↫ /ch \n ◉︙ اوامر الادمن ↫ /admin\n**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳", url=f"https://t.me/ah05v"),
                ],

            ]

        ),

    )
