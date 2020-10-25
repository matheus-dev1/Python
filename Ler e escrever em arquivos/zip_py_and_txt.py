#1 python3

#zip_py_and_txt.py

#O programa deve entrar na pasta Python, buscar por todas os arquivos com as extensoes .txt e .py e 
#compactar todos os arquivo que tem essas extensoes.

import os, string, random, zipfile

def backup_py_and_txt(pasta_backup_local):
    pasta_backup_local = os.path.abspath(pasta_backup_local)
    backup_number = 1
    while True:
        pasta_backup_zip = os.path.basename(pasta_backup_local) + '_' + str(backup_number) + '.zip'
        if os.path.exists(pasta_backup_zip) == False:
            #Se nao exisir uma primeira pasta com este nome ele encerra o looping
            break
        backup_number = backup_number + 1
    print('Creating %s...' % (pasta_backup_zip))
    id_pasta_backup_zip = zipfile.ZipFile(pasta_backup_zip, 'w')

    for Pasta, Subpasta, Arquivo in os.walk(pasta_backup_local):
        for Nome_arquivo in Arquivo:
            if Nome_arquivo.endswith('.txt') or Nome_arquivo.endswith('.py'):
                id_pasta_backup_zip.write(os.path.join(Pasta, Nome_arquivo))
            else:
                continue
    print('Done.')
    id_pasta_backup_zip.close()

Pasta_backup = input('Pasta a fazer backup: ')

backup_py_and_txt(Pasta_backup)