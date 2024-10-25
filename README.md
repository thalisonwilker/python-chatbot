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

