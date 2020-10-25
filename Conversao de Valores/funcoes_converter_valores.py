#! python3

#funcoes_converter_valores

#O programa vai usar as funcoes str(), int() e float() para transformar outros valores nos valores em que nos
#desejamos.


print(str(43)) #Vai converter o valor 43 que e do tipo inteiro para String ficando assim: '43'.

print(str(-1.54))

print(int('100')) #Vamos pegar um numero que esta na forma de String e vamos converter em inteiro e assim
#exibir.

print(int(7.45))

print(float(12)) #O valor do tipo inteiro contido na funcao float() sera convertido para um numero do tipo
#flutuante.

print(float('5.44'))

string_number = input('Type a String number: ')

print('Number String: ' + string_number)

integer_number = int(input('Type a Integer Number: '))

print('Integer Number: ', integer_number)

print('x3: ', integer_number * 3)

#ERRO int('99.99') #Nao podemos arredondar um string com escrita como se fosse um float.

print(int(8.7) + 1)# Transfomar o numero float em int e depois soma ficando 9.7 e exibindo apenas o 9 nao
#nao possui arredondamento.
