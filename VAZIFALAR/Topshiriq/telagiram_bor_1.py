import telebot
from transilet_uz import to_cyrillic, to_latin

TOKEN = "8213323098:AAGnrv42s2kd2BD4oIoVlL6q1R2kmE3IiaM"
bot = telebot.TeleBot(token=TOKEN)

@bot.message_handler(commands=["start"])
def send_welcome(message):
    username = (
        message.from_user.username
    )  
    xabar = f"Assalom alaykum, {username} Kirill-Lotin-Kirill botiga xush kelibsiz!"
    xabar += "\nMatningizni yuboring."
    bot.reply_to(message, xabar)


@bot.message_handler(func=lambda msg: msg.text is not None)
def translit(message):
    msg = message.text
    javob = lambda msg: to_cyrillic(msg) if msg.isascii() else to_latin(msg)
    bot.reply_to(message, javob(msg))


bot.polling()























