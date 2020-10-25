#! python3

#banco_e_qtd_notas

#O programa inicia exibindo algumas informacoes ao usuario que restringe que ele insira certas quantias, depois que ele coloca o valor com suas
#limitacoes, se a operacao der certo ele ira apresentar ao usuario o dinheiro sacado, a quantidade de cada nota e uma mensagem de agradecimento.

print('Welcome to Bradesco Bank!')

saque = int(input('''Valor minimo de saque: R$: 10
Valor Maximo de saque: R$: 600
Notas Disponiveis: R$: 1/5/10/50/100
Digite o valor do saque: '''))

if saque >= 10 and saque <= 600:
#Processamento dedos para pegar quantas notas de 100 possui no valor digitado!
    cem = saque / 100 #Exemplo 550 divido por 100 daria 5 entao sabemos que temos 5 centenas!
    saque = saque % 100
    #Exemplo 55 resto da divisao por 100 e igual a 50, entao isso e o que sobrou para testat com os valores a partir de 50 reais.

    cinquenta = saque / 50#50 Dividido por 50 da 1 entao temos uma nota de 50
    saque = saque % 50# Nao temos mais nada entao fica 0

    dez = saque / 10#Neste exemplo acabou o dinheiro entao todos os outros teste serao zero. 
    saque = saque % 10

    cinco = saque / 5
    saque = saque % 5

    um = saque

    #No final ele ira aprensentar 5 notas de 100 e 1 nota de 50.
    print('Notas de R$100,00 = ',int(cem))
    print('Notas de R$50,00 = ',int(cinquenta))
    print('Notas de R$10,00 = ',int(dez))
    print('Notas de R$5,00 = ',int(cinco))
    print('Notas de R$1,00 = ',int(um))
    print('Obrigado, a Bradesco agradece!')

elif saque < 10:
   print('Saque com o valor menor que 10. Tente novamente!')
else:
   print('Saque com o valor maior que 600. Tente novamente!')
