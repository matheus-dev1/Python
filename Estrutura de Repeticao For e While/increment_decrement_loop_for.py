#! python3

#increment_decrement_loop_for

#O programa solicita ao usuario se ele deseja mostrar os numero dentro do loop de modo positivo ou negativo.

#1. Valor do inicio da variavel number.
#2. O valor maximo que a variavel number pode chegar.
#3. o valor do incremento da variavel number.

opc = input('Show numbers Negative or Positive? [N/P/R]: ')
if opc == 'P' or opc == 'p':
    print('Number 4 to 100, incrementing 2')
    for number in range(4, 100, 2):
        print(number)
        
elif opc == 'N' or opc == 'n':
    print('Number 4 to - 100, decrementing -2')
    for number in range(-4, -100, -2):
        print(number)

elif opc == 'R' or opc == 'r':
    result = 0
    for number1 in range(101):
        result = result + number1
        print(result)

    result2 = 0
    number2 = 0
    while number2 < 101:
        result2 = result2 + number2
        number2 = number2 + 1
        print(result2)
