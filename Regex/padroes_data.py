#! python3

#padroes_data

#O programa deve receber uma serie e datas com padroes diferentes e substituir todas para um padrao unico.

import pyperclip, re, pprint

text_full = str(pyperclip.paste())

#Ano/Mes/Dia
data1 = re.compile(r'''
(\d{4})                                 #Grupo 1 - Ano
(\-|\.|\ )                              #Grupo 2 - Traco, Ponto ou espaco
([10-12]{2}|[1-9]{1})                   #Grupo 3 - Mes
(\-|\.|\ )                              #Grupo 4 - Traco, Ponto ou espaco
([10-31]{2}|[1-9]{1})                   #Grupo 5 - Dia
''', re.VERBOSE)
#Os que nao forem alterados que dizer que estao com a data errada.

phase1 = data1.sub(r'\1/\3/\5', text_full)

#Dia/Mes/Ano
data2 = re.compile(r'''
([10-31]{2}|[1-9]{1})                  #Grupo 1 - Dia
(\-|\.|\ )                             #Grupo 2 - Traco, Ponto ou espaco
([10-12]{2}|[1-9]{1})                  #Grupo 3 - Mes
(\-|\.|\ )                             #Grupo 4 - Traco, Ponto ou espaco
(\d{4})                                #Grupo 5 - Ano
''', re.VERBOSE)

phase2 = data2.sub(r'\1/\3/\5', phase1)

#Mes/Dia/Ano
data3 = re.compile(r'''
([10-12]{2}|[1-9]{1})                  #Grupo 1 - Mes
(\-|\.|\ )                             #Grupo 2 - Traco, Ponto ou espaco
([10-31]{2}|[1-9]{1})                  #Grupo 3 - Dia
(\-|\.|\ )                             #Grupo 4 - Traco, Ponto ou espaco
(\d{4})                                #Grupo 5 - Ano
''', re.VERBOSE)

phase3 = data3.sub(r'\1/\3/\5', phase2)

print(phase3)
print('Datas com as barras copiadas para os Clipboard (Ctrl-v)')
pyperclip.copy(phase3)

