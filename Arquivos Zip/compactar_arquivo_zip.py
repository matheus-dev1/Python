#! python3

#compactar_arquivo_zip

#O programa deve compactar o arquivo chama.txt em formato .zip

import zipfile

chama_zipfile = zipfile.ZipFile('Chama.zip', 'w')
#Nesta funcao nos vamos abrir/criar, no nosso caso criar, um nome para o nosso object zipfile em modo de escrita.
chama_zipfile.write('chama.txt', compress_type = zipfile.ZIP_DEFLATED)
#Vamos compactar o arquivo de texto 'chama.txt' que vai esta dentro da pasta chama.zip com o tipo de compreesao deflated.
chama_zipfile.close()
#No final fechamos o object zipfile.

chama_zipfile = zipfile.ZipFile('Chama.zip', 'a')
#Abrimos o arquivo .zip 'Chama.zip' em modo de adicao.
chama_zipfile.write('regex.py', compress_type = zipfile.ZIP_DEFLATED)
#Vamos adicionar mais um arquivo para ser compactado na mesma pasta, no caso o 'regex.py' com o tipo de compressao deflated.
chama_zipfile.close()
#Fechamos o object zipfile ou podemnos entender tambem como fechamos o arquivo chama.zip