#leap_year

#O programa solicita ao usuario que digite um ano, e sera verificado se este ano e bissexto ou nao!

Year = int(input('Type a Year: '))
if Year % 4 == 0 and Year % 100 != 0 or Year % 400 == 0: #se for múltiplo de 400 automaticamente é de 4.
    print("Leap Year!")
else:
    print("Not is a Leap Year!")
#Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
#Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
#Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata, deixando o resto igual a zero.
