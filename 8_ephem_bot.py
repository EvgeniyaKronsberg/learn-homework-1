"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""


import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
import time

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


# функция, которая по названию планеты определяет ее положение в созвездии на сегодняшнюю дату
def planet_info(update, context):
    planet_command = update.message.text
    planet_name = planet_command.split()[1].capitalize() # извлекаем название планеты
    print(f'Выбрана планета: {planet_name}')
    
    today = time.strftime("%Y/%m/%d") # определяем сегодняшнюю дату
    print(today) 
    print(planet_name)
    print(type(planet_name))

    planet_obj = getattr(ephem, planet_name)(today) # получаем объект ephem с данными для нашей планеты
    print(planet_obj)

    const = ephem.constellation(planet_obj) # извлекаем информацию о созвездии
    print(const)
    print(type(const))

    update.message.reply_text(f'Планета {planet_name} сегодня находится в созвездии {const[1]}') # выводим в телеграм информацию о созвездии


def main():
    mybot = Updater(settings.API_KEY, request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_info))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))


    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
