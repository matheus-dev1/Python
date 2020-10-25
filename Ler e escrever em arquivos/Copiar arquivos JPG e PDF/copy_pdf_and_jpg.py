#! python3

#copy_pdf_and_jpg.py

#O programa deve receber um path e ele vai passar por todos os cantos da pasta e subpastas ate encontrar 
#arquivos com a extensao .pdf e/ou  .jpg. O usuario vai passar um caminho de destino para estes arquivos.
#e ele deve fazer um copia para uma pasta todos os arquivo que coincide com os finais.

# TODO: Criar duas variaveis: 1. o caminho onde deve procurar arquivos com a extensao .pdf e/ou .jpg
# 2. O path para o destino da copia dos arquivos.
# TODO: 

import os, shutil

#european_data_file = os.path.join(os.path.abspath('.'), european_data_file)
#PDF and JPG
path_origem = input('Digite a origem completo da pasta: ')
path_origem = os.path.abspath(path_origem)
print(path_origem)
#C:\Matheus\Study\IT\Python

path_destino = input('Digite o destino completo da pasta: ')
path_destino = os.path.abspath(path_destino)
print(path_destino)
#C:\Matheus\Study\IT\Python\PDF and JPG

for nomePasta, subPastas, nomeArquivo in os.walk(path_origem):
    for arquivo_nome in nomeArquivo:
        if arquivo_nome.endswith('.pdf') or arquivo_nome.endswith('.jpg') or arquivo_nome.endswith('.jpeg') or arquivo_nome.endswith('.png'):
            os.chdir(path_destino)
            if os.path.exists(arquivo_nome) == True:
                continue
            else:
                path_origem = os.path.join(os.path.abspath(nomePasta), arquivo_nome)
                path_destino = os.path.join(os.path.abspath(path_destino))
                print('Renaming %s to %s ...' %(path_origem, path_destino))
                shutil.copy(path_origem, path_destino)
        else:
            continue