#1 python3

#magic_8_ball_with_lists

#O programa mostra uma entre as 6 mensagens.

import random

Magic8Ball = ['Fuck you 1',
'Fuck you 2',
'Fuck you 3',
'Fuck you 4',
'Fuck you 5',
'Fuck you 6']

print('Message:',Magic8Ball[random.randint(0, len(Magic8Ball) - 1)])
#Temos que tirar um do valor do len porque a lista interpreta os valores de 0 a 5 e nao de 0 a 6 isso da um
#numero a mais e por isso temos que apagar 1 mas colocamos como valor de inicio 0.
