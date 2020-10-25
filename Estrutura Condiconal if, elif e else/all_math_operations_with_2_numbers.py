#! python3

#all_math_operations_with_2_numbers

#O programa solicita entre uma das 5 operacoes: Adicao, Subtracao, Multiplicacao, Divisao e Resto da Divisao

Number1 = int(input('Type the first number: '))
Number2 = int(input('Type the second number: '))

Option = int(input('''Choose one option!

[1] Addition
[2] Subtraction
[3] Multiplication
[4] Division
[5] Rest of Division

Type your Decision: '''))

if Option == 1:#Addition
    Addition = Number1 + Number2
    print('Addition Valor: ', Addition)
    if Addition % 2 == 0:
        print('Pair')
    else:
        print('Odd')
    if Addition < 0:
        print('Negative')
    else:
        print('Positive')
    if Addition == round(Addition):
        print('Integer')
    else:
        print('Decimal')
elif Option == 2:#Subtraction
    Subtraction = float(Number2) - float(Number2)
    print('Subtraction Valor: ', Subtraction)
    if Subtraction % 2 == 0:
        print('Pair')
    else:
        print('Odd')
    if Subtraction < 0:
        print('Negative')
    else:
        print('Positive')
    if Subtraction == round(Subtraction):
        print('Integer')
    else:
        print('Decimal')
elif Option == 3:#Multiplication
    Multiplication  = Number1 * Number2
    print('Multiplication Valor: ', Multiplication)
    if Multiplication % 2 == 0:
        print('Pair')
    else:
        print('Odd')
    if Multiplication < 0:
        print('Negative')
    else:
        print('Positive')
    if Multiplication == round(Multiplication):
        print('Integer')
    else:
        print('Decimal')
elif Option == 4:#Division
    Division = Number1 / Number2
    print('Division Valor: ', Division)
    if Division % 2 == 0:
        print('Pair')
    else:
        print('Odd')
    if Division < 0:
        print('Negative')
    else:
        print('Positive')
    if Division == round(Division):
        print('Integer')
    else:
        print('Decimal')
elif Option == 5:#Resr of Division
    restDivision = Number1 % Number2
    print('Rest of Division: ', restDivision)
    if restDivision % 2 == 0:
        print('Pair')
    else:
        print('Odd')
    if restDivision < 0:
        print('Negative')
    else:
        print('Positive')
    if restDivision == round(restDivision):
        print('Integer')
    else:
        print('Decimal')
else:
    print('Invalid Option. Try Again!')
