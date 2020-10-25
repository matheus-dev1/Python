#Thruly

#O programa importa o modulo sys, abre um loop thruly com while que so pode ser quebrado com a funcao break ou sys.exit() dentro do bloco de instrucoes. 

import sys

while True: #Thruly
    res = input('Type "Exit" to exit: ')
    if res == 'exit' or res == 'Exit' or res == 'EXIT':
        print('You typed: "' + res + '".')
        #o + ele apenas adcionas mais alguma coisa no print, a virgula(,) ela adiciona mais alguma coisa e pula uma linha.
        sys.exit()
    print('You typed: "' + res + '".')
