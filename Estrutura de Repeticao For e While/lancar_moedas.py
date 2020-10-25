#! python3

#lancar_moedas.py

#O programa consiste no usuaio digitar 1 para heads ou 0 para tails e vai ter uma random para entre 1 e 0
#se cair no numero em que o usuario digitou ele sera exibido uma mensagem sobre qual foi a lado que caiu e se ele acertou.

#TODO: Trying love programming! It's work :)

import random

guess = ''

while True:
   #Heads = Cara (1)
   #Tails = Coroa (0)
   #Esta intrucao while significa que entao gues nao
   guess = int(input('Guess the coin toss! Enter Heads [1] or Tails [0]: '))
   if guess == 1:
      print('You choose Heads [1]')
   elif guess == 0:
      print('You choose Tails [0]')
      
   toss = random.randint(0, 1)
   if toss == guess:
      #Se o numero em que eu digitei ([Cara - 1] ou [Coroa - 0]) nao for o que deu no random, ele ira pro else.
      if toss == 1:
         print('Heads. You got it!')
         break
      elif toss == 0:
         print('Tails. You got it!')
         break
      
   elif toss != guess:
      if toss == 1:
         print('Heads. Guess again!')
         continue
      elif toss == 0:
         print('Tails. Guess again!')
         continue
      
