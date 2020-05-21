import requests
import telebot
from telebot import apihelper

# If you want to use socket5 proxy you need install dependency pip install 
# requests[socks] and make sure, that you have the latest version of 
# gunicorn, PySocks, pyTelegramBotAPI, requests and urllib3
apihelper.proxy = {'https':'socks5://userproxy:password@proxy_address:port'}


URL = 'http://dwarfpool.com/eth/api?wallet= <ваш_номер_кошелька> &email=mail@example.com'
TOKEN = '<ваш токен>'
bot = telebot.TeleBot(TOKEN)

# Your rig #1
r = requests.get(url = URL)
data = r.json()
hasherate = data['total_hashrate']
sincelast1 = data['workers']['<имя воркера №1>']['second_since_submit']
sincelast2 = data['workers']['<имя воркера №2>']['second_since_submit']

chat_id = <ваш идентификатор чата>

if sincelast1 + sincelast2 > 3800:
    bot.send_message(chat_id, "Your total hash is {} 🚀".format(hasherate))
    bot.send_message(chat_id, "🐌 second since last share! {}, {}!".format(sincelast1, sincelast2))

if hasherate < 319:
    bot.send_message(chat_id, "🔥Your hash is {} but 319 supsd,\nsecs since last share {}, {}!".format(hasherate, sincelast1, sincelast2))
