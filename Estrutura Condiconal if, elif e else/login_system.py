#! python3

#login_system

#O programa solicita ao usuario que digite o seu login e senha, caso esteja corretos ele ira acessar e exibir uma mensagem com o seu nome.

error = 0
print('Digite o nome e senha corretos para logar!')
while True:
    name = input('Digite o seu nome: ')
    password = input('Digite a sua senha: ')
    if name == 'Matheus' or name == 'matheus':
        if password == '123':
            print('Bem Vindo ',name)
            break
        elif password != '123':
            error = error + 1
            continue
            if error == 3:
                print('Acesso negado!')
