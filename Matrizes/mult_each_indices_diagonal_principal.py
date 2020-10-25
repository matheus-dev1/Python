#! python3

#mult_each_indices_diagonal_principal

#O programa solicita ao usuario que digite qual o valor em que ele quer multiplicar cada elemento da diagonal
#principal e no final sera exibido a Matriz com e sem a multiplica

import random

Diag_Princ = int(input('Type a number to do a multiplication to Main Diagonal: '))

Matriz = []

for Linha in range(3):
    criar_Linha = []
    for Coluna in range(3):
        criar_Linha.append(random.randint(0, 100))
    Matriz.append(criar_Linha)

print('Sem a Multiplicacao de ' + str(Diag_Princ))
for Linha in range(3): #Antes da Multiplicacao
    print(Matriz[Linha])
    
for Linha in range(3):
    for Coluna in range(3):
        if Linha == Coluna:
            Matriz[Linha][Coluna] = Matriz[Linha][Coluna] * Diag_Princ
print('Com a Multiplicacao de ' + str(Diag_Princ))
for Linha in range(3): #Depois da Multiplicao.
    print(Matriz[Linha])
