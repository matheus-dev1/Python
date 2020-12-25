#! python3

#erros_digitacao

#O programa deve encontrar 3 possiveis erros em um texto.
#1. Varios espacos entre palavras
#2. Repeticao seguida de palavras.
#3. Apenas um ponto de exclamacao no final de casa sentenca.

#Encontrar erros comuns de digitação como vários      espaços     entre palavras, repetição acidental acidental de palavras 
#ou vários pontos de exclamação no final final das sentenças. São irritantes!!!!'

import pyperclip, re

text_full = pyperclip.paste()

erro_duplicada = re.compile(r'''
\b(\w+)(?:\s+\1\b)+ ########remove todas as palavras que duplicadas.#########
''', re.VERBOSE)

correcao_duplicada = erro_duplicada.sub(r'\1', text_full)

erro_espaco_exclamacao = re.compile(r'''
(\w+\s|\w+\!|\w+\.\ ) #######Remove espacos em branco e faz com que as########
                      ######palavras apenas possuam 1 ponto ou exclamacao.#########
''', re.VERBOSE)

correcao_espaco_exclamacao = erro_espaco_exclamacao.findall(correcao_duplicada)

texto_corrigido = str(''.join(correcao_espaco_exclamacao))
#tranforma em String

print(texto_corrigido)
#(\w+\s|\w+\!|\w+\.\ )
#(\b\w+\b)\W+\1
