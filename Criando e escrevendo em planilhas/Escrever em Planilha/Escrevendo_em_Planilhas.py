#! python3

#Escrevendo_em_Planilhas.py

#O programa descreve como escrever em planilhas excel usando o modulo openpyxl.

#TODO:

import openpyxl, os

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Criando e escrevendo em planilhas\Escrever em Planilha')

workbook = openpyxl.Workbook()

sheet = workbook['Sheet']

sheet['A1'] = "Ola mundo!"

print(sheet['A1'].value)

workbook.save('Escrevendo em Planilhas com Python.xlsx')