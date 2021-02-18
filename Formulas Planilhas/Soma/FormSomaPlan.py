#! python3

#FormSomaPlan.py

#O programa deve definir alguns valores em algumas celulas e em seguida somar o seu resultado.

#TODO:

import openpyxl, os, random

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Formulas Planilhas\Soma')

workbook = openpyxl.Workbook()

sheet = workbook['Sheet']

for row in range(1, 50):
    sheet.cell(row=row, column=1).value = random.randint(1, 1000)

sheet['A51'] = '=SUM(A1:A50)'

workbook.save('FormSomaPlan.xlsx')