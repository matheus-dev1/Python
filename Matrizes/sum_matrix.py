#! python3

#sum_matrix

#O programa cria duas matrizes e faz a soma de seus elementos em cada posicao e depois cria uma terecira
#matriz com os valores de cada elemente somados.

import random

Matriz = []
Matriz2 = []
Matriz3 = []

for Linha in range(2):
    criar_Linha = []
    for Coluna in range(2):
        criar_Linha.append(random.randint(0, 100))
    Matriz.append(criar_Linha)

for Linha in range(2):
    criar_Linha = []
    for Coluna in range(2):
        criar_Linha.append(random.randint(0, 100))
    Matriz2.append(criar_Linha)

for Linha in range(2):
    criar_Linha = []
    for Coluna in range(2):
        criar_Linha.append(Matriz[Linha][Coluna] + Matriz2[Linha][Coluna])
    Matriz3.append(criar_Linha)

for Linha in range(2):
    print(Matriz[Linha])

for Linha in range(2):
    print(Matriz2[Linha])

for Linha in range(2):
    print(Matriz3[Linha])
