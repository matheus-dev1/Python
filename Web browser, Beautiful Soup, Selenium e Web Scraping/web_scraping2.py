#! python3

#O programa e a segunda parte de exemplos de web scraping.

#web_scraping2.py

#TODO:

import requests
#Imports necessarios

object_response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#Neste ponto se a resposta do site ocorreu tudo bem, o arquivo ja foi baixado, agora nos temos que armazena-lo.

try:
    object_response.raise_for_status()
    #Verifica se possui algum erro na resposta do download do site.
    file = open('Romeo and Juliet.txt', 'wb')
    #wb = write binary (EScrita binaria) e como devem ser escrito paginas web em arquivos de texto.
    for parte in object_response.iter_content(100000):#bytes por interacao.
        #O valor passado como argumento ao metodo iter.content() e a quantidade de bytes que ele escreve por interacao do looping
        #isso serve para que o programa seja escrito de forma gradual e fazendo com que o computador nao fique pesado.
        file.write(parte)
        #VAi esquevendo cada parte, da forma igual como esta na web.
    file.close()
    #Fecha o arquivo.
except Exception as error:
    #Caso se um erro armazene o erro na variavel "error"
    print('Error: %s' %error)
    #Exibir erro.