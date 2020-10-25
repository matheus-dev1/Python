#! python3

#argumentos_nomeados

#Basicamente demonstra como funciona o argumento nomeado end = e sep =

print('Hello', end = ' a ')#Depois de Hello com o argumento nomeado end a linha nao sera quebrada.
print('World')
print('Matheus','Carlos','Cezar','Ramon', sep = ' + ') #Com o argumento nomeado sep a gente colocado
                                                       #algo na frente de todo valor.
print('Hello', end=' ')#O argumento nomeado so vai considerar a proximo print para nao pular a linha.
print('World')
print('!')
