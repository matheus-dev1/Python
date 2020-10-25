#! python3

#backup_site.py

#O porograma deve passar por todas as paginas de um site a fim de fazer backup de todas as paginas do site.

#TODO: Encontrar todos os href, src e onclick(porem, o onclick necessita do uso de uma regex para web url)
#TODO: Faz o armazenamento dos sites passados em uma lista e se a gente passar por uma pagina que possui este link no codigo, entao
#ele pula este site.
#TODO: Abre um site, armazenano ele, abre todos os links dele e faco o mesmo, e eu sempre verifico se este site ja nao esta na lista.

import requests, bs4, sys

web_urls_list = []
#Lista vazia aonde nos armazenaremos todos os sits em que passarmos.

if len(sys.argv) < 2:
    #Se na chamada no programa possuir menos de 2 argumentos.
    print('Esta faltando o site. Tente novamente.')

elif len(sys.argv) == 2:
    main_url = sys.argv[1]
    #URL principal armazenada em 'main_url'
    object_response_requests_get = requests.get(main_url)
    #Baixa a pagina principal.
    print('Adding the page... %s' %main_url)
    #Exibe mensagem que esta addicionando a pagina.
    try:
        object_response_requests_get.raise_for_status()
        #Verifica se nao possui erros na chamada.
        object_response_soup = bs4.BeautifulSoup(object_response_requests_get.text)
        #Pegamos o texto(.text) ou conteudo(.conten)
        page_code = object_response_soup.select('div a')
        #Procuramos por uma tag 'a' dentro de uma tag 'div'
        for Link in range(len(page_code)):
            #Passamos por todos os links
            if page_code[Link].get('href') == None or page_code[Link].get('href') in web_urls_list or page_code[Link].get('href') == '#':
                continue
            #Se o link retornar None ou ja estiver na lista ou e igual a '#' ele volta ao inicio do looping e vai para o proximo site.
            else:
                if page_code[Link].get('href').startswith('https:') or page_code[Link].get('href').startswith('http:'):
                    #Se o site comecar com https: ou http: ele vai adicionar apenas o site e nao ira adicionar http:
                    web_urls_list.append(page_code[Link].get('href'))
                    #Adiciona na ultima posicao da o retorno do site.
                else:
                    web_urls_list.append('https:' + page_code[Link].get('href'))
                    #Caso nao exista ele ele adiciona o https e adiciona na ultima posicao da lista.
            if page_code[Link].get('src') == None or page_code[Link].get('src') in web_urls_list or page_code[Link].get('src') == '#':
                continue
            #Se o link retornar None ou ja estiver na lista ou e igual a '#' ele volta ao inicio do looping e vai para o proximo site. 
            else:
                if page_code[Link].get('src').startswith('https:') or page_code[Link].get('src').startswith('http:'):
                    #Se o site comecar com https: ou http: ele vai adicionar apenas o site e nao ira adicionar http:
                    web_urls_list.append(page_code[Link].get('src'))
                    #Adiciona na ultima posicao da o retorno do site.
                else:
                    web_urls_list.append('https:' + page_code[Link].get('src'))
                    #Caso nao exista ele ele adiciona o https e adiciona na ultima posicao da lista.
    except Exception as error:
        print(error)
        #Se ocorrer o erro apenas vai exibi-lo e nao para o programa.

    for Link2 in web_urls_list:
        #Aqui nos iremos passar por todos os link obtidos e adicionar os links desses links obtidos.
        try:
            object_response_requests_get = requests.get(Link2)
            #Verificar se nao possui erro.
            print('Adding the page... %s' %Link2)
            #Exibir que esta adicionando a pagina.
            object_response_requests_get.raise_for_status()
            #Verifica se possui erros
            object_response_soup = bs4.BeautifulSoup(object_response_requests_get.text)
            #Transforma o texto da pagina baixada em um objeto BeuatifulSoup
            page_code = object_response_soup.select('div a')
            #Aqui nos procuramos dentro de toda a pagina tags 'a' que estao dentro de tags 'div'
            for Link3 in range(len(page_code)):
                if page_code[Link3].get('href') == None or page_code[Link3].get('href') in web_urls_list or page_code[Link].get('href') == '#':
                    continue
                #Se o link retornar None ou ja estiver na lista ou e igual a '#' ele volta ao inicio do looping e vai para o proximo site.
                else:
                    if page_code[Link3].get('href').startswith('https:') or page_code[Link3].get('href').startswith('http:'):
                        #Se o site comecar com https: ou http: ele vai adicionar apenas o site e nao ira adicionar http:
                        web_urls_list.append(page_code[Link3].get('href'))
                        #Adiciona na ultima posicao da o retorno do site.
                    else:
                        web_urls_list.append('https:' + page_code[Link3].get('href'))
                        #Caso nao exista ele ele adiciona o https e adiciona na ultima posicao da lista.
                if page_code[Link3].get('src') == None or page_code[Link3].get('src') in web_urls_list or page_code[Link].get('src') == '#':
                    continue
                #Se o link retornar None ou ja estiver na lista ou e igual a '#' ele volta ao inicio do looping e vai para o proximo site.
                else:
                    if page_code[Link3].get('src').startswith('https:') or page_code[Link3].get('src').startswith('http:'):
                        #Se o site comecar com https: ou http: ele vai adicionar apenas o site e nao ira adicionar http:
                        web_urls_list.append(page_code[Link3].get('src'))
                        #Adiciona na ultima posicao da o retorno do site.
                    else:
                        web_urls_list.append('https:' + page_code[Link3].get('src'))
                        #Caso nao exista ele ele adiciona o https e adiciona na ultima posicao da lista.
        except Exception as error:
            print(error)
            #Se ocorer um erro exibe o erro.
    print(web_urls_list)
    #Exibe a lista
else:
    print('Ocorreu um erro. Tente novamente.')
    #Se as expectativas das chamadas nao serem atendidas ou serem diferentes das opcoes oferecidas ele exibe este erro e termina
    #o programa e solicita que tente novamente.