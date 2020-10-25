#! python3

#rede_social

#O programa tem um menu que tem as opcoes para registrar um usuario na rede social, outra para acessar a rede social(em construcao)
#e outro para acessar os dados do usuario

#Variaveis
name_User = ''
age_User = ''
email_User = ''
password_User = ''
User_Create = 0

def MenuCall():
    global name_User, age_User, email_User, password_User, User_Create
    Menu = input('''Welcome to Programmer Hub's Home

[1] Register
[2] My Data
[3] Access
[ ] to Leave
Write something: ''')
    if Menu == '1':
        while True:#Nome
            name_User = input('Enter you name (Letters only): ')
            if name_User.isalpha():#Apenas letras.
                break#Vai para o proximo looping.
            else:
                print('Please enter letters only.')
                continue#Volta para fazer a pergunta novamente.
            
        while True:#idade
            age_User = input('Enter you age (Numbers only): ')
            if age_User.isdecimal():#Se a String for constituida apenas de numeros do tipo inteiro.
                break#Vai para o proximo looping
            else:
                print('Please enter numbers only.')
                continue#Vata para fazer a pergunta novamente.
            
        while True:#E-mail
            email_User = input('Enter your E-mail: ')
            if email_User == '':#Se a variavel estiver vazia, ela volta a fazer a pergunta.
                print('Invalid E-mail. Try Again.')
                continue
            else:
                break#Se nao termina o looping.
            
        while True:#Senha
            password_User = input('Enter your password (Letters and Numbers Only and 8 characteres minimum or more.): ')
            if password_User.isalnum() and len(password_User) >= 8:
                #Se a senha em que eu digitei conter apenas letras e numeros e ainda possui
                #menos que 8 caracteres, sera aprovado e o looping sera quebrado.
                 break
            elif len(password_User) < 8:#Se possui menos que 8 caracteres a senha ele retonara tudo novamente.
                print('Short password. Try again.')
                continue
            elif password_User.isalnum() == False:#Se a Senha nao possuir apenas letras e numero ele ira mandar uma mensarem de erro e ira
                # retornar para voce tentar novamente.
                print('Enter a valid password!')
                continue
            
        print('User Registred!')#Mostra que o registo deu certo e volta ao menu.
        User_Create = 1
        MenuCall()
        
    elif Menu == '2':
        if User_Create == 1:
            print('')
            print('Name User:',name_User)
            print('Age User:',age_User)
            print('email User:',email_User)
            print('Password User:',password_User)
        else:
            print("User doesn't create. Create and try again")
        MenuCall()
        
    else:
        print('Invalid Option. Try again.')
        MenuCall()
        
MenuCall()
