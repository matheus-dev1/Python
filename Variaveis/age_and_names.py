#! python3

#age_and_names

#Basicamente o programa solicita, o nome em valor String para o usuario e a idade em valor Inteiro
#DEpois a idade e somada com mais 2 e exibida na tela uma mensagem com os dados entrados pelo usuario.

#O que vai rodar ele: C:/Users/mathe/AppData/Local/Programs/Python/Python38-32/python.exe 
#O local do Arquivo: c:/Matheus/Study/IT/Python/age_and_names.py
#Ou penas Python + nome do arquivo: python age_and_names.py

userName = input('Name: ')
age = int(input('Age: '))

factor = 2

finalAge = age + factor #Idade mais 2 sempre.

print('In ' + factor + ' years you will be ' + finalAge + ' years old ' + userName + '!')
