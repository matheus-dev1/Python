#! python3

#mult_duas_matrizes_e_criando_terceira

#O programa solicita ao usuario que digite o tamanha da duas Matriz, sao adicionados ao elementos valoers de 0 a 100 e sao exibidas e depois e feito um testo para verificar
#se a linha e a colun das duas matrizes sao iguais para fazer uma multiplicacao e exibir um terceira com o valor da multilplicacao da duas matrizes.

import random

Matriz1 = []
Matriz2 = []
Matriz3 = []

AddLinha = int(input('[Matrix 1]Type Line Numbers: '))
AddColuna = int(input('[Matrix 1]Type Colums Numbers: '))

for Linha in range(AddLinha):#Cria e entra com os dados da Primeira Matriz
    criar_Linha = []
    for Coluna in range(AddColuna):
        criar_Linha.append(random.randint(0, 100))
    Matriz1.append(criar_Linha)

AddLinha2 = int(input('[Matrix 2]Type Line Numbers: '))
AddColuna2 = int(input('[Matrix 2]Type Colums Numbers: '))

for Linha in range(AddLinha2):#Cria e entra com os dados da Segunda Matriz
    criar_Linha = []
    for Coluna in range(AddColuna2):
        criar_Linha.append(random.randint(0, 100))
    Matriz2.append(criar_Linha)

print('Matriz 1')
for Linha in range(AddLinha):
    print(Matriz1[Linha])

print('Matriz 2')
for Linha in range(AddLinha2):
    print(Matriz2[Linha])

if AddLinha == AddLinha2 and AddColuna == AddColuna2:
    for Linha in range(AddLinha):#Cria e entra com os dados da Terceira Matriz
        criar_Linha = []
        for Coluna in range(AddColuna):
            criar_Linha.append(Matriz1[Linha][Coluna] * Matriz2[Linha][Coluna])
        Matriz3.append(criar_Linha)    
    print('Matriz 3')
    for Linha in range(AddLinha):
        print(Matriz3[Linha])

else:
    print('Matriz 1: ', len(Matriz1), 'x', len(Matriz1[0]))
    print('Matriz 2: ', len(Matriz2), 'x', len(Matriz2[0]))
    print('Valores da Matriz 1 e Matriz 2 sao imcopativeis para a multiplicacao delas.')
