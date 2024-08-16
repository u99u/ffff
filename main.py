import asyncio
from os import system, name, path
from time import sleep
from random import choice
from base64 import b64decode
from kvsqlite.sync import Client
try:
    import aiohttp
except:
    system('pip install aiohttp')
    import aiohttp
try:
    from telebot import TeleBot
    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
except:
    system('pip install telebot')
    from telebot import TeleBot
    from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
try:
    from telethon import TelegramClient, errors, functions
    from telethon.tl.functions.account import CheckUsernameRequest
    from telethon.sessions import StringSession
except:
    system('pip install telethon')
    from telethon import TelegramClient, errors, functions
    from telethon.tl.functions.account import CheckUsernameRequest
    from telethon.sessions import StringSession
try:
    from bs4 import BeautifulSoup as S
except:
    system('pip install beautifulsoup')
    from bs4 import BeautifulSoup as S
try:
    from fake_useragent import UserAgent
except:
    system('pip install fake_useragent')
    from fake_useragent import UserAgent
try:
    from datetime import datetime
except:
    system('pip install datetime')
    from datetime import datetime

token = "7358708216:AAEBIRxlKqtSDpi9h5cJVQ1NePQ7Rn5jrFk" #توكنك
chat_id = "7455029068" #ايديك

bot = TeleBot(token=token)
db = Client(f"users.bot")

async def fragment(username):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(f'https://fragment.com/username/{username}', headers={'Cookie': 'stel_ssid=105b9e3f8fc71d3078_18338999148668777485;','Pragma': 'no-cache','Sec-Ch-Ua': '"Not-A.Brand";v="99", "Chromium";v="124"','Sec-Ch-Ua-Mobile': '?1','Sec-Ch-Ua-Platform': '"Android"','Sec-Fetch-Dest': 'document','Sec-Fetch-Mode': 'navigate','Sec-Fetch-Site': 'same-origin','Sec-Fetch-User': '?1','Upgrade-Insecure-Requests': '1','User-Agent': str(UserAgent())}) as response:
                text = await response.text()
                soup = S(text, 'html.parser')
                ok = soup.find("meta", property="og:description").get("content")
                if "An auction to get the Telegram" in ok or "Telegram and secure your ownership" in ok or "Check the current availability of" in ok or "Secure your name with blockchain in an ecosystem of 700+ million users" in ok:return True
                elif "is taken" in ok:return "is taken"
                else:return False
        except:return 

async def channels2(client, username):
    di = await client.get_dialogs()
    for chat in di:
        if chat.name == f'[ {username} ]' and not chat.entity.username:
            client(functions.channels.DeleteChannelRequest(channel=chat.entity))
            print('- Flood : '+username+' .')
            return False
    return True

async def checks(username, client):
    return await client(CheckUsernameRequest(username))

async def claimer(client,username):
    result = await client(functions.channels.CreateChannelRequest(title=f'[ {username} ]',about=f'Source - @skrawi',megagroup=False))
    try:
        await client(functions.channels.UpdateUsernameRequest(channel=result.chats[0],username=username))
        await client.send_message(username,f'⌯ Done Save UserName .\n⌯ UserName : @{username} .\n⌯ Date : {datetime.now().strftime("%H:%M:%S")} .\n⌯ Source : @skrawi .')
        bot.send_message(chat_id,f'⌯ Done Save UserName .\n⌯ UserName : @{username} .\n⌯ Date : {datetime.now().strftime("%H:%M:%S")} .\n⌯ Source : @skrawi .')
        return True
    except Exception as e: bot.send_message(chat_id,f'⌯ Error Message .\nMessage : {e} .\nUserName : @'+str(username));return False

async def checker(username, client,type):
    try:
        check = await checks(username, client)
        if check:
            print('- Available : '+username+' .')
            claim = await claimer(client,username)
            if claim and fragment(username) == "is taken":claim = True
            else:claim = False
            flood = await channels2(client,username)
            if not flood:
            	with open('flood.txt', 'a') as floodX:
            	   floodX.write(username + "\n")
            	if claim:
            		if type == "c" or type == "fl":
            			return
            	if "flood" in type:
            		bot.send_message(chat_id=chat_id, text="Hi New Flood Username\n" + str(username))
        else:
            print('- Taken : ' + username + ' .')
    except errors.rpcbaseerrors.BadRequestError:
        print('- Banned : ' + username + ' .')
        with open("banned4.txt", "a") as banned:
            banned.write(username + '\n')
    except errors.FloodWaitError as timer:
        print('- Flood Account [ ' + str(timer.seconds) + ' Seconds ] .')
    except errors.UsernameInvalidError:
        print('- Error : ' + username + ' .')

def usernameG():
    k = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    n = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    c = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    z = ''.join(choice('1234567890') for i in range(1))
    g = ''.join(choice('1234567890') for i in range(1))
    kk = ''.join(choice("xczvnoiurewas") for i in range(1))
    nn = ''.join(choice("xczvnoiurewas") for i in range(1))
    cc = ''.join(choice("xczvnoiurewas") for i in range(1))
    zz = ''.join(choice("xczvnoiurewas789") for i in range(1))
    ee = ''.join(choice("xczvnoiurewas") for i in range(1))
    kkk = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    nnn = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    ccc = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    zzz = ''.join(choice('qwertyuiopasdfghjklzxcvbnm1234567890') for i in range(1))
    eee = ''.join(choice('qwertyuiopasdfghjklzxcvbnm') for i in range(1))
    try:type = db.get("type")
    except: return False
    if type == "se7":
        u1 = k + n + k + k + k + k + k
        u2 = k + k + n + k + k + k + k
        u3 = k + k + k + n + k + k + k
        u4 = k + k + k + k + n + k + k
        u5 = k + k + k + k + k + n + k
        u6 = k + k + k + k + k + k + n
        s = u1, u2, u3, u4, u5, u6
        return choice(s)
    elif type == "th3":
        u1 = k + "_" + n + "_" + c
        u2 = k + "_" + n + "_" + n
        s = u1, u2
        return choice(s)
    elif type == "f5":
        u1 = kk + cc + ee + ee + ee
        u2 = kk + zz + zz + zz + nn
        u3 = kk + kk + kk + nn + cc
        s = u1,u2,u3
        return choice(s)
    elif type == "f5i":
        u1 = kkk + ccc + eee + eee + eee
        u2 = kkk + zzz + zzz + zzz + nnn
        u3 = kkk + kkk + kkk + nnn + ccc
        s = u1,u2,u3
        return choice(s)
    elif type == "fi5":
        u1 = k + n + k + k + k
        u2 = k + k + n + k + k
        u3 = k + k + k + n + k
        u4 = k + k + k + k + n
        s = u1, u2, u3, u4
        return choice(s)

async def start(client, username,type):
    try:
        ok = await fragment(username)
    except:
        return
    try:
        if not ok:
            if type == "f": type = "flood"
            elif type == "c": type = "claim"
            elif type == "fl": type = "floods"
            await checker(username, client,type)
        elif ok == "is taken":
            print('- Taken : ' + username + ' .')
        else:
            print('- Fragment.com : ' + username + ' .')
            open("fragment.txt", "a").write(username + '\n')
    except Exception as e:
        print(e)

async def clientX():
    session = db.get("session")
    try:
    	client = TelegramClient(StringSession(session),b64decode("MjUzMjQ1ODE=").decode(), b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode())
    	await client.start()
    except:pass
    system('cls' if name == 'nt' else 'clear')
    return client

flag = False
async def work(message):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        username = usernameG()
        if not username:
        	de = bot.edit_message_text(chat_id=chat_id, message_id=de.message_id,text="الرجاء اختر نوع من الاشكال لكي افحص",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="اختيار", callback_data="type")]]))
        	return 
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "f"
        await start(session, username,type)

async def us5(message,username):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزر و صيدة\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "c"
        await start(session, username,type)


async def us3(message,username):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزر لجلب اذا كان خاصية\n\nاذا كنت تريد توقف الفحص اضغط ادناه", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    while not flag:
        if flag:
            break
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "fl"
        await start(session, username,type)

async def checkCombo(message):
    global flag
    session = await clientX()
    if not path.exists('banned4.txt'):
        with open('banned4.txt', 'w') as new:
            pass
    if not path.exists('flood.txt'):
        with open('flood.txt', 'w') as new:
            pass
    try:de = bot.edit_message_text(chat_id=chat_id, message_id=message.message_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    except:de = bot.send_message(chat_id=chat_id,text="تم بدأ فحص اليوزرات لجلب الخاصية لك\n\nاذا كنت تريد توقف الفحص اضغط ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="توقف", callback_data="stop")]]))
    with open(message.document.file_name, 'r') as file:
        usernames = file.readlines()
    for username in usernames:
        if '@' in username:
            username = username.split('@')[1]
        if flag:
            break
        username = username.strip()
        with open('banned4.txt', 'r') as file:
            check_username = file.read()
        if username in check_username:
            print('- Banned : ' + username + ' .')
            continue
        with open('fragment.txt', 'r') as file:
            fragment = file.read()
        if username in fragment:
            print('- Fragment.com : ' + username + ' .')
            continue
        type = "f"
        await start(session, username,type)
    bot.delete_message(chat_id=chat_id, message_id=de.message_id)
    bot.send_message(chat_id=chat_id,text="انتهى الفحص",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))

async def addS(message):
	try:
		client = await TelegramClient(StringSession(message.text),b64decode("MjUzMjQ1ODE=").decode(), b64decode("MDhmZWVlNWVlYjZmYzBmMzFkNWYyZDIzYmIyYzMxZDA=").decode()).start()
		db.set("session",client.session.save())
		bot.send_message(chat_id=chat_id,text="تم الاضافة الحساب بنجاح",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
	except: bot.send_message(chat_id=chat_id,text="عذرا السيشن خطا تاكد منه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
def gg(message):
	asyncio.run(addS(message=message))
@bot.callback_query_handler(func=lambda call: True)
def callB(call):
    global flag
    if call.data == "type":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="اختر النوع من احدى الازرار", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="ثلاثي", callback_data="th3"), InlineKeyboardButton(text="خماسي حرف", callback_data="fi5")], [InlineKeyboardButton(text="خماسي ناعم", callback_data="f5"), InlineKeyboardButton(text="سباعي حرف", callback_data="se7")],[InlineKeyboardButton(text="خماسي حرفين عشوائي", callback_data="f5i")]]))
    elif call.data in ["th3", "fi5", "f5", "se7","f5i"]:
        db.set("type", call.data)
        de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text=f"تم اختيار النوع الذي اخترته")
        sleep(2)
        bot.delete_message(chat_id=chat_id, message_id=de.message_id)
        reset(msg=call.message)
    elif call.data == "start":
        flag = False
        asyncio.run(work(message=call.message))
    elif call.data == "stop":
        flag = True
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        reset(msg=call.message)
    elif call.data == "add":
    	de = bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان سيشن telethon لأضافتة في البوت",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    	bot.register_next_step_handler(call.message,gg)
    elif call.data == "stopp":
        bot.delete_message(chat_id=chat_id, message_id=call.message.message_id)
        reset(msg=call.message)
    elif call.data == "us1":
    	flag = False
    	bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="اختر من احدى الازرار ادناه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="تثبيت لجلب خاصية", callback_data="po"),InlineKeyboardButton(text="تثبيت خاصية", callback_data="pi")]]))
    elif call.data == "pi":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان اليوزر للتثبيت عليه و صيدة\nارسل بهذا الشكل :\n.تثبيت xxMxx",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "po":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان اليوزر للتثبيت عليه حتى يصبح خاصية\nارسل بهذا الشكل : \n.جلب xxMxx",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))
    elif call.data == "combo":
        bot.edit_message_text(chat_id=chat_id, message_id=call.message.message_id, text="ارسل الان الملف المراد فحصه",reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="العودة", callback_data="stopp")]]))

@bot.message_handler(content_types=["document"])
def fromCombo(message):
    file = bot.download_file(bot.get_file(message.document.file_id).file_path)
    open(file=message.document.file_name, mode="wb").write(file)
    asyncio.run(checkCombo(message=message))

def reset(msg):
    if db.exists('session') is False:
    	bot.send_message(chat_id, text="تخصص لجلب خاصيات\n– – – – –\nمطوره : @skrawi", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="اضف حساب",callback_data="add")]]))
    	return 
    bot.send_message(chat_id, text="@skrawi", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="فحص عشوائي", callback_data="start")],[InlineKeyboardButton(text="من ملف", callback_data="combo"),InlineKeyboardButton(text="تثبيت", callback_data="us1")],[InlineKeyboardButton(text="اختيار نوع", callback_data="type"),]]))

@bot.message_handler(func=lambda msg: True)
def startB(msg):
    if msg.chat.id != int(chat_id): return
    elif msg.text == "/start":
    	if db.exists('session') is False:
    		bot.send_message(chat_id, text="اهلا بك عزيزي\بوت متخصص لجلب خاصيات\n– – – – –\nمطوره : @skrawi", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="اضف حساب",callback_data="add")]]))
    		return 
    	bot.send_message(chat_id, text="اهلا بك عزيزي\nبوت متخصص لجلب خاصيات\n– – – – –\nمطوره : @skrawi", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="فحص عشوائي", callback_data="start")],[InlineKeyboardButton(text="من ملف", callback_data="combo"),InlineKeyboardButton(text="تثبيت", callback_data="us1")],[InlineKeyboardButton(text="اختيار نوع", callback_data="type"),]]))
    elif ".فحص" in msg.text:
    	bot.send_message(chat_id=chat_id,text="الفحص شغال طاب يومك")
    elif '.تثبيت ' in msg.text:
    	username = msg.text.split('.تثبيت ')[1]
    	if '@' in username:username = username.split('@')[1]
    	asyncio.run(us5(message=msg,username=username))
    elif ".جلب " in msg.text:
        username = msg.text.split('.جلب ')[1]
        if '@' in username:username = username.split('@')[1]
        asyncio.run(us3(message=msg,username=username))

def polling(bot, interval=5):
    import time ; from requests import exceptions
    while True:
        try:
            bot.polling()
            print('- New Session Bot .')
        except exceptions.ConnectionError:
            print('- New Session Bot .')
            time.sleep(interval)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(interval)
polling(bot=bot)
