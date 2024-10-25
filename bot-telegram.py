import telebot
from decouple import config
import time

from telebot import types

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Inicia a conversa com o bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Fala coisa linda, tudo bem contigo?")

# Faz a saudação e pergunta se quer fazer o download do arquivo
@bot.message_handler(regexp=r'tudo|td|paz')
def saudacao_pergunta(message):
    bot.send_message(message.chat.id, "Bora fazer o download do arquivo? Digite bora para receber o arquivo")

# 
@bot.message_handler(regexp=r'bora|sim|vamos|quero|baixar|download')
def download_do_pdf(message):
    bot.send_message(message.chat.id, "Show! Partiu Download!")
    pdf = open('./2.pdf', 'rb')
    bot.send_chat_action(message.chat.id, 'upload_document')
    time.sleep(2)
    bot.send_document(message.chat.id, pdf, caption="Aqui está o arquivo que você pediu!")
    pdf.close()
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "Muito obrigado pelo download!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "Tmj e boas análises!")


bot.polling() # sondagem, para ver se tem mensagens novas