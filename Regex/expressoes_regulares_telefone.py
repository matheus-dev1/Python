#! python3

#expressoes_regulares_telefone

#Criando um programa de expressoes regulares para encontrar o padrao de telefone.

#Exemplo: (11) 9696-99509

#Obs: A ordem dos if's fazem sentido e devem ser respeitadas.

def phone(number_phone):
    if len(number_phone) != 15:#Se possui 15 caracteres
        return False
    
    if number_phone[0] != '(':#Lado Esquerdo do parenteses
        return False
    
    for i in range(1, 2):#DDD
        if not number_phone[i].isdecimal():
            return False
        
    if number_phone[3] != ')':#Lado direito do parenteses
        return False
        
    if number_phone[4] != ' ':#Espaco
        return False
        
    for i in range(5, 8):#Os quatro primeiros numeros
        if not number_phone[i].isdecimal():
            return False
        
    if number_phone[9] != '-':#Traco
        return False
    
    for i in range(10, 15):#Ultimos 4 numeros
        if not number_phone[i].isdecimal():
            return False
    else:
        return True

Choose = input('''Verificar Apenas numero [1]
Verificar numero em uma frase[2]
Sair[0]
Digite a sua opcao: ''')

if Choose == '1':#Apenas numero
    while True:#Looping infinito
        Number = input('Verifique se um numero e com o formato brasileiro: ')
        if phone(Number) == True:#Se o numero digitado for True, execute a clausula deste if.
            print('O numero ' + Number + ' e um numero com o formato brasileiro.')
            break
        else:#Se retornar Flase, execute a clausula deste else.
            print('O numero ' + Number + ' nao e um numero com o formato brasileiro.')
            Option = input('Deseja tentar novamente? [Y/N]: ')
            if Option.lower() == Option:
                continue
            else:
                break

elif Choose == '2':#Numero com frase
    Sentence = input('Digite uma frase para verificar se possui algum numero no formato brasileiro: ')#Frase
    for Letter in range(len(Sentence)):#Letter sera cada letra
        SentenceVerify = Sentence[Letter:Letter + 15]
        #Aqui nos vamos para uma parte um pouco complexa.
        #Neste trexo nos iremos fazer um slice(pegar de um ponto A a um ponto B) com a String na varaivel Sentence.
        #Usando a frase: 'O numero (11) 9696-99509 e um numero com o formato brasileiro'
        #na primeira interacao a variavel SentenceVerify recebera o valor: 'O numero (11) 96'
        #E entao sera testado se isso representa um numero de telefone com o formato brasileiro, no caso nao entao nao vai exibir nada.
        #na interacao 9 a variavel SentenceVerify ira receber o valor '(11) 9696-99509' e sera testado novamente, no caso e um nuemro de
        #telefone com o formato brasileiro entao sera executado a clausula do if phone(SentenceVerify):
        #E ele segue testando ate terminar a frase.
        if phone(SentenceVerify):
            #Se a variavel SentenceVerify possui os criterios necessairos para ser um numero de telefone com o formato brasileiro
            #ele ira executar esta clausula sempre que for True.
            #Obs: Este if esta dentro do loop, entao toda interacao ele e testado.
            print('O numero ' + SentenceVerify + ' e um numero com o formato brasileiro.')
            
else:#Sair
    print('Adeus')
