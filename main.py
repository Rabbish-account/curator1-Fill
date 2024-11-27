import telebot

bot = telebot.TeleBot('8081777633:AAF_5yURsVz0Fk2QVPj-uPHvkcXJsujolXo')


@bot.message_handler(commands=['Aliexpress'])
def main(message):
    bot.send_message(message.chat.id, '*Алиэкспресс* (https://aliexpress.ru/)', parse_mode='Markdown')


@bot.message_handler(commands=['Ozon'])
def second(message):
    bot.send_message(message.chat.id, '*Озон*  (https://www.ozon.ru/)', parse_mode='Markdown')


@bot.message_handler(commands=['Vb'])
def third(message):
    bot.send_message(message.chat.id, '*Вб*  (https://www.wildberries.ru/)', parse_mode='Markdown')


@bot.message_handler(commands=['Yandexmarket'])
def forth(message):
    bot.send_message(message.chat.id, '*Яндексмаркет*  (https://market.yandex.ru/)', parse_mode='Markdown')


@bot.message_handler(commands=['Avito'])
def forth(message):
    bot.send_message(message.chat.id, '*Авито*  (https://www.avito.ru/)', parse_mode='Markdown')


bot.infinity_polling()