#! python3

#O programa e a primeira parte de exemplos de web scraping.

#web_scraping1.py

#TODO:

#pip install -U pip --user (Para atualizar o pip)
#A funcao exit() no console do VSCode sai do shell do python no VSCode.

import requests
#Import necessarios.
#o modulo requests necessita de download entao digite pip install requests.

object_response = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#A funao requests.get() recebe como argumento uma string da URL do site em que quer baixar o arquivo.
#O retorno e o OBJETO RESPONSE que e a resposta do servidor a minha solicitacao de download do arquivo textual contindo nesta pagina.
#Que e um Objeto Response.
#Neste caso a pagina apenas tem texto, e nenhuma tags de html.
#Mas Caso nos baixamos uma pagina que possuis tags html, css e/ou javascript o que sera retornado no object_response sera o codigo.

print('Tipo do Objeto que a funcao resquests.get() retorna:', type(object_response))
#Aqui iremos exibir qual o tipo de dado de retorno do resquests.get()

print('Protocolo do Object Response: ', object_response)
#Aqui exibimos que o VALOR do retorno pela funcao requests.get().

object_response.raise_for_status()
#Testar se o object response nao deu erro, ou seja, e o 202 e nao o 404.

if object_response.status_code == requests.codes.ok:
    #Vamos verificar se a resposta que recebemos do servidor e o que queriamos, se for, ele retorna True e exibe a primeiro mensagem
    #se nao ele exibe a mensagem de else.
    
    #object_response.status_code = Me retorno o valor de 200, o que quer dizer que deu tudo certo.
    #requests.codes.ok = Tambem me retorna 200, e com if podemos verificar se a solicitacao ao servidor deu certo.
    print('Response Obtained!')
else:
    print('Response not Obtained!')

print('Quantidade de caracteres do arquivo: ', len(object_response.text), '\n')
#Exibimos a quantiade de caracteres da pagina web baixada.

print(object_response.text[0:335], '\n')
#Exibimos do primeiro ate o caractere 335 da pagina web textual.

object_response2 = requests.get('https://automatetheboringstuff.com/files/ihsfusahdfuf')
#Tentando receber o object response 202 de uma pagina que nao existe, entao ele nao vai nos retornar o protocolo 202 e sim o protocolo
#404 que significa pagina nao encontrada.

print('Protocolo do Object Response:', object_response2)
#Pagina nao encontrada.

#object_response2.raise_for_status()
#O metodo raise_for_status()
#Neste caso, se houver falha o programa simplesmente para e exibe a mensagem de erro.

try:
    object_response2.raise_for_status()
    #Verifica se a resposta ao servidor foi recebida de forma como solicitada, ou seja, caso nao for 404, ele passa sem problemas.
    #Caso for o response 404 ele me ira causar um erro e ira executar a excecao, porem neste caso ele nao para a execucao do programa.
except Exception as error:
    #as error essas instrucoes armazenam o erro na variavel 'error' e podemos usa-la para exibir de melhor forma posteriomente.
    print('We have a problem: %s' %error)
    #Exibe uma mensagem de erro com o erro especifico em que ocorreu.