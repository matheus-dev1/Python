#! python3 

#all_of_list_and_metods

#Durante o programa serao definidar e alteradas algumas variaveis para mostrar como podemos utilizar
#de diversas maneira em um programa o tipo de dado Listas.

import copy#Este modulo possui 2 funcoes.
#copy.copy() #Esta funcao e usado para criar uma duplicata de uma valor mutavel como lista ou dicionario e nao apenas copiar uma referencia.
#Copy.deepcopy() #ESta funcao e usada da mesma forma que a copy.copy() porem, ela e usada para lista de listas.

print([1, 2, 3])#Apenas estamos exibindo os itens desta lista. E nao armazenando.

print(['Chama','no','desque'])#Exibindo os itens da lista.

lista = ['isso','aqui','e','uma','lista']#Armazenando um valor de lista em uma variavel chamada "Lista".

print(lista)#Exibindo-a a variavel do tipo lista.

print(lista[3])#Exibindo a variavel lista do tipo lista apenas no indice 4. Obs: Os indices comecam pelo 0.

print(['Chama','no','desque'][2])#Aqui estamos exibindo a posicao 3 da desta lista. No caso 'desque '

print('Chama' + lista[1])#Fazendo a concatenacao de uma String com um item de uma lista do tipo String.
#O valor fica 'Chama aqui'

print('Chama ' + lista[0] + ' aqui de ' + lista[4])#Fazendo uma concatenacao de dois valores de String com
#dois itens de uma lista.

#ERRO print(lista)[1000] #Nao podemos exceder o limite de indices de uma lista se nao da um erro: IndexError

#EROR print(lista[1.0]) #Os indices so podem ser de valores inteiros.

print(lista[int(2.0)])#Podemos usar uma funcao int() para tranformar o valor e inteiro e a lista conseguir
#interpretar o indice.

lista = [['lista', 'com'],
        ['isso','aqui','e','uma','lista']]
        #Criando uma lista de listas e Armazenado na variavel Lista.
        #Possui duas listas dentro de uma lista.
        #Para acessar um valor de uma lista de listas temos que usar indices multiplos.
        #Exemplo listap[1][1]. Com isso eu a lista vai me retornar o valor 'aqui'.
        #Se eu utilizar apenas um indice em uma lista de lista ela vai retornar toda a lista.
        #Exemplo: lista[0]. Vai me retonar: ['lista', 'com']

print(lista[1][4])#Vai me retornar o valor: 'lista'

print(lista[0][-1])#O valor -1 refere-se ao ultimo indice da lista, o valor -2 o penultimo e assim por diante.

print(lista[1][:3])
#Neste comando nos vamo usar indices multiplos e slice para pegar uma parte especifica da lista.
#O primeiro colchete significa a lista de lista onde queremos no caso seria a segunda lista de lista.
#No segundo colchetes significa que nos vamos pegar os itens do inicio ao terceiro item da lista.
#Obs: Ele ira excluir o ultimo item da lista entao sera por isso sera ate o terceiro item da lista.

print(lista[1][:])#Vai retonar do primeiro ao ultimo item da lista.

print('Tamanho da lista: ', len(lista))#O valor retornado sera 2 porque a lista possui dois valor de lista.

print('Tamanho da Lista do segundo indice do valor da lista: ', len(lista[1][:]))
#Aqui estaremos exibindo a segundo lista a lista principal, e em seguida iremos selecionar todos os itens.

lista[0][1] = 'Alterado!'
#Aqui eu vou alterar o valor o segundo valor dentro da primeira lista dentro de uma lista,
#tinha o valor 'com' agora vai ter o valor 'Alterado!'

lista[0][-1] = 'Alterado! (2)'#Alteramos o ultimo valor da primeira lista de listas.

print(lista[0][1])#Exibindo as as alteracoes feitas acima.

lista[0][0] = lista[1][1]
#Alteramos o valor do primeiro item da primeira lista com o segundo valor da segunda lista.

print(lista[0][1] * 3)#Multiplicando o item da lista 3 vezes, e exibindo.
#Podemos armazenar este valor multiplicado em alguma variavel.
#A variavel vai ser do tipo do valor que foi multiplicado, no caso, String.

print([1, 2, 3] * 3)#Multiplicando 3 vezes o valor de lista e exibindo.

Conc = [1, 2, 3] + ['Chama','no','desque']#Concatenacao de listas, ou seja, pega dois valores de lista e
#transforma em um unico valo de lista

print(Conc)#Exibir a lista concatenada e armazenada ena variavel Conc.

Conc = Conc + ['Alow']#Concatenar a Variavel Conc que possui um valor de lista com o valor de lista ['Alow'] e
#adicionar ao ultimo indice.

print(Conc) #Exibir a lista Concatenada.

lista[0][:] += ['Conc mult lists']#Vamos concatenar esta lista na primeira lista de listas da variavel lista.
#NEste caso nos realmente criamos um novo valor e armazenamos na lista.
#Com o metodo append() nos alteramos in plane, isso gera menos processamento e facilita a visualizacao do
#codigo para possiveis manutencoes.

print(lista)#Exibindo mudanca.

del lista[0][0]#Neste caso vamos deletar um item da primeira lista da lista de lista.
#Obs: Podemos deletar uma variavel simples tambem.

print(lista) #Exibir a Lista depois de excluir um item.

Mult = [1, 2, 3]#Criacao da lista que sera usada para multiplo incrementos.

um, dois, tres = Mult#Estamos fazendo um escremento multiplo, estamos colocando cada valor em sequencia.
#Obs: A quantidade de variaveis tem que ser a mesma de indices da lista.

print(um, dois, tres)#Mostrando os valores passados para cada variavel

Mult *= 3#Usamos o operador de atribuicao expandido para multiplicar a lista em tres vezes e atruibuir este
#valor a ela propria ficando: [1, 2, 3][1, 2, 3][1, 2, 3]
#Há operadores de atribuição expandidos para os operadores +, -, *, / e %
#O operador += também pode realizar concatenação de strings e de listas e o operador *=
#pode fazer repetição de string e de lista.

print(Mult)#Exibindo a mudanda pos atruibuicao expandida.

print('Indice do Valor: ', Conc.index('Alow'))
#Um método é o mesmo que uma função, exceto pelo fato de ser chamado “sobre um valor”.
#Se possui dois valores iguais na lista, o primeiro sera exibido seu indice.
#O metodo index, exibe me qual indice o argumento esta na lista.

Conc.append('name')#A chamada anterior ao método append() adiciona o argumento no final da lista.

print(Conc)#Exibindo mudancas pos adicionar item a variavel Conc. Chaamado 'name'.

Conc.insert(3, 'not')#O metodo insert() pode inserir um valor a uma lista em qualquer indice.
#Ele so suporta dois valores, o Indice e o valor a ser alterado.
#O Insert coloca o valor em que voce deseja no indice desejado.
#Os metodos sao alterados 'in plane' isso quer dizer no lugar, entao ele nao recebe um novo valor
#e sim uma alteracao em seu valor.

Conc.remove('desque')#Remove um valor na lista.
#Se o valor aparecer diversas vezes na lista, somente a primeira ocorrência desse valor será removida.
#A instrução del é apropriada quando conhecemos o índice do valor que queremos remover da lista.
#O método remove() é adequado quando conhecemos o valor que queremos remover da lista.

print(Conc)#Exibir a Lista Conc depois das alteracoes.

print('Lista com os valores ordenados: ', Mult.sort())
#Vamos ordenar do menor para o maior uma lista e exibir a alteracao.

print('Lista ordenados na ordem inversa: ', Mult.sort(reverse = True))
#Vamos ordenar uma lista do maior para o menor e exibir a alteracao
#A ordenacao de valores pode ser feita com valores numericos e String(caracteres).

String = ['Anduin', 'archmage', 'Blood', 'bolvar', 'Chris', 'chaco']
#Definimos uma nova lista para ordena-la.
#Apenas podemos ordenar valores de lista apenas um tipo de valor.
#Entao a lista nao pode conter valores do tipo inteiro e String na mesma lista.

print(String.sort())#Tabela ASCII quer dizer que as letras maiusculas vem antes da letras minusculas.
#Sendo assim, a letra a minúscula é ordenada de modo que ela virá após a letra Z maiúscula.

String.sort(key = str.lower)#Usando o Argumento Nomeado (key = str.lower) as letras ficam na Ordem alfabetica
#normal, ou seja, o Python trata como se todas as letras fossem minusculas.

print(String)#Exbindo as alteracoes feitas.

Valor1 = [1, 2, 3]#Definindo uma nova lista.

print('Valor Original da Variavel: ', Valor1)

Valor1 = [4, 5, 6]#a variavel Valor1 tera seus valores sobreescritos (1, 2, 3- sera excluido e o
#valor 4,5,6 entrara na variavel.

print('Subescrevendo um valor na variavel: ', Valor1)#Exibindo o valor sobreescrito.

Valor2 = [7, 8, 9] + [10, 11, 12]#Neste caso o valor sera concatenado.

for i in range(2, -1, -1):
    #Ele vai fazer tres interacoes a 2, 1 e 0 e assim ele vai apagar os tres valores na lista.
    del Valor1[i]

print('Valor1 Vazio: ', Valor1)#Vai estar vazio porque ele foi apagado

f = 7

for i in range(2, -1, -1):#Vai fazer tres interacoes. E vai adicionar tres valores a lista Valor1
    #Os valores sao 7, 8 e 9.
    Valor1.append(f)
    f += 1

print('Valor1 preechido novamente: ', Valor1)#Exibir os valores colocados atraves do looping.

print('Eu vou comecar aqui e, ' + \
      'terminar aqui...')#A instrucao '+ \' faz com que a nossa intrucao possa continuar na proxima linha.

VarRef = [1, 2, 3]#Declarando uma lista.

VarRef2 = VarRef#Passando o valor de lista de outra variavel por refencia para a VarRef2

VarRef2[1] = 5000#Quando alteramos um valor na VarRef2 a VarRef vai sofrer tambem porque apenas passamos a referencia de VarRef para VarRef2.

print('Alteracao na lista referecianda em VarRef2:', VarRef2)#Exibindo as alteracoes feitas em ambas variaveis por causa da referencia.

print('Alteracao tambem na lista VarRef tambem esta sendo refereciada pela mesma lista: ', VarRef)#Alteracao pela referencia.

def ReferenceList(ArgumentReferenceId):#Definimos uma funcao onde o seu parametro vai receber o valor de lista de refencia da variavel VarRef.
    ArgumentReferenceId.append(100)#Nos vamos colocar um valor na ultima posicao do parametro ArgumentReferenceId porem como este parecemetro
    #recebeu apenas a recefencia e nao a lista propriamente dita a alteracao que o parametro vai sofrer a variavel VarRef tambem vai.

ReferenceList(VarRef)
#Mais acima no codigo nos fazemos uma referencia de uma lista a a esta variavel agora vamos ver as mudancas que ela tambem sofre quando
#passando elas como argumento para uma funcao e como o parametro sendo alterado a variavel VarREf sofre alteracoes por fazer referencia
#e nao passar o valor propriamente dito. Valor final : 1, 5000, 3, 100

print(VarRef)#Vai exibir o valor por alteracao do parametro: 1, 500, 3, 100

ListReference = ['Matheus', 'de', 'Oliveira', 'Silva']#Definimos uma referencia de lista para a variavel ListReference.

ListReference2 = copy.copy(ListReference)#Passamos o mesmo valor porem com outro id para a variavel ListReferencia por causa da funcao copy.copy()

ListReference2[0] = 'Karina' #Alteramos o valor da segunda variavel para mostrar que uma nao tem relacao com a outra.

print(ListReference)#Exibir a variavel de lista com id 01 <- Exemplo

print(ListReference2)#Exibir a variavel de lista com o id 02 <- Exemplo
#Explicando a funcao copy,copy()
#Neste ponto nos criamos uma nova lista entao isso quer dizer um novo Id de lista com o mesmo valores da lista
#referenciada na variavelListReference
#Que seria ['Matheus', 'de', 'Oliveira', 'Silva'], porem como e outra lista recebe um novo id, entao e outra lista.
#Se nos fazemos uma alteracao no valor de Lista ListReference2 nao afetara ListReference porque sao duas lista diferentes.

ListReference3 = [[1, 2, 3], [4, 5, 6]]#Declarando uma lista de lista como referencia na varaivel ListReference3

ListReference4 = copy.deepcopy(ListReference3)
#A unica diference do copy.copy() para o copy.deepcopy() e que o deep copy e quando temos mais listas dentro de lista.

ListReference4[0][2] = 'Three' #Alterando o valor da ListReference4 que nao possui o mesmo id da ListReference3.

print(ListReference3)#Exbindo a que cada variavel possui seu id proprio.

print(ListReference4)#Exibindo que apenas esta variavel foi alterada.
