import telebot
import config
import random

from telebot import  types

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.jpeg', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Че ты?")
    item2 = types.KeyboardButton("В кино пойдешь?")

    markup.add(item1, item2)

    bot.send_message(message.chat.id, f"Приветствую бандит, {message.from_user.first_name} !\n Меня Ерлан звать.",
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Че ты?':
            bot.send_message(message.chat.id, 'В очко')
        elif message.text == 'В кино пойдешь?':
            bot.send_message(message.chat.id, 'Нет нах.')
        else:
            bot.send_message(message.chat.id, 'Э нормально базарь нах.\n Иначе камрюху белую поставишь')



# RUN
bot.polling(none_stop=True)