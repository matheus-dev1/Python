#bigger_number

#O maior numero entre tres valores inteiro

N1 = int(input('Digite o primeiro numero: '))
N2 = int(input('Digite o segundo numero: '))
N3 = int(input('Digite o terceiro numero: '))
Maior = N1

if N2 > Maior:
   Maior = N2
if N3 > Maior:
   Maior = N3

print ('Maior numero: ', Maior)
