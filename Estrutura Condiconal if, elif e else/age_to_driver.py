#! python3

#age_to_driver

#O programa solicita que o usuario digite a sua idade e depois retornar se voce ou nao tirar uma carta de motorista.

idade = int(input('Digite a sua Idade: '))
if idade >= 18: #Resultado Boleano, se for true executa a primeira clausula
   print ('voce e maior de idade, pode dirigir!')
else: #Se for falso executa a segunda clausula
   print ('Voce e menor de idade, nao pode dirigir!')
