#! python3

#bytes_and_biggest_file.py

#O programa solicita ao usuario que digite um path ate a pasta aonde ele saber qual a e a pasta com a maior
#quantidade de itens e a pasta com maior quantidade de bytes.

# TODO: Pasta que tenha o maior tamanho entre todas as pastas
# TODO: Ou pasta que contenha a maior quantiade de arquivos dentro dela.
# TODO: Em cada pasta devemos abrir a sub pasta e contas em cada pasta e sub pasta todos os arquivos.

import os
#Imports necessarios para rodar o programa.

local_pasta = input('Digite o caminho de uma pasta: ')
#Variavel que armazena o input do usuario com o path ate o arquivo em que ele queira receber a pasta com o
#maior quantiade de itens e a pasta com a maior quantidade de bytes.

maior_pasta_itens_qtd = 0
#A quantidade itens comeca em zero.
maior_pasta_itens_nome = 'Sem pasta!'
#O nome da maior pasta comeca com vazio, sem valor.
tamanho_pasta_bytes_qtd = 0
#O tamanho em bytes da maior pasta do diretorio onde o usuario insericao em Local_pasta. Comcaca em 0
pasta_bytes_nome = 'Sem pasta!'
#O nome da maior pasta em relacao a bytes.

for nomePasta, subPastas, nomeArquivo in os.walk(os.path.abspath(local_pasta)):
    qtd_arquivos = 0
    #Quantidade de arquivo em uma pasta comeca em zero. E volta para 0 toda vez que for para outra pastas.

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
        print('Sub Pasta: ' + nomePasta + ' - Sub Pasta da Sub Pasta: ' + pastas_sub)
        #Vai exibir a string 'Sub pasta: ' + o nome da pasta atual + o nome da subpasta atual.

    for arquivo_nome in nomeArquivo:
        #O nomeArquivo vai exibir o local e nome de um arquivo, ele pode esta tanto dentro da pasta 
        #atual como das subpastas.
        print('Nome do Arquivo: ' + nomePasta + ' - Nome do Arquivo: ' + arquivo_nome)
        #O formato de exibircao sera: String 'Nome do Arquivo: ' + nome da pasta aonde o looping esta + nome
        #do arquivo aonde o looping esta.
        qtd_arquivos = qtd_arquivos + 1
        #Vai contar a quantiade de arquivos uma pasta possui.
        
        if maior_pasta_itens_qtd < qtd_arquivos:
            #Se possui alguma pasta dentro looping que for maior que a varaivel 'maior_pasta_itens_qtd'
            #a variavel recebe a quantidade de itens desse pasta que possui a quantiade de itens maior que
            #a anterior e armazena seu valor e seu nome na proxima variaveis.
            maior_pasta_itens_qtd = qtd_arquivos
            #Recebe o valor da pasta com a maior quantidade de itens.
            maior_pasta_itens_nome = os.path.abspath(nomePasta)
            #Recebe o nome da pasta com a maior quantidade de itens.
        
        if tamanho_pasta_bytes_qtd < os.path.getsize(nomePasta):
            #Se uma pasta o tamanho de uma pasta formaior que a da pasta anterior ele recebe
            #O tamanho da maior em bytes e o seu nome.
            pasta_bytes_nome = nomePasta
            #Nome da maior pasta
            tamanho_pasta_bytes_qtd = os.path.getsize(nomePasta)
            #Quantidade de bytes da maior pasta.

    print('Pasta: ' + nomePasta + ' - Quantidade de arquivos: ' + str(qtd_arquivos))
    #Exibe a pasta atual + a quantiade de arquivos nela.
    print('')
    #Apos terminar de exibir os arquivo de uma pasta ele pula uma linha.

print('Pasta com a maior quantidade de itens: %s - Quantidade de Itens: %s' %(maior_pasta_itens_nome, maior_pasta_itens_qtd))
#Este print exibe ao usuario a pasta com a maior quantidade de itens e a quantidade de itens.
print('Pasta com a maior quantiade de Bytes: %s - Quantidade de Bytes: %s' %(pasta_bytes_nome, tamanho_pasta_bytes_qtd))
#Este print exibe ao usuario a pasta com a maior quantidade de bytes e a quantidade de bytes.