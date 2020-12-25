#! python3

#funcoes

#Programa que defenine diversas funcoes de diversas maneiras. Para revisao
import random

eggs = 'Variavel Escopo Global 1'
Global = 'Variavel Escopo Global 1'
Start = 'y' #Variavel Global.

def parameters(name): #1
    print('Hello, ',name)

def sum(val1, val2): #2
    print('Function 1:', val1 + val2)
    return val1 + val2

def sum2(n1, n2):#3
    print('Function 2:', n1 + n2)
    return n1 + n2

def Decisions(Answer):#4
    if Answer == 1:
        print('Number One!')
        return 'Number One!'
    elif Answer == 2:
        print('Number Two!')
        return 'Number Two!'
    elif Answer == 3:
        print('Number Three!')
        return 'Number Three!'
        
def text():#6
    print('Hello', end = ' ')
    print('World', end = '')
    print('!')
    
def EscopoLocal():#7.0
    eggs = 'Variavel Escopo Local 1'
    ham = 1336
    EscopoLocal2()#Depois de terminar a execucao desta funcao, ela vai ser apagada, entao
                  #a variavel que vai aparecer no print vai ser do valor 1337
    print(eggs)
    print(ham)
    print(Global)

def EscopoLocal2():#7.1
    eggs = 'Variavel Escopo Local 2'
    ham = 1337
    print(eggs)
    print(ham)

def EscopoLocal3(): #8.0
    eggs = 'Variavel Escopo Local 3'
    print(eggs)

def EscopoLocal4(): #8.1
    eggs = 'Variavel Escopo Local 4'
    EscopoLocal3()
    print(eggs)

def ModificarEggs(): #9
    global eggs
    eggs = 'Variavel Escopo Global 1 [Modificada]'
    print(eggs)

def Recusividade(num):
    if num == num + 10:
        return num
    Recusividade(num + 1)
        
def Leave():#Leave / 0
    Start = input('Do you want to try again? [Y/N]: ')
    return Start

while Start == 'y':
    opc = int(input('''[1] Type your name
[2] Sum 1
[3] Sum 2
[4] Random Number Function
[5] Sum1 + Sum2
[6] Hello World!
[7] Local Variable examples
[8] Local Variable examples 2
[9] Modificar Variavel Global em uma Funcao.
[10] or [Any number to Leave]: '''))
    
    if opc == 1: #1
        Name1 = input('Type a name: ')
        parameters(Name1)
        Start = Leave()
        
    elif opc == 2: #2
        sum(5, 5)#Retornamos o valor porem nao atribuimos ele a nenhuma variavel.
        Start = Leave()
        
    elif opc == 3: #3
        sum2 = sum2(5, 5)#Pega o valor de retorno da funcao sum2 e atribui a variavel global sum2.
        Start = Leave()
        
    elif opc == 4: #4
        Decisions(random.randint(1, 3)) #Variavel TheAnswer e declarada e recebera o valor de retorno da funcao Decisions(RNG) com o parametro RNG.
        Start = Leave()
        
    elif opc == 5: #5
        print('Function 1 + Function 2: ',sum(7, 23) + sum2(5, 5))
        Start = Leave()

    elif opc == 6: #6
        text()
        Start = Leave()
        
    elif opc == 7: #7
        EscopoLocal()
        Start = Leave()

    elif opc == 8: #8
        EscopoLocal4()
        EscopoLocal3()
        print(eggs)
        #Todas as variaveis deste bloco de instrucoes tem a variavel chamada 'eggs'
        Start = Leave()

    elif opc == 9: #9
        print(eggs)
        ModificarEggs()
        Start = Leave()
        #Exemplo, se nos chamamos a opcao 9, ela vai alterar a variavel 'eggs'! Na opcao 8 a variavel
        #'eggs' e chama, portanto se fizemos essa sequencia de chama de funcoes, voce vai ver a
        #alteracao da variavel atraves de uma funcao.
    elif opc == 10:
        Recusividade(random.randint(1, 3))
        Start = Leave()
        
    else:#0
        Start = Leave()
        #print(Decisions(random.randint(1,3))) #Forma bem simplificada de como fazer em uma linha o que
        #as tres linhas a cima fazem.
        #print(TheAnswer, 'It`s works')
        #Eu deixei mais isso aqui pela a ideia de que a variavel TheAnswer apos ser declarada
        #pode ser usada em qualquer parte do programa.
