#! python3

#all_of_tuple

#O programa mostra diversas forma de se utilizar do tipo de dados Tupla.

tupla = ('Hello', 1, 2, 3.0)#Definindo uma tupla com 4 indices.

lista = ['fuck', 1336, 1.1]#Definindo uma lista com 3 indices.

HSBC = 3#Declarando uma variavel com o valor de 3 do tipo inteiro.

print(tupla)#Exibindo a tupla criada.

print(tupla[0])#Exibindo apenas o primeiro valor da tupla.

print(tupla[1:3])#Exibindo do primeiro ao segundo valor da tupla.

print('Indices da Tupla: ' + str(len(tupla)))#Exibindo a quantidade de indices da tupla.

print(type(('Hello',)))#Ele defini Tupla por que esta entre parenteses e possui uma virgula depois do primeiro caractere. E em seguida o exibe.

print(type(('hello')))#Aqui e uma String normal, ela esta entre parenteses mas ainda e uma String.

print(type((HSBC)))#O tipo de dado que esta armazenado nesta variavel e do tipo inteiro.

print(str(55454545454))#Tranformou o que seria uma variavel em um valor de String e assim exibiu na tela.

print(tuple(lista))#Transformar o valor da variavel lista que e uma lista em uma tupla.

print(list(tupla))#Trasmaformar o a variavel Tupla que possui o tipo de dado Tupla em o tipo de dado de Lista.

print(tuple('Hello'))#Transofomar a String 'hello' em uma tupla.

print(list('Bom dia'))#Transformar bom dia em uma lista.

#tupla[0] = 'Chama' \\ #erro o tipo de dado tupla e um dado imutavel entao nao pode ser alterado apenas sobrescrito.

#############TESTANDO DADOS IMUTAVEIS############

#tupla2 = (1, 2, 3) // Tratando-se de um valor de tupla e ser imutavel nos nao podemos fazer alteracao.

#tupla3 = tupla2 // Mas podemos passar seus valroes a outra varaivel ja que os valores sao realmente da variavel e nao uma referencia. 

#tupla3[0] = 'One' // Isso nao pode ser feito porque o tipo de dado tupla nao pode ser alterado apenas sobrescrito.
