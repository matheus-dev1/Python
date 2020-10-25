#! python3

#fluxo_de_controle_and_if_and_round_function

#O programa mostra os valores de seus produtos e seus decontos conforme a quantidade que o cliente compra
#e depois ele faz uma nota fiscal com todas as informacoes da compra.

print('''_______________________________________________________________________
O Hipermercado Tabajara esta com promocoes incriveis!
File Duplo R$ 4,90 por Kg (Até 5 Kg) | R$ 5,80 por Kg (Acima de 5 Kg)
Alcatra R$ 5,90 por Kg (Até 5 Kg) | R$ 6,80 por Kg (Acima de 5 Kg)
Picanha R$ 6,90 por Kg (Até 5 Kg) | R$ 7,80 por Kg (Acima de 5 Kg)''' "\n")

Tipo = int(input('Qual carne o(a) Senhor(a) deseja?' "\n"
                      '[1] File Duplo.' "\n"
                      '[2] Alcatra.' "\n"
                      '[3] Picanha.' "\n"
                      'Digite sua opcao aqui: ' ))

Pagamento = int(input("\n" 'Formas de Pagamento: ' "\n"
                           '[1] Cartao Tabajara (Desconto de 5%)' "\n"
                           '[2] Nota ou Cartao (Valor Original)' "\n"
                           'Digite sua opcao aqui: '))
if Tipo == 1:
    TipoCarne = 'File Duplo'
    Kg = int(input('Digite a quantidade de File Duplo em Kg: '))
    if Kg <= 5:
        ValorCarne = 4.90
    elif Kg > 5:
        ValorCarne = 5.80
    if Pagamento == 1:
        TipoPagamento = 'Cartao Tabajara'
        Desconto = (Kg * ValorCarne) * 0.05
        Total = (Kg * ValorCarne) - Desconto
    elif Pagamento == 2:
        TipoPagamento = 'Nota ou Cartao'
        Desconto = 0
        Total = Kg * ValorCarne

    print('*******Nota Fiscal*************')
    print('Tipo do Produto: ', TipoCarne)
    print('Quantidade de ', TipoCarne, ': ', Kg)
    print('Tipo do Pagamento ', TipoPagamento)
    print('Valor do Desconto: ', round(Desconto, 3))
    print('Total a Pagar : ', Total)

elif Tipo == 2:
    TipoCarne = 'Alcatra'
    Kg = int(input('Digite a quantidade de Alcatra em Kg: '))
    if Kg <= 5:
        ValorCarne = 5.90
    elif Kg > 5:
        ValorCarne = 6.80
    if Pagamento == 1:
        TipoPagamento = 'Cartao Tabajara'
        Desconto = (Kg * ValorCarne) * 0.05
        Total = (Kg * ValorCarne) - Desconto
    elif Pagamento == 2:
        TipoPagamento = 'Nota ou Cartao'
        Desconto = 0
        Total = (Kg * ValorCarne)

    print('*******Nota Fiscal*************')
    print('Tipo do Produto: ', TipoCarne)
    print('Quantidade de ', TipoCarne, ': ', Kg)
    print('Tipo do Pagamento ', TipoPagamento)
    print('Valor do Desconto: ', round(Desconto, 3))
    print('Total a Pagar :', Total)

elif Tipo == 3:
    TipoCarne = 'Picanha'
    Kg = int(input('Digite a quantidade de Picanha em Kg: '))
    if Kg <= 5:
        ValorCarne = 6.90
    elif Kg > 5:
        ValorCarne = 7.80
    if Pagamento == 1:
        TipoPagamento = 'Cartao Tabajara'
        Desconto = (Kg * ValorCarne) * 0.05
        Total = (Kg * ValorCarne) - Desconto
    elif Pagamento == 2:
        TipoPagamento = 'Nota ou Cartao'
        Desconto = 0
        Total = (Kg * ValorCarne)

    print('*******Nota Fiscal*************')
    print('Tipo do Produto: ', TipoCarne)
    print('Quantidade de ', TipoCarne, ': ', Kg)
    print('Tipo do Pagamento ', TipoPagamento)
    print('Valor do Desconto: ', round(Desconto, 3))
    print('Total a Pagar :', Total)

else:
    print('Valor invalido. Tente novamente!')
