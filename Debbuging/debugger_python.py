#! python3

#debugger_python.py

#Programa consegue mostrar como o Debugger do IDLE do Python funciona.

# TODO:

#Stack (Pilha) = Mostra informacoes sobre a linha em que estamos no momento.
#Locals (Variaveis Locais) = Exibe as variaveis locais do programa.
#Source (Codigo-Fronte) = Exibe a linha no codigo fonte do programa aonde esta rodando.
#Globals (Variaveis Globais) = Exibe as variaveis globais do programa.

#Go
#Clicar no botão Go fará o programa executar normalmente até terminar ou até
#que um breakpoint seja alcançado. Se o debugging estiver concluído e você quiser que o
#programa continue normalmente, clique no botão Go.

#Step
#Clicar no botão Step fará o debugger executar a próxima linha de código e
#outra pausa será feita novamente. A lista de variáveis locais e globais da
#janela Debug Control será atualizada caso seus valores sejam alterados. Se a
#próxima linha de código for uma chamada de função, o debugger “entrará”
#nessa função e passará para a sua primeira linha de código.

#Over
#Clicar no botão Over fará a próxima linha de código ser executada, de modo
#semelhante ao que ocorre se você clicar no botão Step. Entretanto, se a
#próxima linha de código for uma chamada de função, o botão Over “pulará” o
#código da função. O código da função será executado em velocidade máxima
#e o debugger fará uma pausa assim que a chamada da função retornar. Por
#exemplo, se a próxima linha de código for uma chamada a print(), você não
#estará interessado no código da função interna print(); você simplesmente
#quer que a string passada a ela seja exibida na tela. Por esse motivo, usar o
#botão Over será mais comum que utilizar o botão Step.

#Out
#Clicar no botão Out fará o debugger executar as linhas de código em
#velocidade máxima até retornar da função em que estiver no momento. Se
#você entrou em uma chamada de função com o botão Step e agora
#simplesmente quer continuar executando as instruções até retornar, clique no
#botão Out para “sair” da chamada de função atual.

#Quit
#Se quiser interromper totalmente o debugging e não se importar em continuar
#com a execução do restante do programa, clique no botão Quit. O botão Quit
#encerrará imediatamente o programa. Se quiser executar o programa
#normalmente mais uma vez, selecione DebugDebugger novamente para
#desabilitar o debugger.


import random

print('Enter the first number to add:')
first = input()
print('Enter the second number to add:')
second = input()
print('Enter the third number to add:')
third = input()
print('The sum is ' + first + second + third)
#Quando a gente for fazer debugging desta parte do program nos percebemos um erros nos tipos de dados nos inputs.
#Eles estao com tipo de dado String e nao Inteiro, e no caso o ultimo print ocorre uma concatenacao em vez de soma.

heads = 0
for i in range(1, 1001):
   if random.randint(0, 1) == 1:#1 representa cara.
      heads = heads + 1
   if i == 500:
      print('Halfway is done!')#Breakpoint.
      #Para saber qual o valor de heads quando 'i' ja estiver com o valor de 500 podemos uar o debugger.
      #Um breakpoint pode ser definido em uma linha específica de código e forçará o debugger a fazer
      #uma pausa sempre que a execução do programa alcançar essa linha.
print('Heads came up ' + str(heads) + ' times.')
#Neste caso nos usamoso debugging com os breakpoints para saber em quantas vezes deu cara na volta 500.
