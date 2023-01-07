#! python

#marca-d-agua.py

#Programa que le dois pdf cria objetos dele e cria um novo pdf com a junção destes dois.

#TODO:

import PyPDF2

arquivo_pdf = open('meetingminutes.pdf', 'rb')
leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)
escritor_pdf = PyPDF2.PdfFileWriter()
for pagina in range(leitor_pdf.numPages):
  pagina_pdf = leitor_pdf.getPage(pagina)
  escritor_pdf.addPage(pagina_pdf)

escritor_pdf.encrypt("swordfish")
novo_pdf_criptografado = open('encryptedminutes.pdf', 'wb')
escritor_pdf.write(novo_pdf_criptografado)
arquivo_pdf.close()
novo_pdf_criptografado.close()