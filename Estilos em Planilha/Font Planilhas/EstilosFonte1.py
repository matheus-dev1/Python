#! pyhton3

#EstilosFonte1.py

#O arquivo mosta a funcionalidade Font() onde nos podemos passar varios argumentos nomeados
#para definir estilos na nossas celulas e usamos o metodo .font de celula para aplicar
# estes estilos de fonte.

#TODO:

import openpyxl, openpyxl.styles, os
#from openpyxl.styles import Font
#Eu nao importo mais a funcao styles, porque ela nao existe mais.

os.chdir('C:\Matheus\Study\IT\Python\Arquivos Python\Estilos em Planilha\Font Planilhas')

workbook = openpyxl.Workbook()

sheet = workbook['Sheet']

FontEspecial = openpyxl.styles.Font(name='Times New Roman', italic=True, size=28, bold=True, outline=True, shadow=True, underline="single", color="FF0000")
#Argumentos nomeado sao parametro com propriedad e valor.
#Aqui estou estou definindo os estilos da minha fonte e armazenando em uma variavel.

#FontEspecialObjStyle = openpyxl.styles.Style(font=FontEspecial)
#Aqui estou difinindo que isto e uma FONTE APLICAVEL.
#ISTO NA REALIDADE NAO ESTA MAIS FUNCIONANDO

sheet['A1'].font = FontEspecial
#Eu uso o metodo .font para aplicar estilos a esta celula.

sheet['A1'] = "Ola estilizacao com Openpyxl"

workbook.save('FontesEmPlanilhas2.xlsx')