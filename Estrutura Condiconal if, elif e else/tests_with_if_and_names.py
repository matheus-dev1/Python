#! python3

#tests_with_if_and_names

#O programa solicita ao usuario que digite um nome e uma idade e depois faz teste e retonra um resposta.

name = input('Type your name: ')
age = int(input('Type your age: '))

if name == 'Alice':
  print('Hi, Alice.')

elif age < 12:
   print('You are not Alice, kiddo.')

elif age > 2000:
   print('Unlike you, Alice is not an undead, immortal vampire.')

elif age > 100:
   print('You are not Alice, grannie.')
   
else:
   print ('Fuck all')
