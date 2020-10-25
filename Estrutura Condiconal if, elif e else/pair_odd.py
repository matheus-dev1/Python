#! python3

#pair_odd

#O programa solicita ao usuario que ele digite um numero, e depois e feito um teste se o numero e Par ou impar

Number = int(input('Type a number: '))

if Number % 2 == 0:
   print(Number, 'is Pair!')
else:
   print(Number, 'is Odd!')
