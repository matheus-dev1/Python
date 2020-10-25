#! python3

#rename_files2(debbugin).py

#O programa renomeia todos os arquivos de forman numerada de uma pasta.

#TODO: Fazer debbugin do arquivo para concertar erros

import random, os, shutil, re, string
#Imports necessarios.

#qtd_files = int(input('Digite a quantiade de arquivo que devem ser criados: '))
#Variavel que solicita ao usuario a quantidade de arquivo que ele deseja criar.

path = input('Digite a origem completo da pasta: ')
path = os.path.abspath(path)
os.chdir(path)
print('Diretorio de trabalho atual: ' + str(os.path.abspath('.')))
print('Qauntidade de arquivos: %s' %len(os.listdir(path)))
#Mudar o diretorio de trabalho atual para path, o caminho digitado pelo usuario.

create_files = input('Quer criar arquivos? [S/N]: ')
if create_files.lower() == 's':
    qtd_files = int(input('Quantidade de arquivos: '))
    for files in range(qtd_files):
        number = str(files)
        Text = ''.join(random.choices(string.ascii_uppercase, k=5))
        Text = Text + number
        number_text = Text + '.txt'
        print(number_text)
        number_file = open(os.path.join(os.path.abspath('.'), number_text), 'w')
        number_file.write(number_text)
        number_file.close()

prefix_numbers = re.compile(r'''^(.*?)
(\d\d|\d)
''', re.VERBOSE)
#((0|1|2|3|4|5|6|7|8|9)?\d)

number_add = 0
for file in os.listdir(path):
    number_add = number_add + 1

    object_match_file = prefix_numbers.search(file)

    if object_match_file == None:
        continue

    Text = object_match_file.group(1)
    numbers = object_match_file.group(2)

    file_renamed = Text + str(number_add) + '.txt'
    file_renamed = os.path.join(os.path.abspath(path), file_renamed)

    file = os.path.join(os.path.abspath(path), file)

    number_file = open(os.path.join(os.path.abspath(path), file), 'w')
    number_file.write(file)
    number_file.close()

    try:
        os.rename(file, file_renamed)
    except FileExistsError:
        continue
    print('Renaming %s to %s ...' %(file, file_renamed))
        