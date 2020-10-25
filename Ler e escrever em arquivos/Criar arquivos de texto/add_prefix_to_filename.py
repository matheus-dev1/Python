#! python3

#add_prefix_to_filename

#O programa deve adicionar um prefixo no inicio do nome de um arquivo. O prefixo e definido pelo usuario.

# TODO: Criar a pasta e mudar o diretorio detrabalho atual para a pasta criada. - OK
# TODO: Criar um input para o usuario digitar a quantidade de arquivo que ele deseja criar.
# TODO: Criar um input para o usuario digitar seu prefixo para adicionar ao arquivo.
# TODO: Criar um input para o usuario digitar a quantiade de caracteres aleatorios ele queira que o nome do 
#arquivo componha.
# TODO: Criar um looping for para que sera criada um numero de arquivo a serem renomeados definido pelo usuario
# TODO: Concatenar o prefixo digitado pelo usuario + o nome original do arquivo.
# TODO: Alterar o nome do arquivo.
# TODO: Exibir a mudando do nome do arquivo.

import random, string, os, shutil
#Imports necessarios para executar o programa.

try:
    print(os.mkdir('Prefix'))
    #Tentar criar a pasta "Dates", caso ja exista execute a excecao.
except FileExistsError:
    #Caso a pasta ja exista apenas de um print na tela.
    print('Diretorio ja criado.')
    #Exiba esta mensagem.

os.chdir('C:\Matheus\Study\IT\Python\Criar arquivos de texto\Prefix')
#Mudando o diretorio de trabalho.

print('Diretorio de trabalho atual: ' + str(os.path.abspath('.')))
#Exibindo o diretorio de trabalho atual.

qtd_files = int(input('Digite a quantiade de arquivo que deve ser criados: '))
#Variavel com a quantiade de arquivo de devem ser criado.

prefixo = input('Digite um prefixo a ser adicionado no inicio do arquivo: ')
#Variavel que defino qual o nome do prefixo que devera ser adicionado ao nome do arquivo.

qtd_caracteres = int(input('Digite a quantidade de letras que o nome do arquivo deve conter: '))
#Quantidade de caracteres que o programa deve conter
#Obs: isso e o nome do arquivo sem o prefixo.

for files in range(qtd_files):
    #Criar a quantiade de arquivos definida pelo usuario.
    filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=qtd_caracteres)) + '.txt'
    #O import de string contem diversas sequencias de caracteres comuns ASCII.
    #string.ascii_uppercase e uma lista de caracteres de A-A de forma maiuscula.
    #string.digits e uma lista de numeros de 1 a 9.
    #random.choice() e uma funcao que no seu primeiro argumento recebe uma string e o segundo
    #recebe a quantidade.
    #de caractere que ele deve retonar de forma aleatoria da string do primeiro argumento.
    #k = qtd_caracateres e a quantidade de caractere que o random.choice deve retornar.
    #o ''.join() retonar um string da lista de random.choice().
    id_file = open(os.path.join(os.path.abspath('.'), filename), 'w')
    #Abrir/ criar o arquivo em modo de leitura.
    id_file.write(filename)
    #Escrever o proprio nome do aruqivo dentro do aruivo de texto.
    id_file.close()
    #Fechar o arquivo.

for files in os.listdir('.'):
    #Passar por todos os arquivos.
    renamed_file = prefixo + files
    #Concatena o prefixo + o nome do arquivo.
    renamed_file = os.path.join(os.path.abspath('.'), renamed_file)
    #Concatena o caminho do novo nome do arquivo.
    files = os.path.join(os.path.abspath('.'), files)
    #Concatenar o caminho do arquivo.
    shutil.move(files ,renamed_file)
    #Mudar o nome do arquivo.
    print('Renaming "%s" to "%s"...' % (files, renamed_file))
    #Exibir a mudanca de nome do arquivo.