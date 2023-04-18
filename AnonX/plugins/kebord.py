
import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)

    
  
REPLY_MESSAGE = "- اهلين ياعيني عندك الازرار تحت استمتع"

REPLY_MESSAGE_BUTTONS = [
         [
             ("طريقة تشغيل حمد"),                   
             ("اوامر حمد")

          ],
          [
             ("المطور"),
             ("السورس")
          ],
          [
             ("اخفاء الازرار . 🕷")
          ]
]

  
@app.on_message(filters.private & filters.command("awamery"))
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

        
        
@app.on_message(filters.regex("^اخفاء الازرار . 🕷$"))
async def down(client, message):
          m = await message.reply(" **- تم اخفاء الازرار بنجاح . 🐰\n\n- لاظهار كيب الارشادات /ARN   \n. 🕷**\n\n- لاظهار كيب الاعضاء والتسليه  /HAMD  \n. 🕷**", reply_markup= ReplyKeyboardRemove(selective=True))
########رسائل الستارت######## 
        

@app.on_message(filters.private & command("طريقة تشغيل حمد"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""- **هلا والله ياعيني عشان تفعل بوت ميرا اتبع الخطوات الي بالاسفل**
1 • ضيف البوت لكروبك 
2 • ارفعه مشرف بكل الصلاحيات 
3 • لو تريد تشوف الاوامر اكتب [ م الاوامر ] ولو تبي تشغل على طول اكتب حمد شغل + اسم المقطع الصوتي
•مثال: حمد شغل حاسد روحي
- لو واجهت مشكله او ما فهمت خطوة كلم مطور البوت ~ @ah_2_v""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("السورس"))
async def addbot(client: Client, message: Message):
    await message.reply_text(f"""**- اهلين فيك بسورس حمد ياحلو
• لو تبي تنصب مثل هالبوت تواصل مع مطور السورس
• عندك استفسار او اقتراح بخصوص البوت تواصل مع مطور البوت**
مطور السورس -› [𝑌.𝑂²¹ ͢͢➛ℍ𝗺!ِٰ𝗱♪](t.me/ah_2_v)
قناة السورس -› [𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳](t.me/ah05v)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

###################new lian#############

REPLY_MESSAGEE = "- هلا فيك في قسم الاوامر"

REPLY_MESSAGE_BUTTONSS = [
         [
             ("شرح التشغيل بمنصات الاغاني")
          ],
          [
             ("اوامر المجموعة"),
             ("اوامر القنوات")
          ],
          [
             ("طريقة البحث"),
             ("ربط القنوات")
          ],
          [
             ("حفظ التشغيل")             
          ],
          [
             ("رجوع")
          ],
          [
            ("اخفاء الازرار . 🕷")
          ]
]

  
@app.on_message(filters.private & command("اوامر حمد"))
async def com(_, message: Message):             
        text = REPLY_MESSAGEE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONSS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )



@app.on_message(filters.private & command("رجوع"))
async def bask(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )


@app.on_message(filters.private & command("شرح التشغيل بمنصات الاغاني"))
async def mnsat(client: Client, message: Message):
    await message.reply_text(f"""** اهلين فيك في قسم تشغيل المنصات
- المنصات المدعومة هي ↓
• Telegram
• Youtube
• SoundCloud
• AppleMusic
• Spotify
- بتلقى شرح لكل هالمنصات في المجموعة اكتب فقط م الاوامر**
- [★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★](t.me/ah05v)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),

                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("اوامر المجموعة"))
async def laksk(client: Client, message: Message):
    await message.reply_text(f"""\n\n\n [★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★](t.me/ah05v) \n\n ✧ **اوامر التشغيل بالمجموعة**\n\n• **حمد شغل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني فالمجموعة\n\n• **حمد طفيها** او ** ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **حمد الي بعده** او **تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **حمد اشش** او **اسكت**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **حمد تكلم**\n-› لالغاء الكتم واكمال التشغيل\n\n• ** حمد ايقاف مؤقت** او **ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• ** حمد كمل** او **استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n [★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★](t.me/ah05v)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )


@app.on_message(filters.private & command("اوامر القنوات"))
async def channvom(client: Client, message: Message):
    await message.reply_text(f"""\n\n [★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★](t.me/ah05v) \n\n ✧ **اوامر التشغيل بالقنوات**\n\n• **ق تشغيل + اسم الاغنية او بالرد** \n-› لتشغيل الاغاني بالقناة\n\n• **ق ايقاف**\n-› لايقاف تشغيل جميع الصوتيات بالمكالمة\n\n• **ق تخطي**\n-› لتشغيل التالي بالانتظار\n\n • **ق اشش**\n-› لكتم صوت الحساب المساعد بالمكالمة\n\n• **ق كمل**\n-› لالغاء الكتم واكمال التشغيل\n\n• **ق ايقاف مؤقت**\n -› لايقاف التشغيل بشكل مؤقت\n\n• **ق استئناف**\n -› لاكمال التشغيل بعد الايقاف المؤقت\n\n [★⊷⧼𝚂𝙾𝚄𝚁𝙲𝙴 𝙷𝙰𝙼𝙳⧽⊶★](t.me/ah05v) """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )



@app.on_message(filters.private & command("طريقة البحث"))
async def dowmmr(client: Client, message: Message):
    await message.reply_text(f"""اهلين فيك في قسم التحميل ♪
للبحث عن اغنية او فيديو استخدم الامر التالي ↓
[ بحث + اسم المطلوب ..]
مثال -› بحث الفراشة انتي
- الامر يشتغل بخاص البوت والمجموعة ايضا .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
@app.on_message(filters.private & command("حفظ التشغيل"))
async def dowhmr(client: Client, message: Message):
    await message.reply_text(f"""✧ **اهلين فيك في قسم حفظ التشغيل**\n\n- **حفظ التشغيل هو حفظ الاغاني الي اشتغلت بالمجموعة وحفظها يعني انك تقدر تشغلها بدون ما ترجع تبحث عنها مرة ثانية وتبقى محفوظة لك فقط**\n\n-  لكي تحفظ الاغنية او المُشغل الحالي بالمكالمة لازم تضغط على زر -› ( **حفظ التشغيل** )\n\n-  لكي تشوف الاغاني او الصوتيات الي حفظتها اكتب امر -› ( **قائمة تشغيلي** )\n\n- وطريقة تشغيل قائمتك تكتب فقط امر -› ( **تشغيل قائمتي** )\n\n- طريقة حذف اغنية او مقطع من محفوظاتك تكتب امر -› ( **حذف تشغيلي** ) وتكمل الخطوات بخاص البوت ..\n\n✶ **ملاحظة : اذا حفظت اغنية بتكون محفوظة عندك فقط يعني كل شخص عنده قائمة تشغيل خاصة فيه ومحد يقدر يحفظ اغنية عندك والعكس ايضا\n✶ لو ما فهمت تابع الفيديو الي فوق  لكي تفهم اكثر ❤️**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )

@app.on_message(filters.private & command("ربط القنوات"))
async def dowhmo(client: Client, message: Message):
    await message.reply_text("""- هلا والله\n◌** لكي تشغل بالقنوات لازم تسوي بعض الخطوات وهي◌** :\n\n1 -› تدخل البوت قناتك وترفعه مشرف\n2 -› ترجع للقروب وتكتب { **ربط + يوزر القناة** }\n3 -› **اضغط على زر اوامر التشغيل عشان تعرف كيف تشغل**..""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "", url=f"https://t.me/ah07v"),
                ],[
                    InlineKeyboardButton(
                        "• ضيفني لكروبك 🎻", url=f"https://t.me/NKQbot?startgroup=true"),
                ],
            ]
        ),
        disable_web_page_preview=True
    )
