#! python3

#fluxo_de_controle_and_if_and_round_function_2

#O programa altera os precos dos produtos confoem a quantidade de kilos em que a pessoa vai 
#comprar, e no final da um resumo com as coisas que a pessoa comprou

print('''__________________________________________________________________
Ola, bem vindo a Frutaria do Seu Joaquin, onde todos sao felizes!
Morango R$ 2,50 por Kg (Até 5 Kg) | R$ 2,20 por Kg (Acima de 5 Kg)
Maçã R$ 1,80 por Kg (Até 5 Kg) | R$ 1,50 por Kg (Acima de 5 Kg)''')

Opcao = int(input("\n" '''Qual fruta o(a) senhor(a) gostaria?
[1] Morango
[2] Maca
[3] Morango e Maca
Digite aqui a sua opcao: '''))

if Opcao == 1:
    Kg = int(input('Quantos kilos de Morango o(s) Senhor(a) gostaria? '))
    if Kg <= 5:
        Morango = 2.50
        Total = Morango * Kg
        print('Quantidade de Kilos: ', Kg)
        print('Valor do Morango referente a quantidade de Kilos: R$', round(Morango, 2))
        print('Total da Compra: R$', int(Total))
    elif Kg > 5:
        Morango = 2.20
        Total = Morango * Kg
        if Kg > 8 or Total > 25:
            Total = Total - 0.1
        print('Quantidade de Kilos: ', Kg)
        print('Valor do Morango referente a quantidade de Kilos: R$', round(Morango, 2))
        print('Total da Compra: R$', int(Total))
elif Opcao == 2:
    Kg = int(input('Quantos kilos de Maca o(s) Senhor(a) gostaria? '))
    if Kg <= 5:
        Maca = 1.80
        Total = Maca * Kg
        print('Quantidade de Kilos: ', Kg)
        print('Valor do Maca referente a quantidade de Kilos: R$', round(Maca, 2))
        print('Total da Compra: R$', int(Total))
    elif Kg > 5:
        Maca = 1.80
        Total = Maca * Kg
        if Kg > 8 or Total > 25:
            Total = Total - 0.1
        print('Quantidade de Kilos: ', Kg)
        print('Valor do Maca referente a quantidade de Kilos: R$', round(Maca, 2))
        print('Total da Compra: R$', int(Total))
elif Opcao == 3:
    KgMorango = int(input('Quantos kilos de Morango o(s) Senhor(a) gostaria? '))
    KgMaca = int(input('Quantos kilos de Maca o(s) Senhor(a) gostaria? '))
    if KgMorango + KgMaca <= 5:
        Morango = 2.50
        Maca = 1.80
        Total = (KgMorango * Morango) + (KgMaca * Maca)
        print('Quantidade de Kilos de Morango: ', KgMorango)
        print('Quantidade de Kilos de Maca: ', KgMaca)
        print('Valor do Morango referente a quantidade de Kilos: R$', round(Morango, 2))
        print('Valor do Maca referente a quantidade de Kilos: R$', round(Maca, 2))
        print('Total da Compra: R$', int(Total))
    elif KgMorango + KgMaca > 5:
        Morango = 2.20
        Maca = 1.50
        Total = (KgMorango * Morango) + (KgMaca * Maca)
        if KgMorango + KgMaca > 8 or Total > 25:
            Total = Total - 0.1
        print('Quantidade de Kilos de Morango: ', KgMorango)
        print('Quantidade de Kilos de Maca: ', KgMaca)
        print('Valor do Morango referente a quantidade de Kilos: R$', round(Morango, 2))
        print('Valor do Maca referente a quantidade de Kilos: R$', round(Maca, 2))
        print('Total da Compra: R$', int(Total))
else:
    print('Opcao invalida. Tente novamente!')
