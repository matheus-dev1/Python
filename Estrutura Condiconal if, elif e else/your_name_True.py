import sys

#A lista argv e o aonde armazena e recebe o valor digitado pelo usuario atraves da linha de comando.

if len(sys.argv) >= 3 : #Esta linha significa que se possui 3 ou mais agumentos execute este bloco.
    print(sys.argv[0]) #Sera o proprio nome do arquivo Python
print(sys.argv[1]) #O primeiro argumento passado para programa atraves de um argumento da linha de comando passado pelo usuario.
print(sys.argv[2]) #Segundo Argumento
Leave = input()
