#! python

#read-meetingminutes.py

#Programa que le um arquivo PDF e pega o texto da primeira pagina.

#TODO:

import PyPDF2

arquivoPdfObjeto = open('meetingminutes.pdf', 'rb') # rb leitura binaria
leitorPdf = PyPDF2.PdfFileReader(arquivoPdfObjeto)
numeroPaginas = leitorPdf.numPages
print(numeroPaginas)
paginaDoObjeto = leitorPdf.getPage(0)
textoPagina = paginaDoObjeto.extract_text()
print(textoPagina)