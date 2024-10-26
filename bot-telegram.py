import datetime
import csv
import telebot
from decouple import config
import time

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Salvar dados da conversa com o chatbot em arquivos CSV
def salvar(arquivo, conversa: list):
    with open(arquivo, 'a') as f:
        e = csv.writer(f)
        e.writerow(conversa)

# Inicia o bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Fala coisa linda, tudo bem contigo?", timeout=120, )
# Inicia a conversa
@bot.message_handler(regexp=r'ini?ciar')
def start(message):
    salvar('iniciar.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    bot.send_message(message.chat.id, "Fala coisa linda, tudo bem contigo?", timeout=120, )


# Faz a saudação e pergunta se quer fazer o download do arquivo
@bot.message_handler(regexp=r'tu?do?|paz|tu?do? bem')
def saudacao_pergunta(message):
    salvar('saudacao.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    bot.send_message(message.chat.id, "Bora fazer o download do arquivo? Digite bora para receber o arquivo")


# Download do arquivo
@bot.message_handler(regexp=r'bora')
def download_do_pdf(message):
    salvar('baixou.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    bot.send_message(message.chat.id, "Show! Partiu Download!")
    pdf = open('./2.pdf', 'rb')
    bot.send_chat_action(message.chat.id, 'upload_document')
    time.sleep(4)
    bot.send_document(message.chat.id, pdf, caption="Aqui está o arquivo que você pediu! Espero que você possa aproveitar porque esse conteúdo tá muit bom em 😎😎")
    pdf.close()
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(5)
    bot.send_message(message.chat.id, "Muito obrigado pelo download! qualquer coisa so digitar iniciar que eu tô por aqui!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "Tmj e bora codar! 👨‍💻👨‍💻")


# Mensagem de convencimento
@bot.message_handler(regexp=r'depois|não|nada|não|agora não|não agora|não quero|não quero agora|não,?.?obrigado')
def convencimento(message):
    salvar('naobaixou.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "É sério mesmo ??")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(6)
    bot.send_message(message.chat.id, "Mais eu vou te dar mais uma chance pra tu aprender os fundamentos de Python de graça!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(4)
    bot.send_message(message.chat.id, "Tu já sabe que é só digitar bora que eu te mando o arquivo né?")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "Caso contrário digita tchau, vou ficar triste mas tudo bem, fazer o que né ☹️☹️")

# Finaliza a conversa
@bot.message_handler(regexp=r'tchau|adeus|bye|sair|até mais|vlw|flw|fui|valeu')
def tchau(message):
    salvar('tchau.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "teimosão hein! 😂😂")
    time.sleep(1)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "Brincadeiras a parte")
    time.sleep(1)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(4)
    bot.send_message(message.chat.id, "Mas se você quiser aprender ou reforçar seus conhecimentos sobre fundamentos de Python de graça")
    time.sleep(1)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(4)
    bot.send_message(message.chat.id, "Tu já sabe que é só digitar bora que eu te mando o arquivo né?")
    time.sleep(2)
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(1)
    bot.send_message(message.chat.id, "Tmj e bora codar! 👨‍💻👨‍💻")

bot.polling() # sondagem, para ver se tem mensagens novas