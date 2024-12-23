from translate import translate
import telebot # pyTelegramBotAPI ning nomi

TOKEN ="INSERT YOUR BOT TOKEN"
tarjimonbot = telebot.TeleBot(token=TOKEN)

# \start komandasi uchun mas'ul funksiya
@tarjimonbot.message_handler(commands=['start'])
def salom(message):
    xabar = "Assalomu alaykum, tarjimon botiga xush kelibsiz!"
    xabar += '\nMatningizni yuboring.'
    tarjimonbot.reply_to(message, xabar)

#Matnlar uchun masʼul funksiya
@tarjimonbot.message_handler(func=lambda msg: msg.text is not None)
def tarjima(message):
    msg = message.text
    tarjimonbot.reply_to(message, translate(msg))
    
tarjimonbot.polling()