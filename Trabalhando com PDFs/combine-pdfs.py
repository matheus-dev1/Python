#! python

#combine-pdfs.py

#Programa que le dois pdf cria objetos dele e cria um novo pdf com a junção destes dois.

#TODO:

import PyPDF2

arquivo_pdf1 = open('meetingminutes.pdf', 'rb')
arquivo_pdf2 = open('meetingminutes2.pdf', 'rb')
leitor_pdf1 = PyPDF2.PdfFileReader(arquivo_pdf1)
leitor_pdf2 = PyPDF2.PdfFileReader(arquivo_pdf2)
escritor_pdf = PyPDF2.PdfFileWriter() #bjeto para escrever um novo pdf

for pagina in range(leitor_pdf1.numPages):
  pagina_objeto = leitor_pdf1.getPage(pagina)
  escritor_pdf.addPage(pagina_objeto) #adicionando as paginas a este objeto

for pagina in range(leitor_pdf2.numPages):
  pagina_objeto = leitor_pdf2.getPage(pagina)
  escritor_pdf.addPage(pagina_objeto)

arquivo_pdf_escrita = open('combined-minutes.pdf', 'wb')
escritor_pdf.write(arquivo_pdf_escrita) #escrevendo todas as paginas adicionadas no objeto "escritor_pdf" no pdf combined-minutes.pdf
arquivo_pdf1.close()
arquivo_pdf2.close()
arquivo_pdf_escrita.close()