#! python3

#import

#Programa que importa random da maneira que nao precisa usar o prefixo random.
#Em em seguinda usar um for que exibi 5 numero aleatorios entre 1 e 10.

#Para instalar modulos de Terceiros, nos precisamos ir ate o CMD ou PowerShell e colocar pip
#install 'Nome do Modulo'

#IMPORTANTE Ctrl + Espaco te da todas as funcionalidade de algum, modulo, import e qualquer
#outra funcionalidade do python ou de terceiros.

# BAIXAR MODULO 'import emoji' #Nos importamos emoji da forma em que nos precisamos utilizar o seu prefixo.

import sys #Nos importamos todo o modulo sys e necessitamos de usar o prefixo.

from random import * #Com essa forma da instrução import, as chamadas às funções em random não precisarão
#do prefixo random. Porem a gente pode definir o que a gente quer chamar deste modulo.

#import random, sys, os, math. Possibilidade de importar quadro modulo em apenas uma linha.

from math import sqrt# Importante apenas a funcao de raiz quadrada do modulo math. O modulo de Matematica.

for random_number in range(5): #Range com o valor final, isso significa que o for vai rodar 5 vezes do 0 ao 4
    print(randint(1, 10)) #gera um numero aleatorio entre 1 e 10.

print('Raiz quadrada de 10: ' + str(sqrt(10)))# Raiz quadrada de 10.

# BAIXAR MODULO print(emoji.emojize('Hello :earth_americas:!', use_aliases = True))

Leave = input('Press Enter To Close: ')
if Leave == '':
    sys.exit()

