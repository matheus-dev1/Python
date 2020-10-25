#! python3

#tipos_triangulos

#O programa solicita que o usuario informe tres valores, cada um respectivamente para cada lado de um tringulo depois dos testes com os
#valores obtidos, e feito uma analise para verificar se qual o tipo do triangulo se adqua as valores
#recebidos e posteriomente infomado ao usuario qual o tipo de triangulo vai obetido.

l1 = float(input('Primeiro lado : '))
l2 = float(input('Segundo lado : '))
l3 = float(input('Terceiro lado : '))

if l1 + l2 > l3:
   print ('Formam um triangulo!')
else:
   print('Os valores digitados nao formam um tringulo, tente novamente!')

if l1 == l2 and l1 == l3 and l2 == l3:
   print ('Triângulo Equilátero: três lados iguais!')
   
elif l1 == l2 or l1 == l3 or l2 == l3:
   print ('Triângulo Isósceles: quaisquer dois lados iguais!')

