#! python3

#duplicate_catalog_items_amazom.py

#O programa deve reber os nomes e valores de items de um catalog de um busca no amazon.

#TODO: Nome e preco de produtos da Amazon.

import requests, bs4
#Imports necessarios
main_url = input("Coloque aqui a URL da pesquisa Amazon: ")
#URL Amazon
page = requests.get(main_url)
#Baixar a pagina
soup = bs4.BeautifulSoup(page.content, 'html.parser')
#Tranforma em objeto BeautifulSoup
items_list = soup.find_all('div', class_="a-section a-spacing-medium")
#Capturar o codigo de todos os items.
for item in items_list:
    #Passar item por item.
    try:
        nome_item = item.find('span', class_="a-size-base-plus a-color-base a-text-normal").get_text()
        #Capturar o texto do item atual do looping.
        valor_item = item.find(class_="a-offscreen").get_text()
        #Capturar o valor do item atual do looping.
        print(nome_item, end=' - ')
        #Exibir o nome ao usuario e juntar ao valor na proxima linha.
        print(valor_item)
        #Exibir o valor do item o ao usuario.
        print(nome_item, end=' - ')
        print(valor_item)
        #Repetir este processo.
    except Exception as error:
        print("Produto nao encontrado!")
        #Caso encontrar um erro.