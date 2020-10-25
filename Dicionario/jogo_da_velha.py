#! python3

#jogo_da_velha

#Jogo da velha feito com dicionarios.

#Variaveis Globais
velha = 0
move = ''
Player_Play = ''
theBoard = {'Top-L': 'Top-L', 'Top-M': 'Top-M', 'Top-R': 'Top-R',
            'Mid-L': 'Mid-L', 'Mid-M': 'Mid-M', 'Mid-R': 'Mid-R',
            'Low-L': 'Low-L', 'Low-M': 'Low-M', 'Low-R': 'Low-R'}
#Dicionario que representa um tabuleiro de jogo da velha com os espacos em branco.

def printTheBoard(board):
    line = 0
    print("\n")
    for position in board:
        print('|', board[position], end = ' ')
        line += 1
        if line == 3:
            print('|')
            print('-------------------------')
            line = 0
#Esta funcao basicamente a apresentacao do nosso tabuleiro, ele sera usado dentro de um loop para sempre
#que ouver um alteracao atualizar na tela para o usuario.
            
def Player(play):
    if play == 'x' or play == 'X':
        play = 'O'
    elif play == 'o' or play == 'O':
        play = 'X'
    return play
#Isso aqui e uma funcao para alternar os jogadores entao ele inicia uma vez, para ver quem comeca e vai alternando ate chegar em um resultado.

def result(board, play):
    #Jogos em forma de Linha
    if board['Top-L'] == board['Top-M'] and board['Top-M'] == board['Top-R']:
        return True
    elif board['Mid-L'] == board['Mid-M'] and board['Mid-M'] == board['Mid-R']:
        return True
    elif board['Low-L'] == board['Low-M'] and board['Low-M'] == board['Low-R']:
        return True
    #Jogos em forma de Coluna
    elif board['Top-L'] == board['Mid-L'] and board['Mid-L'] == board['Low-L']:
        return True
    elif board['Top-M'] == board['Mid-M'] and board['Mid-M'] == board['Low-M']:
        return True
    elif board['Top-R'] == board['Mid-R'] and board['Mid-R'] == board['Low-R']:
        return True
    #Jogos em forma de Diagonal
    elif board['Top-L'] == board['Mid-M'] and board['Mid-M'] == board['Low-R']:
        return True
    elif board['Top-R'] == board['Mid-M'] and board['Mid-M'] == board['Low-L']:
        return True

while True:
    Player_Play = input('Quem vai jogar primeiro? (X ou O): ')
    if Player_Play.upper() == 'X' or Player_Play.upper() == 'O':
        break
    else:
        print('Jogador Invalido, tente novamente!')
        continue
        #Inicio do jogo e decide quem joga primeiro.

for plays in range(9):#Um looping de nove porque todo jodo da velha pode haver nove jogadas.
    printTheBoard(theBoard)#Exibir como esta o tabuleiro.
    print('\n')#Pula um espaco.
    while True:
        move = input("Turno para '" + str(Player_Play.upper()) + "'" + ''' Qual posicao vai jogar? 
Exemplo: low-L (Canto inferior esquerdo)
Sua resposta: ''')#Pergunta ao jogador da vez a posicao onde ele jogar jogar.
        if move not in theBoard:
            print('Posicao invalida, tente novemente!')
            continue
        else:
            break
    theBoard[move] = Player_Play.upper()#Atribui o valor do jogador (x ou o) a posicao em que ele selecionou.
    result(theBoard, Player_Play)
    Player_Play = Player(Player_Play)#Depois de executar todas as funcoes ele troca de jobgador.
    if result(theBoard, Player_Play) == True:
        printTheBoard(theBoard)
        print("\n")
        print('Jogo Finalizado, o jogador ' + str(Player_Play.upper()) + ' venceu!')
        break
    else:
        velha += + 1
        if velha == 9:
            printTheBoard(theBoard)
            print('Jogo Terminou em Velha')
