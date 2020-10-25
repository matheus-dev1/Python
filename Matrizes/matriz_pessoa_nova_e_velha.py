#! python3

#matriz_pessoa_nova_e_velha

#o programa exibe 10 nomes e idades em forma de lista. Basicamente e uma Matriz de 10 x 2.

Matriz = []

for Linha in range(10):
    criar_Linha = []
    criar_Linha.append(input('Type ' + str(Linha + 1) + ' person name: '))
    criar_Linha.append(int(input('Type ' +  str(Linha + 1) +  ' person age: ')))
    Matriz.append(criar_Linha)

pessoa_nova = Matriz[0][0]
idade_nova = Matriz[0][1]
for Linha in range(10):
    for Coluna in range(2):
        if idade_nova > Matriz[Linha][1]:
            idade_nova = Matriz[Linha][1]
            pessoa_nova = Matriz[Linha][0]
            
for Linha in range(10):
    print(Matriz[Linha])

print('Pessoa mais nova: ', pessoa_nova)
print('Idade da pessoa mais nova: ', idade_nova)


    
