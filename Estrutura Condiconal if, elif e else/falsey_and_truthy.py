#! python3

#falsey_and_truthy

#O programa solicita ao usuario que digite o seu nome e a quantidade de convidados, se o nome dele
#continuar vazio, o looping nao ira terminar. Se o nome dele conter algum caractere o looping ira
#terminar depois de executar as instrucose.
#O if tambem so sera executado caso o numero digitado seja diferente de Zero ou seja nao seja 0

name = '' #Vazio/Falsey
Guest = 0 #/Falsey
while not name:#Enquanto a variavel name com o valor '' (vazio) != (for diferente) de ''(vazio) com o not
#seria igual a name = '' != '' = False. not False = True
#O looping While sera sempre continuado sempre que NAO TIVER NADA na variavel name.
#Este looping pode ser entendido tambem como, 'Se a variavel name estiver vazia continue o looping'
    name = input('Type your name: ')
    if not name:#Se tiver algum valor ele passa reto, se nao executa o if e volta ao comeco do loop.
        continue
    #Toda linha o while verifica se ele inda continua sendo True.
    Guests = int(input('How many guests are you invite? '))
    if Guests:#Esta intrusao if executara o bloco de instrucoes dele se o valor de Guests for diferente de
              #0 ou seja nao ser 0.
        print('Be sure to have enough room for all your guests. (Truthy)')
    else:
        print('This number is Zero Try again. (Falsey)')
print('Done!')
