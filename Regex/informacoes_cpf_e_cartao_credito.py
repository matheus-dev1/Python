#! python3

#informacoes_cpf_e_cartao_credito

#O programa deve receber do clipboardo(Ctrl-C) do usuario uma texto ponde possui Cpf e cartoes de credito este texto deve
#ser retornado de forma aonde apenas fique as 3 primeiras letras do cpf e o 4 primeiros digitos do cartao de credito.

import pyperclip, re

text_full = pyperclip.paste()

cpf = re.compile(r'''
(\d{3})                 #G1 - Primeiro 3 digitos do CPf
(\ |\.|\-)              #G2 - Primeiro Tracos, espapos, pontos do CPF
(\d{3})                 #G3 - Segundo 3 digitso do CPF
(\ |\.|\-)              #G4 - Primeiro Tracos, espapos, pontos do CPF
(\d{3})                 #G5 - Terceiro 3 digitso do CPF
(\ |\.|\-)              #G6 - Traco (Opcional)
(\d{2})                 #G7 - Dois ultimos digitos do CPF
''', re.VERBOSE)
#Padrao CPF 230.149.108-05 | 230-149-108-05 | 230 149 108 05 | 230.149.108 05

phase1 = cpf.sub(r'\1.***.***-**',text_full)

credito = re.compile(r'''
(\d{4})                 #G1 - Quatro primeiro digitos do Cartao de credito
(\ |\.|\-)              #G2 - Primeiro Tracos, espapos, pontos do Cartao de Credito
(\d{4})                 #G3 - Quatro Segundo digitos do Cartao de credito
(\ |\.|\-)              #G4 - Segundo Tracos, espapos, pontos do Cartao de Credito
(\d{4})                 #G5 - Quatro Terceiro digitos do Cartao de credito
(\ |\.|\-)              #G6 - Terceiro Tracos, espapos, pontos do Cartao de Credito
(\d{4})                 #G7 - Quatro Quarto digitos do Cartao de credito
''', re.VERBOSE)
#Padrao Cartao de Credito 1234 5678 9012 1234

phase2 = credito.sub(r'\1 **** **** ****',phase1)

print(phase2)
print('O texto foi corrigido e enviado para o seu clipboard.')
pyperclip.copy(phase2)
