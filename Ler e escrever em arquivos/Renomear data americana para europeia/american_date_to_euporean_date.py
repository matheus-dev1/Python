#! python3

#american_date_to_euporean_date

#Renomeia os nomes de arquivo com formato de data MM-DD-AAAA em estilo americano para
#o formato DD-MM-AAAA em estilo europeu.

#Em projetos com bastanets funcoes, seu os TODO's. Eles ajudarao muito a saber
#o que e pra fazer, quando fazer e ate como fazer eliminando o pensanto de ter que fazer aquilo.

# TODO: Criar arquivos com nomes que repretam a regex do programa.
# TODO: Criarum regex para encontra data do estilo americano em arquivos.
# TODO: Percorre os arquivos do diretório de trabalho com um loop.
# TODO: Ignora os arquivos que não tenham uma data.
# TODO: Obtém as diferentes partes do nome do arquivo.
# TODO: Compõe o nome do arquivo em estilo europeu.
# TODO: Obtém os paths absolutos completos dos arquivos.
# TODO: Renomeia os arquivos.

import os, shutil, re, random
#Funcoes necessaria para a execucao do programa. 

try:
    print(os.mkdir('.\\Dates'))
    #Tentar criar a pasta "Dates", caso ja exista execute a excecao.
except FileExistsError:
    #Caso a pasta ja exista apenas de um print na tela.
    print('Diretorio ja criado.')

print(os.chdir('.\\Dates'))
#Mudar o diretorio de trabalho atual para a pasta Dates.

File = int(input('Digite a quantidade de arquivos a serem criados: '))

for Dates in range(File):
    #Sera criado um numero de arquivo determinado pelo usuario.
    Date_name = str(random.randint(1, 12)) + '-' + str(random.randint(1, 31)) + '-' + str(random.randint(1800, 2020)) + '.txt'
    #Aqui nos vamos criar o nome do arquivo de forma invidual.
    Date_file = open(os.path.join('C:\\Matheus\\Study\\IT\\Python\\Dates', Date_name), 'w')
    #Vamos abrir o arquivo e escrever o numero do arquivo na ordem da sua criacao.
    Date_file.write('Arquivo numero :' + str(Dates))
    #Escrever o numero de criacao deste arquivo.
    Date_file.close()
    #Fecha o arquivo.

#Quando voce for trabalhar com alteracoes, voce vai trabalhar com grupos de nomes.
regex_american_date = re.compile(r"""^(.*?)#Texto antes da data. Obrigatoriamente pode ser 
#qualquer caractere que inicie com o nome do arquivo em qualquer quantidade. Grupo 1
((0|1)?\d)- #Mes. Para o mes temos 0, 1 ou nenhum valor, de forma opcional
#e obrigatoriamente tem que ter mais um numero de 1 a 9 e um traco fora do grupo porem obrigatorio. Grupo 2
((0|1|2|3)?\d)- #Dia. Para o dia temos 0, 1, 2, 3 ou nenhum valor de forma opcinal
#e de forma obrigatoria qualquer numero de 1 a 9 e um traco fora do grupo sendo obrigatorio. Grupo 3 
((18|19|20)\d\d) #Ano. Para o ano temos os dois primeiro valores
#obrigatorios sendo 18, 19 ou 20 e os dois ultimos qualquer numero de 00 a 99. Grupo 4
(.*?)$ #Texto depois da data. Obrigatoriamente tem que ser no final
#do arquivo e pode ser qualquer caractere de qualquer quantidade. Grupo 5
""", re.VERBOSE)

#datePattern = re.compile(r"""^(1)
#(2 (3) )-
#(4 (5) )-
#(6 (7) )
#(8)$
#""", re.VERBOSE)
#Este comentario acima e como devemos interpretar os grupos na regex, podendo ter grupos dentro de grupos
#e se tiver um grupo dentro de outro grupo e voce  for por exemplo exibir o grupo que possui um grupo
#ele vai exibir os dois grupos.

#regex_american_date #Esta e a regex da data americana
#american_date_file #Este aqui e o nome do arquivo em cada looping.
#object_match_american_date #Este aqui e o objeto match do arquivo com a data americana
#european_date #A string com o estilo europeio de data.

for american_date_file in os.listdir('.'):
    #os.listdir('.') vai retornar uma lista de nomes de arquivo do diretorio de trabalho atual deste arquivo.
    object_match_american_date = regex_american_date.search(american_date_file)
    if object_match_american_date == None:
    #No regex, caso ele nao encontre a string que corresponda a regex ele ira retornar None.
    #E no nosso caso se for none ele retorna ao inicio do looping, porem no proximo looping.
        continue
        #A instrução continue fará o restante do loop ser ignorado e prosseguirá para o próximo nome de arquivo
        #Volta ao inicio do looping no proximo valor.
    else:
        #Se ele encontrar um arquivo que corresponde a regex da data americana ele executa este bloco de funcoes
        TextPart1 = object_match_american_date.group(1)
        #No TextPart1 sera armazenado toda a string do grupo 1 do arquivo, ou seja, todo o texto antes da data.
        MonthPart = object_match_american_date.group(2)
        #No MonthPart sera armazenado toda a string do grupo 2 do arquivo, ou seja, o mes.
        #O grupo 2 engloba os grupos 2 e 3.
        DayPart = object_match_american_date.group(4)
        #No DayPart sera armazenado toda a string do grupo 4 do arquivo, ou seja, o dia.
        #O grupo 4 engloba os grupos 4 e 5.
        YearPart = object_match_american_date.group(6)
        #No YearPasrt sera armazenado toda a string do grupo 6 do arquivo, ou seja, o ano.
        #O grupo 6 engloba os gtrupos 6 e 7.
        TextPart2 = object_match_american_date.group(8)
        #No TextPart2 sera armazenado toda a string do grupo 8, ou seja, todo o texto depois da data.
        european_date = TextPart1 + DayPart + '-' + MonthPart + '-' + YearPart + TextPart2
        #A Variavel europena_date armazena as parte da data americana extraida do arquivo atual no looping
        #e armazenada em variaveis com seus respectivos nomes e sao concatenada de forma que sera uma
        #data do estilo europeu.

        american_date_file = os.path.join(os.path.abspath('.'), american_date_file)
        european_date = os.path.join(os.path.abspath('.'), european_date)
        #Vai juntar todo o caminho ate o arquivo mais o nome do arquivo, tranformando o path ate o arquivo.

    shutil.move(american_date_file, european_date)
    #Arquivo vamo alterar o nome do arquivo com a data estilo americano para o estilo europeu
    print('Renaming "%s" to "%s"...' % (american_date_file), os.path.basename(european_date))
    #No final vamo exibir a mudanca.