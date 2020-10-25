#! python3

#Password

passwordFile = open('SecretPassword.txt')
secretPassword = passwordFile.read()
TypedPassword = input('Enter your password: ')
if TypedPassword == secretPassword:
    print('Acess Granted!')
    if TypedPassword == '12345':
        print('Idiot Password!')
else:
    print('Acess Denied!')
