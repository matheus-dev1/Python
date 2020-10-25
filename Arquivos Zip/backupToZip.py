#! python3

#backupToZip.py

#Copia uma pasta toda e seu conteúdo para um arquivo ZIP cujo nome seja incrementado.

# TODO: Criar um pasta para armazenar pastas a serem feitos backups
# TODO: Cada pasta dentro da pasta principal sera feita um backup de uma pasta .zip dela em outra pasta.
# TODO: Adicionar uma numeracao ao nome do arquivo, a cada arquivo e assim subsequentemente.
# TODO: Passar pelas sub-pastas.
# TODO: Nome da pasta + o nome Backup
# TODO: Exibir local aonde foi feito o backup.

import os, string, random, zipfile
#Imports necessarios.

def backupToZip(Pasta_backup_local):
    #Esta funcao vai receber a string o caminho da pasta.
    #No nosso exemplo C:\\Matheus\\Study\\IT\\Python\\ExemploBackup
    Pasta_backup_local = os.path.abspath(Pasta_backup_local)
    #Aqui nos vamos garantir que, o caminho passado pelo ususario seja sempre absoluto.
    Backup_number = 1
    while True:#Looping infinito.
        Pasta_backup_zip = os.path.basename(Pasta_backup_local) + '_' + str(Backup_number) + '.zip'
        #Cria o nome da pasta que devemos fazer o backup.
        #Obs: O backup vai sair dentro da pasta.
        if os.path.exists(Pasta_backup_zip) == False:
            #Obs: Nos estamos dentro da pasta cujo vamo fazer um backup.
            #Caso dentro da pasta aonde vamos fazer o backup, nao exista um arquivo com o mesmo nome
            #Exemplo, caso exista um ExemploBackup_1.zip sera criado o ExemploBackup_2.zip
            break
            #Caso exista ele volta ao inicio do looping while com a funcao break.
        Backup_number = Backup_number + 1
        #Caso nao exista ele continua a executar o looping e chega nesta parte para adicionar 
        #um numero ao contador de backup's, entao se ja existia um ele ira adicionar mais 1 ao valor
        #e vai criar o ExemploBackup_2.zip
    print('Creating %s...' % (Pasta_backup_zip))
    #Exibir na tela que como se tivesse carreando que esta criando um backup da pasta e das subpastas
    #em um unico arquivo zip.
    id_Pasta_backup_zip = zipfile.ZipFile(Pasta_backup_zip, 'w')
    #Vamos abrir a pasta aonde queremos fazer o backup em modo de escrita.
    #E o nome do arquivo sera o que esta armazenado em Pasta_backup_zip
    #Exemplo_backup_1.zip _2.zip e assim adiante.
    for Pasta, Subpasta, Arquivo in os.walk(Pasta_backup_local):
        #Vamos usar o metodo os.walk() para passar por todas as pastas, subpastas e arquivo da pasta principal
        print('Adding files in %s...' % (Pasta))
        #A cada pasta que ele passa vai exibir que esta adicionando a pasta em questao no arquivo .zip
        #Como o nosso arquivo e feito basicamente de pastas, ele vai exibir todas as pastas.
        id_Pasta_backup_zip.write(Pasta)
        #A funcao write() com arquivos .zip vai fazer com que o arquivo que nos abrirmos receba
        #uma pasta, subpasta ou arquivo.
        for Nome_arquivo in Arquivo:
            #VAmos procurar arquivo dentro de cada pasta, caso exista, ele sera acrescentado no 
            #arquivo .zip a partir de todo o caminho criado para chegar nele.
            Nome_base = os.path.basename(Pasta_backup_local) + '_'
            if Nome_arquivo.startswith(Nome_base) and Nome_arquivo.endswith('.zip'):
            #Se ele comecar com ExemploBakcup_ e terminar com .zip
            #Ele pula para o priximo arquivo.
            #Caso dentro de alguma pasta existir um arquivo com estas caracteristicas ele nao ira fazer o
            #backup dele e vai voltar para o looping for como se ja tivesse passador por esse arquivo
            #e fosse para a proxima pasta.
                continue
                #instrucao para voltar ao looping do comeco e ir para o proximo arquivo.
            id_Pasta_backup_zip.write(os.path.join(Pasta, Nome_arquivo))
            #Caso o arquivo/pasta nao atenda aos requisitos do if, nos vamo pegar o nome do arquivo mais
            # a pasta aonde estamos, ou seja a pasta do arquivo e vamos usar o os.path.join() para 
            #criar um string cujo valor e o path ate o arquivo em aonde estamos.
    id_Pasta_backup_zip.close()
    #Fechamos o arquivo.
    print('Done.')
    #Exibimos 'Done' ao terminar de compactar todos os arquivo.

try:
    os.mkdir('.\\ExemploBackup')
except FileExistsError:
    print('Pasta ja existente.')

os.chdir('.\\ExemploBackup')

print('Pasta de Trabalho atual: ' + str(os.getcwd()))

#for pastas in range(5):
    #Text = ''.join(random.choices(string.ascii_uppercase + string.digits, k=random.randint(5, 20)))
    #Path = os.path.join(os.path.abspath('.'), Text)
    #os.mkdir(Path)

Pasta_backup = input('Pasta a fazer backup: ')

backupToZip(Pasta_backup)