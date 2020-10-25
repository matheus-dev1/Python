#! python3

#download_photos_web.py

#O programa deve baixar uma serie de fotos referente a pesquisa e sites colocados como argumento.

#TODO:

import webbrowser, requests, bs4, sys, re, os
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

sites_resgistred = {'flickr': 'https://www.flickr.com/search/?text=',
 'imgur': 'https://imgur.com/search/score/?q=',
 'freepik': 'https://www.freepik.com/search?query=', 
 'pixabay': 'https://pixabay.com/images/search/', 
 'pinterest': 'https://br.pinterest.com/search/pins/?q='}

if len(sys.argv) == 1:
    print('O arquivo avaliacoes_produto.py possui apenas um argumento. Tente novamente.')

elif len(sys.argv) == 2:
    print('Por favor coloque qual imagem deseja pesquisar.')

elif len(sys.argv) == 3:
    if sys.argv[1] in sites_resgistred:
        curretly_site = sys.argv[1]
        os.makedirs(curretly_site, exist_ok=True)
        os.chdir('C:\\Matheus\\Study\\IT\\Python\\' + curretly_site)
        local = 'C:\\Matheus\\Study\\IT\\Python\\' + curretly_site
        print(os.getcwd())
        object_response_requests = requests.get(sites_resgistred[curretly_site] + ''.join(sys.argv[2:]))
        try:
            object_response_requests.raise_for_status()
            object_response_soup = bs4.BeautifulSoup(object_response_requests.text, features="html.parser")
            Links = object_response_soup.select('img')
            if Links == []: #FLICKR
                Links = object_response_soup.select('div')
                urls = web_ulr.findall(str(Links))
                for Pagina in urls:
                    if Pagina.endswith('.jpg') == True:
                        print('Opening... %s' %Pagina)
                        Pagina = 'http://' + Pagina
                        object_response_requests = requests.get(Pagina)
                        object_imagem_file = open(os.path.join(local, os.path.basename(Pagina)), 'wb')
                        for Parte in object_response_requests.iter_content(100000):
                            object_imagem_file.write(Parte)
                        object_imagem_file.close()
                        #webbrowser.open(Pagina)

            elif curretly_site == 'pinterest':
                urls = web_ulr.findall(str(object_response_requests.text))
                for Pagina in urls:
                    if Pagina.endswith('.jpg') == True:
                        print('Opening... %s' %Pagina)
                        Pagina = 'http://' + Pagina
                        object_response_requests = requests.get(Pagina)
                        object_imagem_file = open(os.path.join(local, os.path.basename(Pagina)), 'wb')
                        for Parte in object_response_requests.iter_content(100000):
                            object_imagem_file.write(Parte)
                        object_imagem_file.close()
            else:
                for Pagina in range(len(Links)):
                    if curretly_site == 'imgur':
                        Link = Links[Pagina].get("src")
                        Link = Link.split('b')
                        Link = ''.join(Link)
                        Link = 'https:' + Link
                        print('Opening... ' + Link)
                        object_response_requests = requests.get(Link)
                        object_imagem_file = open(os.path.join(local, os.path.basename(str(Link))), 'wb')
                        for Parte in object_response_requests.iter_content(100000):
                            object_imagem_file.write(Parte)
                        object_imagem_file.close()
                    else:
                        Link = Links[Pagina].get("src")
                        Link = 'http://' + Link
                        print('Opening... ' + Link)
                        object_response_requests = requests.get(Link)
                        object_imagem_file = open(os.path.join(local, os.path.basename(Link)), 'wb')
                        for Parte in object_response_requests.iter_content(100000):
                            object_imagem_file.write(Parte)
                        object_imagem_file.close()

        except Exception as error:
            print(error)
            '''
                A intrucao as e como se fosse uma atribuicao de objetos.
                Exemplo
                try:
                    ...
                except TypeError as exc:
                    ...
                '''
