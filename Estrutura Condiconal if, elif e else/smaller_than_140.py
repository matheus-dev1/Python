#! python3

#smaller_than_1000

#O programa solicita ao usuario que digite um numero menor que 1000, e depois mostra as centenas, dezenas e unidades dentro do numero digitado!

Number = int(input('Type one Integer Positive Number less than 1000: '))

if Number < 1000:
   Unit = Number % 10 #Coletando a unidade do valor digitado!
   Number = (Number - Unit) / 10 #Eliminando a unidade do ultimo numero!
   Ten = Number % 10 #Coletando a dezena!
   Number = (Number - Ten) / 10 #Eliminando a dezena do numero original, fica a centena!
   Hundred = Number

   print(int(Hundred), ' centena(s) ', int(Ten), 'dezena(s) ', int(Unit), ' unidade(s)')

else:
   print(Number, 'e maior que 1000. Tente novamente!')
