#! python3

#sobrenome_Nakamoto

#O programa consiste em encontrar em um texto as ocorencias de nome que tenhas as primeiras letra do nome se maisucula
#e o sobre nome seja Nakamoto.

import re

#re.compile(r'[A-Z][a-z]*\sNakamoto')
Nakamoto = re.compile(r'[A-Z]\w+ Nakamoto')
Nakamoto_name = Nakamoto.findall('Satoshi Nakamoto sdafasdfsdaf Alice Nakamoto sdafsdafsdafsdaf RoboCop Nakamoto \
sdfsdafsdasafa satoshi Nakamoto sdfsadfsdafsdaf Mr. Nakamoto asdfsdfsadfsa Nakamoto asdfdfsadfa Satoshi nakamoto')

print(Nakamoto_name)
