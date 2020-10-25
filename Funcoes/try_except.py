#! python3

#try_except

#O programa cria uma funcao, que tem dois parametros o dividido e o dividendo, ele tenta fazer a divisao, se
#der certo, ele retorna o valor da divisao caso o programa cause o erro ZeroDivisionError que e um
#erro que o dividendo nao pode ser Zero, vai para o bloco Except e executa os bloco.
#Depois na ultima linha ele chama e printa o resultado obtido.

def divide(divideByL, dividerByL):
    try:
        return int(divideByL / dividerByL)
    except ZeroDivisionError:
        return 'ZeroDivisionError'
    #A ideia do except com ZeroDivisionError e que se o bloco dentro de Try nao for executado corretamente
    #ele vai executar a excesao e se o error ZeroDivisionError acontecer ele ira executar o bloco
    #dentro da excesao.
    
divideBy = int(input('Type a number how divide: '))
dividerBy = int(input('Type a number how divider: '))

print('Result: ', divide(divideBy, dividerBy))
#posso usar o try except na chamada da funsao.
