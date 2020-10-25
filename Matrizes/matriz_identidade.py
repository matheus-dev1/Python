#! python3

#matriz_identidade

#Multiplicacao de Matrizes e igual a valores da linha da uma matriz pelo valores de uma coluna de um Matriz.
#Leia duas A e B de inteiro e verificar de a multiplicacao de A por B da uma Matriz identidade.

import random

matriz1 = []# Matriz A
matriz2 = []# Matriz B
matriz3 = []# MAtriz C
ident = 0 #Varivel de identificado de Matriz Identidade.

l1 = int(input('Digite a dimensao da Linha da Matriz [A]: '))
c1 = int(input('Digite a dimensao da Coluna da Matriz [A]: '))

for l in range(l1):#Cria e entra com os dados Matriz A
    criar_l = []
    for c in range(c1):
        criar_l.append(random.randint(0, 100))
    matriz1.append(criar_l)
    
print('Matriz A')
for l in range(l1):#Exibir a matriz A
    print(matriz1[l])

l2 = int(input('Digite a dimensao da Linha da Matriz [B]: '))
c2 = int(input('Digite a dimensao da Coluna da Matriz [B]: '))

for l in range(l2):#Cria e entra com os dados Matriz B
    criar_l = []
    for c in range(c2):
        criar_l.append(random.randint(0, 100))
    matriz2.append(criar_l)
    
print('Matriz B')
for l in range(l2):
    print(matriz2[l])

if l1 == c2:#Para podermos multiplicar matrizes as linhas da primeira matriz tem que ser igual as colunas da segunda matriz.
    #Os valores dentro do Range tem que ser colocados da seguinte forma.
    #Porque colocando os valores das linhas e colunas respectivamente como esta abaixo nos vamo conseguir passar
    #por todos os cantos da MAtriz e conseguir fazer a multiplicacao de MAtriz como deve ser feito.
    #Exemplo: 3 x 2 * 2 x 3 = 3 * 3 * 2 = 18, Entao o looping vai passar 18 por todos os cantos necessarios
    #da Matriz para fazer a Multiplicacao.
    for l in range(l1):#CAso o range so tenha um valor o valor inicial vai ser 0 e vai ate o valor - 1.
        matriz3.append([])#Exemplo da quantidade de voltas que daria com MAtriz 2 x 2 (C : 2 + L: 4 + 8)
        print('l: ', l)
        for c in range(c2):# Sempre que ele passar por aqui ele vai repetir a quantidade de vezes que esta em c2
            matriz3[l].append(0)#AQui nos valores colocar mais um valor ao indice da linha entao se fosse 2 x 2 fna primeira linha ficaria assim: [1, 0] que seria uma linha com dois valores.
            print('c: ', c)
            for k in range(c1):
                print('k: ', k)
                matriz3[l][c] += matriz1[l][k] * matriz2[k][c]#Ele vai fazendo a soma da dos valores e colocando em apenas um lugar na matriz C.
    
    for l in range(l1):
        for c in range(c2):
            if l == c:
                if matriz3[l][c] == 1:
                    ident += + 1
    if ident == c2:
        print('Matriz Identidade de A e B:')

        for c in range(c2):
            print(matriz3[c])

else:
    print('Matriz A e B nao sao matrizes inversas. (ou seja a Matriz [A] tem as mesmas colunas e linhas da matriz [B])')
