#! python3

#previsao_tempo.py

#O programa abre uma pesquisa no google como "Previso do tempo" e ele tem a previsao do tempo local.

#TODO:

import webbrowser
#imports necessarios.

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
#Registra abrir o firefox como navegador padrao.

webbrowser.get('firefox').open("https://www.google.com/search?safe=active&client=firefox-b-d&sxsrf=ALeKk01l003cojV \
yiOFOP7xPrBR9sXHikA%3A1597581185098&ei=gSc5X8LSBdvD5OUP_8qR0A8&q=Previs%C3%A3o+do+Tempo&oq=Previs%C3%A3o+do+Tempo&gs \
_lcp=CgZwc3ktYWIQAzIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywEyBQgAEMsBMgUIABDLATIFCAAQywE6BAgjECdQs \
IsKWLCLCmDQjwpoAnAAeACAAeUBiAHHA5IBAzItMpgBAKABAqABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwiCl6bY3Z_rAhXbIbkGHX9lBPoQ4dUDCAs&uact=5")
#Abre o site do google com a previsao do tempo local aonde voce se esta localizado.