#! python3

#CriarGraficoExcel.py

#O program deve criar um grafico no excel a partir de 10 dados da mesma planilha.

#TODO:

import os, sys
import openpyxl
import openpyxl.chart

workbook = openpyxl.Workbook()

sheet = workbook['Sheet']

for column in range(1, 11):
    sheet['A' + str(column)] = column
    #Aqui eu vou criar valores para que o meu grafico possa ter dados.

graficotype = sys.argv[1]

if graficotype.lower() == 'barra':
    ChartObject = openpyxl.chart.BarChart()
elif graficotype.lower() == 'pizza':
    ChartObject = openpyxl.chart.PieChart()
elif graficotype.lower() == 'linha':
    ChartObject = openpyxl.chart.LineChart()
elif graficotype.lower() == 'dispersao':
    ChartObject = openpyxl.chart.ScatterChart()

ReferenceObject = openpyxl.chart.Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=10)
#openpyxl.charts.Reference() | Este e um objeto reference. Ele e usado para selecionar os dados.
#Primeiro argumento: E a planilha em que eu quero selecionar os dados.
#Primeiro e Segundo Argumento: Eu seleciono a coluna e linha inicial. Neste caso eu estou selecionando A1.
#Sendo min_col = 1 igual a coluna A e min_row = 1 a linha 1, ou seja, A1.
#Terceiro e Quarto Argumentos: Eu seleciono a coluna e linha final. Neste caso eu estou selecionando a A10.
#Sendo max_col = 1 igual a coluna A e max_row = 10 a linha 10, ou seja, A10.

#ChartObject = openpyxl.chart.BarChart()
#Aqui estou criando um objeto Chart(Grafico) neste caso Grafico de Barra.

SeriesObject = openpyxl.chart.Series(ReferenceObject, title='First Chart')
#openpyxl.charts.Series() | Este e um objeto series. Ele coloca um titulo no Grafico.

ChartObject.append(SeriesObject)
#Aqui eu estou adicinando o objeto Series (Titulo) no objeto Chart (Grafico).

#ChartObject.drawing.top  = 50
#ChartObject.drawing.left = 100
#Nestas duas meodos eu defino a posicao do grafico, ou seja, onde ele vai ficar.

#ChartObject.drawing.width = 300
#ChartObject.drawing.height = 200
#Aqui eu defino o tamanho(altura e largura) do grafico.

sheet.add_chart(ChartObject)
#Aqui eu vou adicionar o grafico no objeto da planilha.

workbook.save('Grafico ' + graficotype + '.xlsx')

os.startfile('Grafico ' + graficotype + '.xlsx')