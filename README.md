# Python-скрипт для мониторинга майнинг-ригов через Telegram

Скрипт для мониторинга ваших ригов-worker'ов на пулах (ethermine, dwarfpool и т.д.) с помощью телеграм-бота.

## Getting Started

Суть работы кода такова:
Каждые десять минут скрипт опрашивает API пула на предмет текущего reportedhashrate и времени прошедшего с момента последней принятой шары, сравнивает их с заданными и при необходимости присылает оповещение.

### Prerequisites

1. Создаем своего бота к примеру по этой инструкции:
https://vc.ru/22593-howto-bot-selectel

2. Устанавливаем Python https://www.python.org/downloads/  (python 3)


### Installing

3. Устанавливаем дополнительные модули (в зависимости от вашей ОС и версии python команды могут отличаться):

```
pip3 install requests
pip3 install pyTelegramBotAPI
```
4. Берем файл **rig_watch.py** (в файле указанны значения для примера). 
Вставляем в него небходимые значения, например: **token вашего бота** , **id майнера** и **id чата** (см. соответствующие строки в скрипте):
```
URL = "https://api.ethermine.org/miner/тут ваш майнер/currentStats"
TOKEN = 'тут token вашего bota'
```
5. Получаем ID чата:
```
https://api.telegram.org/bot<YourBOTToken>/getUpdates

```

6. Ставим задачу на выполнение каждые 10 минут в cron или в планировщик задач если у вас windows.

```
C:\....путь_к_папке_с_установленным_phyton\python.exe c:\путь_к_файлу_rig_watch.py

```
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

* Спасибо Сатоши Накамото, Виталику Бутерину, Павлу Дурову и Валере
* Om mani padme hum
* etc
