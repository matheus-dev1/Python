#! python3

#CongelarPainel.py

#O programa deve congelar um painel definido pelo programador.

#TODO:

import openpyxl, os

os.chdir('C:/Matheus/Study/IT/Python/Arquivos Python/Painel Congelado Planilhas')

workbook = openpyxl.load_workbook('produceSales.xlsx')

sheet = workbook['Sheet']

#sheet.freeze_panes = 'A2'
#AQui eu vou congelar a linha 1 inteira.

sheet.freeze_panes = 'B1'
#AQui eu vou congelar a coluna A inteira.

workbook.save('CongelandoColunaA.xlsx')