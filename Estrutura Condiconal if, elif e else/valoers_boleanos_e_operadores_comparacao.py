#! python3

#controle_de_fluxo

#O programa trata-se de usos de valores boleanos.

x = 100

spam = True

print(spam)

#ERRO print(true) #True e com letra maiuscula.

#ERRO True = 2 + 2 # Da errado porque o True e um nome proprio e 4 + 4 e uma expressao que vai reduzir a
#um valor inteiro e nao um valor boleano (True ou false).

print(42 == 42) #Temos que pensar que o programa esta tentando afirmar isso.

print(3 != 3)

print('Hello' == 'Hello')

print(42 == '42')

print(42 != 42.0) #False.

print(42 < 100) #True

print(42 > 42) #False

print(x > 99)# True.

print(x >= 100) #True

print(x <= 98) #False

print (True and True) #igual a True

print(True and False) #Igual False

print(True or False) #True

print(False or False) #False

print(True or True) #True.

print(not True) #False

print(not False) #True

print(4 < 5 and 5 < 6) #True

print(4 != 3 or 5 <= 5) #True

print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
#Ordem de precedencia dos operadores, primeiro os operadores matematicos, depois os operadores de comparacao
#depois os operadores not e depois o operador and e por fim o operador or.
option = int(input('''[1] One, Two, Three
[2] if and elif
[3] Loop While 1
[4] Loop While 2
[5] Loop while 3
[6] Loop While 4
[6] Loop While 5
[7] loop While 6
Type your answer: '''))

if option == 1:
    number = int(input('Type a number: '))
    if number == 1:
        print('One')
    elif number == 2:
        print('Two')
    elif number == 3:
        print('Three')
    else:
            print('Invalid Number!')

elif option == 2:
    #A ordem dos elif importa. Segue um codigo com um bug.
    name = input('Type a name: ')
    age = int(input('Type a age for him: '))
    if name == 'Alice':
        print('Hi, Alice.')
    elif age < 12:
        print('You are not Alice, kiddo.')
    elif age > 100:
        print('You are not Alice, grannie.')
    elif age > 2000:
        print('Unlike you, Alice is not an undead, immortal vampire.')
#Caso a variavel Age possuio um valor de 3000 por exemplo ira causar um error porque provavelmente voce
#vai querer o valor de 3000 para executar o ultimo elif mas na realidade vai executar o segundo porque
#age sendo 3000 essa condicao e verdadeira e todas as outras sao ignoradas.

elif option == 3:
    g = 0
    print('g'"\n")
    if g < 5:
        print(g + 1)
        g += 1

elif option == 4:
    t = 0
    print('f'"\n")
    while t < 4:
        print(t + 1)
        t += 1
elif option == 5:
    name = ''
    while name != 'your name':
        name = input('Type your name: ')
    print('Thank you.')

elif option == 6:
    while True: #Quando usamos while True a gente naturalemente cria um looping infinito entao a gente precisa
        #usar o break para quebrar este looping de forma impulsiva.
        name2 = input('Type your name: ')
        if name2 == 'your name':
            print('Thank you')
            break
elif option == 7:
    loginUser = 'Matheus'
    passwordUser = '123'
    print('Hello please, login your account.'"\n")
    while True:
        login = input('Enter your login: ')
        password = input('Enter your password: ')
        if login == loginUser and password == passwordUser:
            print('Access Granted!')
            break
        else:
            print('Incoherent information. Try Again.')
            continue
else:
    print('Invalid Option!')
