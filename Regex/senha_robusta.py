#! python3

#senha_robusta

#O programa deve identificar se a senha em que o usuario colocou atende aos requisitos para 
#ser considerada uma senha robusta.

import re, pyperclip

def senha_robusta(senha_try_argv):
    correct_senha = re.compile(r'''([a-z]|[A-Z]|[!|@|#|_]|[0-9]){8,256}''', re.VERBOSE)
    senha_corrigida = correct_senha.search(senha_try_argv)
    print(senha_corrigida)
    if senha_corrigida == None:
        print('Senha nao atende aos requisitos, tente novemente.')
        return 'Senha invalida, tente novamente'
    else:
        senha_corrigida_1 = senha_corrigida.group()
        print('Sua senha e valida e foi passada para o seu clipboard')
        pyperclip.copy(senha_corrigida_1)
        return senha_corrigida_1
    
senha_try = input('''Sua senha deve conter pelo menos oito (8) caracteres
Deve ter no minimo uma (1) letra maiuscula
Deve ter pelo menos um (1) numero e um (1) caractere especial
Digite sua senha aqui: ''')
#Senha exemplo: Matheus_1

senha_aplicavel = senha_robusta(senha_try)

print('Sua senha: ' + senha_aplicavel)
