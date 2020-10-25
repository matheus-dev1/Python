#! python3

#advinhar_while_break_continue_e_if_elif

#Basicamente o jogo te fala que possui um numero de 1 a 20 e voce tem que acertar, quando voce da
#uma tentativa, voce recebe uma frase que corresponde se voce acertou ou errou, e tem varias
#frases que sao aleatoria de cair quando uma situacao acontece.

import random

print('I am thinking of a number beetwen 1 to 20!')
tries = 0 #Quantidade de tentativas comecando pelo Zero.
numberSecret = random.randint(1, 20)#Numero aleatorio gerado.

while True:
    opc = int(input('Take guess: '))#usuario vai tentar o numero.
    if opc == numberSecret:#se for o numero correto ele vai executar este bloco e para o while.
        print('You got damn right!')
        break
    elif opc < numberSecret:
        generator = random.randint(1, 3)
        if generator == 1:
            print('Your guess is Low')
        elif generator == 2:
            print('Think e try again')
        elif generator == 3:
            print('Just Little more... or less...')
        tries = tries + 1
        continue
    elif opc > numberSecret:
        generator = random.randint(1, 3)
        if generator == 1:
            print('Your guess is High')
        elif generator == 2:
            print('Think e try again, oohhh you close!')
        elif generator == 3:
            print('Just Little more... or less...')
        tries = tries + 1
        continue
print('Number of Tries: ', tries,'. The Secret number: ',numberSecret)
