#! python3

#if_inside_a_if

#O programa solicita ao usuario um numero que vai ser feito teste logico e acontece algo conforme a respota dada.

spam = int(input('Type a number: ')) #Declarando variavel spam e lendo.

if spam > 10: #(if - 1)#Abrindo o if - 1
  print('eggs')#Dentro do if - 1 #Primeiro Bloco

  if spam == 10: #(if - 2)  #Dentro do if - 1 e abre o if - 2
    print('bacon')#Dentro do if - 2

  else: #(else - 1)#Abrindo o else - 1
    print('ham')#Dentro do else - 1
    #O segundo Bloco esta entre o if - 2 e else - 1, porque apenas um deles sera executado.

  print('spam1')#Dentro do if - 1 e fora do if - 2 e else - 1 #O Spam1 ocorre quando o if - 1 e True.
  #Terceiro Bloco 

print('spam2')#Fora de qualquer if.
