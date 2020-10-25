#! python3

#all_of_debugging.py

#O programa exemplifica, mostra e explica de diversas forma como usar determinadas funcoes para fazer debugging de programa Python.

#TODO: Continuar escrevendo ate terminar o capitulo.
#TODO: Lembrete: Os debuggings logs (registros de erros) sao destinados ao programador.

import traceback, logging
#Imports necessarios para o progra rodar.
logging.basicConfig(filename='all_of_debugging_file_log.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#Usando o argumento nomeado filename='all_of_debugging_file_log.txt' ira abrir/criado um arquivo de texto e armazenar todas as 
#chamadas da funcao logging.DEBUG, ou qualquer outro nivel de debugging, dependendo do nivel que voce colocou.

#logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#A funcao loggin.basicConfig() configura como e o que nos queremos exibir o nosso debug e como 
#ele apareca no decorrer das ocorrencias do programa
#level=logging.DEBUG e referente a %(levelname)s que exibe a palavra debug em todos as ocorrencias da funcao logging.debug().
#format= %(asctime)s Exibe em cada interacao do logging.debug() exibe o tempo em que a linha foi executada.
#format= %(message)s Exibe a cada interacao do loggin.debug() uma string em que o usuario digitou.
#O arquivo nomeado level=logging.DEBUG mostrata todos os niveis de logging.
#Por exemplo nos queremos apenas mostrar os loggings de erros, entao nos passamos ao argumento nomeado, logging.ERROR
#e os logs apenas apresentarao as mensagem ERROR e CRITICAL.

#logging.disable(logging.CRITICAL)
#Com esta linha nos desabilitamos todos os logs do programa.

'''
raise Exception('Isto e uma erro, sua mula. Tente novamentente.')
A instrucao raise + a funcao Exception cria um excessao personalizada, porem, ela pracisa estar em uma
funcao try except.
'''

def print_symbols(symbol_local, width_local, height_local):
    #Funcao criada para receber o simbolo, tamanho de largura e altura.
    #E verificar se tudo esta diacordo para criar um quadrado com o tamanho e 
    #simbolo em que o ususario digitou.
    if len(symbol_local) != 1:
        #Se a quantidade de simbolos em que o usuario digitou for diferente de 1, ou seja, maior ou menor 
        #que um, ele ira executar o bloco de comando a baixo.
        raise Exception('O simbolo possui mais de um caractere.')
        #Como nos estamos rodando esta funcao dentro de um Try...Except caso ele execute esta exceção
        #ele ja fecha a funcao e executa a intrucao Except ESTA FUNCAO.

        #Esta palavra Excecao, Exception('O simbolo possui mais de um caractere.') que sera pasada para a
        #a intrucao Except.

        #Nestar excecoes nao precisamos usar a instrucao return.
    if width_local <= 2:
        #Caso o tamanho passado pelo usuario for diferente de  2, entao o execute o bloco de comando abaixo.
        raise Exception('O valor da Largura e menor ou igual a 2.')
        #A linha a cima significa mais ou menos, passe esta exceção para a funcao Except.
    if height_local <= 2:
        #Caso o tamanho passado pelo usuario for diferente de  2, entao o execute o bloco de comando abaixo.
        raise Exception('O valor da Altura e menor ou igual a 2.')
        #A linha a cima significa mais ou menos, passe esta exceção para a funcao Except.
    
    print(symbol_local * width_local)
    #Multiplica a string do simbolo X quantidade de vezes igual ao valor da largura.
    for contador in range(height_local - 2):
        #Nos tiramos 2 por que a largura ja ocupa os dois primeiros espacos que seriam constituidos
        #pela altura.
        print(symbol_local + (' ' * (height_local - 2)) + symbol_local)
        #Exbie o primeiro simbolo como se tivesse fechando o quandrado e depois pula uma quantidade de 
        #linhas igual ao tamanho da largura - 2 por que os dois sera escritos de forma separada.
        #Depois exibe o simbolo no final do quadrado assim fechando uma parte do quadrado.
        
        #Exemplo: Simbolo: * | Largura: 10 | Altura: 10
        # **********
        # *        *
        # *        *
        # *        *
        # *        *
        # *        *
        # *        *
        # **********

        #       $
        #      $ $
        #     $   $
        #    $     $
        #   $       $ 
        #  $         $
        # $           $
        # $$$$$$$$$$$$$
    print(symbol_local * width_local)
    #Multiplica a string do simbolo X quantidade de vezes igual oa valor da largura

while True:
    #Looping infinito.
    symbol_user = input('Digite um simbolo: ')
    #Usuario digita o simbolo em que ele quer que seja representado pelo quadrado.
    width_user = int(input('Digite a largura de simbolos: '))
    #Usuario digita a quantidade vezes em que o simbolo seja escrito como largura do quadrado.
    height_user = int(input('Digite a altura de simbolos: '))
    #O usuario digita a quantidade de vezes em que o simbolo seja escrito como altura do quadrado.

    #for symbol, width, height in symbol_user, width_user, height_user:
    try:
        #Tenta executar o bloco de comandos abaixo.
        print_symbols(symbol_user, width_user, height_user)
        #A funcao criada por mim recebera os valores: Simbolo, tamanho da largura, tamanho do altura
        #width = Largura
        #height = Altura
        option = input('Quer digitar outro quadrado? [S/N]: ')
        #Pergunta se quer digitar novamente.
        if option.lower() == 's':
            continue
        else:
            break
    except Exception as error:
        #Caso o bloco de comando acima nao de certo ele executara este bloco.
        #Se um objeto Exception for retornado de print_symbols(), essa instrução
        #except o armazenará em uma variável chamada error.
        print('Uma exceção aconteceu: ' + str(error))
        #Exibe uma mensagem + um dos erros criado por nos.
        option_local = input('Quer tentar outro quadrado? [S/N]: ')
        #Pergunta se quer tentar novamente.
        if option_local.lower() == 's':
            continue
        else:
            break

num = int(input('tamanho do triangulo(numero): '))
b = 0
for i in range(num, 0, -1):
    a = i // 2
    if i % 2 == 1:
        print((' ' * a) + '%' * b + (' ' * a))
    b = b + 1

name = 'matheus'
print("Names: {}".format(name))

try:
    raise Exception('This is an error!')
    #Aqui a gente ja tenta executar este bloco de comando que ja nos dirige para a excecao criada por nos.
except Exception:
    #Esta excecao pega o erro executado em try e armazena em uma aruivo de texto.
    object_file_traceback = open('ErrorInfo1.txt', 'w')
    #Criamos uma arquivo de texto em modo escrita.
    object_file_traceback.write(traceback.format_exc())
    #tracebakc.format_exc() esta funcao pega o erro/excecao ocorrida, no caso o erro da clausula try:
    #e retorna a string do erro, e no nosso caso nos estamos escrevendo este erro em um arquivo de texto.
    object_file_traceback.close()
    #Fechamos o arquivo.
    print('The Traceback erro was be sended to ErrorInfo1.txt')
    #Exibimos ao usuario que o log do erro foi armazenado em ErrorInfo1.txt

'''
def error1():
    error2()

def error2():
    raise Exception('This is an error.')
    #NEste comentario se eu fosse executa-lo ele me daria tres erros, o primeiro error1(),
    #o segundo error2() e o terceiro raise Excepetion('')
error1()
'''

valor1 = int(input('Digite um numero: '))
#Usuario digita um valor do tipo inteiro.
valor2 = int(input('Digite outro numero: '))
#Usuario digita outro valor do tipo inteiro.

assert valor1 == valor2, 'O valor1: %s nao e igual ao valor2: %s!' %(valor1, valor2)
#AssertionError
#Aqui a gente usa um assert para comparar os valores, se ele sao iguais, caos for, o programa passa sem
#problema, se nao ele exibe um erro AssertionError  com uma string criada pro voce atraves do Traceback.

#A ideia do assert e verificar se o valor de uma variavel esta com este valor durante todo o programa
#ou ate aonde voce quer, e se nao tiver ele te mostra uma erro, facilitando assim a encontrar erros com valores.

#Falando de forma simples, uma instrução assert diz: “afirmo que esta 
#condição é verdadeira, mas, se não for, há um bug em algum lugar do #programa”.

rua1_para_rua2 = {'Norte-Sul': 'Green', 'Leste-Oeste': 'Red'}
#Sao duas ruas, e cada rua possui uma luz ligada, ou seja, entquando a rua em direcao Norte-Sul esta com a luz verde
#a luz Leste-Oeste esta com a luz vermelha.
rua3_para_rua4 = {'Norte-Sul': 'Red', 'Leste-Oeste': 'Green'}

def semaforo(rua1_para_rua2_local):
    #Funcao semaforo rebece o valor rua1_para_rua2_local
    for chave in rua1_para_rua2_local.keys():
        #No caso terao 2 loopings
        if rua1_para_rua2_local[chave] == 'Green':
            #Se a chave atual for Verde execute o bloco de comandos abaixo.
            rua1_para_rua2_local[chave] = 'Yellow'
            print(rua1_para_rua2_local)
            #A chave atual recebe Amarelo.
            assert 'Red' in rua1_para_rua2_local.values(), 'Neighter light is red' + str(rua1_para_rua2_local)
            #Verifica se possui alguma cor vermelha na chave

        elif rua1_para_rua2_local[chave] == 'Yellow':
            #Se a chave atual for Amarelo execute o bloco de comandos abaixo.
            rua1_para_rua2_local[chave] = 'Red'
            print(rua1_para_rua2_local)
            #A chave atual recebe Vermelho
            assert 'Red' in rua1_para_rua2_local.values(), 'Neighter light is red' + str(rua1_para_rua2_local)
            #Verifica se possui alguma cor vermelha na chave

        elif rua1_para_rua2_local[chave] == 'Red':
            #Se a chave atual for vermelha execute o bloco de comandos abaixo.
            rua1_para_rua2_local[chave] = 'Green'
            print(rua1_para_rua2_local)
            #A chave atual recebe Verde
            assert 'Red' in rua1_para_rua2_local.values(), 'Neighter light is red' + str(rua1_para_rua2_local)
            #Verifica se possui alguma cor vermelha na chave.
            #No segundo loop Leste-Oeste e red, e assim recebe green e assim verificamos se a chave Leste-Oeste e vermelha e no 
            #momento e verde, e o Norte-sul possui a cor amarela, entao quer dizer que nao temos a cor verde neste momento do teste.

semaforo(rua1_para_rua2)
#Chama afuncao semaforo.

#Para desabilitar os teste das assercoes(asserts) no programa python podemos passar a intrucao -O antes do nome do nosso
#programa no momento de executa-lo. Exemplo: python -O all_of_debugging.py

def fatorial(number):#Parâmetros: são os nomes dados aos atributos que uma função pode receber.
    #Funcao rebece um valor do tipo inteiro para fazer o fatorial dele.
    logging.debug('Start of Fatorial: %s' %(number))
    #Exibimos um log de debugging como inicio do processo de debugging desta funcao, e exibindo uma mensagem e o valor recebido na funcao
    for fatorial_turn in range(1, number):
        #Este for faz o fatorial do valor em que a funcao recebe.
        number = number * fatorial_turn
        #Fatorial armazenamento de valor.
        logging.debug('Fatorial: ' + str(fatorial_turn) + ' = ' + str(number) + '!')
        #Aqui o log ira exibir em qual looping no estamos, ou seja, para qual valor ele esta multiplicando valor, e o resultado da 
        #multiplicacao do fatorial e ele vai fazer o log ate o for acabar.
    logging.debug('Final Valor: %s' %(number))
    #Exibir o log do resultado final do fatorial com o valor passado pelo usuario como argumento da funcao.
    return number
    #Retorna o valor do fatorial a chamada da funcao.
    
fatorial_number = int(input('Type a number to do Fatorial: '))
#Usuario digita o valor em que ele quer fazer um fatorial!

logging.debug('Start of Fatorial Debugging!')
#debug() chama logging.basicConfig para saber o que deve ser exibido. Vao estar no formato especificado em logging.basicConfig().
#O retorno de logging.debug() retornara : Tempo + a palabra DEBUG + a string dentro dos parenteses ao console.
print('Fatorial Result: %s' %fatorial(fatorial_number)) #Argumento.
logging.debug('End of Fatorial Debugging!')
#O .debug indica o o nivel de %(levelname)s
#O retorno de logging.debug() retornara : Tempo + a palabra DEBUG + a string dentro dos parenteses ao console.

#Nível    | Função de logging  | Descrição
#DEBUG    | logging.debug()    | É o nível mais baixo. Usado para pequenos detalhes. Geralmente, você estará
#interessado nessas mensagens somente quando estiver diagnosticando problemas.
#INFO     | logging.info()     | Usado para registrar informações sobre eventos em geral em seu programa ou para
#confirmar se tudo está funcionando nesse ponto do programa.
#WARNING  |  logging.warning() | Usado para indicar um problema em potencial que não impede o programa de
#funcionar, porém poderá fazer isso no futuro.
#ERROR    |  logging.error()   | Usado para registrar um erro que fez o programa falhar em fazer algo.
#CRITICAL | logging.critical() | É o nível mais alto. Usado para indicar um erro fatal que fez ou está prestes a fazer o
#programa parar totalmente de executar.