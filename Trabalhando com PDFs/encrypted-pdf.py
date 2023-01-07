#! python

#encrypted-pdf.py

#Programa que descriptografa a senha de um arquivo PDF e le o conteudo da primeira pagina.

#TODO:

import PyPDF2

def pega_texto(pagina: int):
  pagina_do_objeto = leitorPdf.getPage(pagina)
  texto_pagina = pagina_do_objeto.extract_text()
  print(texto_pagina)

arquivoPdfObjeto = open('encrypted.pdf', 'rb') # rb leitura binaria
leitorPdf = PyPDF2.PdfFileReader(arquivoPdfObjeto)
estaCriptografado = leitorPdf.isEncrypted
print(estaCriptografado)
if(leitorPdf.isEncrypted):
  leitorPdf.decrypt('rosebud')
  pega_texto(0)
else:
  pega_texto(0)