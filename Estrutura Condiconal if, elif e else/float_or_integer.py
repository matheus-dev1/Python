#! python3

#float_or_integer

#O programa solicita ao usuario que digite um numero e postiormente e verificado se o numero digitado e inteiro ou flutuante.

Number = float(input('Type a Number: '))

if Number == int(Number):#O truque deste programa e que todos os valores float que tiverem .0 depois do numero
                         #sao numero inteiros entao se eu digitar 45.0 e um numero inteiro se eu digitar
                         #45.1 e um numero float.
    print(int(Number), ' = Integer')
else:
    print(Number, ' = Float')
