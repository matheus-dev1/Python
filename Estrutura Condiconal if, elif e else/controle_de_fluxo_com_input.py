#! python3

#controle_de_fluxo_com_input

#O programa executa uma das linhas conforma o que o usuario digitar.

spam = int(input('[1] Hello'"\n"
                 '[2] Howdy'"\n"
                 '[Others]: '))

if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings')
