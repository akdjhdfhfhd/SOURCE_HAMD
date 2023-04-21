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
    command("ch")
) 
async def cr_usage(_, callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text="""**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**
★¦ اهلا بك عزيزي في قسم اوامر التشغيل في القنوات
★¦ تشغيل +اسم الاغنيه
★¦ شغل + اسم الاغنيه
★¦ قناه + اسم الاغنيه
★¦ حمد + اسم الاغنيه
★¦ ق + اسم الاغنيه
★¦ اغاني + اسم الاغنيه
★¦ . + اسم الاغنيه
★¦ / + اسم الاغنيه
**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳", url=f"https://t.me/ah05v"),
                    
                ]
            ]
        )
    )
