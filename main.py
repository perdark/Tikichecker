import requests
import random
abc ='ABCDEFGHIJKLMNOPQRSTUVWXYZ_1234567890'
abc1 ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
import telebot
from telebot import types
bot_token ="5446689009:AAHhc54DpkslzukSj4kGQkaMvV70NEDbXFc"
bot = telebot.TeleBot(bot_token)
admin=[2029773594,5487311341,2053044330,1959561727,5244755240,2067768173,1854384004,1777649029,1403347605,1640747466,5244755240]

@bot.message_handler(commands=['start'])
def start_message(message):
    first = message.from_user.first_name
    url = 'https://t.me/N1111V/3'
    bot.send_animation((message.chat.id), url, caption=f"""اهلا {first}

    بُكَ فِيُ بُۅتِ صِيُډ يُۅࢪِ࣪ࢪاެتِ تِيُݪيُجَࢪاެمِ
اެݪبُۅتِ مِډفِۅعٰ ۅݪيُسُ مِجَاެنِيُ اެضِغِطَ /TXN
ݪكَيُ اެتِحِقِقِ هَݪ اެنِتِ مِشِتِࢪكَ فِيُ اެݪبُۅتِ ❤️‍🔥
_

اެنِتِ كَنِتِ ݪسُتِ مِشِتِࢪكَ ࢪاެسُݪ اެݪمِطَۅࢪ @E_4_1 ݪكَيُ يُفِعٰݪ ݪكَ اެݪاެشِتِࢪاެكَ بُمِقِاެبُݪ بُسُيُطَ جَډاެ ❤️‍🔥""", reply_to_message_id=(message.message_id))

@bot.message_handler(commands=['TXN','txn','Txn'])
def hamo(message):
    if message.from_user.id in admin:
        mas = types.InlineKeyboardMarkup(row_width=3)
        us0 = types.InlineKeyboardButton(text='شِبُهَ ثِݪاެثِيُ', callback_data='us0')
        us1 = types.InlineKeyboardButton(text='ࢪبُاެعٰيُ ݪݪبُۅتِ', callback_data='us1')
        us2 = types.InlineKeyboardButton(text='ثِݪاެثِيُ ݪݪبُۅتِ', callback_data='us2')
        us3 = types.InlineKeyboardButton(text='شِبُهَ ࢪبُاެعٰيُ ', callback_data='us3')
        us4 = types.InlineKeyboardButton(text='خِمِاެسُيُ مِمِيُࢪِ࣪', callback_data='us4')
        us5 = types.InlineKeyboardButton(text='سُډاެسُيُ مِمِيُࢪِ࣪', callback_data='us5')
        us6 = types.InlineKeyboardButton(text='شِبُهَ ثِݪاެثِيُ بُۅتِ', callback_data='us6')
        us7 = types.InlineKeyboardButton(text='تِسُاެعٰيُ مِمِيُࢪِ࣪', callback_data='us7')
        us8 = types.InlineKeyboardButton(text='ثِمِاެنِيُ مِمِيُࢪِ࣪', callback_data='us8')
        h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
        mas.add(us0,us3,us4)
        mas.add(us2,us1,us6)
        mas.add(us5,us8,us7)
        mas.add(h7am0)
        bot.reply_to(message, text='اެخِتِاެࢪ شِنِۅ تِࢪيُډ حِبُ', reply_markup=mas)
    else:
        mas = types.InlineKeyboardMarkup(row_width=1)
        h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
        mas.add(h7am0)
        bot.reply_to(message, '''يروحي اسف انت ما مشترك بلبوت
للتفعيل اسبوع في البوت مقابل 2 ارقام تليجرام
تريد تفعل اسبوعين 3 ارقم تليجرام
تريد تفعل شهر 5 ارقام تليجرام
اقبل اي شي اخر فقط تواصل @E_4_1''', reply_markup=mas)

@bot.message_handler(func=lambda message:True)
def msg(message):
    if message.chat.type == 'private':
        if message.from_user.id in admin:
            pass
        else:
            mas = types.InlineKeyboardMarkup(row_width=1)
        h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
        mas.add(h7am0)
        bot.reply_to(message, '''يروحي اسف انت ما مشترك بلبوت
للتفعيل اسبوع في البوت مقابل 2 ارقام تليجرام
تريد تفعل اسبوعين 3 ارقم تليجرام
تريد تفعل شهر 5 ارقام تليجرام
اقبل مقابلات اي شي فقط تواصل @E_4_1''', reply_markup=mas)

@bot.callback_query_handler(func=lambda call: True)
def calling(call):
    if call.data == 'us0':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user = (v1 + '_' + v2 + '_' + v3)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -=1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="جاري الفحص ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f''' هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -=1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text="جاري الفحص ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تم فحص 500 يوزر اضغط /HAMO للصيد مره اخري')
        except:
            bot.reply_to(call.message,'حدث خطأ اضغط /HAMO وصيد مره اخري')
    if call.data == 'us1':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1+v2+v2+v2+'bot')
                user2 = (v1+v2+v2+v1+'bot')
                user3 = (v1+v1+v1+v2+'bot')
                user4 = (v1+v1+v2+v2+'bot')
                hamo010 = (user1, user2, user3, user4)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
            bot.reply_to(call.message,'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN ݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us2':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user = (v1+v2+v3+'bot')
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ...", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جاري الفحص... ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تم فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN ݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us3':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1+'_'+v2+'_'+v2+'_'+v2)
                user2 = (v1+'_'+v1+'_'+v2+'_'+v1)
                user3 = (v1+'_'+v2+'_'+v1+'_'+v1)
                user4 = (v1+'_'+v1+'_'+v1+'_'+v2)
                hamo010 = (user1, user2, user3, user4)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN ݪݪصِيډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us4':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1 + v1 + v1 + v2 + v3)
                user2 = (v1 + v1 + v2 + v3 + v1)
                user3 = (v1 + v2 + v3 + v1 + v1)
                user4 = (v1 + v3 + v2 + v2 + v2)
                user5 = (v1 + v1 + v2 + v3 + v3)
                user6 = (v1 + v2 + v2 + v3 + v3)
                user7 = (v1 + v1 + v2 + v2 + v3)
                hamo010 = (user1, user2, user3, user4, user5, user6, user7)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN ݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us5':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1 + v1 + v1 + v1 + v3 + v2)
                user2 = (v1 + v1 + v1 + v2 + v3 + v1)
                user3 = (v1 + v1 + v2 + v3 + v1 + v1)
                user4 = (v1 + v2 + v3 + v1 + v1 + v1)
                user5 = (v1 + v3 + v2 + v2 + v2 + v2)
                hamo010 = (user1, user2, user3, user4, user5)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُگ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جاري الفحص... ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN ݪݪصِيُډ مِࢪهَ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us6':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1 + '_' + v2 + '_' + v3 + 'bot')
                user2 = (v1 + v2 + v3 + '_bot')
                user3 = (v1 + v2 + '_' + v2 + 'bot')
                user4 = (v1 + '_' + v2 + v2 + 'bot')
                user5 = (v1 + v1 + '_' + v2 + 'bot')
                hamo010 = (user1, user2, user3, user4, user5)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جاري الفحص ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ/TXN ݪݪصِيُډ مِࢪاެ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN ݪݪصِيُډ مِࢪاެ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us7':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v2)
                user2 = (v1 + v1 + v1 + v1 + v1 + v1 + v1 + v2 + v1)
                user3 = (v1 + v1 + v1 + v1 + v1 + v1 + v2 + v1 + v1)
                user4 = (v1 + v1 + v1 + v1 + v1 + v2 + v1 + v1 + v1)
                user5 = (v1 + v1 + v1 + v1 + v2 + v1 + v1 + v1 + v1)
                user6 = (v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1)
                user7 = (v1 + v1 + v2 + v1 + v1 + v1 + v1 + v1 + v1)
                user8 = (v1 + v2 + v1 + v1 + v1 + v1 + v1 + v1 + v1)
                user9 = (v1 + v2 + v2 + v2 + v2 + v2 + v2 + v2 + v2)
                hamo010 = (user1, user2, user3, user4, user5,user6,user7,user8,user9)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ...☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ /TXN ݪݪصِيُډ مِࢪاެ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'تِمِ فِحِصِ 500 يُۅࢪ࣪ࢪ /TXN ݪݪصِيُډ مِࢪاެ ثِاެنِيُهَ اެضِغِطَ')
    if call.data == 'us8':
        GO = 0
        WR = 0
        AL = 0
        ALL = 500
        try:
            for bbb in range(500):
                v1 = str(''.join((random.choice(abc1) for i in range(1))))
                v2 = str(''.join((random.choice(abc) for i in range(1))))
                v3 = str(''.join((random.choice(abc) for i in range(1))))
                user1 = (v1 + v1 + v1 + v1 + v1 + v1 + v1 + v2)
                user2 = (v1 + v1 + v1 + v1 + v1 + v1 + v2 + v1)
                user3 = (v1 + v1 + v1 + v1 + v1 + v2 + v1 + v1)
                user4 = (v1 + v1 + v1 + v1 + v2 + v1 + v1 + v1)
                user5 = (v1 + v1 + v1 + v2 + v1 + v1 + v1 + v1)
                user6 = (v1 + v1 + v1 + v1 + v1 + v1 + v1 + v1)
                user7 = (v1 + v2 + v1 + v1 + v1 + v1 + v1 + v1)
                user8 = (v1 + v2 + v2 + v2 + v2 + v2 + v2 + v2)
                hamo010 = (user1, user2, user3, user4, user5,user6,user7,user8)
                user = random.choice(hamo010)
                url = requests.get(f'https://t.me/{user}').text
                if 'tgme_username_link' in url:
                    GO += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="*#")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="*#")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="*#")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="*#")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="*#")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
                    bot.reply_to(call.message, f'''هَاެكَ حِبُ صِډتِݪكَ يُۅࢪِ࣪ࢪ اެنِتِبُهَ مِتِاެحِ اެۅ مِبُنِډ ݪاެ تِعٰصِبُ عٰݪيُاެ اެحِبُكَ
@{user}''')
print('''
username : {name}


'''
                else:
                    WR += 1
                    AL += 1
                    ALL -= 1
                    ms = types.InlineKeyboardMarkup(row_width=1)
                    V = types.InlineKeyboardButton(f"ALL USERS : {ALL}", callback_data="dj")
                    T = types.InlineKeyboardButton(f"USER : @{user}", callback_data="F1")
                    B = types.InlineKeyboardButton(f"Done CHECK: {AL}", callback_data="Fsi1")
                    e = types.InlineKeyboardButton(f"SUCCESS ✅: {GO}", callback_data="Fsi1")
                    z = types.InlineKeyboardButton(f"WORNG❌ : {WR}", callback_data="Fakz1")
                    h7am0 = types.InlineKeyboardButton('مِطَۅࢪيُ', url='t.me/E_4_1')
                    ms.add(V, B, T, e, z, h7am0)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                          text="جَاެيُ اެفِحِصِ... ☠️ ", reply_markup=ms)
            bot.reply_to(call.message, 'تِمِ فِحِصِ 500 يُۅࢪِ࣪ࢪ/TXN ݪݪصِيُډ مِࢪاެ ثِاެنِيُهَ اެضِغِطَ')
        except:
            bot.reply_to(call.message,'صِاެࢪ خِطَاެ حِبُ /TXN صِيُډ مِࢪهَ ثِاެنِيُهَ')
print('bot run - HAMO \n'*5)
bot.polling(True)
