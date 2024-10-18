import requests
from bs4 import BeautifulSoup

r = requests.get("https://horo.mail.ru/prediction/aquarius/today/")
html = BeautifulSoup(r.content, "html.parser")

# for el in html.find('div','article__item article__item_alignment_left article__item_html'):
#     print(el.text)
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
print(zodiac_signs['Овен'].lower())

