#! python3

#atribuicao_multipla_de_listas

#O programa solicita ao usuario que digite o nome, cor e idade de uma pessoa, depois sao exibidos para ele.

statusPersonId = ['name', 'color', 'age']#Lista
number = 0
for person in statusPersonId:
    print('Type',statusPersonId[number],'to a person', end = ': ')
    person = input()
    statusPersonId[number] = person
    number += 1
    
name, color, age = statusPersonId #Atribuicao multipla.
print(' Name:', name, "\n", 'Color:', color, "\n", 'Age:', age, "\n")
