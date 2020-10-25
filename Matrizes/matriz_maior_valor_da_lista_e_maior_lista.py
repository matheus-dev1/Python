#! python3

#matriz_maior_valor_da_lista_e_maior_lista

#O Programa cria uma matriz 3 x 3 e entra com valores aleatorio de 1 a 100 e ele descombre qual o a Linh da Matriz tem a soma do valores maior e exibe a lista e o valor.

import random

Matriz = []
MaiorValorMatriz = [] #usar isso para testar qual o maior valod da lista
MaiorValor = 0
Posicao = 0

#Criacao e entrada de dados da Matriz.
for Linha in range(3):
    criar_Linha = []
    for Coluna in range(3):
        criar_Linha.append(random.randint(1 ,100))
    Matriz.append(criar_Linha)
for Linha in range(3):#Exibir a matriz 3 x 3 completa
    print(Matriz[Linha])
for Linha in range(3):#Fazendo a soma dos valores da Matriz
    Soma = 0
    for Coluna in range(3):
        Soma += Matriz[Linha][Coluna]
    MaiorValorMatriz.append(Soma)
MaiorValor = MaiorValorMatriz[0]
for Linha in range(3):#Descobrindo qual o maior valor da soma das Listas e pegando sua posicao.
    if MaiorValor < MaiorValorMatriz[Linha]:
        MaiorValor = MaiorValorMatriz[Linha]
        Posicao = Linha
print('Maior Lista da Matriz:', Matriz[Posicao])
print('A lista com o maior valor: ', MaiorValor)    
