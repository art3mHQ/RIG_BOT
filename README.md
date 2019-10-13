# Python-скрипт для мониторинга майнинг-ригов через Telegram

Скрипт для мониторинга ваших ригов-worker'ов на майнинг-пуле (ethermine, dwarfpool и т.д.) с помощью телеграм-бота.

## Getting Started

Суть работы кода такова:
Каждые десять минут мы опрашиваем api пула на предмет нашего текущего reportedhashrate и времени прошедшего с момента последней принятой шары, сравниваем их с заданными и при необходимости присылаем оповещение.

### Prerequisites

1. Создаем своего бота к примеру по этой инструкции:
https://vc.ru/22593-howto-bot-selectel

2. Устанавливаем Python c офф. сайта https://www.python.org/downloads/  (код проверялся на python 3)


### Installing

3. Устанавливаем дополнительные модули:

```
pip3 install requests
pip3 install telebot
pip3 install pytelegrambotapi
```
В зависимости от вашей ОС и версии python команды могут отличаться. 

4. Берем файл rig_watch.py (в файле указанны значения для примера). 
Копируем в него след. текст в котором дописываем , token вашего бота , id майнера и id чата:
```
URL = "https://api.ethermine.org/miner/тут ваш майнер/currentStats"
TOKEN = 'тут token вашего bota'
```
5. Получаем ID чата:
https://api.telegram.org/bot<YourBOTToken>/getUpdates

```
chat_id = <ваш идентификатор чата>

@bot.message_handler(content_types=["text"])
bot.send_message(chat_id, hasherate)

if hasherate < ТУТ ваш Reporthashrate с которым сравниваете результат:
	bot.send_message(chat_id, hasherate)

```

6. Ставим задачу на выполнение каждые 10 минут в cron или в планировщик задач если у вас windows.
c:\....путь к папке с установленным phyton\python.exe c:\путь к файлу watch.py


## Deployment

Желательно запускать этот код на стороннем компьютере, а не на самой ферме т.к. в случае её падения ничего приходить естественно не будет. 

## Built With

* [Vim](https://www.vim.org) - the ubiquitous text editor.
* [SublimeText](https://www.sublimetext.com) - a sophisticated text editor for code, markup and prose.
* [SublimeSix](http://www.sublimesix.com) - The power of Sublime Text and Vim combined.

## Authors

* **Denspb** - *Initial work* - форум Майнингклаб (https://miningclub.info/)

See also the list of [contributors] who participated in this project.

- art3mHQ 

## License

n/a

## Acknowledgments

* Спасибо Сатоши Накамото, Виталику Бутерину, Валере
* Om mani padme hum
* etc
