#! python3

#collatz2

#O programa solicita ao usuario que digite o valor 1 ou qualquer outro. Caso seja um ele entrara em um looping que fara uma soma de 0 a 100a ate chegar
#em 5050 e caso ele digite qualquer outro caractere vai fazer o calculo 50 * 101 que chega ao mesmo resultado.

print('Sum of 0 to 100')
opc = int(input('Type [1] or [any other number]: '))
if opc == 1:
    total = 0
    for number in range(101):
        total = number + total
else:
    total = 50 * 101 #E * 101 porque nos somamos 101 numeros contando com o ZERO.
print(total)
