#! python3

#function_mult_duas_matrizes

#o programa solicita ao usuario que digite o tamanho da matriz a e b e depois faz uma multiplicacao.

import random

def mult_mat(a, b):
    global True_false
    num_linhas_a, num_colunas_a = len(a), len(a[0]) #Atribuicao multiltipla
    num_linhas_b, num_colunas_b = len(b), len(b[0])

    if num_linhas_a == num_colunas_b:
        c = []
        for linhas in range(num_linhas_a):
            c.append([])
            for colunas in range(num_colunas_b):
                c[linhas].append(0)
                for k in range(num_colunas_a):
                    c[linhas][colunas] += a[linhas][k] * b[k][colunas]

        for i in range(num_linhas_a):
            print(c[i])
        return c
    else:
        print('Matriz A e B nao sao matrizes inversas. (ou seja a Matriz [A] tem as mesmas colunas e linhas da matriz [B])')
        return 'Matriz A e B nao sao matrizes inversas. (ou seja a Matriz [A] tem as mesmas colunas e linhas da matriz [B])'

a = []
b = []
True_False = False

l1  = int(input('Linha Matriz 1: '))
c1 = int(input('Coluna Matriz 1: '))

for linhas in range(l1):#Cria e entra com os dados Matriz A
    criar_l = []
    for colunas in range(c1):
        criar_l.append(random.randint(1, 100))
    a.append(criar_l)

l2  = int(input('Linha Matriz 2: '))
c2 = int(input('Coluna Matriz 2: '))

for linhas in range(l2):#Cria e entra com os dados Matriz A
    criar_l = []
    for colunas in range(c2):
        criar_l.append(random.randint(1, 100))
    b.append(criar_l)

mult_mat(a, b)
