#1 python3

#media_alunos_matriz_3

#Faça um programa que lê duas notas para cada aluno (cada turma tem 3 alunos) de duas turmas.
#Armazene os dados em uma matriz M.
#Cada aluno deve ter três notas (as duas digitadas e a média dessas duas).
#Calcule a média de cada turma e armazene em um vetor TURMA.
#Informe qual turma tem maior média, e quais alunos tiveram média maior que a média de sua turma.

import random

alunos = [[[],[],[]],[[],[],[]]]
media_turma = [[],[]]

for turmas in range(2):
    for aluno in range(3):
        for notas in range(2):
            alunos[turmas][aluno].append(random.randint(0, 10))
        alunos[turmas][aluno].append(sum(alunos[turmas][aluno]) / 2)

for turmas in range(2):
    for aluno in range(3):
        for notas in range(3):
            if notas == 2:
                media_turma[turmas].append(alunos[turmas][aluno][notas])
    media_turma[turmas] = sum(media_turma[turmas]) / 3

if media_turma[0] > media_turma[1]:
    maior_media = 'A primeira turma tem a maior media com ' + str(round(media_turma[0], 3))
else:
    maior_media = 'A segunda turma tem a maior media com ' + str(round(media_turma[1], 3))

print('As duas primeiras notas de cada aluno e no final a terceira nota a media das duas notas.')
for matriz in range(2):
    print(alunos[matriz])#Mostra as notas dos alunos das duas turmas.
    
for media in range(2):
    print('Media da Turma' ,media + 1,':',round(media_turma[media], 3))#Media das turmas.

print(maior_media)#A turma com a maior media.

print('As medias do alunos que foram melhor que a media de sua turma.')
for turmas in range(2):
    for aluno in range(3):
        if media_turma[turmas] < alunos[turmas][aluno][2]:
            print('O aluno',aluno + 1,', sua media:',alunos[turmas][aluno][2], 'e a media de sua turma [',turmas + 1,']', round(media_turma[turmas], 3))
