#! python

#InsertRowsExcel.py

#O programa deve receber tres parametros. O primeiro e a linha aonde queremos inserir as linhas em 
#branco a segunda eh a quantidade de linhas que se deve pular e a terceira mas nao menos importante
#a plnailha em que queremos fazer isso. Sabendo que a planilha em que vamos usar ja deve ter dados.

#TODO:

import sys, os, openpyxl

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Inserir Linhas em Branco Excel')

#Primeiro argumento: Chama do arquivo.
#Segundo Argumento: Definir a Linha em que devera comecar a inserir linhas em brnaco.
#Terceiro Argumento: Definir a quantidade de linha em que devera ser colocada em branco.
#Quarto Argumento: Nome da planilha. Em que ja existe.
Linha =  ''.join(sys.argv[1:2])
#Aqui eu vou pegar o segundo argumento da chamada do meu programa
QtdLinha = ''.join(sys.argv[2:3])
NomeWorkbook =  ''.join(sys.argv[3:4])

workbook = openpyxl.load_workbook('produceSales.xlsx')

sheet = workbook['Sheet']

for index in range(int(QtdLinha)):
    sheet.insert_rows(int(Linha))
#O metodo inser_rows() adiciona uma linha em branco na linha igual ao valor que esta sendo passado
#como parametro. Neste meu exemplo eu passei 7 entao eu vou adicionar uma linha em branco na linha 7
#e se tiver alguma valor la na hora da insercao ele vai para a linha de baixo.
#OBS: Se possui formulas na linha onde voce esta adicionando um valor a formula nao ira descer tambem
#fazendo com que por exemplo uma soma fique errado. ATENCAO COM ISSO!!!

workbook.save(NomeWorkbook)