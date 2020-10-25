#! python3

#download_lastest_version_skin_lol.py

#O programa deve, baixar a ultima versao do lol skin, armazenar em uma pasta, descompact-lo e executar para fazer a instalacao.

#TODO:Baixar o arqivo, usuario descide aonde ele vai ser armazenado.
#TODO Usuario mostra aonde esta o arquivo e ele e descompactado.
#TODO: cxfreeze download_lastest_version_skin_lol.py --target-dir Skin-Lol-Executable

import requests, bs4, zipfile, os, shutil
#Imports necessarios.

os.makedirs('Lol Skin', exist_ok=True)
#Cria um diretorio na area de trabalho atual chamado 'Lol Skin'
object_response_requests_get = requests.get('http://leagueskin.net/p/download-mod-skin-2020-chn')
#Entra no site onde contem a tag do download.
print('Downloading Page... http://leagueskin.net/p/download-mod-skin-2020-chn')
#Exibe que esta baixando o arquivo.
try:
    object_response_requests_get.raise_for_status()
    #Verifica se possui algum erro de resposta do servidor.
    lol_skin_soup = bs4.BeautifulSoup(object_response_requests_get.text, features="html.parser")
    #Baixa a pagina toda do site do lol skin.
    Link_download = lol_skin_soup.select('a')
    #Procura pelas tags 'a' da pagina.
    for Download in range(len(Link_download)):
        #Depois de selecionar apenas as tags 'a', nos vamos passando uma por uma, ate chegar na que possui o final .zip.
        Link = Link_download[Download].get('href')
        #Procuramos por todos os links atrelados a 'href'
        if Link.endswith('.zip'):
            os.chdir(r'.\\Lol Skin')
            object_response_requests_get = requests.get(Link)
            #Se o link de href encontrado possui .zip, nos o baixamos, ele que o arquivo do lol skin.
            print('Downloading... %s' %Link)
            #Exibe que esta baixando o arquivo.
            object_lol_skin_file = open('Lol Skin.zip', 'wb')
            for Parte in object_response_requests_get.iter_content(100000):
                object_lol_skin_file.write(Parte)
            object_lol_skin_file.close()
    object_lol_skin = zipfile.ZipFile('Lol Skin.zip')
    object_lol_skin.extractall('Lol Skin Extract')
    os.chdir(r'.\\Lol Skin Extract')
    for filename in os.listdir():
    #Verificamos todos os arquivos, e qual terminar com .exe, devera ser executado.
        if filename.endswith('.exe'):
            os.startfile(filename)
            break
        #os.starfile executa um arquivo. Sendo seu argumento o path ate o arquivo.
    object_lol_skin.close()
    #Fecha o objeto do skin lol.
except Exception as error:
        #Se possui algum erro na resposta do servidor ele devera exibir a mensagem de erro aqui.
        print('Error: %s' %error)