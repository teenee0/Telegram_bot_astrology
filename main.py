import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup
import datetime
zodiac_signs = {
    "Овен": "Aries",
    "Телец": "Taurus",
    "Близнецы": "Gemini",
    "Рак": "Cancer",
    "Лев": "Leo",
    "Дева": "Virgo",
    "Весы": "Libra",
    "Скорпион": "Scorpio",
    "Стрелец": "Sagittarius",
    "Козерог": "Capricorn",
    "Водолей": "Aquarius",
    "Рыбы": "Pisces"
}

bot = telebot.TeleBot("6734544372:AAFGWJ1kKFgNcnzTlrKpDkilVVI8ee0zdSM")

@bot.message_handler(commands=['start'])
def start(message):
    mark = types.InlineKeyboardMarkup()
    for sign in zodiac_signs:
        btn = types.InlineKeyboardButton(sign, callback_data=sign)
        mark.add(btn)
    photo = open('main.jpg', "rb")
    bot.send_photo(message.chat.id, photo=photo, caption='''Приветствую тебя, звездный странник! Добро пожаловать в мир Гороскопов на каждый день! Готов прогнозировать твои звездные перспективы и помочь раскрывать тайны Вселенной! Тогда давай начнем наше захватывающее приключение по звездам! ✨🔮✨''', reply_markup=mark)


@bot.callback_query_handler(func=lambda callback:True)
def get_info(callback):
    mark = types.InlineKeyboardMarkup()
    for sign in zodiac_signs:
        btn = types.InlineKeyboardButton(sign, callback_data=sign)
        mark.add(btn)
    r = requests.get(f"https://horo.mail.ru/prediction/{zodiac_signs[callback.data].lower()}/today/")
    html = BeautifulSoup(r.content, "html.parser")
    otvet = []
    for el in html.find('div', 'article__item article__item_alignment_left article__item_html'):
        otvet.append(el.text)
    current_date = datetime.date.today()
    photo = open(f"{zodiac_signs[callback.data]}.jpg", "rb")
    bot.send_photo(callback.message.chat.id, photo=photo,  caption=f'Прогноз {callback.data} на {current_date.strftime("%d.%m.%Y")}:\n\n{" ".join(otvet)}', reply_markup=mark)



bot.polling(none_stop=True)