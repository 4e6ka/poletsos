# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['sos'])
def send_welcome(message):
       bot.reply_to(message, '🙏 Список экстренных служб: \nПротивопожарная служба - 84965141863 \nАварийная сантехническая служба -  89099908170, 89295256583 \nПолиция - 84965115025 \nУК Полёт (круглосуточно!) - 89031473597 \nЛифтовая аварийная служба (круглосуточно) - 84965114636 \nПожарная безопасность и домофоны - 89671520144 \nТелефон доверия - 84985054170 \nНичего не подходит? - звоните 112 😥')

@bot.message_handler(commands=['raspisanie'])
def send_welcome2(message):
       bot.reply_to(message, '🚌 Расписание 3П и 3Пб от Полёта 🚌'),
       bot.send_photo(message.chat.id, photo=open('tests/raspisanie.jpg', 'rb'))


@bot.message_handler(content_types=['text'])
def text_handler(message):
    text = message.text.lower()
    chat_id = message.chat.id
    if text == "sos":
        bot.send_message(chat_id, '🙏 Список экстренных служб: \nПротивопожарная служба - 84965141863 \nАварийная сантехническая служба -  89099908170, 89295256583 \nПолиция - 84965115025 \nУК Полёт (круглосуточно!) - 89031473597 \nЛифтовая аварийная служба (круглосуточно) - 84965114636 \nПожарная безопасность и домофоны - 89671520144 \nТелефон доверия - 84985054170 \nНичего не подходит? - звоните 112 😥')
    elif text == "расписание":
        bot.send_message(chat_id, '🚌 Расписание 3П и 3Пб от Полёта 🚌'),
        bot.send_photo(chat_id=chat_id, photo=open('tests/raspisanie.jpg', 'rb'))
    else:
        None
		
		
	

if __name__ == '__main__':
     bot.infinity_polling()
