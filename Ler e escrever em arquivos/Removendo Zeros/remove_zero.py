#! python3

#remove_zero.py

#O programa deve remover os 'zeros' dos arquivos.

#TODO: Usar a lista de strin para remover os zeros, e em cada looping reformular a string.

import random, os, shutil, re, string
#Imports necessarios.

qtd_files = int(input('Digite a quantiade de arquivo que devem ser criados: '))
#Variavel que solicita ao usuario a quantidade de arquivo que ele deseja criar.

try:
    os.mkdir('.\\Zeros')
    #Criar uma pasta chamada Zeros
except FileExistsError:
    print('Diretorio ja criado.')
    #Caso o diretorio ja tenha sido criado.

os.chdir('.\\Zeros')
#Mudar o diretorio de trabalho atual para Zeros.

print('Diretorio de trabalho atual: ' + str(os.path.abspath('.')))
#Exibir o diretorio de trabalho atual ao usuario.

for files in range(qtd_files):
    #Quantiade de arquivo que vao ser criados.
    Text1 = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 20)))
    Text2 = ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 20)))
    Date_string = str(Text1) + str('0' * random.randint(5, 10)) + str(''.join(random.choices(string.digits, k=random.randint(5, 20)))) + str(Text2) + '.txt'
    Date_file = open(os.path.join(os.path.abspath('.'), Date_string), 'w')
    #Abrimos ou criamos o arquivo em modo leitura.
    Date_file.write(Date_string)
    #Escrevemos no arquivo o proprio nome do arquivo dentro dele.
    Date_file.close()
    #Fechamos o arquivo.

#file = Arquivo sem alteradao
#new_name_file = Arquivo com alteracao

for file in os.listdir('.'):
    new_name_file = ''
    for carac in file:
        if carac != '0':
            new_name_file += carac

    file = os.path.join(os.path.abspath('.'), file)
    new_name_file = os.path.join(os.path.abspath('.'), new_name_file)

    shutil.move(file, new_name_file)
    print('Renaming %s to %s ...' %(os.path.basename(file), os.path.basename(new_name_file)))