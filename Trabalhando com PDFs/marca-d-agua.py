#! python

#marca-d-agua.py

#Programa que le dois pdf cria objetos dele e cria um novo pdf com a junção destes dois.

#TODO:

import PyPDF2

arquivo_pdf = open('meetingminutes.pdf', 'rb')
leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)
primeira_pagina = leitor_pdf.getPage(0)
arquivo_pdf_marca_d_agua = open('watermark.pdf', 'rb')
leitor_pdf_marca_d_agua = PyPDF2.PdfFileReader(arquivo_pdf_marca_d_agua)
primeira_pagina_marca_d_agua = leitor_pdf_marca_d_agua.getPage(0)
primeira_pagina.mergePage(primeira_pagina_marca_d_agua) # Aqui eu coloco uma pagina em cima da outra, e a pagina afetada é a "primeira_pagina"
escritor_pdf = PyPDF2.PdfFileWriter()
escritor_pdf.addPage(primeira_pagina)
for pagina in range(1, leitor_pdf.numPages):
  pagina_objeto = leitor_pdf.getPage(pagina)
  escritor_pdf.addPage(pagina_objeto)

novo_pdf_com_marca_d_agua = open('marca-d-agua-pdf.pdf', 'wb')
escritor_pdf.write(novo_pdf_com_marca_d_agua)
arquivo_pdf.close()
arquivo_pdf_marca_d_agua.close()
novo_pdf_com_marca_d_agua.close()