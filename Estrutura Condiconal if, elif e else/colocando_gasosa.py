#colocando_gasosa

#O programa comforme a quantidade de litros o recebe um disconto por litro.

Opcao = int(input('Opa, como vai chefia?' "\n" '[1] Alcool ' "\n" '[2] Gasolina' "\n" 'Vai de que hoje? '))

Alcool = 1.90
Gasolina = 2.50

if Opcao == 1: #Opcao do Alcool
    Litros = int(input('Quantos litros de Alcool chefia? '))
    if Litros <= 20:
        Total = (Litros * Alcool) - 0.03
        print('Quantidade de Litros: ', Litros)
        print('Valor do Litro do Alcool: ', Alcool)
        print('Quantidade de desconto: 3%')
        print('Total a ser pago: ', Total)
        print('Obrigado, volte sempre!')
    if Litros > 20:
        Total = (Litros * Alcool) - 0.05
        print('Quantidade de Litros: ', Litros)
        print('Valor do Litro do Alcool: ', Alcool)
        print('Quantidade de desconto: 5%')
        print('Total a ser pago: ', Total)
        print('Obrigado, volte sempre!')
elif Opcao == 2: # Opcao da Gasolina
    Litros = int(input('Quantos litros de Gasolina chefia? '))
    if Litros <= 20:
        Total = (Litros * Gasolina) - 0.04
        print('Quantidade de Litros: ', Litros)
        print('Valor do Litro da Gasolina: ', Alcool)
        print('Quantidade de desconto: 4%')
        print('Total a ser pago: ', Total)
        print('Obrigado, volte sempre!')
    if Litros > 20:
        Total = (Litros * Gasolina) - 0.06
        print('Quantidade de Litros: ', Litros)
        print('Valor do Litro da Gasolina: ', Alcool)
        print('Quantidade de desconto: 6%')
        print('Total a ser pago: ', Total)
        print('Obrigado, volte sempre!')
else:
    print('Valor invalido. Tente novamente!')
