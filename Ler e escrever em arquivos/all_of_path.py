#! python3

#O programa mostra varias funcoes e forma de usar "path" no Windows com Python

#all_of_path

import os, pprint, shelve, namesImport, sys

sys.path.append('C:\\Matheus\\Study\\IT\\change_cwd_example')
#podemos adicionar mais um caminho a lista de pastas aonde o python procura por modulos.

print(sys.path)
#A lista de pastas onde o python procura modulos.

print(os.path.join('usr', 'bin', 'spam'))
#Ele vai criar o caminho correto dependendo o sistema em que voce usa.
#No caso do Windows, ele vai colocar duas barras invertidas, por uma vai escapar a outra, e assim ele ira criar um caminho
#e retonar em forma de String para dependo so Sistema Operacional em que voce usa.

myPythonFiles = ['urls.py', 'marcadores_wiki.py', 'moedas.py']
#Definimos tres arquivos, depois vamos passar por um laco de repeticao FOR.
for PythonFileName in myPythonFiles:
    #Como temos apenas 3 arquivos("Strings que reperesenta os arquivos") vamos pegar um caminho determinado
    #E retonar o caminho mais cada uma dos 3 arquivos.
    #Obs: Olhe que depois de Python nao temos "\" entao ele sera adicionada automaticamente atraves do metodo os.path.join
    #Chamado e depois sera retonar a string certinha para cada sistema operacional em que usamos.
    print(os.path.join('C:\\Matheus\\Study\\IT\\Python', PythonFileName))
    #Aqui vamos exibir o path de cada caminho individualmente.

print('CWD atual: ' + str(os.getcwd()))
#get de obter, cwd e o diretorio de trabalho do arquivo, neste caso o path deste arquivo.

print(os.chdir('C:\\Matheus\\Study\\IT\\change_cwd_example'))
#Me retorna None, porque nao tem nada para retonar apenas efetuar uma alteracao do diretorio aonde o programa esta sendo exeucutado
#"ch" tem o signifcado de MUDAR "dir" tem o significado de DIRETORIO, ou seja, a juncao singnifica MUDAR DIRETORIO.
#change_cwd_examplo e uma pasta, entao o programa esta funcionando dentro daquela pasta.

print('CWD Alterado: ' + str(os.getcwd()))
#Aqui nos exibimos que a alteracao do CWD, ou seja, mostramos aonde esta o CWD deste arquivo esta rodando depois da alteracao.
#change_cwd_example e uma pasta com um arquivo em uso, entao se por exemplo a gente tantar excluir nao da, por que ele esta em uso

print(os.chdir('C:\\ThisFolderDoesntExist'))
###ERRO###Este comentario mostra que, ele apenas altera. Ele nao cria e altera!

print(os.makedirs('C:\\Matheus\\Study\\IT\\make_dir_1\\make_dir_2')) ###Diretorios ja criados###
#Retonar, None, porque essa funcao apenas criar um diretorio nao exibe nada.
#"Make" de cria e "dirs" de diretorios, ou seja, criar diretorios.
#Essa funcao pode cria criar um ou mais diretorios.
#E no caso eu apenas posso criar diretorios dentro do diretorio anteriormente criado.
#Caso o nome do diretorio que voce esta tentando criar ja existir ele dara um erro.

#Path Relativo Exemplo deste arquivo. -  .\\IT\\change_cwd_examplo
#Path Absoluto Exemplo deste arquivo. -  C:\\Matheus\\Study\\IT\\change_cwd_example

print(os.path.abspath('.\\'))
#O ponto (.) quer dizer, ESTE DIRETORIO, ou seja, nos vamos pegar o caminho absoluto deste arquivo.
#Retorno: C:\Matheus\Study\IT\change_cwd_example
#Com esta funcao ele vai exibir o path absoluto deste path relativo que agente colocou como argumento.
#Obs: Como a gente alterou o diretorio de trabalho atual, a gente ele vai exibir no diretior em que este arquivo esta rodando.

print(os.path.abspath('..\\change_cwd_example'))
#Neste caso nos vamos pegar pasta atual aonde esta rodando o arquivo e vamo ate a pasta "pai"/drive-raiz.
#Obs: Como a gente sempre vai comecar desta pasta, por a gente esta rodando atraves deste arquivo, a gente vai sempre comecar pela
#change_cwd_example, entao podemos ou nao usar o caminho aonde comecamos.

print(os.path.abspath('..\\'))
#Dois ponto significa pasta "pai"/pasta-raiz
#Nos paramos em IR, porque ela e a pasta aonde a pasta aonde esta rodando este aquivo esta, no caso, change_cwd_example.

Abs_Rel = input('Descubra se um path e Absoluto ou Relativo: ')
#Se o caminho for True ele me retonar que o caminho e Absoluto.
#Se o caminho for False ele me retonra que o caminho e Relativo.
if os.path.isabs(Abs_Rel) == True:
    print(str(os.path.isabs(Abs_Rel)) + ' - Absoluto')
else:
    print(str(os.path.isabs(Abs_Rel)) + ' - Relativo')

print(os.path.isabs('C:\\Matheus\\Study'))#True
#Obs: um caminho e sempre absoluto, desde que ele comece pelo Drive-Raiz/pasta pai.

print(os.path.isabs('.\\Python\\urls.py'))#False
#Me retorna falso porque, o nosso path comeca na pasta Python e nao na pasta "pai"/Drive Raiz.
#Se o argumento da funcao os.path.isabs() for um path absoluto, ele retornara, True e False para caminho Relativo.

print(os.path.isabs(os.path.abspath('urls.py\\')))#True
print(os.path.isabs(os.path.abspath('.\\')))#True
#Tudo vai gerar True aqui, ate porque nos primeiramente vamos retornar o valor relativo do path que passamos em os.path.abspath
#e ele vai retornar o caminho absoluto a funcao os.path.isabs(), que obviamente vai dar True.

print(os.path.relpath('C:\\Matheus\\Study', 'C:\\'))
#Entao o primeiro argumento o path(caminho), podendo ser ele absoluto ou relativo, e o caminho da onde nos iremos "recortar"
#o caminho, no caso do exemplo acima nos temos um caminho (path) C:\\Matheus\\Study e a gente vai tirar o inicio dele e pegar o que
#tem depois dele, no caso a pasta Matheus.
#Obs: Se início não for especificado, o diretório de trabalho atual (CWD) será usado como path de início.

print(os.path.relpath('.\\Matheus\\Study', 'Matheus'))
#Nao necesariamente temos que comecar pelo drive-raiz/ pasta "pai".

print(os.path.relpath('C:\\Matheus\\Study\\IT', '\\Matheus'))
#Ele vai retonar C:\\Matheus do path passado no primeiro argumento.

print(os.path.relpath('C:\\Matheus\\Study\\IT\\Python\\urls.py', '\\Matheus\\Study'))
#Podemos tambem por exemplo, porgar uma parte do caminho no meio, aonde ele vai remover ate o final.
#Vai remover C:\\Matheus\\Study

print(os.path.relpath('C:\\Matheus\\Study\\IT'))
#Ele me retonar ponto-ponto (..) porque ele vai me nao passamos nada no segundo argumento, entao o segundo argumento fica "oculto"
#ficaria como o segundo argumento fosse o CWD deste arquivo e ficaria mais ou menos assim:
#os.path.relpath('C:\\Matheus\\Study\\IT', 'C:\\Matheus\\Study\\IT\\change_cwd_example')
#O que me resultaria em ponto-ponto (..)
#Basicamente a gente tira mais do tem, essa e a ideia.

print(os.path.relpath('C:\\Matheus\\Study\\IT\\change_cwd_example'))
#Neste caso a gente nao vai passar o segundo argumento a funcao os.path.realpath.
#Se a gente usar apenas um argumento que seria o "path" ele vai considerar de forma oculta o segundo agumento a area de
#trabalho deste arquivo atual entao o se eu escrevo assim:
#os.path.relpath('C:\\Matheus\\Study\\IT\\change_cwd_example, C:\\Matheus\\Study\\IT\\change_cwd_example)
#Ele me retonar um ponto (.) que quer dizer esta pasta aonde este arquivo esta rodando.

print(os.path.relpath('C:\\Matheus\\Study', 'C:\\Program Files (x86)\\Adobe\\Acrobat Reader DC'))
#Caso a gente passa um "inciio" (segundo argumento) que nao exista o "path" (primeiro argumento) ele vai pegar o caminho do
#primeiro argumento e a cada pasta/arquivo do segundo argumento que nao condiz com o primeiro argumento ele vai colocar
#ponto-ponto + barra-barra (..\\) e cada um desses significa que possui um diretorio que nao condiz com "path" (primeiro-argumento)

print(os.path.relpath('C:\\Matheus\\Study\\IT\\Python', 'C:\\Matheus\\Study\\IT\\dfgdbg.py\\asdfsdafsadf'))
#Neste caso nos vamos tirar C:\\Matheus\\Study\\IT e vai sobrar python + os dois arquivos\psatas que nao estao no caminho
#que serao representadas por ..\\

print(os.path.dirname('C:\\Matheus\\Study\\IT'))#Return C:\\Matheus\\Study
#A funcao os.path.dirname() vai me retornar tudo o que vem antes da ultima barra inventida que esta no caminho.
#No caso acima,a sera: C:\\Matheus\\Study que vem antes das duas ultimas barras invertidas.
#Ele vai excluir a ultima barra do path.

print(os.path.basename('C:\\Matheus\\Study\\IT'))#Return IT
#Neste caso ele vai me retonar tudo o que vem depois da ultima barra, no caso o que vem depois da ultima barra e a pasta IT.
#O nome base vem depois da ultima barra em um path.

print(os.path.split('C:\\Matheus\\Study\\IT'))
#Basicamente este split e a juncao do dirname com basename que antes da ultima barra invertida e um valor e depois
#da barra invetida e outro valor e seria o ultimo valor, entao o segundo valor da tupla e o ultimo valor do path
#e o primeiro valor da tupla e tudo antes da ultima barra invertida do path.
#O primeiro valor da tupla retornado pelo os.path.split sera o nome de diretorio do path e o
#segundo argumento e o nome base do path.

print('Com o valor de retorno das funcoes dirname() e basename() - ', end = '')
print((os.path.dirname('C:\\Matheus\\Study\\IT'), os.path.basename('C:\\Matheus\\Study\\IT')))
#Usando os dirname + o basename a gente chega no mesmo resultado do split.
#Podemos tambem usar os valores de retonos da funcoes dirname() e basename() para a gente usar no os.path.slipt().

path1 = 'C:\\Matheus\\Study\\IT'
#Declarando uma variavel para usar no metodo Split com e sem o separador.

print(path1.split())
#Ele retorna o mesmo caminho em forma de lista. Com um unico valor.

print(path1.split(os.path.sep))
#AQui a gente vai criar um lista aonde cada \\ signifaca a separacao de uma valor.
#Entao nao teremos as barras mas teremos os valores separados por elementos da lista.
#Por exemplo, neste caso C:\\Matheus\\Study\\IT nos temos 4 elementos na lista.
#path1 = Variavel aonde esta armazenada a String com o caminho.
#split = Metodo usado em uma valor do tipo string para transformar em lista.
#os.path.sep = Variavel usada em argumentos para criar um elemento na lista para cada "\\"

print(str(os.path.getsize('C:\\Matheus\\Study\\IT\\Python\\Thruly.py')) + ' Bytes')
#Esta funcao vai nos dar o tamanho do arquivo final, no caso o tamanho do arquivo Thruly.py
#Obs: Temos que dar o caminho absoluto para que ele encontre o caminho do tamanho do arquivo.

print(str(os.path.getsize('C:\\Matheus\\Study\\IT\\Python\\regex.py')) + ' Bytes')
#Tamanho do arquivo Regex.py

print(str(os.path.getsize('C:\\Matheus\\Study\\IT\\Python')) + ' Bytes')
#tamanho da pasta Python.

print('Pasta Python: ', end='')
pprint.pprint(os.listdir('C:\\Matheus\\Study\\IT\\Python'))
#Vai me resultar em todos os arquivo da ultima pasta, no caso da pasta Python.
#Resulta todos os arquivos do "path".

print("\n")
total_size = 0
for filename in os.listdir('C:\\Matheus\\Study\\IT\\Python'):
    #Ideia do laco for, normalmente nos podemos, usar o laco for, quando temos uma serie de dados,
    #por exemplo neste caso a gente tem uma serie de arquivos na psta Python entao o python vai pegar na ordem alfabetica
    #cada nome do arquivo e armazenar em "filename" e executar o bloco de comandos.
    total_size = total_size + os.path.getsize(os.path.join('C:\\Matheus\\Study\\IT\\Python', filename))
    #Usamos o os.path.join por que o os.path.getsize suporta apenas um argumento e a ideia do os.path.join
    #e sempre receber o nome do novo arquivo do filename.
    #E aqui tambem fazemos a soma de todos os bytes de cada arquivo e exibimos no final.
    print(str(os.path.basename(os.path.join('C:\\Matheus\\Study\\IT\\Python', filename))) + ' |', end=' ')
    #Vamo exibir o nome de cada arquivo.
    print(str(os.path.getsize(os.path.join('C:\\Matheus\\Study\\IT\\Python', filename))) + ' Bytes')
    #Vamos exibir o tamanho de cada arquivo.
print('Total de Bytes da pasta Python: ' + str(total_size))
print("\n")
#Exibir o tamanho total da soma de todos os arquivos.

if os.path.exists('C:\\Matheus\\Study\\IT\\Python') == True:
    #podemos colcoar um input tambem, mas neste caso nao vamos.
    print('O path: ' + 'C:\\Matheus\\Study\\IT\\Python' + ' e um caminho valido')
    #Se for verdadeiro ele me retorna True, o que significa que este caminho existe e tambem e valido.
else:
    print('O path: ' + 'C:\\Matheus\\Study\\IT\\Python' + ' e um caminho invalido')
    #Se me retornar False, significa que ele e o caminho passado para a funcao os.path.exists() e um caminho invalido.

if os.path.isfile('C:\\Matheus\\Study\\IT\\Python\\bigger_and_smaller.py') == True:
    print('O path: ' + 'C:\\Matheus\\Study\\IT\\Python\\bigger_and_smaller.py' + ' e referente a um arquivo')
else:
    print('O path: ' + 'C:\\Matheus\\Study\\IT\\Python\\bigger_and_smaller.py' + ' nao referente a um arquivo')

if os.path.isfile('C:\\Matheus\\Study\\IT') == True:
    print('O path: ' + 'C:\\Matheus\\Study\\IT' + ' e referente a um arquivo')
else:
    print('O path: ' + 'C:\\Matheus\\Study\\IT' + ' nao e referente a um arquivo')

if os.path.isdir('C:\\Matheus\\Study\\IT\\Python\\colocando_gasosa.py') == True:
    print('O path: ' + 'C:\\Matheus\\Study\\IT\\Python\\colocando_gasosa.py' + ' e um diretorio/pasta')
else:
    print('O path: ' + 'C:\\Matheus\\Study\\IT\\Python\\colocando_gasosa.py' + ' nao e um diretorio/pasta')

if os.path.isdir('C:\\Matheus') == True:
    print('O path: ' + 'C:\\Matheus' + ' e um diretorio/pasta')
else:
    print('O path: ' + 'C:\\Matheus' + ' nao e um diretorio/pasta')

if os.path.exists('D:\\') == True:
    print('Pendrive conectado!')
else:
    print('Pendrive desconectado!')

object_file_edit_text_test = open('C:\\Matheus\\Study\\IT\\change_cwd_example\\edit_text_test.txt')
#A ideia da funcao open() e de abrir mesmo o arquivo e como se a gente abrir ele gerasse para
#nos uma ID, onde podemos usar em qualquer parte do programa apos aberta.

#Basicamente ele representa um arquivo no nosso computador.

#O objeto normalemnte e armazenado em uma variavel por ele pode ser usado em varios metodos de leitura e escrita de arquivos.

print(object_file_edit_text_test)
#Exibir os dados que formam um objeto file.

object_file_edit_text_test_content = object_file_edit_text_test.read()
#Aqui nos fazemos a leitura do conteudo do objeto file e o armazenamos em object_edit_text_test_content.

print(object_file_edit_text_test_content)
#Exibir os dados do arquivo de texto edit_text_test.txt.txt

object_file_edit_text_test.close()
#Esta funcao nao retonar nada, apenas fecha e salva as possiveis alteracoes feitas.
#Lembrando que lendo ou escrevendo nos temos que fechar no final de tudo.
print("\n")

object_file_lines = open('Black Alien_Carta pra Amy.txt', 'r')
#o mode = 'r' ou apenas 'r' significa que o arquivo esta no mode de apenas leitura.

print(object_file_lines)
#Objeto files que sera usado para leitura de todas as linhas.

object_file_lines_content = object_file_lines.readlines()
#A leitura do conteudo do arquivo de texto para retonar cada linha como um valor de elemento

print(object_file_lines_content)
#Exibir a lista com o conteudo do arquivo separado por linha.

object_file_lines.close()
#Fechamos o arquivo para salver as alteracoes, mesmo que voce apenas leu o arquivo. Sempre feche-o depois de abrir ou escrever.

object_file_write_and_append = open('write_and_append_text.txt', 'w')
#Aqui nos vamos abrir (no caso nao existe este arquivo de texto, entao ele sera criado no momento em que linha rodar)
#o arquivo de texto em modo de escrever, obs: se a gente abrir um arquivo com este modo se possui alguma coisa dentro do arquivo
#de text ele sera excluido e vai entrar um novo texto, apagando o anterior.
#Neste modo a gente subtitui o que gente escrever no texte, e nao adiciona.

print(object_file_write_and_append)
#Exibir o Objetc file do arquivo em que abrimos na forma de objet file.

text = input('Digite alguma coisa para ser colocada em um arquivo de texto: ')
object_file_write_and_append.write(text + '\n')
#Aqui a gente vai colocar um input de uma string ao usuario digitar qualquer coisa para ser colocada no arquuivo de texto
#O metodo write permite colocar um texto em um arquivo que suporte texto. No caso um arquivo .txt

object_file_write_and_append.close()#Fechar o object file.
#Neste caso a gente vai fechar porque nas proxima linhas a gente vai abrir o mesmo arquivo, porem de outro modo
#no modo de adicao (append) entao ele precisa ser fechado e depois reaberto com o novo modo.
#Nos usamos o close quando a gente nao vai mais fazer nada referente ao modo em que agente abriu, por exemplo
#se eu abrir no modo append 'a' eu posso escrever duas coisas e fechar, para depois abrir de novo e ler como esta escrito.

object_file_write_and_append = open('write_and_append_text.txt', 'a')
#Abrindo o arquivo no modo de adicao (append), no caso de adicao e nao de escrever, entao se possuir algum texto,
#ele apenas adionara, e nao vai sobreescrever.

print(object_file_write_and_append)
#Exibir o Objetc file do arquivo em que abrimos na forma de objet file.

text = input('Digite alguma coisa para ser adicionada em um arquivo de texto[1]: ')
object_file_write_and_append.write(text + '\n')
#Aqui nos vamos ADICIONAR um texto ao arquivo de texto.

text = input('Digite alguma coisa para ser adicionada em um arquivo de texto[2]: ')
object_file_write_and_append.write(text)
#Aqui nos vamos ADICIONAR um texto ao arquivo de texto.

object_file_write_and_append.close()#Fechar o object file.
#Nos usamos o close quando a gente nao vai mais fazer nada referente ao modo em que agente abriu, por exemplo
#se eu abrir no modo append 'a' eu posso escrever duas coisas e fechar, para depois abrir de novo e ler como esta escrito.

object_file_write_and_append = open('write_and_append_text.txt', 'r')
#Aqui nos estamos abrindo ele no modo de leitura.

print(object_file_write_and_append)
#Exibir o Objetc file do arquivo em que abrimos na forma de objet file.

object_file_write_and_append_content = object_file_write_and_append.read()
#Retonar o conteudo do arquivo.
#Vamos ler o que foi escrito na linha anterior e depois vamos armazenar em uma variavel.
#Vamos ler as alteracoes feitas e armazenar a string em uma variavel.
#A gente armazena em uma variavel por alguns motivos
#!. Nos armazenamos o conteudo e podemos usa-lo de qualquer forma, ate para exibir depois.

object_file_write_and_append.close()#Fechar o object file.
#Nos usamos o close quando a gente nao vai mais fazer nada referente ao modo em que agente abriu, por exemplo
#se eu abrir no modo append 'a' eu posso escrever duas coisas e fechar, para depois abrir de novo e ler como esta escrito.

print(object_file_write_and_append_content)
#Exibir o texto da ultima alteracao feita.
#Vamos exibir a String de tudo o que esta escrito e das alteracoes feitas no arquivo de texto.

##########################################################shelf_arquivo = shelve.open('my_data') ###CRIAR 1###
#Esta linha esta como comentario porque o arquivo ja foi criado e assim exemplificamos que nao precisamos criar ele novamente
#apenas acessar os dados ja criados.

#Nesta linha a gente vai abrir (ou criar caso nao exista) e vamo armazenar o arquivo vazio em shelf_arquivo.
#Ele vai funcionar mais ou menos como uma indicacao, os dados serao armazenados nas proxima linhas.

###########################################################names_data = ['Matheus', 'Joao', 'Cesar', 'Ricardo']
#Aqui nos criamos uma lista comundo, entao nos colocares todos este dados em uma "chave".

############################################################shelf_arquivo['Names'] = names_data
#Nesta linha nos armazenamores a lista "names_data" no arquivo shelf_arquivo com a chave ['NAmes']
#Obs: Nos podemos usar usar metodos de dicionarios no arquivo shelf_arquivo.

############################################################shelf_arquivo.close()
#E como sempre ao final de alterar arquivos nos o fechamos

shelf_arquivo = shelve.open('my_data') ###EXIBIR 1###
#Abrin do o arquivo ja criado novamente.
#ESte arquivo shelf, e como se fosse um arquivo com um dicionario. Valores dentro de uma Chave.

print(type(shelf_arquivo))
#Exibindo o tipo de dado e o "shelf_arquivo".

print(shelf_arquivo)
#<shelve.DbfilenameShelf object at 0x0353E3A0>

print(shelf_arquivo['Names'])
#Aqui vamos acessar os dados do arquivo "shelf_arquivo" na sua chaves 'Names' onde se encontra os dados desta chave.

shelf_arquivo.close()
#No final fechamos o arquivo.

shelf_arquivo = shelve.open('my_data') ###EXIBIR 2###
#Abrir o arquivo

print(list(shelf_arquivo.keys()))
#Como dito anteriomente nos podemos usar metodo de dicionarios em arquivos, ja que o que esta armazenado e um pseudo-dicionario
#Podem nos precisamos transformar o retorno do metodo em lista.

print(list(shelf_arquivo.values()))
#AQui podemos usar o metodo values() que seria para dicionario nos valores do arquivo "shelf_arquivo" para retornar todos os
#valores, que estao dentro da unica chave existente no caso "Names" e pegamos o valor de retorno e tranformamos em lista
#e no final de tudo exibi-mos.

shelf_arquivo.close()
#Fechamos o arquivo no final.

#####################################################shelf_arquivo = shelve.open('my_data') ###CRIAR 2###
#Abrimos o arquivo shelf_arquivo

#####################################################last_names_data = ['Oliveira' , 'Felipe', 'Silva', 'Marreco']
#Criamos mais uma lista.

#####################################################shelf_arquivo['Last_names'] = last_names_data
#criamos mais uma chave ao arquivo e armazenamos a lista "last_names_data"

#####################################################shelf_arquivo.close()
#Fechamos tudo ao final de criar e adicionar tudo o que queriamos ao arquivo.

shelf_arquivo = shelve.open('my_data') ###EXIBIR 3###
#Abrir o arquivo

print(list(shelf_arquivo.keys()))
#Exibir todas as chaves.
#Obs: A partir de agora qualquer parte do programa que eu  use isso vai exibir todas as chaves que existem no arquivo.

print(list(shelf_arquivo.values()))
#Exibir todo os valores de todas as chaves existes no arquivo.

shelf_arquivo.close()
#Fechar o arquivo.

names_and_last_names = [{'name': 'Matheus', 'last_name': 'Oliveira'},
                        {'name': 'Ricardo', 'last_name': 'Silva'},
                        {'name': 'Cida', 'last_name': 'Aparecida'}]
#A lista de dicionarios que sao os dados do arquivo .py

names_string = pprint.pformat(names_and_last_names)
#A funcao pprint.pformat vai retonar em forma de string a lista ou dicionario.

print(names_string)
#Exibindo a string transformada por pprint.pformat()

names_arquivo_import = open('C:\\Matheus\\Study\\IT\\Python\\namesImport.py', 'w') ###CRAIR 3###
#Criamos um arquivo.py que suporta o nosso texto e escrevemos um texto, lembrando que quando escrevemos strings ele excluir
#as aspas.
#Nao pode esta na pasta de trabalho do arquivo (CWD).
#Os modulos python nao sao nada menos que scripts python.

names_arquivo_import.write('names = ' + names_string + '\n')
#A string names_string funciona e e identificada copmo uma lista de dicionarios, porque ela esta sinteticamente
#esta correta, mesm estando como string.
#Quando nos escrevemos ('names = ' + names_string + '\n') no arquivo ele vai excluir todos os
#asteriscos, fazendo com que ele fique igual a declaracao de uma lista de dicionarios.
#names = [{'last_name': 'Oliveira', 'name': 'Matheus'},
# {'last_name': 'Silva', 'name': 'Ricardo'},
# {'last_name': 'Aparecida', 'name': 'Cida'}]

names_arquivo_import.close()
#Fechamos o arquivo.

print(namesImport.names)

for keys in range(0,3):
    print(namesImport.names[keys])
for values in range(0,3):
    print(namesImport.names[values]['name'], end=' ')
    print(namesImport.names[values]['last_name'])

#Um modulo e um arquivo que pode ser usado como conteiner  para funcoes, modulos, variveis, de
#modo a reaproveita-las quando necessario, importando o modulo com o comando import.

#Os modulos sao arquivos que possuem a extensao .py.

#Onde se localizam os modulos.

#Quando um modulo e importado, o interpretador procura primeiro por um modulo padrao com o nome do modulo.
#Se nenhum for encontra, ele procurara um arquivo com o nome do modulo e extensao .py
#em uma lista de diretorios presenta na variavel SYS.PATH, a qual e inicializada dos seguintes locais:
#- Na prorpia pasta onde esta localizado o arquivo python principal.
#- PYTHONPATH, que e uma lista de nomes de diretorios, com a mesma sintaxe da variavel do shell PATH.
#- O local padrao, dependente da instalacao.
