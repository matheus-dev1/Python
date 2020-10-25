#! python3

#sub_remover_espacos_em_branco

#O programa recebe um texto com que seus lados esquerdos todos, comecem com espacos em branco.
#Nos o removemos e retornamos para o ctrl-c do usuario sem espacos em branco na esquerda.

import pyperclip, sys, pprint, re

sub_espacos = pyperclip.paste()

regex_espacos_em_branco = re.compile(r'(\ *)(\w*)', re.VERBOSE)

espacos_removidos = regex_espacos_em_branco.sub(r'\2', sub_espacos)

pyperclip.copy(espacos_removidos)

print(espacos_removidos)
