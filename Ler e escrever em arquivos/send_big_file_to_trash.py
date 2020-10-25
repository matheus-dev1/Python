#! python3

#send_big_file_to_trash.py

#O programa deve receber um path do usuario e deve pesquisar no path passado se possui algum arquivo 
#maior que 100MB ou seja, 100000000 Bytes, e no final devemos transferir o arquivo para a lixeira.

# TODO: Receber o path do usuario
# TODO: Criar um looping para passar por todas as pastas, sub pastas e arquivos do path passado
# TODO: E em cada passada de arquivo verificar se possui algum arquivo com mais de 100000000 Bytes
# se possui ele sera enviado para lixeira, se nao o looping continuara ate passa por todas as pastas.

import os, shutil, send2trash

path = input('Digite a origem completo da pasta: ')
path = os.path.abspath(path)
print(path)
#100000000 Bytes

for nomePasta, subPastas, nomeArquivo in os.walk(path):
    for arquivo_nome in nomeArquivo:
        os.chdir(path)
        if os.path.getsize(arquivo_nome) >= 100000000:
            #Para o os.getsize() a nossa diretorio de trabalho atual (CWD) tem que esta na pasta com a 
            #funcao os.chdir()
            print('Renaming %s to %s ...' %(arquivo_nome, 'Recycle bin'))
            send2trash.send2trash(arquivo_nome)
        else:
            continue