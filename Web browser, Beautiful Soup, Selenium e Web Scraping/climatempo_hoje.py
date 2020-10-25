#! python3

#climatempo_hoje.py

#O programa pega o a maxima e a minima de hoje.

#TODO:

import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.climatempo.com.br/')
#Baxai o HTML da pagina.

print(type(html.text))
#A diferenca do .content para o .text e o tipo da classe o content e do tipo Bytes e o Text e do tipo string.
#Porem ambos retornam o HTML da pagina.

soup = BeautifulSoup(html.content, 'html.parser')
#Aqui nos nao precisamos usar o prefixo 'bs4' porque nos importamos da menira from bs4 import BeuatifulSoup, que faz com que ele importe
#apenas um funcao do modulo e a gente nao precise usar o prefixo bs4.
#O html.parser serve para o mostrar error na chamada.

#print(soup.prettify())
#O metodo prettify atribulado ao valor do retorno de BeautifulSoup faz uma apresentacao 'bonita e organizada'.

hoje_temp_day = soup.find_all("span", class_="_block _margin-b-5 -bold -dark-blue")
hoje_temp_temp = soup.find_all("span", class_="_block _margin-b-5 -gray")
#O metodo find encontra uma linha HTML especifica.
#O metodo find_all entra todas as ocrrencias desta classe, tag e elemento.

print(type(hoje_temp_day), type(hoje_temp_temp))
#E uma tag, ou seja, uma linha do HTML inteiro.

for Dias in range(len(hoje_temp_day)):
    print(hoje_temp_day[Dias].string, end=' - ')
    #O metodo string retira o texto dentre as tags e elementos HTML.
    print(hoje_temp_temp[Dias].string)
    #O metodo string retira o texto dentre as tags e elementos HTML.

#Essas propriedades dão nomes aos elementos HTML, e os tornam mais fáceis de interagir quando estamos 
#fazendo o scraping. Cada elemento pode ter várias classes, e uma classe pode ser compartilhada entre elementos.
#Cada elemento pode ter apenas um  id, e um id pode aparecer somente uma vez na página.