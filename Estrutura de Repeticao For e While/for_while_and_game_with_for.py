#! python3

#For_While_and_gameWithFor

#O programa solicita se o usuario vai querer o looping ser utilizado com For ou While. Dentro do For tem uma pergunta em todo looping, se voce acertar
#o looping continua se nao ele para, se voce conseguir acertar o maximo de vezes, exibe uma mensagem.

opc = input('Type your looping preference [For or While]: ')

print('My name is')
if opc == 'For' or opc == 'for':
    for times in range(5):
        print('Matheus Oliveira (',str(times + 1),')')
        trys = int(input('Which the looping position? Obs: Loops starts on position Zero'))
        if trys != times:
            print('Curretly position:',times,"\n"'You Wrong. Try again!')
            break
            #A funcao continue apenas ira voltar para o inicio do looping for, o que o for ja faz isso depois de executar todas as tarefas
            #Agora a funcao Break para definitivamente o looping quando alcancado.
        elif times == 4:
            print('Great you got it right all looping position!')
            
elif opc == 'While' or opc == 'while':
    times = 0
    while times < 5:
        print('Matheus Oliveira (',str(times),')')
        times = times + 1
