#! python3

#add_names_list

#O programa possui um menu aonde inicia o programa, tendo 5 opcoes, adicionar pessoas na variavel do
#dado lista(peopleNames[]), mostrar as pessoas adiconadas, deletar nomes, mostrar as posicoes de cada nome
#ou sair do programa, as duas primeiras opcoes sao chamadas atraves de funcoes.

#Uma lista e semelhante a um vetor, porem dentro de uma lista podem ter tipos de dados mesclados.

#Imports
import sys

#Variaveis globais
peopleNames = []

#Estta funcao comeca aqui.
def menu():
    opc = int(input('''\nOptions Menu!

Add People Names [1]

Show Poeple Names added [2]

Find a specific name in your data [3]

Delete a name [4]

Posicion name [5]

To Exit! [Type nothing]

Type here: '''))
    
    if opc == 1:
        addingPeopleNames()
    elif opc == 2:
        print('\nThe People name is: ')
        for name in range(len(peopleNames)):
        #Primeiro nos colocamos uma variavel chamada name para ser como se fosse o indice a cada interacao
        #que o looping vai fazendo. No range nos temos que colocar o len() para que as interacoes ocorra
        #referente a quantidade de nomes em que a lista possui. Entao como nos usamos uma funcao print que
        #colocamos a lista com o name como indice que vai sendo alterado a cada secao do looping. E assim nos
        #conseguimos aprensentar todos os nomes que foram digitados pelo usuario na funcao de adicionar nomes.
            print('Name:',peopleNames[name],'[',name + 1,']')
        menu()
    elif opc == 3:
        findName = input('Search a name in your data: ')
        if findName in peopleNames: #Verifica se o nome digitado dentro da lista.
            print('Name finded: ',findName)
            if findName in peopleNames:#Aqui confimarmamos que o nome esta nos dados.
                print('Status: Name finded!')
            menu()
        elif findName not in peopleNames: #Verifica se o nome nao digitado dentro da lista.
            print('This',findName,'doesnt is in your data!')
            if findName not in peopleNames:#Aqui confirmamos queo nomes nao esta nos dados
                print('Status: Name not finded!')
            menu()
    elif opc == 4:
        findName = input('Delete a name in your data: ')
        if findName in peopleNames:
            for name in range(len(peopleNames)):
                if findName == peopleNames[name]:
                    print(peopleNames[name] + ' deleted!')
                    del peopleNames[name]
            menu()
        else:
            print('This',findName,'doesnt is in your data!')
            menu()
    elif opc == 5:
        findName = input('Type a name to knew your posicion: ')
        print('Posicion name: [', peopleNames.index(findName) + 1,']')
        #Se houver nomes iguias dentro na lista, ele ira buscar e apresentar o primeiro.
        menu()
    else:
        sys.exit
#E termina aqui.

#Esta funcao comeca aqui
def addingPeopleNames():
    while True:
        global peopleNames
        try:
            print('Type a person name [',str(len(peopleNames) + 1),']', end = ': ')
            name = input()
            peopleNames = peopleNames + [name]
            #Ele adiciona um nome e aloca na primeira posicao, se nos adicionamos mais um nome ele
            #aloca mais uma posicao na lista.
            #Isso aqui e a concatenacao de lista cada vez que eu adicionar mais um valor ele vai ser colocado
            #Na ultima posicao da lista.
            opc = input('Stored Data. Do you want to Type again? [Y/N]: ')
            if opc == 'Y' or opc == 'y':
                continue
            else:
                menu()
        except ValueError:
            opc = input('Invalid data. Do you want to Type again? [Y/N]: ')
            if opc == 'Y' or opc == 'y':
                continue
            else:
                menu()
#E termina aqui.
    
menu()#Inicia o programa, chamando a funcao menu()
