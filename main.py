from telebot import *
import os
from dotenv import load_dotenv

load_dotenv()
Token = os.getenv('TOKEN')

bot = telebot.TeleBot(Token)




@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('Январь', style="success")
    bt2 = types.KeyboardButton('Феврель')
    bt3 = types.KeyboardButton('Март')
    bt4 = types.KeyboardButton('Апрель')
    bt5 = types.KeyboardButton('Май')
    bt6 = types.KeyboardButton('Июнь')
    markup.row(bt1, bt2, bt3)
    markup.row(bt4, bt5, bt6)
    bot.send_message(message.chat.id, f'Привет, моя любимая! Поздравляю с полугодием <3. Предлагаю с помощью этого бота вспомнить каждый из этих шести счастливых месяцев. Люблю тебя ❤️', reply_markup=markup)
    bot.register_next_step_handler(message, main_menu)

def January(message):
    print(f"вызвали {message.text}")

def February(message):
    print(f"вызвали {message.text}")

def March(message):
    print(f"вызвали {message.text}")

def April(message):
    print(f"вызвали {message.text}")

def May(message):
    print(f"вызвали {message.text}")

def June(message):
    print(f"вызвали {message.text}")

def main_menu(message):
    if message.text in MonthsAction:
        MonthsAction[message.text](message)
    else:
        print("Неизвестная команда")

MonthsAction = {
    "Январь": January,
    "Феврель": February,
    "Март": March,
    "Апрель": April,
    "Май": May,
    "Июнь": June
}

bot.polling(non_stop=True)