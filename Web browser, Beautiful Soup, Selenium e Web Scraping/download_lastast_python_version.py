#! python3

#download_lastast_python_version.py

#O program baixa a ultima versao do python, sempre!

#TODO:URL(SOURCE-PAGE) DO PYTHON AONDE FAZ O DOWNLOAD DO PYTHON NO WINDOWS.

import webbrowser, requests, bs4
#Imports necessarios.

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
#Aqui nos registramos o navegador firefox, e que todo ulr em que nos abirmos deve ser a partir deste navegador.

object_response_python_download = requests.get('https://www.python.org/downloads/')
#Baixa a pagina e armazena o codigo fonte em object_response_python_download

try:
    object_response_python_download.raise_for_status()
    #Verifica se possui erros na resposta do servidor.

    object_response_python_download_soup = bs4.BeautifulSoup(object_response_python_download.text)
    #Transforma a pagina baixada para o tipo BeautifulSoup

    LinkDownaload = object_response_python_download_soup.select('a')
    #Procuramos por todas tags a.
    
    for Windows in range(len(LinkDownaload)):
        #Passa por todos os links encontrados.
        urls = LinkDownaload[Windows].get('href')
        #Filtramos para buscar por todas as href.
        if urls.endswith('.exe') == True:
            print("Opening... %s" %urls)
            #se terminar com .exe sabemos que e io unico download para windows.
            webbrowser.get('firefox').open(urls)
            #E assim abrimos a pagina pra fazer o download.
            
except Exception as error:
    print('Error: %s' %error)
    #Caso ouver um erro na resposta do servidor ele exibira o erro.