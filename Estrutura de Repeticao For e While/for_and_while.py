#! python3

#for_and_while

#O programa representa 10 numeros na tela com o looping while ou for.

opc = int(input('''[1] While
[2] For
[3] Name with For
[4] For com tres argumentos
Type your answer: '''))

if opc == 1:
    valor = 0
    while valor < 10:#While somando
        print(valor + 1)
        valor = valor + 1
        
elif opc == 2:#For subtraindo
    valor = 10
    for valor in range(0, -10, -1):#
        print(valor - 1)
elif opc == 3:
    print('My name is \|/')
    for nameNumber in range(5):
        print('Matheus de Oliveira Silva (' + str(nameNumber + 1) + ')')
elif opc == 4:
    for number in range(4, 74, 2):
        print(number)
