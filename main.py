import random, os
import requests
import telebot
from telebot import types
bot = telebot.TeleBot("5137968496:AAG7h0QirEyWS8Ti7AMLBtN5zMfhEUIWKsM")



#START FUN
@bot.message_handler(commands=['start'])
def boten(message):
    mas = types.InlineKeyboardMarkup(row_width=2)
    #BUTTONS
    #BTN1
    A = types.InlineKeyboardButton(text ="USER (AAAB)", callback_data="F1")
    #BTN2
    B = types.InlineKeyboardButton(text ="USER (AAA1)", callback_data="F2")
    C = types.InlineKeyboardButton(text ="USER (AB_1)", callback_data="F3")
    D = types.InlineKeyboardButton(text ="USER (AB_C)", callback_data="F4")
    Dev = types.InlineKeyboardButton('المطور', url='https://t.me/sedthon/1')
    
    mas.add(A,B,C,D,Dev)
    
    bot.send_message(message.chat.id, f'''
    اهلاً بكَ في بوت صيد يوزرات تيكي 
ملاحظة : البوت يفحص 500 يوزر ولازم ترجع تشغله 
           اختر زر من الازرار : 
    ''',reply_markup=mas)
    
    
@bot.callback_query_handler(func=lambda call: True)
def masg(call):
	
	
	global nam
	
	#FUN1
	
	if call.data =="F1":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		
		
		ok=0
		cp=0
		sk=0
		for i in range(500):
			letter1 = str(''.join(random.choice(xu)for i in range(1)))
			letter2 = str(''.join(random.choice(xu)for i in range(1)))
			
			username = ""
			username = letter1+letter1+letter1+letter2
			respone = requests.get(f"https://tiki.video/@{username}/?lang=en").status_code
			if respone == 404 :
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f'''	𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :
					@{username} 
				𝘿𝙚𝙫 : @Dar4k
				''')
				print(" AVIABLE :"+ username)
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/dar4k')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
				
	if call.data =="F2":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xd = "123456789"
		ok=0
		cp=0
		sk=0
		for i in range(500):
			letter1 = random.choice(xu)
			num1 = random.choice(xd)
			username = ""
			username = letter1+letter1+letter1+num1
			respone = requests.get(f"https://tiki.video/@{username}/?lang=en").status_code
			if respone == 404 :
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f'''
	𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :
					@{username} 
				𝘿𝙚𝙫 : @Dar4k
				''')
				print("AVIABLE  :"+username )
			
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/dar4k')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)
	if call.data =="F3":
		
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		xd = "123456789"
		ok=0
		cp=0
		sk=0
		for i in range(500):
			letter1 = random.choice(xu)
			letter2 = random.choice(xu)
			num1 = random.choice(xd)
			username = ""
			username = letter1+letter2+"_"+num1
			respone = requests.get(f"https://tiki.video/@{username}/?lang=en").status_code
			if respone == 404 :
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f'''
	𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :
					@{username} 
				𝘿𝙚𝙫 : @Dar4k
				''')
				print("AVIABLE  :"+username )
			
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/dar4k')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)

	if call.data =="F4":
		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"
		ok=0
		cp=0
		sk=0
		for i in range(500):
			letter1 = random.choice(xu)
			letter2 = random.choice(xu)
			letter3 = random.choice(xu)
			username = ""
			username = letter1+letter2+"_"+letter3
			respone = requests.get(f"https://tiki.video/@{username}/?lang=en").status_code
			if respone == 404 :
				ok+=1
				sk+=1
				bot.send_message(call.message.chat.id,f'''
	𝖠𝗏𝖺𝗂𝗅𝖺𝖻𝗅𝖾 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 :
					@{username} 
				𝘿𝙚𝙫 : @Dar4k
				''')
				print("AVIABLE  :"+username )
			
			else:
				cp+=1
				sk+=1
				mas = types.InlineKeyboardMarkup(row_width=2)
				A = types.InlineKeyboardButton(f'GOOD : {ok}',callback_data="1x")
				E = types.InlineKeyboardButton(f'EROR : {cp}', callback_data="1x")
				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")
				R = types.InlineKeyboardButton(f'{sk}', callback_data="1x")
				M = types.InlineKeyboardButton('المطور', url='https://t.me/dar4k')
				mas.add(A,E,B,R,M)
				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)

bot.infinity_polling()
