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


@app.on_message(command("حالات$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل حـالات واتـس ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@xxgfj", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎆┊حـالات واتـس قصيـرة 🧸♥️**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("ستوري انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الستـوري ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@AA_Zll", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎆┊ستـوريات آنمـي قصيـرة 🖤🧧**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("رقيه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرقيـه ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@Rqy_1", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**◞مقاطـع رقيـه شرعيـة ➧🕋🌸◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("رمادي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shababbbbR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات شبـاب ࢪمـاديه ➧🎆🖤◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("رماديه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الافتـار ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banatttR", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات بنـات ࢪمـاديه ➧🎆🤎◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("بيست$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...🧚🏻‍♀🧚🏻‍♀╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@Tatkkkkkim", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات بيست تطقيـم بنـات ➧🎆🧚🏻‍♀🧚🏻‍♀◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("حب$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...♥️╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@tatkkkkkimh", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات حـب تمبلـرࢪ ➧🎆♥️◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("رياكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        ZTHONR = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@reagshn", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"** 🎬┊رياكشـن تحشيـش ➧🎃😹◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("ادت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل مقطـع ادت ...**")
    try:
        ZTHONR = [
            asupan
            async for asupan in event.client.iter_messages(
                "@snje1", filter=InputMessagesFilterVideo
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(ZTHONR),
            caption=f"**🎬┊مقاطـع ايـدت منوعـه ➧ 🖤🎭◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("غنيلي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الاغنيـه ...𓅫╰**")
    try:
        zedgan = [
            desah
            async for desah in event.client.iter_messages(
                "@TEAMSUL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختياࢪ الاغنيـه لك 💞🎶**ٴ▁ ▂ ▉ ▄ ▅ ▆ ▇ ▅ ▆ ▇ █ ▉ ▂ ▁\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")
        

@app.on_message(command("شعر$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الشعـر ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@L1BBBL", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختيـار مقطـع الشعـر هـذا لك**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("ميمز$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الميمـز ...**")
    try:
        zedgan = [
            zlzzl77
            async for zlzzl77 in event.client.iter_messages(
                "@MemzWaTaN", filter=InputMessagesFilterVoice
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedgan),
            caption=f"**✦┊تم اختيـار مقطـع الميمـز هـذا لك**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("ري اكشن$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل الرياكشـن ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@gafffg", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**🎆┊رياكشـن تحشيـش ➧🎃😹◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("معلومه$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل صـورة ومعلومـة ...**")
    try:
        zedph = [
            zilzal
            async for zilzal in event.client.iter_messages(
                "@A_l3l", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**🎆┊صـورة ومعلومـة ➧ 🛤💡◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆٠](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("تويت$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ كـت تـويت بالصـور ...**")
    try:
        zedre = [
            zlzz7
            async for zlzz7 in event.client.iter_messages(
                "@twit_selva", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedre),
            caption=f"**✦┊كـت تـويت بالصـور ➧⁉️🌉◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("خيرني$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ لـو خيـروك بالصـور ...**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@SourceSaidi", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**✦┊لـو خيـروك  ➧⁉️🌉◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("ولد انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@dnndxn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات آنمي شبـاب ➧🎆🙋🏻‍♂◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("بنت انمي$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@shhdhn", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات آنمي بنـات ➧🎆🧚🏻‍♀◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("بنات$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮ - جـارِ تحميـل الآفتـار ...𓅫╰**")
    try:
        zedph = [
            zelzal
            async for zelzal in event.client.iter_messages(
                "@banaaaat1", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(zedph),
            caption=f"**◞افتـارات بنـات تمبلـرࢪ ➧🎆🧚🏻‍♀◟**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


@app.on_message(command("رمزيات شباب$")
async def _(event):
    zzevent = await edit_or_reply(event, "**╮•⎚ جـارِ تحميـل حـالات الرمزيات ...**")
    try:
        samir = [
            zlzzl
            async for zlzzl in event.client.iter_messages(
                "@GTTUTY", filter=InputMessagesFilterPhotos
            )
        ]
        aing = await event.client.get_me()
        await event.client.send_file(
            event.chat_id,
            file=random.choice(samir),
            caption=f"**🎆┊رمزيات شباب قامده 🧸♥️**\n\n[᥉᥆υᖇᥴᥱ ᥉ᥱꪔ᥆](https://t.me/FTTUTY)",
        )
        await zzevent.delete()
    except Exception:
        await zzevent.edit("**╮•⎚ عـذراً .. لـم استطـع ايجـاد المطلـوب ☹️💔**")


