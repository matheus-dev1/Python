#aumento_salario

#o programa solicita o valor do salario atual assim aplica um aumento confome o valor anterior e no final exibi o salatio anterior e depois a quantidade que foi aumentado
# e a soma do aumento com o salario anetrior que torna o salario atual.

salario = float(input('Digite o valor do salario: '))

if salario <= 280:
   porcentagem = 20
elif salario <= 700:
   porcentagem = 15
elif salario <= 1500:
   porcentagem = 10
elif salario > 1500:
   porcentagem = 5
else:
   print('Invalido tente novamente!')

print ('Salario antes do reajuste: ', salario)
print ('Percentual do salario: ', porcentagem)

porcentagem = porcentagem / 100.0#Aqui definimos que sera uma porcentaegem
aumento = salario * porcentagem#Aqui pegamos a porcetagem que devemos aumentar em cima do salario
salAumento = aumento + salario#Juntanmos o valor do aumento com o salario e armazenamos na varaivel do salario com o aumento.

print ('Valor aumentado: ', aumento)
print ('Salario aumentado:  ', salAumento)
