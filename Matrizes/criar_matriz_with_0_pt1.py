#! python3

#criar_matriz_with_0_pt1

#O programa solicita que digite a quantidade de Linhas e Colunas e que insira dados em cada coluna da das linhas e no
#final exibira Matriz completa.

Matriz = []

AddLinha = int(input('Adicionar dimensão de Linhas a Matriz: '))
AddColuna = int(input('Adicionar dimensão de Colunas a Matriz: '))

for Linha in range(AddLinha):
    CriarLinha = [] #Cria uma Lista vazia para ser adicionado valores e depois colocado na lista principal 'Matriz'
    for Coluna in range(AddColuna):
        CriarLinha.append(0)#Vamos inserrir dados em todas as colunas da linha.
    Matriz.append(CriarLinha)#Vamos passa o valor de lista para a lista principal chamada "Matriz".
for Pular in range(AddLinha):
    print(Matriz[Pular])#Exibir a matriz.
    
#turma = []
#for i in range(3):
#cria linha vazia
#linha= []
#for j in range(5):
#vai adicionando as notas na linha
#linha.append(int(input('Digitea nota [' + str(i) + ',' + str(j) + ']:')))
#adiciona a linha na matriz turma
#turma.append(linha)
#print(turma)
