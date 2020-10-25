#! python3

#all_of_dictionary_range_in_and_not_in

#Yudo sobre Dicionario, um pouco de lista, ideias de organizacao de Dados com Dicionario e outra coisas que podem
#ajudar no desenvolvimento de outras coisas.

import pprint
#Funcoes de Pprint sao pprint e pformat

myStatus = {'size': 'fat plus', 'color': 'white', 'age': 21}
#Nos atribuindo um dicionario e seus par chave-valor a variavel 'myStatus'.

numberPhone = {'matheus': '(11) 96969509', 'casa matheus': '(11) 43452610'}
#Atribuicao de um dicionario a variave 'numberPhone'.

censo = {'AK': {'Aleutians East': {'pop': 3141, 'tracts': 1},
'Aleutians West': {'pop': 5561, 'tracts': 2},
'Anchorage': {'pop': 291826, 'tracts': 55},
'Bethel': {'pop': 17013, 'tracts': 3},
'Bristol Bay': {'pop': 997, 'tracts': 1}}}

print(censo)
#Neste exemplo nos iremos mostrar todos os dicionarios.

print(censo["AK"])
#Neste exemplo nos iremos mostar todos os dicionarios de AK, ou seja, nao ele propriamente dito, mas
#o que tem dentro dele.

print(censo["AK"].keys())
#Aqui ele ira apenas mostrar a apenas o dicionario de Aleutians East que posuis os valores
#{'pop': 3141, 'tracts': 1}

for county in censo["AK"].keys():
    print(censo["AK"][county])
    #AQui iremos exibir os dicionarios de cada condado.

print(myStatus)#Exibir o valor do tipo dicionario armazenado na variavel 'myStatus'.

print('Its my size: ', myStatus['size'])
#Para exibir o valor de uma chave nos temos que usar a variavel + [nome da chave] e assim o dicionario vai
#nos retornar o valor dentro desta chave.

#print('Its my size:',myStatus['height']) #ERRO se nao tiver a chave entre colchetes ele causara um erro KeyError.

print('I am',myStatus['color'],'and i have',myStatus['age'],'years old')
##Exibindo os valores de algumas chaves do dicionario armazenado em 'myStatus'.

data = {21: 'My age', 43452610: 'My house number phone'}#Atribuindo um dicionario a variavel 'data'.

data2 = {21: 'My age', 43452610: 'My house number phone'}#Atribuindo um dicionario a variavel 'data2'.

print(data)#Exibindo um dicionario armazenado na variavel 'data'.

print(data[21],'is 21')#Exibindo um valor dentro de uma chave do dicionario armazenado em 'data'.

print(data[43452610],'is (11) 43452610')#Exibindo um valor dentro do dicionario 'data'.

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
#O dicionario 'eggs' da Gata zohpie possui, nome, especie e idade

ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
#O dicionario 'ham' da Gaa Zophie possui, nome, especie e idade tambem, porem organizados de outra forma.

print('Valores de Par chave-valor de dois dicionarios com valores desorganizados. Resultado:',eggs == ham)
#Com as 3 linhas a cima no entedemos que nos nao precisamos ter os valores ordenados
#para saber que os valores dos dicionarios sao iguais.

print('Valores de Par chave-valor de dois dicionarios com valores Organizados. Resultado:',data == data2)
#Valores Par chave-valor ordenados, tambem vai dar True.
#Com isso podemos entender que para dar True apenas precisamos que os dois
#dicionarios tenham todos os valores iguais mas nao necessariamente ordenados.

aa = [1, 2]
bb = [2, 1]
#Duas listas com valores iguais, porem nao esta organizada, ou seja, as lista sao diferentes.

print('Valores de Lista desordenado. Resultado: ',aa == bb)#False
#Porem nos valoers de lista para sabemos se os valoers de uma lista tambem possui na outra lista os valoes tem que esta ordenados.

aa2 = [2, 1]
bb2 = [2, 1]
#As duas lista estao ordenadas e com os mesmos valores, entao isso significa que as lista sao iguais.

print('Valores de Lista Ordenados. Resultado: ',aa2 == bb2)#True
#Valores de lista ordenados e ai mostrar True

#print(data['error']) #ERRO #Vai dar um KeyError porque nao existe esta chave dentro do Dicionario.

print('O metodo Values() do Dicionario data: ' + str(data.values()))
#O metodo values() retonar todos os valores de todas as chaves do dicionario,
#porem o valor com que ele retonar nao e uma lista. O valor retonarnado e dict_values.

rotation = 1
for value_uni in data.values():
    #Podemos usar o metodo values() dentro de um loop para, conseguir apresentar os valores de um por um. 
    #Quando nao usamos range nos nao vamo apresentar valores e sim dados, entao ele apresenta um dado de cada vez.
    print('Dictionary Valor: ' + str(rotation) + ' ' + str(value_uni))
    rotation += 1

rotation = 1
for value_uni_list in list(data.values()):
    print('List Valor Return: ' + str(rotation) + ' '  + str(value_uni_list))
    rotation += 1
    #O valor de Retorno vai ser em forma de Lista a cada interacao

print('O metodo keys() do Dicionario data: ', data.keys())
#O metodo Keys vai me retornar todas as chaves que um dicionario possui.

rotacao = 1
for i in data.keys():
    print('Dictionary Keys: ' + str(rotacao) + ' ' + str(i))
    rotacao += + 1
    #Aqui a gente vai retonar as chaves do dicionario a cada interacao

rotacao = 1
for i in list(data.keys()):
    print('List Return: ' + str(rotacao) + ' ' + str(i))
    rotacao += + 1
    #Vamos retonar as chaves do dicionario em forma de lista a cada interacao

print('O metodo Items() do Dicionario data: ', data.items())
#O metodo Items vai me retonar cada valor Par chave-valor do dicionario

rotacao = 1
for i in data.items():
    print('Dictionary Items (Par chave-valor): ' + str(rotacao) + ' ' + str(i))
    rotacao += + 1
    #AQui nos vamores retonar os valores da par-chave do dicionario a cada interacao

rotacao = 1
for i in list(data.items()):#Me retonar o valor par chave-valor em forma de lista.
    print('Items (Par chave-valor)',rotacao, i)
    rotacao += + 1

print(type(data.items()))#Entao este metodo me retonar um dicionario que foi retornado atraves de um metodo items() == dict_Items.
#O mesmo aconteceria se caso eu usasse os metodos keys ou value.
print(type(data))#Aqui ele vai mostrar que mesmo me retornando atraves do metodo, items, ele ainda continua sendo um dicionario.

for key, value in myStatus.items():
    print('Chave:',key, '| Valor:',value)
    #O truque da atribuicao multipla pode ser usada tanto para atribui valores de uma lista para duas ou mais variaveis.
    #Exemplo: cat = ['fat', 'black', 'loud']
    #size, color, disposition = cat
    #Ou podemos usar o truque atribuir para duas variaveis dentro de um loop for e os valores serao retirados de um dicionario
    #Exemplo: spam = {'color': 'red', 'age': 42}
    #for k, v in spam.items():
        #print('Key: ' + k + ' Value: ' + str(v))

print('size' in myStatus)
#Quando nao usamos nenhuma metodo paara verificar se possui algum valor em especifico no dicionario, ele
#vai buscar dentre as chaves.

print('size' in myStatus.keys())#Verifica entre as chaves se possui o valor 'size'.
#Para procurar uma chave especifica dentro de um dicionario nos temos que usar o metodo keys para buscar apenas pelas chaves.

print('fat plus' in myStatus.values())#Verificar se possui um valor chamado 'fat plus' dentre os valores do dicionario.
#Para procurar um valor especifico dentro de um dicionario nos que usar o metodo values para buscar apenas por valores.

print('tall' not in myStatus.values())#Verifica se nao possui um valor chamado 'tall' dentro de todas as chaves do dicionario.

if 'fat plus' in myStatus:
#Verifica dentre as chaves se possui um valor chamado 'fat plus', se for True executa a clausula if se nao excuta else.
    print('Chave')   
else:
    print('Valor')

carac = input('Caracteristica da Zhopie: ')
#O usuario devera digitar uma das caracteristicas da Zhopie que esta dentro de um dicionario.
#A chave e o tipo da caracteristica e o valor e a caracteristica propriamente dita.

print(eggs.get(carac, 'Numero nao encontrado'))
#O metodo get vai buscar no dicionario eggs uma chave que tenha o valor igual o de carac que pode ser qualquer coisa, sendo que
#sera o usuario que ira digitar o valor, e depois de verificar se a chave existi no dicionario, entao ele ira mostra o seu
#valor, se nao ele ira mostra a segunda opcao que n ocaso deste get e 'nao encontrado'.

#ERROR print(eggs['asdsad']) #Vai dar erro porque a chave 'asdsad' nao existe dentro deste dicionario.

number = input('''\nLista de Contatos do Matheus.
Nome de uma pessoa cadastrada: ''')

numberNaoCadastrado = number + ' nao cadastrado'#Criacao de mensagem caso nao possua um numero castrado.

print(numberPhone.get(number, numberNaoCadastrado))
#A linha a cima vai nos mostrar um uma entre duas informacoes dependendo do que o usuario digitar.
#Se ele digitar uma chave correspondente ao que existe no dicionario, ira ser retornado pra ele
#o valor da chave em que ele digitou.
#Entao no nosso caso e se ele digitou o nome de uma pessoa que significa a chave e ela
#estiver no dicionario, sera exibido oseu valor que normamente e o seu numero.
#Mas tambem pode ser um lembrete que tenha sido deixado com o nome desta pessoa e nao o numero.

#A ideia do metodo Get() e verificar se o valor em nos digitamos e uma chave no dicionario associado
#se for ele nos retonar a chave se nao ele nos da um valor padrao de retorno.

if number not in numberPhone:#A partir daqui vamo apresentar um forma arcaica de adicionar uma chave com um valor a um dicionario.
    while True:
        decision = input('''Quer adicionar um numero para esta pessoa? [1]
Quer adicionar um lembre ou menssagem para esta pessoa? [2]
Quer sair? [0] or [ ]: ''')
        if decision == '1':
            number_person = input('Digite o numero de ' + str(number) + '. Exemplo: (11) 43452610: ')
            numberPhone[number] = number_person
            print('Numero de ' + number + 'Adicionado com Sucesso!')
            print('Ultima atualizacao da Base de Dados de Contatos: ',numberPhone)
            break
        elif decision == '2':
            tip = input('Digite uma frase de lembrete para este contato: ')
            numberPhone.setdefault(number, tip)
            #A ideia do setdefault() e semelhante a do Get() com uma unica diferenca em vez dele simplesmente retornar um valor
            #caso o primeiro argumento exista como chave nao dicionario.
            #se o primeiro argumento nao estiver no dicionario ele vai adicionar ao dicionario o valor do primeiro argumento como chave
            #e o valor do segundo argumento de setdefault() como o valor da chave.
            #Obs: ele serao colocados no primeiro 'indice'.
            
            #Exemplo se eu digitar 'matheus' e nao existir este valor como chave no dicionario ele vai adicionar este nome
            #como chave e o valor do segundo argumento
            #de setdefault, que por exemplo seja, 'contato sem numero' e se fosse exibido em seguida o valor par chave
            #seria assim ('matheus': 'contato sem numero')

            #Outra coisa nesta lista ele tambem vai retornar o valor do segundo argumento, entao se tu manda um print ele
            #vai exibir o que tem no segundo argumento.
            print('Ultima atualizacao da Base de Dados de Contatos: ',numberPhone)
            break
        elif decision == '':
            print('Nenhum numero foi adicionado, alterado e nao possui nenhum lembrete para adicionar um numero!')
            break
        else:
            print('Nenhum numero foi adicionado, alterado e nao possui nenhum lembrete para adicionar um numero!')
            break
        
message = 'jiohsdgfsdaiogfsdajklhgjkflhadjklhdjklahfjaklshfjsdakhfjsdak'
count = {}

for caractere in message:
    count.setdefault(caractere, 0)
    count[caractere] = count[caractere] + 1
    #Atribuicao de Dicionario de valor da um dicionario!

print("\n")
print('Contar Caracteres.')
print(count)
#Explicacao completa do programa na pagina 149.

print('\npprint.pprint.')
pprint.pprint(count)#Ele vai printar com as chaves ordenadas, cada par chave-valor por linha.
#Ele vai exibir cada chave e valor em cada linha e depois pular uma linha.

print('\npprint.pformat.')
print(pprint.pformat(count))
#Os dois metodos do modulo importado fazem a mesma coisa.
