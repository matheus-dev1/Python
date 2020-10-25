#! python3

#matriz_tridimensional

#O programa cria uma matriz tridimensional e nos exibimos todas individualmente de cada dimensao atraves de um for.

Matriz = [[[5.0, 4.5, 7.0, 5.2, 5.1],
[2.1,6.5,8.0,7.0,6.7],
[8.6,7.0,9.1,8.7,9.3]],#Deste ponto para cima podemos entender a primeira turma, com tres alunos representando as linhas e cinco notas cada aluno
[[4.2,5.1,6.0,5.4,5.1],
[9.0,8.0,7.5,8.1,8.8],
[2.3,4.4,6.7,6.6,7.0]]]#Aqui em baixo a mesma coisa, porem e outra turma.

#Exemplo de uso da exibicao de determindao valores em uma matriz. Se nos quisermo apenas o valor de uma profundidade(indice)
#completa nos usamo o Matriz[0] ou Matriz[1].
#Se nos quisermos apresentar cada lista individual de cada profundidade, nos usamos dois indices na Matriz[0][1]
#(Exibindo a primeira lista da primeira profundidade)
#Se nos quisermos apresentar um valor(indice 3) dentro de uma profundidade(indice 1) e de uma lista(indice 2) nos
#usamos Matriz[0][0][3], nos apresentaremos o quarto valor
#a primeira lista da primeira profundidade da Matriz.

print('Primeira Turma!')
for Turma in range(3):#Acessa as tres lista dentro de cada dimensao
    print(Matriz[0][Turma])
print('Segunda Turma!')
for Turma in range(3):#Acessa as tres lista dentro de cada dimensao
    print(Matriz[1][Turma])
