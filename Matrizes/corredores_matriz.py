#! python3

#corredores_matriz

#o programa cria uma matriz de 6 por 11 onde o primeiro valor de todas as linhas sao os nomes do corredores que sao inseridos pelo
#usuario atraves do teclado
#e no fianl do programa e feita uma seria de analises e exibicoes de informacoes obtida atraves da corridas, os corredores, tempos e etc.

import random

matriz = []

for linha in range(6):#Cria a matriz com o nome e tempos dos corredores.
    criar_linhas = []
    criar_linhas.append(input('Digite o nome do corredor ' +  str(linha + 1) + ': '))
    for coluna in range(1, 11):
        criar_linhas.append(random.randint(0, 120))#Em segundos
    matriz.append(criar_linhas)
    
for linha in range(6):
    print(matriz[linha])

m_temp = matriz[0][1]
for linha in range(6):
    for coluna in range(1, 11):
        if m_temp > matriz[linha][coluna]:
            m_temp = matriz[linha][coluna]
            volta = coluna
            corredor = matriz[linha][0]
            
soma_tempos = []
media_tempos = []
for linha in range(6):#obtendo a soma de todos os tempos do corredores
    soma = 0
    for coluna in range(1, 11):
        soma += matriz[linha][coluna]
    soma_tempos.append(soma)
    media_tempos.append(soma_tempos[linha] / 10)
    
menor_media = media_tempos[0]
corredor_menor_media = ''
for linha in range(6):#o corredor com a media de voltas mais rapidas
    if menor_media > media_tempos[linha]:
        menor_media = media_tempos[linha]
        corredor_menor_media = matriz[linha][0]   
    
print('Melhor volta da prova com', m_temp, 'do corredor',corredor_menor_media, 'na volta',volta)
print('O Corredor', corredor_menor_media, 'com a media mais rapida: ', menor_media)
print('media de tempo de cada corredor: ')
for linha in range(6):
    print(matriz[linha][0], media_tempos[linha])
print('media de tempo de cada corredor ordenados: ')
media_tempos.sort()#ordena os valores das media dos corredores.
for linha in range(6):
    print(str(linha + 1) + 'o.' + ' ' + str(media_tempos[linha]))
