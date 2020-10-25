#! python3

#media_alunos

#O programa solicite que entre com duas notas e posteriomente calcula sua media e exibi a situacao, conceito e media.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media >= 9.0 and media <= 10.0:
   msg = 'Aprovado'
   conce = 'A'
elif media >= 7.5 and media <= 9.0:
   msg = 'Aprovado'
   conce = 'B'
elif media >= 6.0 and media <= 7.5:
   msg = 'Aprovado'
   conce = 'C'
elif media >= 4.0 and media <= 6.0:
   msg = 'Reprovado'
   conce = 'D'
elif media <= 4.0 and media >= 0.0:
   msg = 'Reprovado'
   conce = 'E'
else:
   print ('Dados invalido. Tente novamente!')

print ('Primeira Nota: ', nota1)
print ('Segunda Nota: ', nota2)
print ('Conceito da Media: ', conce)
print ('Situacao Final: ', msg)
