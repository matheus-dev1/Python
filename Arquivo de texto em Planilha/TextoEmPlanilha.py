#! python3

#TextoEmPlanilha.py

#O programa deve pegar o texto de um arquivo de texto e passar para uma planilha.

#TODO:

import openpyxl, os

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Arquivo de texto em Planilha')

Texto = open("Texto.txt", "r")

TextoLinhas = Texto.readlines()

workbook = openpyxl.Workbook()

sheet = workbook['Sheet']

print(len(TextoLinhas))

for row in range(len(TextoLinhas)):
    sheet.cell(row = row + 1, column = 1).value = TextoLinhas[row]

workbook.save('TextoemPlanilha.xlsx')

Texto.close()