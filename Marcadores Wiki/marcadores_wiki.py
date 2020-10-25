#! python3

#marcadores_wiki

#Cria marcadores wiki e coloca no seu clipboard.

import pyperclip, sys

without_bullets = pyperclip.paste()
#Nos recebemos o valor que esta no clipboard (Ctrl C) do usuario que armazenamos ema um Variavel chamada without_bullets.
#Obs: Ao passar o text ele tem que esta na forma de lista.

print('Clipboard do Usuario sem nenhuma alteracao')
print(without_bullets)
print()
#Estamos aprensentado como esta a aparencia da lista em que usuario esta passando em seu Ctrl-C de primeira.

with_bullets = without_bullets.split('\n')
#O metodos split com o argumento '\n' vai remover todos as quebras de linha e aonde tinha uma quebra de linha ele vai criar uma lista.

print(r"Clipboard tranformado em Lista e sem Quebra de linhas gracas ao metodo split('\n')")
print(with_bullets)
print()
#Apresenta o clipboard do usuario agora em forma de lista e sem as quebras de linhas.

for Text in range(len(with_bullets)):
        with_bullets[Text] = '* ' + with_bullets[Text]
#Usamos renge(len()) porque necessiatamos passar por todo os indices da lista.
#A variavel Text onde sera passado os valores do indice a cada interacao, sera o indice onde acontecera a concatenacao da String.

with_bullets = '\n'.join(with_bullets)
#Com o metodo Join() a cada indice da lista a gente vai quebrar a linha e no final de tudo tranformar em String.
    
print('Clipboard com os asteriscos e passado para o Ctrl-C do Usuario')
print(with_bullets)
print()
#Clipboard final com os asteriscos copiados para o clipboard, com os asteriscos adicionados e em forma de string.
    
pyperclip.copy(with_bullets)
print("A lista com os 'bullets' foram adicionadas ao seu clipboard (Ctrl C) ")
#Aqui passamos para o Clipboard do usuario a String depois de todo os processor feitos.
