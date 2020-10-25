#! python3

#soma_yes_not

#O programa solicita dois numero ao usuario faz soma e depois mostra o resultado. Nofinal ele pergunta se voce quer fazer outra soma.
#Caso sim o programa continua e retorna ao inicio do looping, caso nao ele encera o programa, caso nenhuma deste dois valores forem escolhidos,
#o programa mostra uma mensagem de erro e volta ao inicio do programa.

while True:#(Truthy)
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    soma = n1 + n2
    print('Soma de',n1,'+',n2,'e igual a',soma)#A virgula ela faz que com voce possa adicionar um novo tipo de dado e pula um caractere
    sair = input('Deseja fazer outra soma? [S/N]')
    if sair == 'n' or sair == 'N':
        break
    elif sair == 's' or sair == 'S':
        continue
    else:
        print('Dado invalido. Tente novamente!')
        continue
