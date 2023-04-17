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

@app.on_message(command(["اشتراك"]))
async def must_join_channel(bot: Client, msg: Message):
    if not SUPPORT_CHANNEL:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(CHANNEL_SUDO, msg.from_user.id)
        except UserNotParticipant:
            if SUPPORT_CHANNEL.isalpha():
                link = u"https://t.me/{SUPPORT_CHANNEL}"
            else:
                chat_info = await bot.get_chat(CHANNEL_SUDO)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"︙عـذراً، عـلـيـڪ الانـضـمـام الى هـذهِ الـقـنـاة أولاً\n︙اشـتـرڪ ثـم أرسـل : /start",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton(f"{AFYONA_NAME}", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"عليك رفع البوت آدمن في القناة أولاً ؟؟ : {SUPPORT_CHANNEL} !")
