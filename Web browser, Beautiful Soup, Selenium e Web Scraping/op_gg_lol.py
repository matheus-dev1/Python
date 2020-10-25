#! python3

#op_gg_lol.py

#O programa deve pesquisar nos principais sites de lol sobre runas e builds sobre determinado campeao.

#TODO:

import webbrowser, sys
#Imports necessarios.

if len(sys.argv) < 2:
    #Menos que dois argumento na chamada do programa, exibe um print.
    print('Digite um site.')
elif len(sys.argv) == 2:
    #Apenas dois argumentos na chamada do progrma exibe outra mensagem.
    print('Digite o campeao que deseja buscar.')
elif len(sys.argv) == 3:
    #O argumento na chama igual a 3 executa o bloco de comandos a baixo.
    site = sys.argv[1]
    #Armazena o valor do primeiro argumento em "site".
    champion = sys.argv[2]
    #Armazena o valor do segundo argumento em "champion".
    if site.lower() == 'opgg':
        #se o site pasado como primeiro argumento for opgg, entao ele abrira o site do op.gg + no nome do terceiro argumento.
        webbrowser.open('https://na.op.gg/champion/' + champion)
        #Abrir o navegador na pagida do campeao em que o usuario digitou.
    else:
        print('site nao cadastrado.')
        #Se site nao for igual a op.gg entao ele ira exibir esta mensagem.