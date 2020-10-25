#! pyrhon3

#criar_matriz_with_0_pt2

#O programa solicita que digite a quantidade de Linhas e Colunas e que insira dados em cada coluna da das
#linhas e no final exibira Matriz completa.

DLinha = int(input('Digite a dimensão da Linha da Matriz: '))
DColuna = int(input('Digite a dimensão da Coluna da matriz: '))
Matriz = []
for Linha in range(DLinha):
    Matriz.append([0] * DColuna)#Exemplo a gente vai multiplicar o numero [0] cinco vezes entao ele vai ter [0, 0, 0, 0, 0] dentro da mesma lista
    #Pega um valor de Lista com um elemento e tento o valor 0. Depois multiplicamos pelo valor 'm' que vamo supor que possui
    #o valor 2 entao ele ira
    #pegar o valor de lista que possui apenas um elemento e vamo multiplicar os elemento dentro da lista, entao
    #a a lista ficaria 2 x 1(este um referente a quantidade de
    # elemento dentro da lista) = [0, 0] esta lista possui dois elemente ou 1 elemento multiplicado pelo valor de 'm'.
for Linha in range(DLinha):
    print(Matriz[Linha])
