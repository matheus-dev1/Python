#! python3

#frase_regex

#O programa de encontrar uma frase tenha como a primeira palavra Alice, Bob ou Carol
#A segunda tenha eats, pets ou throws
#A terceira apples, cats ou baseballs

import re

frase = re.compile(r'''
(Alice\s|Bob\s|Carol\s)
(eats\s|pets\s|throws\s)
(apples.\s|cats.\s|baseballs.\s)
''', re.VERBOSE | re.IGNORECASE)

frase_encontradas = frase.findall('Alice eats apples. asdfasdfsdafas Bob pets cats. asdfasdfafaf Carol throws baseballs.\
asdfasdfadfasdf Alice throws Apples. asdfasdfsdafsda BOB EATS CATS. asdfsdafsdaf RoboCop eats apples. sdafsdafsdafsdaf\
ALICE THROWS FOOTBALLS. sdfadfasdfsdafa Carol eats 7 cats.')
print(frase_encontradas)

#
