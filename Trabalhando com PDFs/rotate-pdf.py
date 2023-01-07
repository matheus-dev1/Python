#! python

#rotate-pdf.py

#O programa pega um pdf cria um objeto de leitura e adiciona a pagina virada, e a partir deste objeto criado, criar um novo pdf com esta pagina virada

#TODO:

import PyPDF2

arquivo_pdf = open('meetingminutes.pdf', 'rb')
leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)
pagina = leitor_pdf.getPage(0)
pagina.rotateClockwise(90) #gira a pagina 90 graus
escritor_pdf = PyPDF2.PdfFileWriter()
escritor_pdf.addPage(pagina)
novo_pdf_virado = open('rotated-pdf.pdf', 'wb')
escritor_pdf.write(novo_pdf_virado)
arquivo_pdf.close()
novo_pdf_virado.close()