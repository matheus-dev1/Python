#! python3

#AlturaLarguraLinhaColunaPlanilha.py

#O programa deve aumentar a altura e largura de uma celula de uma planilha no excel.

#TODO:

import openpyxl, os

os.chdir('C:/Matheus/Study/IT/Python/Arquivos Python/Altura e Largura de Linha e Coluna Planilhas/')

workbook = openpyxl.Workbook()

sheet = workbook['Sheet']

sheet['A1'] = 'A1'

sheet['B2'] = 'B2'

sheet.row_dimensions[1].height = 70
#Aqui eu vou usar o metodo row_dimensions e colocar entre as chaves uma linha, neste caso eu coloquei
#a linha 1, e depois eu coloco .height para aumentar a altura desta linha e atribu-o um valor que 
#sera o tamanho da altura da linha.
#Quando eu aumento a ALTURA eu vou aumnetar a altura de toda a LINHA.

sheet.column_dimensions['B'].width = 40
#Aqui eu vou usar o metodo column_dimnesions e colocar entre chaves a coluna, neste caso eu coloquei
#a coluna B, e depois eu coloco o .width para aumentar a largura desta coluna e atribu-o um valor que
#sera o tamanho da largura desta coluna.
#Quando eu aumento a LARGURA eu vou aumentar a largura de toda a COLUNA.

workbook.save('AlturaLarguraLinhaColunaPlanilha.xlsx')