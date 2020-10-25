#! python3

#lists_to_string_function

#O programa solicita ao usuario que digite uma serie de qualquer coisa, e estes nomes serao passado para uma String.

import copy

def Virgula(ParameterList):#Parametro
    global String
    Contador = 0
    if len(ParameterList) >= 2:
        LenLista = len(ParameterList) - 1
        ParameterList.insert(LenLista, 'and')
    for V in ParameterList:
        if len(ParameterList) >= 2: 
            if Contador >= ParameterList.index('and'): #And ja ta na lista neste ponto!
                String = String + V + ' '    
            elif Contador < ParameterList.index('and'):
                String = String + V + ', '
        elif len(ParameterList) < 2:
            String = String + V + ' '
        Contador += 1
    return String
          
ListValor = []
String = ''

while True:
    LastValor = input('Type something name: ')
    ListValor.append(LastValor)
    Cont = input('Do you want add another name? [Y/N]: ')
    if Cont == 'y' or Cont == 'Y':
        continue
    else:
        ListBackup = copy.copy(ListValor)
        String = Virgula(ListValor)
        #Argumento = Virgula(ListValor) A funcao recebe o valor ListVAlor que e um argumento na hora da chamada da funcao.
        break

print(String)

print("Tipo da Variavel 'String' " + str(type(String)))
