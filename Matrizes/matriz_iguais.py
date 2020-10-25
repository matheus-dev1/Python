#! python3

#matriz_iguais

#O programa solicita ao usuario que digite as dimensoes da linhas e colunas da MAtriz e em seguida o apresentara o tamanho de cada linhae coluna e apresentara a Matriz.

while True:
    criar_Linha = int(input('Dimensao de linhas: '))
    criar_Coluna = int(input('Dimensao de Colunas: '))
    if criar_Linha == criar_Coluna:
        print('Dimensoes iguais, Correto!')
        break
    else:
        print('Dimensoes diferentes, Incorreto. Tente Novamente!')
        continue

Matriz = []

for Linha in range(criar_Linha):
    Matriz.append([0] * criar_Coluna)
    #Nesta parte nos vamos preencher a nossa matriz.
    #Vamos daro exemplo que o valro de "criar_linha" e igual a 10 e de "criar_colun" e igual a 10.
    #Entao teremos uma matriz de 10 por 10.

for Linha in range(criar_Linha):
    print(Matriz[Linha])#Usamos este looping for para exibir linha por linha e ter uma melhor aparencia.

print('Numero de Linhas: ', len(Matriz))#Quantidade de linhas.
print('Numero de Colunas: ', len(Matriz[0]))#Qauntidade de Colunas. Vamos ver o len() da primeira coluna que define o valor da coluna.
