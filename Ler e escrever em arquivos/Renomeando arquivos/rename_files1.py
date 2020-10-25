#! python3

#rename_files1.py

#O programa possui diversas formas de renomear arquivos.

#TODO: Verificar sobre o raw_input, por enquanto, apenas sera input

import os
import sys

try:
  if sys.argv[1] == '-h':
    print ("Ajuda do programa:\nSintaxe: rename.py [argumento] [diretorio] [prefixo/sufixo] [sufixo]\n\
    \n-h\t Mostra essa ajuda\n\
    \n-i\t Modo Interativo, ideal para a primeira vez de uso\n\
    \n-p\t Renomeia automaticamente todos os arquivos do diretorio especificado \n\tusando o prefixo indicado (numericamente sequencial)\n\
    \n-s\t Renomeia automaticamente todos os arquivos do diretorio especificado \n\tusando o sufixo indicado (numericamente sequencial)\n\
    \n-a\t Renomeia automaticamente todos os arquivos do diretorio especificado \n\tusando prefixo e sufixo indicados (numericamente sequencial)\n\
    \n-e\t Substitui os espacos por underlines e deixa tudo minusculo nos arquivos\n\tdo diretorio especificado")

  elif sys.argv[1] == '-i':
    diretorio = input("Digite o diretorio onde serao feita as alteracoes: ")
    #raw_input

    while not os.access(diretorio, 1):
      print('O diretorio nao existe! Tente novamente')
      diretorio = input("\nDigite o diretorio onde serao feita as alteracoes: ")
      #raw_input
    else:
      os.chdir(diretorio)
      
      print ("Escolha as opcoes abaixo:\n\n\
      1. Substituir espacos por underlines e deixar tudo minusculo\n\
      2. Renomear arquivos sequencialmente\n\n")
      
      opcao = input("Qual opcao ira ser, newbaboy ? ")
      #raw_input
      
      if opcao == '1':
        print ("Os seguintes arquivos serao modificados: \n")
        print (os.listdir(diretorio))
        confirm = input("Deseja prosseguir ? S/N: ")
        #raw_input
        print (os.getcwd())
        if confirm == 'S' or 's':
          try:
            for arquivo in os.listdir(diretorio):
              x = arquivo
              os.rename(x,x.lower())
              for arquivo in os.listdir(diretorio):
                x = arquivo
                s = x.split()
                z = '_'.join(s)
                os.rename(x,z)
          except OSError:
                pass
          print ("Operacao realizada com sucesso! Os arquivos modificados ficaram assim:\n")
          print (os.listdir(diretorio))
              
              
      elif opcao == '2':
        y = 1
        prefixo = input("Coloque prefixo, se houver. Enter para prosseguir ")
        #raw_input
        sufixo = input("Coloque sufixo se houver. Enter para prosseguir ")
        #raw_input
        for arquivo in os.listdir(diretorio):
          x = arquivo
          s = x.split('.')
          if prefixo and sufixo:
            os.rename(x,prefixo+str(y)+sufixo+'.'+s[1])
            y = y + 1
          elif prefixo:
            os.rename(x,prefixo+str(y)+'.'+s[1])
            y = y + 1
          elif sufixo:
            os.rename(x,str(y)+sufixo+'.'+s[1])
            y = y + 1
          else:
            os.rename(x,str(y)+'.'+s[1])
            y = y + 1
  
  elif sys.argv[1] == '-p' and sys.argv[2]:
    y = 1
    try:
      prefixo = sys.argv[3]
      diretorio = sys.argv[2]
      os.chdir(diretorio)
      for arquivo in os.listdir(diretorio):
        x = arquivo
        s = x.split('.')
        #AQui nos dividimos o nome em duas listas, a primeiro e o nome do arquivo prorpiamente dito.
        #O segundo e o tipo da extensao do arquivo, no caso da pasta lacunas. .txt
        print(prefixo + str(y))
        try:
          os.rename(x, prefixo + str(y) + '.' + s[1])
        except FileExistsError:
          continue
        
        #Primeiro argumento o arquivo, segundo argumento e o novo nome do arquivo.
        y = y + 1
      print ("\nOperacao realizada com sucesso!")
    except IndexError:
        print ("\nPrefixo invalido")
  
  elif sys.argv[1] == '-s' and sys.argv[2]:
    y = 1
    try:
      sufixo = sys.argv[3]
      diretorio = sys.argv[2]
      os.chdir(diretorio)
      for arquivo in os.listdir(diretorio):
        x = arquivo
        s = x.split('.')
        os.rename(x,str(y)+sufixo+'.'+s[1])
        y = y + 1
      print ("\nOperacao realizada com sucesso!")
    except IndexError:
        print ("\nSufixo invalido")
  
  elif sys.argv[1] == '-a' and sys.argv[2]:
    y = 1
    try:
      diretorio = sys.argv[2]
      prefixo = sys.argv[3]
      sufixo = sys.argv[4]
      os.chdir(diretorio)
      for arquivo in os.listdir(diretorio):
        x = arquivo
        s = x.split('.')
        os.rename(x,prefixo+str(y)+sufixo+'.'+s[1])
        y = y + 1
      print ("\nOperacao realizada com sucesso!")
    except IndexError:
      print ("\nTem certeza que digitou ambos ? (Prefixo e sufixo)")
    
except IndexError:
  print ("\nO argumento -h mostra a ajuda do programa")