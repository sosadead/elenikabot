from cny import CNY
import telebot
from telebot import types


bot = telebot.TeleBot('6318582915:AAGh0ftK7zfCUFf-gCUrleZeiRe0KmKs1K4')

amount = 0
commission = 0
keyboard = telebot.types.InlineKeyboardMarkup()

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я помогу рассчитать стоимость вашего товара!')
    bot.send_message(message.chat.id, 'Введите стоимость товара(ов) в юанях:')
    bot.register_next_step_handler(message, summa)

def summa(message):
    global amount
    global commission
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Это не стоимость товара🫤. Впишите число!')
        bot.register_next_step_handler(message, summa)
        return
    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=1)
        btn1 = types.InlineKeyboardButton('Рассчиать', callback_data='price')
        markup.add(btn1)
        bot.send_message(message.chat.id, '⬇️📱', reply_markup=markup)
    else:
         bot.send_message(message.chat.id, 'Число должно быть больше "0"☝️. Впишите число!')
         bot.register_next_step_handler(message, summa)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if amount <= 100:
        commission = 500
    elif 100 < amount <= 350:
        commission = 750
    else:
        commission = 1000
    if call.data == 'price':
        res = amount * CNY
        finaly_price = res + commission
        bot.send_message(call.message.chat.id, f'Стоимость товара: {round(res, 2)}₽\nКомиссия: {commission}₽\nИтог: {round(finaly_price, 2)}₽\n*Доставка не входит в итоговую стоимость!')
        bot.register_next_step_handler(call.message, summa)


bot.polling(none_stop=True)