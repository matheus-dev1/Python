#! python3

#CriandoEscrevendo1.py

#Neste programa eu crio um Workbook vazio com um planilha(que e pedrao e vem com o nome Sheet), e vou
#alterar e salvar a plailha 

#TODO: 

import openpyxl, os

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Criando e escrevendo em planilhas\Criando e escrevendo 1')
#Altero o local do arquivo para que o Workbook seja criado no local onde este arquivo esta.

workbook = openpyxl.Workbook()
#Cria um Workbook vazio.

print(workbook.get_sheet_names())
#Exibimos as planilhas do workbook, porem como criamos um agora ele vem como padrao apenas
#uma planilha a ['Sheet'].

sheet = workbook['Sheet']
#Armazenando as planilhas existente neste workbook na variavel sheet que no caso e uma so a ['Sheet'].

sheet.title = "Vida de Programdor!"
#Nome da planilha, normalmente usamos o title quando queremos saber o nome da planilha e caso queira alterar o nome.
#.title e um atributo.

print(workbook.get_sheet_names())
#Exibimos a mudanca.

workbook.save('Escrevendo.xlsx')
#SAlvamos o arquivo propriamente dito.