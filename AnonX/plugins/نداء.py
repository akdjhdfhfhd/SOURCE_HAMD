print("Wait i work code new.⚡")
import random
from pyrogram import Client, filters

app = Client(
    "Bot",
    api_id = 21563297,
    api_hash = "e2df7de79f05aca7297acd0ff65a4241",
    bot_token = "5976672123:AAE_6qf89QYudrHC8cAQrTb8Rd6Nd2PZ84Y"
)

@app.on_message(filters.command(['نداء'], prefixes=""))
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