import spacy

nlp = spacy.load('pt_core_news_sm')

# txt1 = nlp( u"Eu estou aprendendo a utilizar chatbots.")
# txt2 = nlp( u"O Canal do YouTube do professor 'Cláudio Bonel' está chegando a 11.000 inscritos.")

txt3 = input("Como posso te ajudar hoje? ")

txt3 = nlp(txt3)

texto_comparativo = nlp("conhecimento")

for token in txt3:
    similaridade = round( (token.similarity(texto_comparativo) * 100), 2)

    if(similaridade == 100):
        print( f"A palavra {token.text} é {similaridade}% similar ao texto conhecimento " )
    elif(similaridade >= 39 and similaridade <= 99):
        pergunta_similaridade = input("Você quis dizer conhecimento? ")
        if(pergunta_similaridade == "sim"):
            print( f"A palavra {token.text} é {similaridade}% similar ao texto conhecimento " )
        else:
            print( f"Favor refaça sua solicitação " )