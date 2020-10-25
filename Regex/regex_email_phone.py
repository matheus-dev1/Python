#! python3

#regex_email_phone

#O programa pega o texto que esta no clipboard(ctrl-C) do usuario e pegar todos os numero em formatos do brasil e amiricano e tambem
#pega os emails no texto e retorna um texto para o clipboard(Ctrl-V) do usuario com apenas as ocorrencias de numeros e emails.

import pyperclip, re, pprint

text_full = str(pyperclip.paste())
#Receber o texto do usuario e armazenar em text_full sem nenhuma alteracao.

values = []

regex_brazil_phonenumber = re.compile(r'''
(\(?\d{2}\)?\ )             #DDD padrao brasileiro.
(\d{4})                     #Quatro primeiros digito de um numero do padrao brasileiro, todo numero deve conter este primeiros 4 digitos.
(\s|-|/|.)?                 #Traco para separa os quatro primeiro digitos do ultimos 4 ou 5 dependendo se for fixo ou movel.
(\d{5}|\d{4})               #(1) Grupo final de numeros de telefones fixos. (2) Grupo final de numero de telefones celulares.
''', re.VERBOSE)
#Obs: Quando for trabalhar com quantidade de valares com expressoes regulares sempre coloque do maior para o menor.
#Podemos colocar uma barra no inicio e outra no fim para receber o numero inteiro tambem.

phone = regex_brazil_phonenumber.findall(text_full)
#Armazena em phone todos os numero de telefones coletados.

regex_american_phonenumber = re.compile(r'''
(\(?\d{3}\)?)                   #Código de Area, ou seja, opcional
(\s|-|\.)                       #Separador, o numero pode ser separado por diversos digitos, mas o comum e o '-'
(\d{3})                         #Primeiros 3 dígitos, que sao obrigatorios.
(\s|-|\.)                       #Segundo Separador, porem este e obrigatorio.
(\d{4})                         #Ultimos 4 dígitos, do numero de telefone com o padrao americano.
''', re.VERBOSE)

american_phone = regex_american_phonenumber.findall(text_full)
#Armazena todos os numero de telephones no formato americano.

regex_email = re.compile(r'''
(\w{8,64})              #Nome de usuario
(@)                     #Separador
(\w+)                   #Dominio
(.com)                  #.com
(.br)?                  #.br (Opcional)
''',re.VERBOSE)
email = regex_email.findall(text_full)
#{64}@{255} isto é, 64 + 1 + 255 = 320
#Coleta todos emails e armazena na variavel email

#tranformas todas as tuplas em listas
for indice in range(len(phone)):
    values.append(list(phone[indice]))

for indice in range(len(american_phone)):
    values.append(list(american_phone[indice]))

for indice in range(len(email)):
    values.append(list(email[indice]))

#Exibir que todas as strings estao em lista de listas.
pprint.pprint(values)
print()

value_uni = ''

#for indice in range(len(values)):
for indice in range(len(values)):
    value_uni = value_uni + '\n' + str(''.join(values[indice]))
    
if values == []:
    print('Nenhum valor encontrado! Nada foi passado para o sue CtrlV')
else:
    pyperclip.copy(value_uni)
    print('valor encontrados e copiados para o seu Ctrl-V: ', end ='')
    print(value_uni)
