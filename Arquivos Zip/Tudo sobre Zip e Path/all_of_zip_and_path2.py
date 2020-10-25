#! python3

#all_of_zip

#tudo sobre arquivos .zip

import shutil, os, send2trash, zipfile, pprint
#Imports: Shutil: necessarios para Mover, Copiar, Renomear Apagar Arquvios.
#OS: Criar, Ler, Escreve em arquivos.

os.mkdir('Organizando Arquivos') ##JA CRIADO ##
#Criar UM diretorio, neste caso, no diretorio de trabalho do arquivo.

os.chdir('.\\Mad Libs')
#Alterar Diretorio de Trabalho Atual(CWD).

print('Alteracao 1: ' + str(os.getcwd()))
#Exibir CWD.

print(shutil.copy('new_text_libs.txt', 'C:\\Matheus\\Study\\IT\\Python\\Organizando Arquivos\\new_text_libs.txt'))
#Copiar um arquivo de um diretorio para outros.
#Obs: Se o destivo final, for o nome de um arquivo Ex: new_text_libs.txt (Arquivo que deve ser copiado )
#C:\\Matheus\\Study\\IT\\Python\\Organizando Arquivos\\new_text_libs2.txt (Local e nome novo)
#Obs: Se o arquivo com o mesmo nome ja existir no diretorio ele nao copia outro.

os.chdir('C:\\Matheus\\Study\\IT\\Python')

print('Alteracao 2: ' + str(os.getcwd()))

print(shutil.copytree('Livros e Apostilas Python', 'Livros e Apostilas Python - Copy')) ###JA COPIADO###
#Com a funcao shutil.copytree, nos copiamos todas as pastas, arquivos, subpastas, subarquivos, basicamente tudo a partir
#desta pasta.
#Obs: A parte de origem nao pode exisitr, tem que ser criada uma nova pasta.

print(shutil.move('Livros e Apostilas Python - Copy', 'Livros e Apostilas Python')) ###JA MOVIDOS###
#A funcao shutil.move vai mover um arquivo/pasta de um local para o outro.

print(shutil.move('Livros e Apostilas Python - Copy', 'Livros e Apostilas Python\\Livros e Apostilas Python - Moved'))
#Obs: Se no destino (2. Argumento) tiver um arquivo com o mesmo nome do arquivo do arquivo que deve ser movido (1. Argumento)
#ele sobreescrevera o arquivo.
#Exemplo: Se já houver um arquivo bacon.txt em C:\eggs, ele será sobrescrito.

print(shutil.move('urls.py', 'urls_renamed')) ###JA COPIADO###
#Se nao tiver nenhuma pasta chamada urls_renamed ele vai criar um arquivo do tipo 'File', ou seja, sem nenhum tipo especificado.
#Ele entende que, como ele nao encontrou uma pasta chamada urls_renamed, se trata de um arquivo, entao ele o renomeia e gravas
#as informacoes do arquivo urls, porem voce tambem nao especificou tipo do arquivo, entao ele fica sem tipo.

print(shutil.move('collatz2.py', 'Does_not_Exist\\2\\1')) ###ERRO###
#O Python procura 2 e 1 no diretório Does_not_Exist.
#Obs: As pastas ja devem exisitir, se nao causara um erro.

print(os.unlink('123.txt'))
#Retorna None
#Com a funcao os.unlink() podemos exluir uma pasta/arquivo.

print(os.rmdir('123'))
#A funcao os.rmdir() vai excluir uma pasta vazia.
#Obs: Ele excluir a pasta permanentemente.

print(shutil.rmtree('123'))
#A funcao shutil.rmtree() vai excluir tudo de uma pasta.

print(shutil.copytree('Provas', 'Provas - Copy'))
#Copia um arvore de diretorios para outro diretorio.

os.chdir('.\\Provas - Copy')

for filename in os.listdir():
    if filename.endswith('.py'):
        #os.unlink(filename)
        print(filename)
#Neste looping for nos vamos passar por todos os arquivo do diretorio de trabalho do arquivo, que foi passado para 
#Provas - Copy e se so arquivo forem do tipo .txt ele vai exclui-lo.

print(send2trash.send2trash('lixeira.txt'))
#Com a instalacao do send2trash e depois de importalo
#Umas das funcoes e enviar um arquivo/pasta para a lixeira, em vez de excluido permanentemente.

for nomePasta, subPastas, nomeArquivo in os.walk('C:\\Matheus'):
    #A funcao os.walk() percorre por todos os cantos de uma pasta, ou seja, pela pasta, subpastas e arquivos.
    #Entao ele me retornar como primeiro valor a pasta aonde ele vai estar.,
    #Como segundo valor vai me retornar o ou os nomes da pastas que possui dentro da pasta.
    #E o segundo vai ser os arquivos que possui tanto dentro de pastas quando dentro de subpastas.

    #Dentro do primeiro for temos mais 2 for's, e ele vao estar juntos, por dentro de uma pasta tem que ser verificado
    #se possui tanto subpastas, quanto arquivos.
    print('Pasta Atual: ' + nomePasta)
    #As Pastas sao o diretorio atual onde o looping esta percorrendo. Entao se eu estiver na pasta atual de Study
    #O valor de nomePasta vai ser C:\\Matheus\\Study.
    for pastas_sub in subPastas: 
        #As sub pasta vai me mostrar pastas que estao dentro de outras pastas.
        #Exemplo da pasta C:\\Matheus. Dentro dela possui outras pastas, ou seja, outras sub-pastas.
        print('Sub Pasta: ' + nomePasta + ': ' + pastas_sub)
        #Vai exibir a string 'Sub pasta: ' + o nome da pasta atual + o nome da subpasta atual.
    for arquivo_nome in nomeArquivo:
        #O nomeArquivo vai exibir o local e nome de um arquivo, ele pode esta tanto dentro da pasta atual como das subpastas.
        print('Nome do Arquivo: ' + nomePasta + ': ' + arquivo_nome)
        #O formato de exibircao sera: String 'Nome do Arquivo: ' + nome da pasta aonde o looping esta + nome do arquivo aonde 
        #o looping esta.
    print('')
    #Espaco para separar a mudanca de pastas.

object_zipfile_livros_python = zipfile.ZipFile('Livros Python zip.zip')
#Para usamos as funcoes de arquivos zipados ou zip files, devemos importa-lo com 'import zipfile'
#A funcao zipfile.ZipFile() retonar um objeto zipfile, semelhante ao objeto file, podemos entender isso como um "id" do arquivo
#aonde ele sera localizado.
#No argumento deve conter um arquivo .zip

for zipfile in object_zipfile_livros_python.namelist():
    print(zipfile)
#A o metodo .namelist() vai listar pastas, subpastas e arquivos dentro do arquivo .zip referente ao id do object zipfile.
#Podemos usar o looping for para apresentar os arquivo de uma melhor forma.

object_zipfile_livros_python_info = object_zipfile_livros_python.getinfo('Livros Python zip/Automatize Tarefas Macantes com Python/automate_online-materials/zophie.png')
#Com o metodo getinfo nos conseguimos um object zipfile info que tem seus proprios atributos.
#E como se tivesse abrindo um arquivo com o metodo open().
#Ou seja ao pegar um arquivo dentro da pasta zipada e passa-lo pelo metodo getinfo() nos conseguimos usar
#uns metodos exclusivos para o object zipfile info. 

print('Tamanho do arquivo: ' + str(object_zipfile_livros_python_info.file_size))
#Este metodo do object zipfile info chamado file_size retornar o valor do tamanho do arquivo nao compactado.

print('Tamanho do arquivo comprimido: ' + str(object_zipfile_livros_python_info.compress_size))
#Este metodo do object zipfile info chamado comprees_size retornar o valor do tamanho do arquivo compactado.

print('O arquivo comprimido: ' + object_zipfile_livros_python_info.filename + ' é %s vezes menor!' %round(object_zipfile_livros_python_info.file_size / object_zipfile_livros_python_info.compress_size, 2))
#A funcao round vai pegar um valor e retonar um arredondamento sobre ele.
#O valor que nos vamos usar no exemplo acima e o tamanho do arquivo nao compactado com o tamanho do arquivo compactado.
#O numero 2 mostra quantos valores pos virgula o retorno de round() deve conter.

print(object_zipfile_livros_python.extract('Livros Python zip/Automatize Tarefas Macantes com Python/automate_online-materials/zophie.png', 'C:\\Matheus\\Study\\IT\Python\\Foda'))#Foi kkkk
#A o metodo extract vai extrair um unico item de uma arquivo .zip
#Ele pode ter 2 argumentos, sendo o primeiro o arquivo a ser extraido e o segundo o local para onde o arquivo vai.
#Se a pasta aonde o arquivo vai nao exista ela e criada pelo Python.
#Eu consegui extrair apenas o chama.txt

print(object_zipfile_livros_python.extractall('.\\Livros Python Extract'))
#A funcao extractall() vai extrair todos os arquivos do arquivo zip para a area de trabalho do arquivo .py
#O argumento deve ser o nome da pasta aonde sera armazenado os arquivos extraidos.

object_zipfile_livros_python.close()
#Fechamos o arquivo .zip