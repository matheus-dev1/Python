#! python3

#open_browser.py

#O promava deve receber uma url do segundo argumento na chamada no programa e abrir um navegador nesta pagina.

#TODO:

import webbrowser, sys, requests
#Imports importantes.

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
#O primeiro argumento e o navegador em que nos vamos querer que o modulo webbrowser com o metodo .get() abram.
#o segundo argumento e vazio.
#O tervceiro argumento e qual o caminho em que em que o arquivo do browser se encontrar.
#Aqui nos registramos o navegador firefox, e que todo ulr em que nos abirmos deve ser a partir deste navegador.
#Nao retorna nada.

if len(sys.argv) < 2:
    print('Para abrir o navegador digite a URL!')
    #Caso o usuario nao digite um segundo argumento, ele exibe esta mensagem apenas.
else:
    url = sys.argv[1]
    webbrowser.get('firefox').open(sys.argv[1])
    #Com o metodo get, e o valor igual ao navegador registrado em webbroser.register, o navegador sempre abrira o mesmo navegador.
    #Caso possua mais de mais de 1 argumento na chamada do programa, ele sera aberto, caso seja uma URL.