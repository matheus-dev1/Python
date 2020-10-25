#! python3

#matriz_com_valores_impares

#O programa cria uma matriz de 4x4 e coloca valores aleatorio entre 0 e 1000 e em seguida verifica
#se possui valores impares e se possui quantos possuir.

import random

Matriz = []
Impar = 0

for Linha in range(4):
    LinhaMatriz = []
    for Coluna in range(4):
        LinhaMatriz.append(random.randint(0, 1000))
    Matriz.append(LinhaMatriz)

for Linha in range(4):
    for Coluna in range(4):
        if Matriz[Linha][Coluna] % 2 == 1:
            Impar += 1

for Linha in range(4):
    print(Matriz[Linha])#Imprima a matriz em formato de Matriz
        
print("A Matriz possui %d valores impar" %Impar)
#O operador porcento(%) dentro de um print mostra o valor do subsequente a ele com o mesmo simbolo de (%).
