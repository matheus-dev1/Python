#! python3

#download_all_xkcd.py

#O programa deve baixar todas as tirinhas do xkcd e armazenar em uma pasta com o nome xkcd.

#TODO: Verificar se a determinda tirinha ja esta baixada
#TODO: Caso chave vazia botrao prev e continue
#TODO: O nosso programa deve ser separado em passo, sendo cada passo uma parte do programa, e isso deve ser feito sabendo
#o que deve ser desenvolvido e os TODO's nao devem ser removidos do programa, isso serve como log (registro de informacoes) do programa.

import requests, bs4, os
#Imports necessarios.

xkcd_url = 'https://xkcd.com/'
#Url da pagina inicial de xkcd, nos precisamos armazena-la em uma varaivel para pode fazer alteracoes com o decorrer do programa.
#No final de cada looping nos fazemos uma concatenacao da URL do link Prev com a da Url do xkcd, assim passando por todos os links.

os.makedirs('xkcd', exist_ok=True)
#Criamos ou abrimos um diretorio dependo se ele ja existe ou nao.
#o argumento nomeado verifica se o diretorio 'xkcd' ja existe, caso ele ja existir, entao ele ignora a criacao da pasta com o nome'xkcd'
#e segue para a proxima linha, caso nao existir ele cria a pasta.
#Obs: Nos nao precisamo mudar o diretorio de trabalho atual porque o nosso arquivo python esta dentro dele, ou seja a pasta esta em
#C:\\Matheus\\Study\\IT\\Python e a pasta tambem, assim nao necessitando a alteracao do CWD deste arquivo.
while xkcd_url.endswith('#') == False:
    #Aqui criamos um looping que faz o downloads e troca de paginas ate a url possui um asterisco como ultimo valor de sua url
    #o que representa que nao possui mais paginas antes desta pagina, ou seja e a primeira pagina, finalizando assim todos os sites.
    print('Downloading page %s...' %xkcd_url)
    #Exibe que esta baixando a pagina.
    object_response_requests_get = requests.get(xkcd_url)
    #Obtemos o objeto response da funcao requests.get().
    try:
        object_response_requests_get.raise_for_status()
        #Verificamos se a resposta do site nao possui problemas.
        object_response_soup = bs4.BeautifulSoup(object_response_requests_get.text)
        #Criamos o object response do metodo BeautfilSoup.
        Comic_Element = object_response_soup.select('#comic img')
        #O #comic img ira buscar por um elemento 'id' com o valor 'comic' e o elemento 'img' depois referente a imagem.
        #O metodo select() com o argumento '#comic img' neste site nos retorna o elemento CSS da imagem que queremos baixar,
        #ou seja, a imagem do quadrinho.
        if Comic_Element == []:
            print('Could not find comic image.')
            #Caso o elemento que nos buscamos esteja vazio(pode ocorrer por que a imagem foi postada de uma maneira diferente do comum)
            #Ele dele exibir esta mensagem.
            Prev_link = object_response_soup.select('a[rel="prev"]')[0]
            #Nos identifcamos o elemento a, que possui o que precisamos, porem possui varios atributos 'a' entao nos devemos 
            #especificar mais, usado o input[type="button"][0] igual ao PRIMEIRO rel="prev" que identifica o que isso e um botao, porem
            #nos nao iremos apertar o botao nos iremos pegar o conteudo que ele leva, exemplo: /2351/
            xkcd_url = 'https://xkcd.com/' + Prev_link.get('href')
            #Depois de ter obtido apenas a linha que realmente nos queremos, nos devemos pegar o text de 'href'
            #e concatenas para um novo link, como se tivesse usando o botao "prev".
            #Tambem devemos contatenar o link para a tirinha anterior porque esta acabou causando um erro e nao sera baixada.
            continue
            #E utilizamos a intrucao 'continue' para que ele volte para o inicio do program, ja na proxima pagina.
        else:
            Comic_Url = 'http:' + Comic_Element[0].get('src')
            #Nos buscamo pelo primeiro atributo src dentro de '#comic img' buscado anteriormente.
            #Fazemos a concatenacao de 'http:' com o elemento obtido, exemplo: //imgs.xkcd.com/comics/synonym_date.png
            print('Downloading image %s...' %Comic_Url)
            #Exibe que esta baixando a imagem.
            object_response_requests_get = requests.get(Comic_Url)
            #A antiga variavel que recebeu o object response da pagina agora ira receber o object response apenas da url da imagem.
            try:
                object_response_requests_get.raise_for_status()
                #Verificamos novamente se nao possui erros na chamada.
                object_xkcd_imagem_file = open(os.path.join('xkcd', os.path.basename(Comic_Url)), 'wb')
                #NA funcao os.path.join() nos vamo 'concatenar' a string para o caminho em que devemos abrir/criar um arquivo.
                #Que tera um aspecto mais ou menos assim: xkcd\\6_foot_zone.png
                #Entao tera um arquivo 6_foot_zone.png dentro da pasta xkcd
                #O open na funcao write binary escreve programa em foram binaria, entao podemos escrever qualquer tipo de arquivo
                #com este tipo de dado.
                #OBS: Observe que o caminho criado por os.path.join() nao possui o .\\, isso e porque ele nao e obrigatorio
                #neste caso ele e opcional, entao caso queira colocar, nao ira fazer diferenca nenhuma, mas se isso facilita sua leitura.
                for Parte in object_response_requests_get.iter_content(100000):
                    #Nos baixamos 100000 bytes por looping.
                    object_xkcd_imagem_file.write(Parte)
                    #Ecrevemos os bytes do arquivo.
                object_xkcd_imagem_file.close()
                #E no final fechamos o arquivo.

                Prev_link = object_response_soup.select('a[rel="prev"]')[0]
                #Nos identifcamos o elemento a, que possui o que precisamos, porem possui varios atributos 'a' entao nos devemos 
                #especificar mais, usado o input[type="button"][0] igual ao PRIMEIRO rel="prev" que identifica o que isso e um botao, porem
                #nos nao iremos apertar o botao nos iremos pegar o conteudo que ele leva, exemplo: /2351/
                xkcd_url = 'https://xkcd.com/' + Prev_link.get('href')
                #Depois de ter obtido apenas a linha que realmente nos queremos, nos devemos pegar o text de 'href'
                #e concatenas para um novo link, como se tivesse usando o botao "prev".

            except Exception as error:
                print(error)
                #Se possui um erro, exibe o erro.
        
    except Exception as error:
        print(error)
        #Se possui um erro, exibe o erro.