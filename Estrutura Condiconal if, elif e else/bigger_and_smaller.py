#! python3

#bigger_and_smaller

#Maior e menor numero de tres numero digitados pelo usuario.

#Faça um Programa que leia três números inteiros, em seguida mostre o maior e o menor deles.

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

maior = n1 #Encontrando o maior numero!

if n2 > maior:
   maior = n2
if n3 > maior:
   maior = n3

print('Maior numero:', maior)

menor = n1 #Encontrando o menor numero!

if n2 < menor:
   menor = n2
if n3 < menor:
   menor = n3

print('Menor numero:', menor)
