#! python3

#hello_world_and_age_and_name.py

#O programa exibe Hello World e depois pergunta o seu nome e sua Idade.

print('Ola, Mundo!')
#Esse Comentario na expressao acima, mostra a possibilidade de fazer comentario em certar partes
#do programa para apenas executar o que deseja ou apenas, "esconder" certa parte do programa.

print('Whats your name? ')
name = input('Name: ') #Atribui valor do tipo String na variavel Nome.
print('Nice to meet you,', name) #Exibe uma frase e o nome em que o usuario digitou anteriormente.
print('Your name have', len(name),'words!') #A funcao len() conta quantas letras tem a string e
#retorna o numero de letras na forma de Inteiro.
print('Whats your age? ')
age = int(input('Age: ')) #Na propria entrada de Dados nos conseguimos colocar qual vai
#ser o tipo de dados que nos iremos colocar. Neste caso nos vamos pegar a idade do usuario
#depois com a funcao int() ele vai retonar o valor que o usuario digitou em inteiro.
#assim atribuindo a variavel 'age'.
print('You born in', 2020 - age) #Nos nao precisamos usar a funcao str() para retornar a expressao
#dentro do print acima, porem nos temos que usar a virgula(,) e nao o + porque o "+" vai concatenar
#e o print possui dois tipos de valores, de string e inteiros, e nao da pra concatenar dois tipos
#de valores distintos, entao neste caso usaremos a virgula.
print('In one year youll have', age + 1 ,'years old!')
#Ele executa os parenteses de dentro e vai executando os de fota e assun sucetivamente.

leave = input()#Macete usado para dar um enter para o programa encerar.
