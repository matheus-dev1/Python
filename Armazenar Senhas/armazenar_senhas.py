#! python3

#Armazenar_senhas

#O programa associa os nome associados a uma senha armazenados em um dicionario.

import sys, pyperclip
#A variável sys.argv nada mais é do que uma lista chamada atraves do metodo sys.

#Para passar um argumento em um programa deve dar um espaco mais o argumento. Exemplo: armazenar_senhas email

#Quando chamamos um programa atraves de um terminal ou o Run(Executar / Win-R) nos estamos passando um argumento, o argumento no caso e o nome do
#proprio programa, entaose agente da um espaco e colocamos mais alguma coisa a gente esta pssando outro argumento, e
#assim a variavel sys.argv funciona.

account = 'Without Argument'#Onde vamos armazenar o nosso segundo argumento.

passwords = {'email': 'email_sdpkiojhsdaifhsad',
            'blog': 'blog_phfusdapihfsdap9hf',
            'luggage': 'luggage_sjklhfsdajkflh',
             'ola': 'mundo'}#Os 4 possiveis argumento que podemos chamar.

print('Variavel sys.argv (Primeiro argumento): ' + str(sys.argv))

if len(sys.argv) < 2:
    print('Usage: Python Armazenae_senhas.py [' + account + ']')
    sys.exit()
#O que isso estas tres linhas quer dizer?
#Se quando chamarmos o programa, apenas houver o argumento do proprio programa ou seja (armazenar_senhas.py) ele exibira esta mensagem e vai
#fechar o program proque, nos nao queremos apenas um argumento durante a chama do programa. Queremos o segundo que vai nos retonar uma imformacao
    
account = sys.argv[1]#sys.argv e o segundo arumento que voce digitou na hora de chamar o programa. Obs: O nome do proprio programa e um argumento

if account in passwords:
#Se o argumento passado na hora de abrir o programa estiver em conta, ele vai pegar o valor da chave do dicionario e passar para oseu Ctrl-C
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to Clipboard.')
else:
    print('There is no account named ' + account)
