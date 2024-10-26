## Cuidados
- Não ficar totalmente robotizado
- limites, o chatbot será utilizado somente como filtro, como uma porta
- Existem algumas situações que o chatbot pode auxiliar de ponta a ponta
- Cuidado para não robotizar tanto para que o usuário não ficar chateado
- disponibilidade 24 / 7

#### Livro


# Aula 01 - Chatbots: Fundamentos da NLP (Processamento em Linguagem Natural)
## Mini chatbotinho

[Aula 01](https://www.youtube.com/watch?v=Gjgv42Z5z_4&t=2572s)

Biblioteca [Spacy](https://spacy.io/usage)

```sh
pip install -U pip setuptools wheel
pip install -U spacy
# languages packages

python -m spacy download en_core_web_sm
python -m spacy download pt_core_news_sm
```

Uso básico para NPL
```python
import spacy

nlp = spacy.load('pt_core_news_sm')

```

#### Tokenização
É o básico do básico do NPL. Um token é um 'pedaço' da fala, ou ponto de parada, ou espaço

#### Exemplo 1: Verificando os tokens
```python
import spacy

nlp = spacy.load('pt_core_news_sm')

txt = nlp( u"Eu estou aprendendo a utilizar chatbots.")

for token in txt:
    print(token.text, token.pos_)
    # pos_: Part of Speech, é uma parte da fala
    # o que cada pedaço da fala significa
    # Ele separa todo detalhe do texto
```
Saída

```sh
Eu PRON # Pronome
estou AUX # Verbo auxiliar
aprendendo VERB # verbo
a SCONJ # Conjunção subordinativa
utilizar VERB # Verbo
chatbots NOUN # Substantivo
. PUNCT # Ponto final, pontuação
```

#### Exemplo 2: Mais alguns atributos do token
```python
import spacy

nlp = spacy.load('pt_core_news_sm')

txt = nlp( u"O Canal do YouTube do professor 'Cláudio Bonel' está chegando a 11.000 inscritos.")

for token in txt:
    print(
        "Texto: ", token.text, "\n",
        "Forma raíz da palavra: ", token.lemma_, "\n",
        "tipo da palavra: ", token.pos_, "\n",
        "Se são letras: ", token.is_alpha, "\n",
        "Se são números: ", token.is_digit, "\n",
        )
```
#### Exemplo 3: Buscando similaridade
Buscar similaridade entre as palavras e os contextos
```python
import spacy

nlp = spacy.load('pt_core_news_sm')

txt3 = input("Como posso te ajudar hoje? ")

txt3 = nlp(txt3)

for token in txt3:
    for token1 in txt3:
        similaridade = token.similarity(token1) * 100
        print( f"A palavra {token} é {round(similaridade, 2)}% similar a palavra do {token1}" )
```
Dessa forma é possível analisar similaridade entre as palavras
#### Exemplo 4: Buscando similaridade e comparando com as regas do meu chatbot

```python
import spacy

nlp = spacy.load('pt_core_news_sm')

txt4 = input("Como posso te ajudar hoje? ")

txt4 = nlp(txt4)

texto_comparativo = nlp("conhecimento")

for token in txt4:
    similaridade = round( (token.similarity(texto_comparativo) * 100), 2)

    if(similaridade == 100):
        print( f"A palavra {token.text} é {similaridade}% similar ao texto conhecimento " )
    elif(similaridade >= 39 and similaridade <= 99):
        pergunta_similaridade = input("Você quis dizer conhecimento? ")
        if(pergunta_similaridade == "sim"):
            print( f"A palavra {token.text} é {similaridade}% similar ao texto conhecimento " )
        else:
            print( f"Favor refaça sua solicitação " )
```
Simular a busca de similaridade entre termos

# Aula 02 - Chatbots: Árvore de decisão, integração e interação do chatbot com o Telegram, em Python

[Aula 02](https://www.youtube.com/watch?v=KZCMFAc3UAM)

#### Ávore de decisão: processo decisório baseado na iteração do chatbot com o interlocutor (usuário)
- A árvore de decisão será sempre projetada antes da criação do chatbot
- Árvore de decisões tem que ser simples de fazer

#### Criar o bot no telegram com o [BotFather](https://t.me/BotFather)

#### Instalar bibliotecas para a integração com o Telegram
```sh
pip install pyTelegramBotAPI
pip install --upgrade pyTelegramBotAPI
pip install telebot
pip install python-decouple
```
Preparando a codificação

```python
import telebot
from decouple import config
```

Criação do arquivo .env

```txt
TELEGRAM_TOKEN=<TELEGRAM_TOKEN>
```
Carregar a configuração
```python
import telebot
from decouple import config

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
```

Criar a função da primeira parte do fluxo decisório
```python
import telebot
from decouple import config

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'inicio'])
def start(message):
    bot.send_message(message.chat.id, "Fala coisa linda, tudo bem contigo?")

bot.polling() # sondagem, para ver se tem mensagens novas
```
Recuperando a mensagem de resposta do usuário
```python
import telebot
from decouple import config

TELEGRAM_TOKEN = config("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'inicio'])
def start(message):
    bot.send_message(message.chat.id, "Fala coisa linda, tudo bem contigo?")

@bot.message_handler(regexp=r'tudo|td|paz')
def start(message):
    bot.send_message(message.chat.id, "Bora fazer o download do arquivo? Digite bora para receber o arquivo")

bot.polling() # sondagem, para ver se tem mensagens novas
```
#### Árvore de decisão do bot
![Chatbot Decision Tree](https://github.com/thalisonwilker/python-chatbot/blob/main/arvore-decisao-bot-telegram.png?raw=true)

A árvore de decisão irá consistir em guiar o usuário para digitar o que precisamos, depois de projetar o fluxo o bot já pode as etapas necessárias podem ser codificadas

#### Etapas
- Iniciar o bot
- Mensagem de saudação e pergunta se quer baixar o PDF
- Se sim, enviar o arquivo e envia mensagem de encerramento
- Se não, tenta convencer a baixar o livro, e pergunta novamente se quer baixar o PDF
- Se sim, enviar o arquivo e envia mensagem de encerramento
- Se não, envia o link do YouTube e depois a mensagem de encerramento

#### Codificação das etapas
##### Iniciar o bot
Para iniciar o bot, é importante criar uma `message_handler` para tratar o comando _/start_

```python
# Inicia a conversa com o bot
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Fala coisa linda, tudo bem contigo?", timeout=120)
```
Agora é necessário tratar a resposta do usuário, o método que pode ser utilizado para buscar os textos que queremos também é o `message_handler`, mas ao invés de usar o parâmetro _commands=['start']_ é bem mais interesante utilizar o parâmetro _regexp=r''_
##### Saudação e pergunta se quer baixar o PDF
```python
# Faz a saudação e pergunta se quer fazer o download do arquivo
@bot.message_handler(regexp=r'tu?do?|paz|tu?do? bem') # aqui eu fiz um pouco diferente do que o prefessor mostrou, mas funciona igal
def saudacao_pergunta(message):
    bot.send_message(message.chat.id, "Bora fazer o download do arquivo? Digite bora para receber o arquivo")
```
##### Se sim, enviar o arquivo e envia mensagem de encerramento
```python
# Download do arquivo
@bot.message_handler(regexp=r'boo?ra|sim|vamos|quero|baixar|download') # Aqui eu também fiz um pouco diferente do que o professor mostrou, para testar outras situações de input
def download_do_pdf(message):
    bot.send_message(message.chat.id, "Show! Partiu Download!")
    pdf = open('./2.pdf', 'rb')
    bot.send_chat_action(message.chat.id, 'upload_document')
    time.sleep(4)
    bot.send_document(message.chat.id, pdf, caption="Aqui está o arquivo que você pediu! Espero que você possa aproveitar porque esse conteúdo tá muit bom em 😎😎")
    pdf.close()
    # Mensagem de encerramento
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(3)
    bot.send_message(message.chat.id, "Muito obrigado pelo download! qualquer coisa so digitar iniciar que eu tô por aqui!")
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)
    bot.send_message(message.chat.id, "Tmj e bora codar! 👨‍💻👨‍💻")
```
##### Se não, tenta convencer a baixar o livro, e pergunta novamente se quer baixar o PDF
```python
# Mensagem de convencimento
@bot.message_handler(regexp=r'depois|não|nada|não|agora não|não agora|não quero|não quero agora|não,?.?obrigado') # Sempre faço essa parte diferente do que o professor mostrou haha, mas funciona igualmente!
def convencimento(message):
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
```
Se o usuário digitar bora, ele retorna para o fluxo anterior, se ele digitar tchau, ou algum termo da regex o bot entra no fluxo final
```python
# Finaliza a conversa
@bot.message_handler(regexp=r'tchau|adeus|bye|sair|até mais|vlw|flw|fui|valeu')
def tchau(message):
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
```

# Aula 03 - Desenvolvendo algoritmo para salvar dados da conversa com o chatbot do Telegram
[Aula 03](https://www.youtube.com/watch?v=zqUfVqDkf9o)

Criação da função para salvar as conversa em CSV
Importar a biblioteca
```python
import csv
```

Codificar a função para salvar os dados da conversa
```python
# Salvar dados da conversa com o chatbot em arquivos CSV
def salvar(arquivo, conversa: list):
    with open(arquivo, 'a') as f:
        e = csv.writer(f)
        e.writerow(conversa)
```
Após isso, basta chamar a função dentro do handler

```python
# Inicia a conversa
@bot.message_handler(regexp=r'ini?ciar')
def start(message):
    salvar('iniciar.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    ...
```

```python
# Faz a saudação e pergunta se quer fazer o download do arquivo
@bot.message_handler(regexp=r'tu?do?|paz|tu?do? bem')
def saudacao_pergunta(message):
    salvar('saudacao.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    ...
```
```python
# Download do arquivo
@bot.message_handler(regexp=r'bora')
def download_do_pdf(message):
    salvar('baixou.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    ...
```
```python
# Mensagem de convencimento
@bot.message_handler(regexp=r'depois|não|nada|não|agora não|não agora|não quero|não quero agora|não,?.?obrigado')
def convencimento(message):
    salvar('naobaixou.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    ...
```
```python
# Finaliza a conversa
@bot.message_handler(regexp=r'tchau|adeus|bye|sair|até mais|vlw|flw|fui|valeu')
def tchau(message):
    salvar('tchau.csv', [message.chat.id, message.from_user.username, message.text, datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")])
    ...
```

Com os arquivos gerados, é possível consultar depois para melhorar o bot e torna-lo mais humanizado e mais esperto