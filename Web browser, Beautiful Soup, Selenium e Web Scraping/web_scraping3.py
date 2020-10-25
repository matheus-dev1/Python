#! python3

#O programa e a terceira parte de exemplos de web scraping

#web_scraping3.py

#TODO:

import requests, bs4, os
#Imports necessarios.

object_response_requests = requests.get('http://nostarch.com')
#Obtendo o codigo fonte da pagina http://nostarch.com

print(type(object_response_requests))

try:
    object_response_requests.raise_for_status()
    #Verificando se nao possui erros na resposta do servidor.
    object_file = open('Nostarch.html', 'wb')
    #Criando/abrindo o arquivo Nostarch.html em forma de escrita binaria.
    for parte in object_response_requests.iter_content(100000):
        #Excreve 10000 bytes por looping.
        object_file.write(parte)
        #Escreve o conteudo do looping no arquivo.
    object_file.close()
    #Fecha o arquivo.
except Exception as error:
    #Caso se um erro armazene o erro na variavel "error"
    print('Error: %s' %error)
    #Exibir erro

#print(object_response_requests.text)                       #CODIGO-FONTE
#EXibe todo o codigo fonte do arquivo no console.

print('Quantidade de caracteres do arquivo: ', len(object_response_requests.text), '\n')
#Exibe a quantidade de caractere em que o codigo fonte desta pagina possui.

object_beautiful_soup = bs4.BeautifulSoup(object_response_requests.text, features="html.parser") #SITE.
#O retorno de bs4.BeautifulSoup e de uma string de todo codifo fonte do arquivo html, porem ele vai estar com o tipo bs4.BeautifulSoup
#o que da possibilidade de usar funcoes de BeautifulSoup nesta string, para encontrar dados que a gente queira dentro do html.

#print(object_beautiful_soup)                               #CODIGO-FONTE
#Exibe todo o codigo fonte html.

print('Tipo da classe do site:', type(object_beautiful_soup))
#Printa o tipo da classe desta variavel.
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

Exemplo = open('Exemplo.html')
#Abri o arquivo Exemplo.html em modo de leitura.

Exemplo = bs4.BeautifulSoup(Exemplo.read(), features="html.parser") #ARQUIVO.
#Pegar todo o conteudo do arquivo Exemplo.html, armazenar na variavel Exemplo e transforma-la em uma classe do tipo BeautifulSoup.

print('Tipo da classe do arquivo:', type(Exemplo), "\n")
#Exibit o tipo da classe do arquivo Exemplo.html.

#Seletor passado ao método select()  | Corresponde a...
#soup.select('div')                  | Todos os elementos de nome <div>.
#soup.select('#author')              | O elemento com um atributo id igual a author. (ou qual for o nome do id)
#soup.select('.notice')              | Todos os elementos que utilizem um atributo class de CSS chamado notice.
#                                    | .notice e o atributo dentro do elemento class
#soup.select('div span')             | Todos os elementos de nome <span> que estejam em um elemento chamado <div>.
#soup.select('div > span')           | Todos os elementos de nome <span> que estejam diretamente em um elemento chamado <div>,
#                                    | sem que haja outros elementos intermediários.
#soup.select('input[name]')          | Todos os elementos de nome <input> que tenham um atributo name com qualquer valor.
#soup.select('input[type="button"]') | Todos os elementos de nome <input> que tenham um atributo chamado type com o valor button.

Elementos = Exemplo.select('#author')
#No arquivo Exemplo.HTML posusi uma linha aonde tem o id autor, Exemplo.selct('#author') vai nos retornar a linha inteira aonde esta 
#o #author. E nos armazenaremos em "Elementos".
#Retornar uma lista de objetos tag.

print("Lista das linhas obtidas pelo metodo .select():", Elementos)
#Exibir a linha inteira de #author.
#Exibe todo o conteudo retornado pelo .select().

print("Tipo da classe do retorno de .select():", type(Elementos))
#Exibe o tipo da classe da variavel elemento.
#A classe <class 'bs4.element.ResultSet'> significa todo o retorno de .select()

print("Quantidade de linhas do retorno do metodo .select():", len(Elementos))
#Exibimos a quantidade de linhas que retornamos da funcao .select()
#A gente possui apenas uma linha, entao temos apenas um valor na lista de tags.

print("Tipo da classe da lista de tags na possivel 0: ", type(Elementos[0]))
#Tipo da classe da variavel elemento na possisao 0.
#A classe <class 'bs4.element.Tag'> significa que e uma tag.

print("Texto do elemento 0:", Elementos[0].getText())
#Obter o texto de Elementos na possicao 0.
#Retornara apenas o texto dentro da tag.

print("Elemento String:", str(Elementos[0]))
#Passar a funcao strin dentro do elemtento faz ele retornar uma string com as tags de abertura e fechamento do texto do elemento.

print("Dicionario do elemento 0:", Elementos[0].attrs, '\n')
#Retonar um dicionario do elemento 0 do texto da Variavel Elementos.
#Como nos buscamos "author" e ele esta assiciado a uma "id=" entao "id=" sera a chave e "author" sera o valor.
#Atributos HTML em forma de dicionarios.
#attrs nos fornece um dicionário com o atributo 'id' do elemento e o valor desse atributo, ou seja, 'author'.
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#
ElementosP = Exemplo.select('a')

for Text in range(len(ElementosP)):
    print(ElementosP[Text].getText(), "-", Text)
print()

for Text in range(len(ElementosP)):
    print(str(ElementosP[Text]), '-', Text)
print()

for Text in range(len(ElementosP)):
    if ElementosP[Text].attrs == {}:
        print("Dicionario Vazio!")
    else:
        print(ElementosP[Text].attrs, '-', Text)
print()
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||#

SecondP = Exemplo.select('p')

for Text in range(len(SecondP)):
    print(SecondP[Text].attrs)
    #Dicionario de todas as tags <p> <\p>
    #class = slogan
    #{'class': ['slogan']}
    #Todos os atributos de um objeto Tag.
print()

for Text in range(len(SecondP)):
    print(SecondP[Text].get('class'))
    #Passar o nome de atributo 'class' para get() faz o valor do atributo, ou seja, 'slogan', ser retornado.
print()

for Text in range(len(SecondP)):
    print(SecondP[Text].get('Elemento_nao_existente') == None)
    #Buscar elemento que nao existe retorna None
print()