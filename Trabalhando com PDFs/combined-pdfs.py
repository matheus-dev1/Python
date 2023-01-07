#! python3

#combined-pdfs.py

#Combina todos os PDFs do diretório de trabalho atual em um único PDF.

#TODO:

import PyPDF2, os

#Declaração de objetos usados por todo o programa.
arquivos_pdf = []
escritor_pdf = PyPDF2.PdfFileWriter()

# Obtém os nomes de todos os arquivos PDF.
for arquivo in os.listdir('.'):
  if arquivo.endswith('.pdf'):
    # Vou colocar na ultima posição do array
    arquivos_pdf.append(arquivo)
# Depois que o looping terminar eu vou ordenar os pdf do menor para o maior.
arquivos_pdf.sort(key=str.lower)
print(arquivos_pdf)

# Percorre todos os arquivos PDF em um loop.
for arquivo in arquivos_pdf:
  arquivo_pdf_objeto = open(arquivo, 'rb')
  leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf_objeto)
  print(leitor_pdf.isEncrypted)
  if(leitor_pdf.isEncrypted == False):
    # Percorre todas as páginas (exceto a primeira) e as adiciona no PDF de saída.
    for numero_pagina in range(1, leitor_pdf.numPages):
      pagina = leitor_pdf.getPage(numero_pagina)
      escritor_pdf.addPage(pagina)
  else:
    print(arquivo + "criptografado")
  

# Salva o PDF resultante em um arquivo.
novo_pdf = open('allminutes.pdf', 'wb')
escritor_pdf.write(novo_pdf)
novo_pdf.close()