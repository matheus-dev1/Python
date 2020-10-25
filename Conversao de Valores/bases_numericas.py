#! python3

#bases_numericas.py

#O programa deve conver um numero na base 10 para a base binario, octal ou hexadecimal.

#TODO:

num = int(input("Digite um numero inteiro: "))

opcao = int(input('''
[1] Converter para Binario.
[2] Converter para Octal.
[3] Converter para Hexadecimal.
[None] Opcao Invalida.
Escolha uma Opcao: '''))

if opcao == 1:
    print("O numero %s convertido para Binario e igual a %s" %(num, bin(num)))
    #A funcao bin() converte um numero inteiro para binario.
elif opcao == 2:
    print("o numero %s convertido para Octal e igual a %s" %(num, oct(num)))
    #A funcao oct() converte um numero inteiro para octal.
elif opcao == 3:
    print("O numero %s convertido para Hexadecimal e igual a %s" %(num, hex(num)))
    #A funcao hex() converte um numero inteiro para hexadecimal.
else:
    print("Opcao invalida!")