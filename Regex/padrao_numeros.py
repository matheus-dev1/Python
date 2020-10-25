#! python3

#padrao_numeros

#O programa deve saber identificar numero que tenha uma virgula e depois 3 numeros.

import re

#\d\,\d{3}\,\d{3}|\d\,\d{3}|\d{2} OU \d\,\d{3}\,\d{3}|\d\,\d{3} OU ^\d{1,3}(,\d{3})*$
regex_number = re.compile(r'\d,\d{3},\d{3}|\d,\d{3}')
regex_values = regex_number.findall('42 1,234 6,368,745 12,34,567 1234')
print(regex_values)
#42 1,234 6,368,745 12,34,567 1234
