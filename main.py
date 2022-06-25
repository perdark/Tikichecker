import requests

import user_agent

import json

import flask

import telebot

import random

import os

import sys

import telebot

from telebot import types

from user_agent import generate_user_agent

import logging

from config import *

from flask import Flask

bot = telebot.TeleBot("5554345313:AAEIcNmKzGYm6mFCIzGi2PjqYMoXmNsiVUQ")

#START FUN

@bot.message_handler(commands=['start'])

def boten(message):

    mas = types.InlineKeyboardMarkup(row_width=2)

    #BUTTONS

    #BTN1

    A = types.InlineKeyboardButton(text ="USER (BFFFL)", callback_data="F1")

    #BTN2

    B = types.InlineKeyboardButton(text ="USER (BFFF2)", callback_data="F2")

    #BTN3

    C = types.InlineKeyboardButton(text ="USER (BFLBOT)", callback_data="F3")

    #BTN4

    D = types.InlineKeyboardButton(text ="USER (BF1BOT)", callback_data="F4")

    #BTN5

    M = types.InlineKeyboardButton('المطور', url='https://t.me/dar4k')

    

    mas.add(A,B,C,D,M)

    

    bot.send_message(message.chat.id, f'''

𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝗍𝗁𝖾 𝖻𝗈𝗍 

	𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗎𝗌𝖾𝗋 𝖼𝗁𝖾𝖼𝗄𝖾𝗋    

    𝘽𝙮 : @dar4k

    ''',reply_markup=mas)

    

    

@bot.callback_query_handler(func=lambda call: True)

def masg(call):

	

	

	global nam

	

	#FUN1

	

	if call.data =="F1":

		

		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xm = "0987654321"

		ok=0

		cp=0

		sk=0

		while True:

			letter1 = str(''.join(random.choice(xu)for i in range(1)))

			letter2 = str(''.join(random.choice(xn)for i in range(1)))

			letter3 = str(''.join(random.choice(xa)for i in range(1)))

			num1 = str(''.join(random.choice(xm)for i in range(1))) 

			username = str(letter1)+str(letter2)+str(letter2)+str(letter2)+str(letter3)

			url = "https://t.me/"+str(username)

			headers = {

            "User-Agent": generate_user_agent(),

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Encoding": "gzip, deflate, br",

            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

            

			response = requests.get(url, headers=headers)

			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:

				ok+=1

				sk+=1

				bot.send_message(call.message.chat.id,f'''

				𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :

					@{username} 

				

				𝘽𝙔 : @dar4k

				''')

				if ok == 25 :

					bot.send_message(call.message.chat.id,f"𝗖𝗛𝗘𝗖𝗞𝗘𝗗 25 𝗨𝗦𝗘𝗥 /n 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗦𝗧𝗔𝗥𝗧 𝗔𝗚𝗔𝗜𝗡 𝗧𝗬𝗣𝗘 /start")

					os.exit()

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

				

			

		

		#FUN2

	elif call.data =="F2":

		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xm = "0987654321"

		ok=0

		cp=0

		sk=0

		while True:

			letter1 = str(''.join(random.choice(xu)for i in range(1)))

			letter2 = str(''.join(random.choice(xn)for i in range(1)))

			letter3 = str(''.join(random.choice(xa)for i in range(1)))

			num1 = str(''.join(random.choice(xm)for i in range(1))) 

			username = str(letter1)+str(letter2)+str(letter2)+str(letter2)+str(num1)

			url = "https://t.me/"+str(username)

			headers = {

            "User-Agent": generate_user_agent(),

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Encoding": "gzip, deflate, br",

            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

			response = requests.get(url, headers=headers)

			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:

				ok+=1

				sk+=1

				bot.send_message(call.message.chat.id,f'''

				𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :

					@{username} 

				

				𝘽𝙔 : @dar4k

				''')

				print(" available : ",username)

				if ok == 25 :

					bot.send_message(call.message.chat.id,f"𝗖𝗛𝗘𝗖𝗞𝗘𝗗 25 𝗨𝗦𝗘𝗥 /n 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗦𝗧𝗔𝗥𝗧 𝗔𝗚𝗔𝗜𝗡 𝗧𝗬𝗣𝗘 /start")

					os.exit()

			else:

				t = ""

				cp+=1

				sk+=1

				mas = types.InlineKeyboardMarkup(row_width=2)

				A = types.InlineKeyboardButton(f'Available : {ok}', callback_data="1x")

				E = types.InlineKeyboardButton(f'Not available : {cp}', callback_data="1x")

				B = types.InlineKeyboardButton(f'{username}', callback_data="1x")

				

				

				M = types.InlineKeyboardButton('المطور', url='https://t.me/dar4k')

				

				

				mas.add(A,E,B,M)

				

				bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ok start",reply_markup=mas)

				

	#FUN3

	elif call.data =="F3":

		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xm = "0987654321"

		ok=0

		cp=0

		sk=0

		while True:

			letter1 = str(''.join(random.choice(xu)for i in range(1)))

			letter2 = str(''.join(random.choice(xn)for i in range(1)))

			letter3 = str(''.join(random.choice(xa)for i in range(1)))

			num1 = str(''.join(random.choice(xm)for i in range(1))) 

			username = str(letter1)+str(num1)+str(letter2)+str("BOT")

			url = "https://t.me/"+str(username)

			headers = {

            "User-Agent": generate_user_agent(),

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Encoding": "gzip, deflate, br",

            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

            

			response = requests.get(url, headers=headers)

			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:

				ok+=1

				sk+=1

				bot.send_message(call.message.chat.id,f'''

				𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :

					@{username} 

				

				𝘽𝙔 : @dar4k

				''')

				if ok == 25 :

					bot.send_message(call.message.chat.id,f"𝗖𝗛𝗘𝗖𝗞𝗘𝗗 25 𝗨𝗦𝗘𝗥 /n 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗦𝗧𝗔𝗥𝗧 𝗔𝗚𝗔𝗜𝗡 𝗧𝗬𝗣𝗘 /start")

					os.exit()

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

				

	#FUN4

	elif call.data =="F3":

		

		xu = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xn = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xa = "MNBVCXZLKJHGFDSAPOIUYTREWQ"

		xm = "0987654321"

		ok=0

		cp=0

		sk=0

		while True:

			letter1 = str(''.join(random.choice(xu)for i in range(1)))

			letter2 = str(''.join(random.choice(xn)for i in range(1)))

			letter3 = str(''.join(random.choice(xa)for i in range(1)))

			num1 = str(''.join(random.choice(xm)for i in range(1))) 

			username = str(letter1)+str(num1)+str(letter2)+str("BOT")

			url = "https://t.me/"+str(username)

			headers = {

            "User-Agent": generate_user_agent(),

            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",

            "Accept-Encoding": "gzip, deflate, br",

            "Accept-Language" : "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"}

            

			response = requests.get(url, headers=headers)

			if response.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:

				ok+=1

				sk+=1

				bot.send_message(call.message.chat.id,f'''

				𝗧𝗛𝗜𝗦 𝗨𝗦𝗘𝗥 𝗔𝗩𝗔𝗜𝗟𝗔𝗕𝗟𝗘 :

					@{username} 

				

				𝘽𝙔 : @dar4k

				''')

				if ok == 25 :

					bot.send_message(call.message.chat.id,f"𝗖𝗛𝗘𝗖𝗞𝗘𝗗 25 𝗨𝗦𝗘𝗥 /n 𝗜𝗙 𝗬𝗢𝗨 𝗪𝗔𝗡𝗧 𝗧𝗢 𝗦𝗧𝗔𝗥𝗧 𝗔𝗚𝗔𝗜𝗡 𝗧𝗬𝗣𝗘 /start")

					os.exit()

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
