#! python3

#criando_matriz_3x3

#O programa solicita ao usuario uma serie de numero para preencher uma matriz.

import random

Matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#Cada lista dentro da lista pode ser entendido como uma linha, entao como temos tres listas dentro da lista temos 3 linhas os valores dentro de cada linha representa
#uma coluna entao somando as colunas nos temos uma valor de nove colunas, isso esta sendo representado de forma exata e poderiamos representar de forma que a matriz
#poderia de um valor de 20 x 20.

for Linha in range(0, 3):
    for Coluna in range(0, 3):
        print('Type a number position [',Linha + 1,']','[',Coluna + 1,']: ', end = '')
        Matriz[Linha][Coluna] = random.randint(1, 100)
        print()

for Linha in range(0, 3):
    for Coluna in range(0, 3):
        print('[',Matriz[Linha][Coluna],']', end = '')
    print()
