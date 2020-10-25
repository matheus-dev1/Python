#! python3

#google_maps.py

#O programa pode abrir o site do google com o endereco digitado pelo usuario como segundo argumento da chamada do programa ou 
#podemos pelo seu clipboard, caso voce nao tenha digitado um segundo argumento.

#TODO:

import webbrowser, sys, pyperclip
#imports importantes.

if len(sys.argv) > 1:
    adress = sys.argv[1]
    #Devemos usar aspas duplas para colocar o endereco ou usar address = ' '.join(sys.argv[1:])
    #address = ' '.join(sys.argv[1:]) = Voce pode usar assim caso nao queira digitar aspas antes do endereco.
    print('Opening: https://www.google.com/maps/place/' + adress + '...')
    webbrowser.open('https://www.google.com/maps/place/' + adress)
    #Abre um navegador na pagina do google maps mais o endereco digitado pelo usuario como segundo argumento na chamada do programa.
else:
    adress = pyperclip.paste()
    print('Opening: https://www.google.com/maps/place/' + adress + '...')
    webbrowser.open('https://www.google.com/maps/place/' + adress)
    #Abrimos o navegador com o endereco pelo Clipboard do usuario.