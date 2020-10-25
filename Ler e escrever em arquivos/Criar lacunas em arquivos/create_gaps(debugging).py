#! python3

#create_gaps(debugging).py

#A ideia do programa e o usuario escolher um arquivo e criar um lacunas dentre varios aruivos numerados
#de forma ordenada.

#TODO: Fazer debbuing do programa para ver se tudo esta funcionando como desejado.

import random, os, shutil, re, string

path = input('Digite a origem completo da pasta: ')
path = os.path.abspath(path)
os.chdir(path)
print('Diretorio de trabalho atual: ' + str(os.path.abspath(path)))
print('Escolha um numero de 1 a %s' %len(os.listdir(path)))
prefixo = input('Digite o numero do prefixo que deseja abrir uma lacuna: ')

prefix_numbers = re.compile(r'''^(.*?)
(\d\d|\d)
(_)?
''', re.VERBOSE)

for file in os.listdir(path):
    object_match_file = prefix_numbers.search(file)

    if object_match_file == None:
        continue

    if object_match_file.group(2) == prefixo:
        text = object_match_file.group(1)
        barra = object_match_file.group(3)
        
        renamed_file = text + '_' + '.txt'
        renamed_file = os.path.join(os.path.abspath(path), renamed_file)

        file = os.path.join(os.path.abspath(path), file)

        object_file_open = open(os.path.join(os.path.abspath(path), file), 'w')
        object_file_open.write(renamed_file)
        object_file_open.close()

        os.rename(file, renamed_file)
        print('Renaming %s to %s ...' %(file, renamed_file))