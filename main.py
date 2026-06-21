from telebot import *
from telebot.types import InputMediaPhoto, InputMediaVideo
import os
from dotenv import load_dotenv


load_dotenv()
Token = os.getenv('TOKEN')

bot = telebot.TeleBot(Token)
Photes = [
    [InputMediaPhoto(open('Junary/1.jpg', 'rb')),
    InputMediaPhoto(open('Junary/2.jpg', 'rb')),
    InputMediaPhoto(open('Junary/3.jpg', 'rb')),
    InputMediaVideo(open('Junary/6.mp4', 'rb'))],
    [InputMediaPhoto(open('Junary/4.jpg', 'rb')),
     InputMediaPhoto(open('Junary/5.jpg', 'rb'))],
    [InputMediaPhoto(open('Junary/7.jpg', 'rb')),
     InputMediaPhoto(open('Junary/8.jpg', 'rb'))]
]

texts = ["мииии, на каточке)", "люти вайб ловлю с этих фоток если честно", '"на кухню меня повором пристройте"']

markup_index = types.ReplyKeyboardMarkup()
btnext = types.KeyboardButton('Далее')
markup_index.row(btnext)
number_index = 0

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    bt1 = types.KeyboardButton('ЕЕЕЕ ГОУ')
    markup.row(bt1)
    bot.send_message(message.chat.id, f'Привет, моя любимая! Поздравляю с полугодием <3. Предлагаю с помощью этого бота вспомнить все счатливые моменты. Люблю тебя ❤️', reply_markup=markup)
    bot.register_next_step_handler(message, main_menu)

def main_menu(message):
    print(len(Photes[number_index]))
    bot.send_media_group(message.chat.id, Photes[number_index])
    bot.send_message(message.chat.id, f'{texts[number_index]}', reply_markup=markup_index)
    bot.register_next_step_handler(message, checking_messages)

def checking_messages(message):
    global number_index
    if message.text == "Далее":
        number_index += 1
        main_menu(message)
    else:
        bot.send_message(message.chat.id, "Нажмите кнопку 'Далее'")
        bot.register_next_step_handler(message, checking_messages)

bot.polling(non_stop=True)