import telebot
import requests
from telebot import types
sudo_id = "1748768168"
token = "5844861055:AAH3E3zKmSn44T_eYx5EL_utA5ogZDaPJQ8" 
bot = telebot.TeleBot(token)
def group_id(idc):
	result = False
	file = open('fcm.txt','r')#تكدر تغير اسم 
	for line in file:
	 if line.strip()==idc:
	 	result = True
	 file.close()
	 return result	 
@bot.message_handler(commands=['start'])
def start(message):
 idd = message.from_user.id
 i = open("ch.txt","r")
 ii = i.readline()
 for line in i:
 	r = True
 i.close()
 url = f"https://api.telegram.org/bot{token}/getchatmember?chat_id=@{ii}&user_id={idd}"
 req = requests.get(url)
 if idd == i or 'member' in req.text or 'creator' in req.text or 'administartor' in req.text:
 	k = telebot.types.ReplyKeyboardMarkup(True)
 	b = telebot.types.KeyboardButton(text="• اضف قناة ➥")
 	b2 = types.InlineKeyboardButton("• حذف القنوات ➥")
 	b1 = types.InlineKeyboardButton(text="• عرض القنوات ➥")
 	k.add(b,b1)
 	k.add(b2)
 	bot.reply_to(message,"اهلا بك عزيزي  في بوت الاشتراك الاجباري",reply_markup=k)	
 else:
 	bot.send_message(message.chat.id, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه
* *
- مــعرف القـناة :* {} 

‼️| اشترك ثم ارسل /start """.format(ii),parse_mode="markdown")
@bot.message_handler(regexp="• اضف قناة ➥")
def hej(message):
	f = open('fcm.txt','a+')
	id = message.chat.id
	if(not group_id(str(id))):
 	  	f.write("{}\n".format(id))
 	  	f.close()
 	  	bot.reply_to(message,"""*• حسناً عزيزي اول قم برفع البوت ادمن في القناة 
ثمة ارسل معرف القناة مع - @
يجيب ان تكون القناة عامة .*""",parse_mode="markdown")
	else:
		bot.reply_to(message,"""*• حسناً عزيزي اول قم برفع البوت ادمن في القناة 
ثمة ارسل معرف القناة مع - @
يجيب ان تكون القناة عامة .*""",parse_mode="markdown")
	bot.register_next_step_handler(message,xsx)
def xsx(message):
	m = message.text
	i = open("ch.txt","a")
	i.write(f"\n{m}\n")
	i.close()
	bot.send_message(message.chat.id,f"تم اضافة القناة اشتراك اجباري في البوت\nالقناة : {m}")
@bot.message_handler(regexp="• عرض القنوات ➥")
def hej(message):
	i = open("ch.txt","r").read()
	bot.reply_to(message,f"عزيزي قنوات الاشتراك الاجباري هيه : \n{i}")
@bot.message_handler(regexp="• حذف القنوات ➥")
def hej(message):
	i = open("ch.txt","w")
	m = message.text
	i.write(f"@pjpppppp")
	i.close()
	bot.reply_to(message,"حسناً تم  حذف القنوات")
bot.polling()