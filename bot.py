import telebot
import config
import random

from telebot import  types

bot = telebot.TeleBot(config.TOKEN)
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/welcome.jpeg', 'rb')
    bot.send_sticker(message.chat.id, sti)

    # keyboards
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Че ты?")
    item2 = types.KeyboardButton("В кино пойдешь?")
    item3 = types.KeyboardButton("Саида знаешь ?")
    item4 = types.KeyboardButton("Ты откуда сам ?")
    item5 = types.KeyboardButton("Хасана даргинца знаешь ?")
    item6 = types.KeyboardButton("Шому знаешь ?")
    item7 = types.KeyboardButton("За Фарида че скажешь?")
    item8 = types.KeyboardButton("Ты сам где сейчас ?")


    markup.add(item1, item2, item3, item3, item4, item5, item6, item7, item8)

    bot.send_message(message.chat.id, f"Приветствую бандит, {message.from_user.first_name} !\n Меня Ерлан звать.",
                     parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        pass
    if message.text == 'Че ты?':
        bot.send_message(message.chat.id, 'В очко')
    elif message.text == 'В кино пойдешь?':
        bot.send_message(message.chat.id, 'Нет нах.')
    elif message.text == 'Саида знаешь ?':
        bot.send_message(message.chat.id, 'эмм... давай не об этом.')
    elif message.text == 'Ты откуда сам ?':
        bot.send_message(message.chat.id, 'Вырос на бабайке, там стал мужчиной, \n но все равно мое детсво прошло довольно таки спокойно,\n пока там не начались боевые дейтвия.')
    elif message.text == 'Хасана даргинца знаешь ?':
        bot.send_message(message.chat.id, 'Да, шут гороховый. Че не так чтоли нах ?')
    elif message.text == 'Шому знаешь ?':
        bot.send_message(message.chat.id, 'Да такой же клоун, что и Хасан.')
    elif message.text == 'За Фарида че скажешь?':
        bot.send_message(message.chat.id, 'Добряк, сколько раз выручал меня, косячник правда, лучше уж купить работу,\n чем годами исправлять то, что  он своими жопоруками сделал.')
    elif message.text == 'Ты сам где сейчас ?':
        bot.send_message(message.chat.id, 'В Москве работаю мастером,\n ну сам понимешь не последний чел в городе.')
    else:
        bot.send_message(message.chat.id, 'Э нормально базарь нах.\n Иначе камрюху белую поставишь.')



# RUN
bot.polling(none_stop=True)