#! python3

#regex_search

#Ler todos os arquivo .txt de uma determinada pasta e procurar pelas linhas que esta dentro do regex em que o usuario digitou.

import os, re
#Imports necessarios.

for filename in os.listdir('C:\\Matheus\\Study\\IT\\Python\\Mad Libs'):
    #Vai passar por todos os arquivo do diretorio C:\\Matheus\\Study\\IT\\Python\\Mad Libs, onde a string de cada arquivo
    #sera armazenada em 'filename'
    if filename.endswith('.txt'):
        #Se os arquivo forem arquivo de texto ele ira executar.
        print(os.path.join('C:\\Matheus\\Study\\IT\\Python\\Mad Libs', filename))
        #Vai printar o caminho do arquivo em que ele esta lendo.
        file_read = open(os.path.join('C:\\Matheus\\Study\\IT\\Python\\Mad Libs', filename), 'r')
        #Vai ler o arquivo e armazenar o seu 'id' em 'file_name'
        file_readed = file_read.read()
        #Lemos o 'id' e o armazenamos a string do arquivo .txt em file_readed
        print('Arquivo: ' + str(filename) + ' - ' + 'Conteudo Arquivo: ' + str(file_readed))
        regex_user = input("Digite uma Expressao Regular (Ex: (\w*))): ")
        #Usuario digitar a regex em que ele quer procurar no arquivo de texto.
        file_regex = re.compile(regex_user)#r'\w*'
        #Vai ler a string do usuario e criar um obejto regex em cima dele.
        file_regex_correct = file_regex.findall(file_readed)
        #Vamo encontrar todos os caractere que este dentro do regex do usuario.
        file_regex_correct = ' '.join(file_regex_correct)
        #Vamo transformar a string em lista para podemos remover os espacos em branco.
        erro_espaco_exclamacao = re.compile(r'''
        (\w+\s|\w+\!|\w+\.\ ) #Remove espacos em branco e faz com que as palavras apenas possuam 1 ponto ou exclamacao.
        ''', re.VERBOSE)
        #Regex para tirar espacos em branco.
        correcao_espaco_exclamacao = erro_espaco_exclamacao.findall(file_regex_correct)
        #Encontrar todos os textos que esta o sem espacos adicionais.
        texto_corrigido = str(''.join(correcao_espaco_exclamacao))
        #Voltar para String e sem espacos.
        print(texto_corrigido)
        #Exibir a string.
        file_read.close()
        #Fecha o arquivo
