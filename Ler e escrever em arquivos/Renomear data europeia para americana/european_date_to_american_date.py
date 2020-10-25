#! python3

#european_date_to_american_date.py

#Renomeia os nomes de arquivo com formato de data DD-MM-AAAA em estilo europeu para
#o formato MM-DD-AAAA em estilo americano.

# TODO: Criar arquivos com nomes que repretam a regex do programa.
# TODO: Criarum regex para encontra data do estilo europeio em arquivos.
# TODO: Percorre os arquivos do diretório de trabalho com um loop.
# TODO: Ignora os arquivos que não tenham uma data.
# TODO: Obtém as diferentes partes do nome do arquivo.
# TODO: Compõe o nome do arquivo em estilo americano.
# TODO: Obtém os paths absolutos completos dos arquivos.
# TODO: Renomeia os arquivos.

import random, os, shutil, re, string
#Imports necessarios.

qtd_files = int(input('Digite a quantiade de arquivo que devem ser criados: '))
#Variavel que solicita ao usuario a quantidade de arquivo que ele deseja criar.

try:
    os.mkdir('.\\Dates2')
    #Criar uma pasta chamada Dates2
except FileExistsError:
    print('Diretorio ja criado.')
    #Caso o diretorio ja tenha sido criado.

os.chdir('.\\Dates2')
#Mudar o diretorio de trabalho atual para Dates2

print('Diretorio de trabalho atual: ' + str(os.path.abspath('.')))
#Exibir o diretorio de trabalho atual ao usuario.

for files in range(qtd_files):
    #Quantiade de arquivo que vao ser criados.
    Text1 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 20)))
    Text2 = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 20)))
    #Criamos um texto aleatorio antes e depois da data.
    Date_string = str(Text1) + ' ' + str(random.randint(1, 31)) + '-' + str(random.randint(1, 12)) + '-' + str(random.randint(1800, 2020)) + ' ' + str(Text2) + '.txt'
    #Assiom criamos uma string que corresponde o nome do arquivo.
    Date_file = open(os.path.join(os.path.abspath('.'), Date_string), 'w')
    #Abrimos ou criamos o arquivo em modo leitura.
    Date_file.write(Date_string)
    #Escrevemos no arquivo o proprio nome do arquivo dentro dele.
    Date_file.close()
    #Fechamos o arquivo.

regex_european_date = re.compile(r'''^(.*?) #Qualquer texto antes da data.
((0|1|2|3)?\d)- #Dias
((0|1)?\d)- #Meses
((18|19|20)\d\d) #Anos
(.*?)$''', re.VERBOSE) #Todo texto depois da data.

for european_data_file in os.listdir('.'):
    #Looping de todos os arquivo do diretorio de trabalho atual. A pasta aonde consta os arquivos.
    object_match_european_data = regex_european_date.search(european_data_file)
    #Procurar o object match no arquivo do looping.
    if object_match_european_data == None:
        continue
        #Caso o o objecto match nao seja encontra, ou seja, a regex nao confere com o nome do arquivo
        #Ele retorna None a instrucao continue e executada, assim fazendo com que o looping volte ao
        #comeco para o proximo valor da lista.
    else:
        Text1 = object_match_european_data.group(1)
        #Texto antes da data.
        Days = object_match_european_data.group(2)
        #Dias
        Month = object_match_european_data.group(4)
        #Meses
        Year = object_match_european_data.group(6)
        #Anos
        Text2 = object_match_european_data.group(8)
        #Texto depois da data
        american_data = Text1 + Month + '-' + Days + '-' + Year + Text2
        #Concatenacao de partes do formato europeio, reorganizado para o formato americano.

        american_data = os.path.join(os.path.abspath('.'), american_data)
        european_data_file = os.path.join(os.path.abspath('.'), european_data_file)
        #Fazer a concatenacao do path ate o arquivo + o nome do arquivo.

        shutil.move(european_data_file, american_data)
        #Renomear do arquivo.
        print('Renaming %s to %s ...' %(os.path.basename(european_data_file), os.path.basename(american_data)))
        #Exibindo a mudanca do texto arquivo com a data estilo europeio para americana.