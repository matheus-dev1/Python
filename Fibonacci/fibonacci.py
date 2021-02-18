#! python3

#fibonacci.py

#O programa descreve a serie de fibonacci

def fibonacci(nUser):
    num1, num2, contador = 0, 1, 0

    print(0)
    print(1)

    while contador <= nUser:
        termo = num1 + num2
        num1 = num2
        num2 = termo
        contador += 1
        print(termo)
fibonacci(10)