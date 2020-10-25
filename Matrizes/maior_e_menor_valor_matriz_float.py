#maior_e_menor_valor_matriz_float

#O programa solicita que seja criado uma matriz com valoers reais e em seguida mores o menor e maior valor da matriz

#basicamente nos sub entendemos que numeros reais no usamos o tipo de dado float (ou Real)

matriz = []

import random

for linha in range(6):
    criar_linha = []
    for coluna in range(3):
        criar_linha.append(round(random.uniform(0, 10), 2))#numeros aletorios do tipo float. Entre 0 e 10
    matriz.append(criar_linha)
print('Matriz de numero Reais')
for linha in range(6):
    print(matriz[linha])
print()

menor_num = matriz[0][0]
maior_num = matriz[0][0]
for linha in range(6):
    for coluna in range(3):
        if menor_num > matriz[linha][coluna]:
            menor_num = matriz[linha][coluna]
        if maior_num < matriz[linha][coluna]:
            maior_num = matriz[linha][coluna]

print('Maior numero na Matriz: ',maior_num)
print('Menor numero na Matriz: ',menor_num)
