'''
a = int(input('Digite um valor: '))
b = int(input('Digite outro valor: '))

x = a + b

print('X = %s' %x)
'''

#Para rodar arquivos com espaco no nome devemos usar como aspas.

#assert 1 != 1, 'Um e igual a um'
'''
a = 'i.imgur.com/EtJctHUb.jpg'.split('b')

print(a)

a = ''.join(a)

print(a)
'''
'''
import webbrowser, requests, bs4, sys, re

a = requests.get('https://www.freepik.com/search?query=' + sys.argv[1])
print('https://www.freepik.com/search?query=' + sys.argv[1])
print(type(a))
print('Opening images...')
#Verifica se possui um erro.
#403 Forbidden (403 Proibido) é um código de resposta HTTP da classe de respostas de erro do cliente, a qual indica que
# o servidor recebeu a requisição e foi capaz de identificar o autor, porém não autorizou a emissão de um resposta.

print(a.status_code == requests.codes.ok)

object_response_soup = bs4.BeautifulSoup(a.text)
#Pega o arquivo baixado e transforma em uma classe BeautifulSoup

Links = object_response_soup.select('a')

print(Links)
for Pagina in range(len(Links)):
    Link = Links[Pagina].get("src")
    print('Opening... ' + Link)
    webbrowser.open(Link)
'''
'''
def triangulo(symbol_local, width_local, height_local):
    if symbol_local != 1:
        raise Exception('O simbolo possui mais de um caractere.')
    elif width_local < 4:
        raise Exception('O valor da Largura e menor ou igual a 4.')
    elif height_local < 4:
        raise Exception('O valor da Altura e menor ou igual a 4.')
    else:
        print()

while True:
    symbol_user = input('Digite um simbolo: ')
    width_user = int(input('Digite a largura de simbolos: '))
    height_user = int(input('Digite a altura de simbolos: '))
    #for symbol, width, height in symbol_user, width_user, height_user:
    try:
        print_symbols(symbol_user, width_user, height_user)
        #width = Largura
        #height = Altura
        option = input('Quer digitar outro quadrado? [S/N]: ')
        if option.lower() == 's':
            continue
        else:
            break
    except Exception as error:
        print('Uma exceção aconteceu: ' + str(error))
        option_local = input('Quer tentar outro quadrado? [S/N]: ')
        if option_local.lower() == 's':
            continue
        else:
            break
    '''

        #         $       
        #        $ $    
        #       $   $
        #      $     $
        #     $       $ 
        #    $         $
        #   $           $
        #  $             $
        # $               $
        # $$$$$$$$$$$$$$$$$

        #

        #   $  
        #  $ $ 
        # $   $
        # $$$$$

          # 
         ###
        #####
'''
for i in range(1, 10):
    print('%' * i)
'''
'''
b = 0
for i in range(44, 0, -1):
    a = i // 2
    if i % 2 == 1:
        print((' ' * a) + '%' * b + (' ' * a))
    b = b + 1

name = 'matheus'
print("Names: {}".format(name))
'''
'''
import webbrowser, requests, bs4, zipfile, os, shutil

os.chdir('C:\\Users\\mathe\\Área de Trabalho\\skin lol')

object_lol_skin = zipfile.ZipFile('skin.zip')
'''
'''
for filename in os.listdir():
    object_lol_skin.extract('C:/Users/mathe/Área de Trabalho/skin lol/' + filename, 'C:\\Users\\mathe\\Área de Trabalho\\skin lol')
'''
'''
#object_zipfile_livros_python.extract('Livros Python zip/Automatize Tarefas Macantes com Python/automate_online-materials/zophie.png', 'C:\\Matheus\\Study\\IT\Python\\Foda')
object_lol_skin.extractall('C:\\Users\\mathe\\Área de Trabalho\\skin lol\\skin.zip', )

object_lol_skin.close()
'''