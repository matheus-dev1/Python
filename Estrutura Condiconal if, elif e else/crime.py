#! python3

#crime

#O programa faz 5 perguntas a uma pessoa e dependendo de quantas respostas posivitas e negativas a pessoa interrogada tera uma resposta.

print('Nos ajude a desvendar um crime, responda estas 5 perguntas!')
resp = input('Voce telefonou para a vitima? [S/N] ')
QuestPos = 0
QuestNeg = 0
if resp == 'S' or resp == 's':
    QuestPos = QuestPos + 1
else:
    QuestNeg = QuestNeg + 1
    
resp = input('Voce esteve no local do crime? [S/N] ')
if resp == 'S' or resp == 's':
    QuestPos = QuestPos + 1
else:
    QuestNeg = QuestNeg + 1
    
resp = input('Voce mora perto da vítima? [S/N] ')
if resp == 'S' or resp == 's':
    QuestPos = QuestPos + 1
else:
    QuestNeg = QuestNeg + 1
    
resp = input('Voce devia para a vítima? [S/N] ')
if resp == 'S' or resp == 's':
    QuestPos = QuestPos + 1
else:
    QuestNeg = QuestNeg + 1

resp = input('Voce já trabalhou com a vítima? [S/N] ')
if resp == 'S' or resp == 's':
    QuestPos = QuestPos + 1
else:
    QuestNeg = QuestNeg + 1

if QuestPos == 2:
    print('Voce e suspeito(a)!')
elif QuestPos >= 3 and QuestPos <= 4:
    print('Voce e Cumplice deste crime!')
elif QuestPos == 5:
    print('Voce e o assasino, maos na cabeca voce esta preso!')
elif QuestNeg == 5:
    print('Voce e um inutil saia da aqui imundisse!')
