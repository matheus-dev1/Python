#! python3

#Password

import os

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Ler e escrever em arquivos\Password')

passwordFile = open('SecretPassword.txt')
secretPassword = passwordFile.read()
TypedPassword = input('Enter your password: ')
if TypedPassword == secretPassword:
    print('Acess Granted!')
    print(secretPassword)
    if TypedPassword == '12345':
        print('Idiot Password!')
else:
    print('Acess Denied!')
