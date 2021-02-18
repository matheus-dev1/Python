#! python3

#FormSomaPlan.py

#O programa deve verificar os VALORES de FORMULAS EXCEL de uma PLANILHA.

#TODO:

import openpyxl, os

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Formulas Planilhas\Soma')

workbook = openpyxl.load_workbook('FormSomaPlan.xlsx', data_only=True)
#Eu vejo apenas os valores e nao formulas em celulas.

sheet = workbook['Sheet']

print(sheet['A51'].value)
#OBS: Pra eu conseguier ver o valor conforme eu coloquei, eu tive que ir na propria planilha
#e escrever a formula novamente para que ficasse no CACHE e assim eu usando o argumento
#nomeado data_only=True funcionasse.