import telebot
import json 
import requests 
from datetime import datetime
from var import *
from telebot import types

TOKEN = "5033571765:AAHxt9JUbJn1O0QZI88TaiP3Ea9Wep6HiQo"

bot = telebot.TeleBot(TOKEN,parse_mode='HTML') 
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=True)
	markup.add(*[types.KeyboardButton(advert) for advert in button])
	bot.send_message(message.chat.id,'Привет\nВыберите город',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):
	city = cities[message.text]
	now = datetime.now()
	url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=26454d75bbab05ee07f45b7026fb0069&units=metric&lang=ru')
	data = url.json()
	temp_min = data['main']['temp_min']
	temp_max = data['main']['temp_max']
	temp = data['main']['temp']
	wind = data['wind']['speed']
	weather = data['weather'][0]['description'].title()
	text = f"<b>Время:</b>{now}\n\n<b>Погода:</b>{weather}\n<b>Температура:</b>{temp}°C\n<b>Ветер:</b>{wind}м/c"
	bot.send_message(message.chat.id,text)
bot.infinity_polling()