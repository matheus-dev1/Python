#! python3

#open_photos.py

#O programa deve abrir os sites de imagems registrados e abrir todas as fotos de uma determinada pesquisa.

#TODO:

import webbrowser, requests, bs4, sys, re
#imports necessarios.

web_ulr = re.compile(r"""
(?i)\b((?:https?:
(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.]
(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)
(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.]
(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)
\b/?(?!@)))
""", re.VERBOSE)
#Regex para encontrar qualquer site na web.

print('Versao atual do Python: %s' %sys.version_info.major)
#o atributo sys.version_info.major identifica qual a versao do nosso python, para nao ocorrer erros de compatibilidade.

#webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
#Aqui nos registramos o navegador firefox, e que todo ulr em que nos abirmos deve ser a partir deste navegador.

if len(sys.argv) == 1:
    print('O arquivo avaliacoes_produto.py possui apenas um argumento. Tente novamente.')

elif len(sys.argv) == 2:
    print('Por favor coloque qual imagem deseja pesquisar.')

elif len(sys.argv) == 3:
    #Exibe este print como se tivesse carregando.
    if sys.argv[1] == 'flickr':#FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | FLICKR | 
        object_response_requests = requests.get('https://www.flickr.com/search/?text=' + ' '.join(sys.argv[2:])) #OK
        print('Opening images...')
        try: 
            object_response_requests.raise_for_status()
            #Verifica se possui um erro.

            object_response_soup = bs4.BeautifulSoup(object_response_requests.text)
            #Pega o arquivo baixado e transforma em uma classe BeautifulSoup
            
            Links = object_response_soup.select('div')

            urls = web_ulr.findall(str(Links))
            for Pagina in urls:
                if Pagina.endswith('.jpg') == True:
                    print('Opening... %s' %Pagina)
                    webbrowser.open(Pagina)
                    #webbrowser.get('firefox').open(Pagina)

        except Exception as error:
            print('Error: %s' %error)
            #Exibe uma mensamgem de erro.

    elif sys.argv[1] == 'imgur':#IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | IMGUR | 
        url_user = 'https://imgur.com/search/score/?q=' + ' '.join(sys.argv[2:]) #OK
        object_response_requests = requests.get(url_user)
        print('Opening images...')
        try: 
            object_response_requests.raise_for_status()
            #Verifica se possui um erro.
            #403 Forbidden (403 Proibido) é um código de resposta HTTP da classe de respostas de erro do cliente, a qual indica que
            # o servidor recebeu a requisição e foi capaz de identificar o autor, porém não autorizou a emissão de um resposta.

            object_response_soup = bs4.BeautifulSoup(object_response_requests.text)
            #Pega o arquivo baixado e transforma em uma classe BeautifulSoup

            Links = object_response_soup.select('img')
            #Procura pelas tag img.

            for Pagina in range(5):#range(len(Links))
                Link = Links[Pagina].get("src")
                Link = Link.split('b')
                Link = ''.join(Link)
                print('Opening... ' + Link)
                #webbrowser.get('firefox').open_new(Link)
                #webbrowser.get('firefox').open(Link)
                webbrowser.open(Link)

        except Exception as error:
            print('Error: %s' %error)
            #Exibe uma mensamgem de erro.
            
    elif sys.argv[1] == 'freepik':#FREEPIK | FREEPIK | FREEPIK | FREEPIK | FREEPIK | FREEPIK | FREEPIK | FREEPIK | FREEPIK | FREEPIK | 
        #header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36","X-Requested-With": "XMLHttpRequest"}
        object_response_requests = requests.get('https://www.freepik.com/search?query=' + ' '.join(sys.argv[2:])) #ERRO 403
        print('Opening images...')
        try: 
            object_response_requests.raise_for_status()
            #Verifica se possui um erro.
            #403 Forbidden (403 Proibido) é um código de resposta HTTP da classe de respostas de erro do cliente, a qual indica que
            # o servidor recebeu a requisição e foi capaz de identificar o autor, porém não autorizou a emissão de um resposta.

            object_response_soup = bs4.BeautifulSoup(object_response_requests.text)
            #Pega o arquivo baixado e transforma em uma classe BeautifulSoup

            Links = object_response_soup.select('img')

            print(Links)
            for Pagina in range(len(Links)):
                Link = Links[Pagina].get("src")
                print('Opening... ' + Link)
                webbrowser.open(Link)

        except Exception as error:
            print('Error: %s' %error)
            #Exibe uma mensamgem de erro.
    else:
        print('Enter a site name. [flicker, imgur, freepik]')