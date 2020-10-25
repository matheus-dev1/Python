#! python3

#collatz

#Basicamente o programa solicita um numero ao usuario e depedendo se o numero for par ou impar
#ele tera um tratamento, e enquanto ele for diferente de 1
#o programa vai continuar o tratamento do numero ate chegar em 1.

#Como matematica nao e meu ponto forte pegar da internet o conceito nao um grande problema
#o que devemos nos atentar a logica que a gente esta produzindo.

import sys

def collatz(number):
    while number > 1:
        if number % 2 == 0:
            number = number / 2
            print(int(number))
        elif number % 2 == 1:
            number = 3 * number + 1
            print(int(number))
while True:
    try:
        num = int(input('Type a number : '))    
        collatz(num)
    except ValueError:
        print('Invalid Number')
        continue

leave = input()
if leave == 's':
   sys.exit()


