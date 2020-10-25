#! python3

#beautiful_soup_guide.py

#Um pouco sobre beautiful soup

#TODO:

from bs4 import BeautifulSoup
#Aqui nos importantos apenas a funcao BeautifulSoup do bs4
import requests
#Imports necessarios

page = requests.get('http://dataquestio.github.io/web-scraping-pages/simple.html')
#Baixamos a pagina e armazenamos em 'page'.

soup = BeautifulSoup(page.content, 'html.parser')
#Criamos um objeto beautiful soup da pagina baixada.
#O html.parser serve para nao exibir algum erro referente a pagina baixada.

print(soup.prettify(), '\n')
#Aqui nos iremos exibir o dodigo bixado e posteriormente retornado como objeto soup e o metodo prettify ira exibir
#o codigo de forma estruturada.

print(list(soup.children), '\n')
#Aqui nos iremos exibir uma lista das tags filhas do codigo.
#child (filha): Uma tag child é uma tag dentro de outra tag. Então as tags “p” acima são filhas da tag body.
#parent (pai): Uma tag parent é uma tag que tem outras tags dentro. Acima, a tag html é pai de head e body.
#sibling (irmãos): uma tag sibling é aquela que está aninhada dentro do mesmo pai que outra tag. 
#Por exemplo: head e body são irmãs, pois ambas estão dentro da tag html. Ambas as tags “p” são irmãs, pois estão dentro de body.

for item in list(soup.children):
    #[print(type(item)) for item in list(soup.children)]
    print(type(item))
    #Aqui nos iremos exibir cada tipo de cada objeto encontrado na lista do arquivo HTML.
    #O primeiro (1) é o objeto Doctype, que contém informações sobre o tipo de documento.
    #O segundo (2) é o NavigableString, que representa o texto encontrado no documento HTML.
    #O item final (3) é um objeto Tag, que contém outras tags aninhadas.
print('\n')

html = list(soup.children)[2]
#Como soup.children sera uma lista, nos iremos pegar o terceiro indice que contem todas as tags html.
#O retorno sera uma lista de tags tendo diversos indices.
#OBS: O indice tem que estar no lado de fora da funcao 'list'.

print(list(html.children), '\n')
#AQui nos exibimos a lista de indices contendo todas as tags do arquivo html.

body = list(html.children)[3]
#Aqui nos iremos passar apenas o conteudo da tag body que esta armazenado na possicao [3] que e a quarta posicao (4).

print(list(body.children), '\n')
#AQui nos iremos exibir uma lista dos valores da tag Body do arquivo html baixado.

text_p_body = list(body.children)[1]
#Como tinha uma lista de indices dentro das tags body na posicao 2, ou [1] nos temos um texto, e ele que nos buscamos.

print(text_p_body)
#Aqui esta o texto armazenado em text_p_body
 
all_p = soup.find_all('p')
#Pegamos o objeto soup da pagina baixada e usamos nela o metodo find_all para encontrar todas as tags do argumento passado.
#Obs: Ele retornar em forma de lista.

print(all_p)
#Tags obtidas pelo metodo find_all

all_p = soup.find_all('p')[0].getText()
#Aqui nos vamos pegar apenas a primeira ocorrencia de uma tag 'p' no arquivo html baixado e depois disso usamos o metodo 
#getText referente ao retorno da lista da tag 'p' e retiramos o texto dentre a tag, entao o retorno sera uma stering.
#Obs: Podemos tambem usado o metodo .find() que acha o primeira tag que ocorrer no arquivo html baixado.
#Exemplo soup.find('p').getText()

print(all_p, '\n')
#Apenas o texto de 'p'.

page2 = requests.get('http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html')

soup2 = BeautifulSoup(page2.content, 'html.parser')

all_p_class = soup2.find_all('p', class_="outer-text")
#Aqui nos buscamos por todas os elementos CSS que possui uma tag 'p' e que dentro dela possua uma classe que tenha o nome
#igual ou que contem outer-text e pode ter um pouco mais como nesta classe: class="outer-text first-item"

print(all_p_class, '\n\n')
#Exibir a list a de tags obtidas.

id_second = soup2.find_all(id="second")
#Obs: O getText() funciona apenas com um unico elemento.

print(id_second, '\n\n')
#Exibir a list a de tags obtidas.

#p a: Encontra todas as tags a dentro de uma tag p;
#body p a: Encontra as tags a dentro de uma tag p dentro da tag body;
#html body: Encontra todas as tags body dentro de uma tag html;
#p.outer-text: Encontra todas as tags p com uma classe outer-text;
#p#first: Encontra todas as tags p com um id first;
#body p.outer-text: Encontra quaisquer tags p com uma classe outer-text dentro de uma tag body.

div_p = soup2.select('div p')
#Queremos encontrar todas as tags 'p' que estao dentro de uma tag 'div'.

print(div_p, '\n\n')
#Exibir a list a de tags obtidas.