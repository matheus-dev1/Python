#! python3

#avaliacoes_produto.py

#abre avaliacoes em diversos sites referente a um produto.

#TODO:

import webbrowser, requests, bs4, sys
#imports necessarios.

print('Versao atual do Python: %s' %sys.version_info.major)
#o atributo sys.version_info.major identifica qual a versao do nosso python, para nao ocorrer erros de compatibilidade.

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
#Aqui nos registramos o navegador firefox, e que todo ulr em que nos abirmos deve ser a partir deste navegador.

if len(sys.argv) == 1:
    print('O arquivo avaliacoes_produto.py possui apenas um argumento. Tente novamente.')

elif len(sys.argv) == 2:
    print('Googling...')
    #Exibe este print como se tivesse carregando.

    object_response_requests = requests.get('https://google.com/search?q=' + 'avaliações sobre' + ' '.join(sys.argv[1:]))
    #Exemplo Razer Kraken
    #A funcao requests.get() retornar uma resposta do site referente ao seu conteudo.
    #Podemos tambem apenas passar sys.argv[1]. Porem na chamada o site deve ser escrito em aspas.

    try: 
        object_response_requests.raise_for_status()
        #Verifica se possui um erro.

        object_response_soup = bs4.BeautifulSoup(object_response_requests.text)
        #Pega o arquivo baixado e transforma em uma classe BeautifulSoup

        Links = object_response_soup.select('div#main > div > div > div > a')
        #Aqui ele correspondera aos links que esta dentro de uma div, que esta dentro de um id #main, que possui mais 3 div's uma
        #dentro de cada uma que no final na ultima div possui uma tag 'a', e dentro dela possui o link que queremos.

        #LinkOpen = min(5, len(Links))
        #A funcao min() pega um valor minimo de paginas para abrir e coloca na variavel numOpen.
        #A função interna min() do Python retorna o menor argumento inteiro ou de ponto flutuante que receber.
        #Há também uma função max() interna que retorna o maior argumento recebido.

        for Pagina in range(len(Links)):
            Link = Links[Pagina].get("href")
            if Link.startswith('http://google.com') == True:
                print('Opening... ' + Links[Pagina].get("href"))
                webbrowser.open(Links[Pagina].get("href"))
            else:
                print('Opening... http://google.com' + Links[Pagina].get("href"))
                webbrowser.open('http://google.com' + Links[Pagina].get("href"))
            #Abre e exibe o site abrindo.

    except Exception as error:
        print('Error: %s' %error)
        #Exibe uma mensamgem de erro.