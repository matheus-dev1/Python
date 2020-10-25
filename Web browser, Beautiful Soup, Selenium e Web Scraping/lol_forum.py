#! python3

#lol_forum.py

#Nos extraimos os texto de determinado pergunta feita no forum do lol por algum usuario.

#TODO:

import requests, bs4
#Imports necessarios

main_url = input("Coloque aqui a URL do forum de League of Legends que deseja extrair: ")
#Exemplo: https://forums.comunidades.riotgames.com/t5/Outros-Assuntos-de-LoL/Que-rank-vcs-pegaram-na-MD10/m-p/905162
page = requests.get(main_url)
soup = bs4.BeautifulSoup(page.content, 'html.parser')
forum_topics = soup.find_all(class_="lia-quilt lia-quilt-forum-message lia-quilt-layout-forum-topic-message-support")
for item in forum_topics:
    titulo = item.find(class_="lia-message-body-content").get_text()
    texto = item.find(class_="lia-message-subject lia-component-message-view-widget-subject").get_text()
    print(titulo)
    print(texto)