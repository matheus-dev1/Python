#! python3

#matriz_transposta

#Faca uma matriz que possui linhas e colunas iguais ate 100 e depois altere os valores de linhas para colunas e colunas para linhas.

import copy
import random

t_linhas = int(input('Digite o tamanho das linhas da Matriz: '))
t_colunas = int(input('Digite o tamanho das colunas da matriz: '))
#Se as linhas e coluns posusirem valores impares e iguais a linha do meio da esquerda superior para direita infeiro nao vai ser alterada.
matriz = []
matriz2 = []

for linha in range(t_linhas):#Desenvolvimento de criacao das duas matrizes
    criar_linhas = []
    for coluna in range(t_colunas):
        criar_linhas.append(random.randint(1, 100))
    matriz.append(criar_linhas)

for linha in range(t_colunas):#Desenvolvimento de criacao das duas matrizes
    criar_linhas = []
    for coluna in range(t_linhas):
        criar_linhas.append(random.randint(1, 100))
    matriz2.append(criar_linhas)

print('Matriz 1')
for linha in range(t_linhas):
    print(matriz[linha])

print('Matriz 2')
for linha in range(t_linhas):
    print(matriz2[linha])

for linha in range(t_linhas):
    for coluna in range(t_colunas):
        matriz2[coluna][linha] = matriz[linha][coluna]

print('Matriz Transposta 1')
for linha in range(t_colunas):
    print(matriz[linha])

print('Matriz Transposta 2')
for linha in range(t_colunas):
    print(matriz2[linha])
