import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

#       #             #  #####  #####      ####
#        #           #  #         #            #     #
#          #        #  #####   #            #####     
#           #    #    #          #     ##    #     #
#              #       #####   ######   #     #
                
                
@app.on_message(
    command(["المطور","مبرمج","مطور السورس","المبرمج"])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fb3e0c602a7da30ce6498.jpg",
        caption=f"""**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطور سورس ميوزك\nللتحدث مع مطور السورس اضغط علي الازرار بالاسفل👇\n**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑌.𝑂²¹ ͢͢➛ℍ𝗺!ِٰ𝗱♪", url=f"https://t.me/ah_2_v"), 
                 ],[
                   InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳", url=f"https://t.me/ah05v"),
                ],

            ]

        ),

    )








@app.on_message(
    command(["المبرمج","مبرمج","مطور" ,"المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["المطور","المبرمج",])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("ah_2_v")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★\n\n🧞‍♂️ ¦𝙽𝙰𝙼𝙴 :{name}\n🎯 ¦𝚄𝚂𝙴𝚁 :@{usr.username}\n💣 ¦𝙸𝙳 :`{usr.id}`\n🚀 ¦𝙱𝙸𝙾 :{usr.bio}\n\n**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    


@app.on_message(
    command(["/api"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/fb3e0c602a7da30ce6498.jpg",
        caption=f"""**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس الميوزك\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝑌.𝑂²¹ ͢͢➛ℍ𝗺!ِٰ𝗱♪", url=f"https://t.me/ah_2_v"), 
                 ],[
                
                    InlineKeyboardButton(
                        "𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳", url=f"https://t.me/ah05v"),
                ],

            ]

        ),

    )



    
