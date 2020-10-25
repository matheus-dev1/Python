#! python3

#organizar_lista_de_lista

#Programa para exibir listas de listas de forma organizada.

lista = [['Matheus', 'Lol', 'Computador'],#Maior e a Computador = 10
        ['Mobile', 'Cacete', 'Caralho'],#Maior e a Caralho = 7
        ['Cuzao', 'Fuck', 'Daledele']]#Maior e a Daledele = 8 

def print_list(lista_org):
    maior_string = [0, 0, 0] 
    for indice_list in range(3):
        for tam_elemento in range(3):
            if len(lista_org[indice_list][tam_elemento]) > maior_string[indice_list]:
                maior_string[indice_list] = len(lista_org[indice_list][tam_elemento])

    print(maior_string)
    
    for indice_list in range(3):
        for tam_elemento in range(3):
            lista_org[tam_elemento][indice_list] = lista_org[tam_elemento][indice_list].ljust(maior_string[indice_list])

    for indice_list in range(3):
        print(lista_org[indice_list])
              
print_list(lista)
