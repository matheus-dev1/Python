#! python3

#day_month_year

#O programa solicita ao usuario que digite dia, mes e ano e verifica se mes em que ele digitou possui 29, 30 ou 31 dias. E depois exibi Dia, Mes e Ano.

Day = int(input('Type Day: '))
Mouth = int(input('Type Mouth: '))
Year = int(input('Type Year: '))

Validation = False

#Mes com 31 dias.
if Day >= 1 and Day <= 31 and Mouth >= 1 and Mouth <= 12:
   Validation = True
#Mes com 29 dias.
elif Day >= 1 and Day <= 29 and Mouth >= 1 and Mouth <= 12:
   Validation = True
if Validation == True:
   print ('Valid Date: (',Day, '/', Mouth, '/', Year,')')
else:
   print('Invalid Date, Try Again!')
