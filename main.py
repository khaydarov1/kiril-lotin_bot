from transliterate import to_latin, to_cyrillic
import telebot

TOKEN = '5995137894:AAHag-WrCC_vHn7Aj0M3h6XP-NUEB248AD4'
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu aleykum! Kiril-lotin botiga xush kelibsiz!\n Matn kiriting")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg=message.text
    if msg.isascii():
        javob=to_cyrillic(msg)
    else:
        javob=to_latin(msg)
    bot.reply_to(message,javob)

bot.polling()

