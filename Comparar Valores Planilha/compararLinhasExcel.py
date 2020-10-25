#! python3

#compararLinhasExcel.py

#O programa deve analisar uma planilha, verificar cada linha e retornar e aprensentar para nos qual a linha que possui maior valor 
#somados e tambem quais sao os valores.

#TODO: 1. Abrir o Arquivo Excel.
#TODO: 2. Abrir a Planilha de Uso.
#TODO: 3. Fazer um algoritmo para criar listar para cada linha e armazenar o seus valores.

import openpyxl

print('Opening Workbook...')

workbook = openpyxl.load_workbook('dadosExemplo.xlsx')
#Abrir o Arquivo Excel.

mainSheet = workbook.get_sheet_by_name("Dados")
#Abrir a Planilha de uso.

print('Reading Columns and Rows...')

dados = []
total = []
maiorValor = 0

for row in range(1, mainSheet.max_row + 1):
    dadosRow = []

    dadosRow.append(mainSheet["A" + str(row)].value)
    dadosRow.append(mainSheet["B" + str(row)].value)
    dadosRow.append(mainSheet["C" + str(row)].value)

    dados.append(dadosRow)

for row in range(0, len(dados)):
    totalValue = 0
    for column in range(0, len(dados)):
        totalValue += dados[row][column]
    total.append(totalValue)

for row in range(0, len(total)):
    if total[row] > maiorValor:
        maiorValor = total[row]
        maiorValorRow = row

print('Linha: ' + str((maiorValorRow + 1)) + " - Valores: (R$)" + str((dados[maiorValorRow])) + " - Total: R$" + str(total[maiorValorRow]))