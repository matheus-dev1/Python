#! python3

#matriz_aleatorios_e_par

#Programa que solicita o tamanho da linha e coluna de uma matriz e preencher com valores aletorios.

import random

Matriz = []
Par = 0

AddLinha = int(input('Digite a quantidade de Linha da Matriz: '))
AddColuna = int(input('Digite a quantidade de Coluna da Matriz: '))

for Linha in range(AddLinha):
    LinhaMatriz = []
    for Coluna in range(AddLinha):
        LinhaMatriz.append(random.randint(0, 100))
    Matriz.append(LinhaMatriz)
    
for Linha in Matriz:
    #Digamos que a MAtriz tenha um valor de 2 x 4. A o valor de lista 'Linha' ira receber o primeiro de dois indices da 'Matriz'. 
    for Valor in Linha:
        #Neste for o valor 'Linha' ja esta com o indice de Matriz e o valor ira testar cada elemento deste indice.
        if Valor % 2 == 0:
            Par += + 1
            
for Linha in range(AddLinha):
    print(Matriz[Linha])
    
print('Quantidade de valores pares na Matriz:',Par)
