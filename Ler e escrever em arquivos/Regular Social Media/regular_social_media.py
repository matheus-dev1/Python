#! python3

#regular_social_media.py

#O programa deve poder fazer diversas funcoes para auxiliar o usuario a sempre abrir suas redes sociais favoritas de forma rapida.

#"C:\\Matheus\\Study\\IT\\Python\\Regular Social Media\\regular_social_media.py"

#TODO:

import re, webbrowser, shelve, sys, os
#Imports necessarios.

os.chdir('C:\\Matheus\\Study\\IT\\Python\\Regular Social Media')
#Alterando o CWD (Diretoiro de Trabalho do arquivo) para esta pasta.

print('CWD Atual:', os.getcwd())
#Exibindo a pasta atual do CWD deste arquivo.

web_ulr = re.compile(r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.]
(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)
(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.]
(?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)
\b/?(?!@)))
""", re.VERBOSE)
#RegEx para encontrar qualquer Urls em um texto.

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:\\Program Files\\Mozilla Firefox\\firefox.exe"))
#Registrando o Firefox como navegador que deve ser aberto ao chamar a funcao webbbrowser com o metodo .get() e o argumento 'firefox'.

regular_social_media_shelve = shelve.open('regular_social_media_file')
#Abrindo o arquivo contendo os ulrs salvos.

if len(sys.argv) == 1:
    #Se na chamada do programa possui apenas 1 argumento, entao ele exibira o bloco de comandos a baixo.
    print('Arquivo: regular_social_media.py [Sem argumento.]')
    #Exibir que tem apenas um argumento.
    print("Use 'help' para informacoes.")
    #Exinir ao usuario que pode usar o comando help como segundo argumento para receber informacoes.
    sys.exit()
    

elif len(sys.argv) == 4 and sys.argv[1].lower() == 'save': #SAVE | SAVE | SAVE | SAVE | SAVE | SAVE | SAVE | SAVE | SAVE | SAVE | SAVE | 
    #Caso a chamado programa tenha 4 nomes e o segundo argumento seja "save" entao ele exutara o bloco de comandos a baixo.
    #Argumento (0) = Nome do arquivo (O nome deste arquivo aqui vem primeiro, caso esteja usando o VSCode, devemos colocar python antes).
    #Argumento (1) = Palavra 'save' (O segundo argumento deve ser a palavra "save").
    #Argumento (2) = Nome da "chave" (O terceiro argumento deve ser a chave do arquivo, recomendavel usar no nome do site, exemplo facebook)
    #Argumento (3) = Nome do "valor" (O quarto e ultimo argumento deve conter a ulr do site em que deve ser aberto).
    #Obs: Aqui serao salvos todos os site mais comuns de serem usados por que voce, porem ele e mais especifico para redes sociais.
    #Chaves nos arquivos .dir e .bak - Valores no arquivos .dat
    url = web_ulr.search(sys.argv[3])
    #Verificar se o quarto argumento, ou seja, a url e uma url de verdade.
    if url != None:
        #Se a url nao estiver vazia, entao ele executa o bloco de comandos a baixo para fazer o armazenamento da urls junto com nome dele.
        print("Adicionado %s como sites mais usados..." %url)
        #Exibir que o site esta sendo adicionado aos sites mais usados.
        url_argv = str(sys.argv[3])
        regular_social_media_shelve[sys.argv[2]] = url_argv
        #Escreve a chave e o valor nos aruqivos de texto.
        #regular_social_media_shelve[sys.argv[2]] (Se Refere ao arquivo em que sera adicionado e sua chave dentro das chaves.)
        #= url_argv (Se refere ao valor da chave, ou seja, a url e sera armazenada em um arquivo diferente, porem cada um precida do outro).
        print("%s adicinado com sucesso!")
    else:
        #Caso a url digitado pelo usuario nao seja uma URL verdadeira entao ele executara este bloco de comandos. 
        print("Isto nao e uma URL:", sys.argv[3])

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete': #DELETE | DELETE | DELETE | DELETE | DELETE | DELETE | DELETE | DELETE | 
    print("Deleting %s..." %sys.argv[2])
    #Caso a chamada programa tenha 4 nomes e o segundo seja "delete", entao, execute o bloco de comandos a baixo.
    del regular_social_media_shelve[sys.argv[2]]
    #Ele excluira a chave em que o estiver como segundo argumento, ou seja, ele ira
    #excluir a chave(Nome da URL) e ira inutilizar o valor(URL).

elif len(sys.argv) == 2:
    #Caso a chamada do programa possua apenas 2 valores/nomes execute o bloco de comandos abaixo.
    if sys.argv[1] == 'values': #VALUES | VALUES | VALUES | VALUES | VALUES | VALUES | VALUES | VALUES | VALUES | VALUES | VALUES | VALUES |
        #Se o segundo argumento na chamada do programa for "values" entao, execute o bloco de comandos a baixo.
        urls = web_ulr.findall(str(list(regular_social_media_shelve.values())))
        #Neste linha acima vamos pegar todas as urls de cada "Nome da URL" e armazenar em uma lista chamada urls.
        for url in urls:
            #Para cada urls seja aberta por vez em um looping, onde a quantidade de loopings e determinada pela quantidade de urls a abrir.
            print("Opening %s..." %url)
            #Exibe que esta abrindo determinado site.
            webbrowser.get('firefox').open(url)
            #Abre o site no navegador firefox.

    elif sys.argv[1].lower() == 'list': #LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | LIST | 
        #Se o segundo argumento na chamada do programa for "list" entao, execute o bloco de comandos a baixo.
        urls = web_ulr.findall(str(list(regular_social_media_shelve.keys())))
        #Armazenamos os nomes  da URLS dados pelo usuario e podemos abrir os sites apenas com os nomes que nos redireciona para a URL.
        for url in urls:
            #Para cada urls seja aberta por vez em um looping, onde a quantidade de loopings e determinada pela quantidade de urls a abrir.
            print("Opening %s..." %url)
            #Exibe que esta abrindo determinado site.
            webbrowser.get('firefox').open(url)
            #Abre o site no navegador firefox.

    elif sys.argv[1].lower() == 'delete_all': #DELETE ALL | DELETE ALL | DELETE ALL | DELETE ALL | DELETE ALL | DELETE ALL | DELETE ALL | 
        #Se o segundo argumento na chamada do programa for "delete_all" entao, execute o bloco de comandos a baixo.
        '''
        Neste caso a gente apenas deletaria as chaves do arquivo .dir e .bak, porem ficaria do aqruivo .dat
        for keys in regular_social_media_shelve:
            del regular_social_media_shelve[keys]
        '''
        del_all = open('regular_social_media_file.dat', 'w')
        del_all.close()
        del_all = open('regular_social_media_file.dir', 'w')
        del_all.close()
        del_all = open('regular_social_media_file.bak', 'w')
        del_all.close()
        #Em cada Open() e Close() nos abrimos e nao escrevemos nada, substituindo o texto dentro do arquivo para nada.
        #Executando estas 6 linhas a gente excluir tudo de todos os arquivos referente a este programa.

    elif sys.argv[1].lower() == 'help': #HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | HELP | 
        #Se o segundo argumento na chamada do programa for "help" entao, execute o bloco de comandos a baixo.
        print('py.exe/python regular_social_media_file.py – Exbibe que nao possui nenhum argumento e sugere executar o comando "help".\n\
py.exe/python regular_social_media_file.py save <Nome da URL> <URL> – Salva clipboard na palavra-chave.\n\
py.exe/python regular_social_media_file.py <palavra-chave> - .\n\
py.exe/python regular_social_media_file.py list – Abre todos os sites armazenado pelo usuario.\n\
py.exe/python regular_social_media_file.py values – Abre todos os sites armazenado pelo usuario.\n\
py.exe/python regular_social_media_file.py delete - deleta apenas a chave em que o usuario solicitar.\n\
py.exe/python regular_social_media_file.py delete_all - Excluir tudo dentro de todos os arquivos referente a este programa. \n\
py.exe/python regular_social_media_file.py help – Exibe todos os comandos ao usuario.')

    elif sys.argv[1] in regular_social_media_shelve:
        #Caso o nome do URL existir nos arquivos .dir e .bak deste programa ele deve executar o bloco de comandos a baixo.
        url = regular_social_media_shelve[sys.argv[1]]
        #Armazena o site na varaivel "url".
        print("Opening %s..." %url)
        #Exibe que esta abrindo o arquivo.
        webbrowser.get('firefox').open(url)
        #Abre o site no navegador Firefox.

    elif sys.argv[1] not in regular_social_media_shelve:
        #Caso o nome do URL nao existir nos arquivos .dir e .bak deste programa ele deve executar o bloco de comandos a baixo.
        url = sys.argv[1]
        #Armazena o site na varaivel "url".
        print('O site %s nao esta registrado. Tente novamente.' %url)
        #Exibe que o site nao podera ser aberto, por que ele nao se encontra nos arquivos.
regular_social_media_shelve.close()
#Fecha o arquivo do tipo shelve/shelf.