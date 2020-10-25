#! python3

#all_of_string

#O programa demonstra muitas maneiras de como modelar as nossas Strings.

print("Dog's Bar")
#Podemos usar as aspas duplas para usar aspas simples na string como um valor e nao como um fechamento de string.

print('Conca' + 'tenar')
#Intrucao de concatenar duas String e transformar em uma.

print('Docker\'s Team')
#'Caractere de Escape' permite usar caracteres que nao poderia ser usados em uma string de forma comum.
#Lista de Caracteres de escape disponiveis: /' (Aspas Simples), /" (Aspas Duplas),
#/t (Tabulacao), /n (Quebra de Linha / Mudanca de Linha) e \\ (Barra Invertida)

print('Bob\'s the \"Tavern\" proprietary')#Aqui estamos usando tres caracteres de escape. (\', \" e \")

print('Em cima\nEm baixo')#Caractere de Escape para Pular linha

print('\tTabulacao \tTabulacao \tTabulacao \tTabulacao \tTabulacao \tTabulacao \tTabulacao \tTabulacao')
#O Caractere de Escape /t da um espaco grande.

print('Cafe/\\Vodka')#Caractere de Escape para exibir uma barra inversa. Usamos o caracteres de espaco (\\) Vai exibir a "\"

print(r'Mother\'s Room \t')
#O r tranforma a string em uma string pura(raw String), ignorando todos os caracteres de escape exibindo
#todas as barras invertidas que possui na String.
#Nos pdoemos usar este quando QUEREMOS exibir para o usuario como e escrito um caractere de espaco.

#print(r'Mother's Room')#ERRO, mesmo ele ignoranto todos os caracteres de espaco nos nao podemos so usar aspas.

print(r"Favorites Room's \ Sex Room \ Living Room")
#String pura(raw String), aonde ele ignira todas os caracteres de espaco e exibe todas as baras inversas do valor.

'''
Caro Danilo,

Agradeco a oportunidade mas eu nao estou quanlificado para exercer esta funcao.

Porem, obrigado desde ja.

Att, Matheus'''
#String Multiline, este tipo de exibicao de String vai exibi-la em varias linhas, entao
#a Funcao print nao identada significa que cada espaco em branco
#e um pulo de linha e os outros valores sao exibidos em seguida tudo na ordem do codigo.

print('''String de Multilinhas:

Explicando como os caracteres de espaco funcionam dentro de uma strin de multilinhas.

Aspas simples (') e Aspas Duplas ("), sem a necessidade de um Caractere de Escape.
/t Tabulacao nao vai funcionar.
\\ Barra Invertida funciona.
                                        #Quebra de Linha entre as aspas#
/n Pular linha tambem nao funciona.''')
#Algumas coisas que ocorrem pelo fato de abrir uma String de multilinhas.

Letra = 'Matheus'

name = 'Matheus'

print(name[0])#Exibe o primeiro valor da String name que sera 'M'.

print(name[-1])#Ele exibi de tras pra frente, entao ele vai exibi o ultimo valor da lista, com o valor -1 e assim adiante.

print(name[0:4]) #Pega o valor da String de 0 a 3, porque ele nao exibi o ultimo valor.(Slices)

print(len(name))#Mostran quando caracteres possui a String da variavel name.

print('Math' in name) #Sim possui sera retornar o valor True

print('idiot' not in name)#Ele vai printar True pq eu nao sou um idiota.

print(name * 3)#Vai exibir o name na variavel name tres vezes.

#Entra em um loop que faz a quantidade de vezes do nome 'Matheus' no caso 7 vezes vai printa cada letra e o
#argumnto nomeado end = '' faz com que a proxima letra fica na mesma linha.
for i in name:
    print(i, end = '')

print("\n")

#name[0] = 'The' // ERRO vai dar erro porque a string e um tipo de valor imutavel entao ele nao pode ser mudado apenas sobrescrito.

#Como ela a uma variavel imutavel ela recebe o valor propriamente dito, e nao uma referencia.

#Exemplo de como a variavel String poderia ser 'alterada', apenas sobrescrevendo em cima do valor existente e apagando o valor anterior.

#name = 'Sobrescrito'

#print(name)

newName = name[0:4] + ' ' + name[2:5] + ' God'#Concatenacao de String

print(newName)

name2 = 'Matheus'

print(name2[0])#Vai exibir a primeira letra da String name com o valor Matheus.[M]

print(name2[-1])#Vai exibir a ultima letra da String name com o valor Matheus.[s]

print(name2[0:4])
#Vai exibir da primeira ate a quarta de letra da String name com o valor Matheus.
#Ele nao exibi o ultimo valor entao coloque sempre um a mais [Math]

print('Math' in name2)#Ele me da a resposta do retorno deste teste logico. Se na String name possui 'Math' exibirar True.

print('Idiot' in name2)
#Ele me da a resposta do retorno deste teste logico. Se na string name possui 'Idiot' exibirar True mas nao tem entao sera False

for string in name2:
    print(string, end = '')
    #Primeiro no for ele ira denifir name como uma string que possui 7 carateres consequentemente ele ira fazer 7 loops,
    #depois a cada laco ele ira me exibir a letra correspondente ao valor do laco e ira continuar por fato do argumento nomeado end.
print(sep = '')

Zophie = 'Zophie a Cat'

newZophie = Zophie[0:7] + 'the' + Zophie[8:12]
#Ele vai ate 12 porque e o ultimo valor, nao precisamos pular mais um.
#Fazemos a concatenacao de tres valores para tranformar em apenas um.
#Zophie[0:7] == Zophie + the + ophie[8:12] == cat | no final o valor da variavel vai ficar 'Zophie the Cat'
print(newZophie)

newName = name2[0:4] + ' ' + name2[2:5] + ' God!'

print(newName)

del newZophie

print(Letra[0])#Vai axibir a primeira letra da String. "M"

print(Letra[6])#Vai exibir a setima letra da String. "s"

print(Letra[-2])#Vai exibir a quinta letra da String. "u"

print(Letra[0:5])#Vai exibir da primeira ate a quinta letra, lembrando que slices excluiem um valor do segundo argumento. "Mathe"

print(Letra[-7:-3])#Usando Slice com indices negativos. Lembrando que no final ele exclui
#um valor na exibicao, entao adiciona mais um valor. "Math"

print(Letra[:5])#Vai exibir do O primeiro ate o quinto caractere da String. "Mathe"

print(Letra[3:])#Vai exibir do quarto ate o ultimo caractere da String. "heus"

Nome = Letra[0:4] + ' is a God'#Concatenacao de um valor Slice de uma String e um outro valor de String.

print(Nome)#Exibir a String na variavel Nome.

for Num in Nome:
    print('***' + Num + '***')
    #Podemos usar o looping for com string. Cada letra da String gera uma interacao no looping.
    #E a Variavel Num recebe cada valor a cada interacao.
print("\n")

for Num in range(len(Nome)):
    print('***' + str(Num) + '***')
    #Neste caso usado o len() e o range() a gente pegar a quantidade de valores (indices) em que a String possui e coloca no range
    #para ele ter a quantidade de interacoes referente a quantidade de caracteres na String.

#Nome == 'Math is a god'

print(Nome[-3:])#Exibir um Slice da concatenacao de Nome. Ele pegar o -3 (g) e vai seguinte ate o final para a direita.

print('God' in Nome)#Possui a string 'God' na variavel Nome entao vai retornar True.

print('God' not in Nome)#Como possui 'God' na variavel Nome ele vai retornar False.

print('Idiot' in Nome)#Vai me retornar False porque eu nao sou idiota e nem possui idiota no meu nome porra

print('' in Nome)#Acredito que deja true porque e uma String e entao ele caracterize as aspas.

print("" not in Nome)#Mesmo com Aspas Duplas, no caso o not in ele dara falso por que possui string em Nome

print(Letra.upper())#Retornam todas as letras da variavel Letra (que e uma String) em forma de letras Maiusculas, porem nao as altera.

print(Letra.lower())#Retornam todas as letras da Variavel LEtra (que e uma String) em forma de letras Minusculas, porem nao as altera.

while True:
    Name = input('Digite seu usuario (press enter to leave): ')
    if Name.lower() == 'matheus':#A ideia aqui e aceitar o nome Matheus tanto minusculo quando maiusculo.
        Password = input('Digite sua Senha: ')
        if Password == 'Matheus@14':
            print('Access Allowed')
            break
        else:
            print('Access Denied!')
            Again = input('Do you want to try again? [Y/N]: ')
            if Again.lower() == 'y':
                continue
            else:
                print('Ok!\n')
                break
    elif Name == '':
        print('Bye!\n')
        break

Maiusc = 'MATHEUS' #String totalmente de LETRAS MAIUSCULAS
Minusc = 'matheus' #String totalmente de letras Minusuclas
Joaquin = 'Joaquin' #String mesclando valores MAIUSCULOS E MINUSCULOS

print('String vazia, testando se e MAIUSCULA ' + str(''.isupper()))
print('String vazia, testando se e MINUSUCULA ' + str(''.islower()))
#Se a string estiver vazia ele sempre vai retornar como False.
#Porque vazio nao tem um tamanho de caractere para ser retonado grande ou pequeno.

print(Maiusc.isupper())
#A variavel Maiusc e totalmente maiuscula e entao a funcao vai retornar True.

print(Minusc.isupper())
#A variavel Minusc vai me retornar False porque o valor de Minusc e totalmente de letras minusculas.

print(Joaquin.isupper())
#Entao ele me retornou Falso, porque o valor de Joaquin contem tanto letras maiusculas, como letras minusculas.

print(Joaquin.islower())#O metodovai me retornar False, porque a String tambem contem caracteres de Maiusculos.

print('math1234'.islower())
#A funcao recebendo o valor 'math1234' vai me retonar True, porque math esta todas em letras minusculas e os numero '1234' tambem
#sao letra minusculas (mas tambem podemos ignorar numeros quando testados por estes metodos), mesmo sendo numero esta como string.

print('Math1234'.islower())
#Me retorna False, porque o valor possui um valor em letra maiuscula e os numero nao interferem nesta comparacao.

print('1234'.islower())#Vai me retornar False porque nao tem como compara numeros, se ele sao maiores ou menores.

print('1234'.isupper())#Vai me retonar False porque nao tem como comparar numeros, mesmo estando na forma de caracteres.
#No final das contas quando possui numeros e letras e so vai compara os caracteres, e o numero sao ignorados.

print(Joaquin.upper().lower())#Os processo desta linha sao o seguinte.
#Vou passar a Variavel Joaquin para upper aonde ele sera retornada com letras maiusculas e depois o valor retornado por
#Joquin upper, vai passar por Lower e entao e retornado com o valor minusuculo para a funcao print().

print(Joaquin.upper().lower().upper())#Vai me retornar o valor de Joaquin Maiusculo.
#Quando temos varos metodos dentro de metodos nos lemos como ira processar da esquerda para a direita.

print(Joaquin.upper().isupper())
#Vai me retornar True porque o metodo upper tranforma Joquin em maiusculo e depois verifica se e maiuculo e me retornar o valor logico.
#Transforma a string em maiuscula e depois verifica e e maiuscula.

print(Joaquin.lower().islower())
#Vai me retornar True porque o metodo lower transforma joauqin em minusuclo e verifica se e minusculo e retornar o valor logico do teste.
#Transforma a string em minusucla e depois verifica se e minuscula mesmo. 

print('Metodos isX')#Metodos isX sempre ira me retonar um valor boleano.

#Me retorna False porque a funcao me retornar um valor de string concatenado com letras e
#numero e quando o teste logico e feito em isalpha() ira ser retornado False.
print(Maiusc.isalpha())#Vai me retornar True porque a variavel eh somente constituida de caracteres e nao esta vazia.

def Concatenate(Conc):#Funcao para concatenar strings.
    return Conc + '123'

print(Concatenate(Maiusc).isalpha())#Me retonar falso porque Funcao Concatenate vai me retonar um valor com numeros.

print('Matheus@gmail.com'.isalpha())#Me retona false porque possui um caractere especial.

#A funcao isalnum() vai me retonar True se, a String conter letras ou numeros (em forma de string) e nao estiver vazia.
print(Concatenate(Maiusc).isalnum())#Me retonar True porque a funcao retonar uma String com letras e numeros.
#String de Letras e numeros, me retonar True.

print(Maiusc.isalnum())#String de apenas letras me retonam True.

print('123'.isalnum())#String de apenas numeros me retonar True.

#A funcao isdecimal() so vai me retonar True se a String de comparacao for constituida de numero do tipo inteiro.
print('1234'.isdecimal())##String com apenas numero inteiros em forma de String me retonara o valor boleano True.

print('5.0'.isdecimal())#A funcao vai me retonar False, porque o valor de dentro da Strin do tipo float e a funcao apenas suporta do tipo inteiro

#A funcao ispace() vai me retonar True se a string for constituida apenas de Tabulacoes e/ou Espacos e/ou quebra de linhas e nao estiver vazias.
print(' '.isspace())#Neste caso a Strin esta com um espaco em branco ela ira me retonar um valor bolaeno True.

print('\t'.isspace())#Neste caso como possui uma tabulacao, ela vai me retonar um valor boleano True.

print('\n'.isspace())#Neste caso ele ira me retonar um valor boleano True porque a String esta sendo constituida de uma quebra de linha.

#A funcao istitle() vai me retonar True apenas se a primeira letra da String for MAISUCULA e o resto da PALAVRA for MINUSCULA.

#A funvcao istitle() retornar um valor logico se a string em que ele esta comparando tiver cada palavra da String com a primeira
#letra da palavra Maiuscula e o resto com letras minusculas e nao pode estar vazia. Numeros sao ignorados.
print('Matheus De Oliveira Silva'.istitle())
#Esta string para a funcao istitle() esta sendo interpretada como 4 palavra entao para a funcao retona True as 4 palavras tem que
#possui a primeira letra maiuscula

print('Matheus de Oliveira Silva'.istitle())
#Ele vai me retonar falso porque a segunda palavra 'de' esta comecando com letra minuscula e ele entende e pede que, todas as palavras da
#String comecem com a letra Maisucula.

print('Matheus 1234'.istitle())
#Me retonar True porque a primeira palavra e constituida de uma letra Maiuscula e o resto como sao numeros, ele sao ignorados.

print('MATHEUS'.istitle())#Me retona false porque a segunda letra a diante da palavra e maiuscula.

#O motodo startswith() vai me retonar True quando o argumento da funcao for igual a primeira ou a unica palavra da String de comparacao.
#Obs:Se tentar comparar com umm palavra maior do que as que esta sendom comparada sera retornado False.
print('Matheus de Oliveira Silva'.startswith('Matheus'))
#Neste caso ele me retonar True porque a priemira palavra da String e igual ao do argumento da funcao.

print('Matheus de Oliveira Silva'.endswith('Silva'))
#O metodo endswith() vai me retonar True quando o arumento da funcao for igual ao ultima ou a unica palavra da String de comparacao.
#Neste caso vai me retonar True porque a ultima palavra da String e igual ao valor do argumento da funcao.

print('abcd1234'.endswith('123'))#A funcao endswith() retornara False porque o argumento da funcao nao e igual ao final da String de comparacao.

print('abcd'.startswith('abcde'))#A funcao startswith() me retornara False porque o Argumento da funcao nao e igual a String de comparacao.

print('sadfsdaf')
print('Matheus de Oliveira Silva'.endswith('Matheus de Oliveira Silva'))
#Aqui nos verificamos a string completa, entao como e UMA string ele compara o final dessa uma String que e 'Matheus de Oliveira Silva'.
#Este e o final e tambem o comece. Obs: So esta dando certo porque estamos comparando todas as palavras da String.

print('Matheus de Oliveira Silva'.startswith('Matheus de Oliveira Silva'))
#Ambos vao me retornar True porque, nos buscamos pelo nome completo chamado pelo metodo e colocamos o nome completo ao pssar o valor ao metodo

#O metodo join() concatena uma lista de String e troca cada espaco em branco algum valor de comparacao.
#Ele me tranforma a lista em uma String e cada indice sera adicionado o valor de comparacao, entao no exemplo a baixo temos 4 indices
#e cada indice nos adionaremos uma virgula e um espaco.
print(', '.join(['Joaquin', 'Matheus', 'Edson', 'Carla']))
#Me retonara todos os nomes da lista concatenados e em seguida coloca uma virgula depois de cada palavra.

print(' \\ '.join(['1', '2', '3', '4', '5']))
#Aqui a gente vai contatenar cada String da lista e em cada espaco ele vai adicionar uma barra.
#Obs: Usamos \\ por conta do caractere de espaco.

Vazio = ' ' #Espaco.

Vazio = Vazio.join(['Matheus', 'de', 'Oliveira', 'Silva'])
#Concatenamos cada items da lista de String e adicionamos um espaco depois de mudar de indice.

print(Vazio)
#Vai Concatenar a lista e armazenar em Vazio depois vazio vai passar para a propria variavel para ela ter realmente o valor e em seguida exibe.

#O metodo split() pega uma string e transfoma em lista.
#Obs: Cada espaco na String significa que ele vai criar mais um indice, entao porb exemplo a string 'Matheus de Oliveira Silva' teria 4 indices.
print('Matheus de Oliveira Silva'.split('.'))
#O Metodo vai transformar a string em uma Lista com 4 indices porque ele possui 4 palavras e e separada por um espaco que e padrao do metodo.

print('Matheus_de_Oliveira_Silva'.split())#Neste caso apenas teremos um indice.

print('MatheusABCdeABCOliveiraABCSilva'.split('ABC'))
#De forma padrao todo espaco em branco vai ser excluido e criado outro indice. Mas podemos alterar, em vez de ser um espaco podemos colocar
#um ABC, entao todo ABC vai ser excluido e criado outro indice.
#Como no exemplo acima, ele ira me retonar ['Matheus', 'de', 'Oliveira', 'Silva']

print('Matheus de Oliveira Silva'.split('a'))
#O metodo vai excluir todos os 'a' da string e em seguida vai transformar cada valor em um elemento de lista.

#String de Multilinhas
SeuJorge = '''Nos gostamos de rap porque deixa feliz
Eu nao entendo porque mas e incrivel, eu fico feliz,
inspirado e consigo fazer as coisas, eu levanto pelo rap
faco pelo rap, vivo pelo rap.'''

print(SeuJorge.split('\n'))
#Podemos alterar em vez de espaco para caracteres de espaco tambem. No caso cada quebra de linha ele vai ser um indice.

#Metodos rjust() e ljust()
#O metodo rjust() vai majoritariamente adicionar espacos em branco para a direita da String de comparacao ate que a string de comparacao
#(a string antes do .rjust()) tenha a quantidade de caracteres igual ao primeiro argumento do metodo rjust(), o segundo
#argumento e o que vai ser adicionado, caso nao tenha nenhuma valor de argumento no segundo espaco vai ser adicionado espacos em branco.

#O metodo ljust() vai majoritariamente adicionar espacos em branco para a esquerda da String de comparacao ate que a string de comparacao
#(a string antes do .ljust()) tenha a quantidade de caracteres igual ao primeiro argumento do metodo ljust(), o segundo
#argumento e o que vai ser adicionado, caso nao tenha nenhuma valor de argumento no segundo espaco vai ser adicionado espacos em branco.

print('Hello'.rjust(10))
#Nesta linha acima, nos temos uma string de cinco caracteres e o primeiro argumento de rjust() e 10, entao a string tera dez caracteres
#no total , como nos ja temos cinco da string de comparacao, serao adicionados mais cinco caracteres de empacos em branco a
#direita da string ficando assim: 'Hello     '. 

print('Hello'.ljust(10))
#Nesta linha acima, nos temos uma string de cinco caracteres e o primeiro argumento de ljust() e 10, entao a string tera dez caracteres
#no total , como nos ja temos cinco da string de comparacao, serao adicionados mais cinco caracteres de empacos em branco a
#esquerda da string ficando assim: '     Hello'.

print(Maiusc.ljust(20, '*'))#A varaivel MAIUSC tem 7 caracteres.
#Neste linha acima nos sabemos que a variavel Maiusc possui 7 caracteres, entao o metodo vai adicionar mais 13 asteriscos a esquerda da
#string ate a string possui um total de vinte caracteres.

tt = 'Encontrados!!!'.strip('!')

print(tt.ljust(len(tt) + 1, '!'))

print(Joaquin.rjust(len(Joaquin) + 10, '*'))
#Truque + Esplicacao: A variavel Joaquin possui sete caracteres, entao vamo super que eu quero adicionar mais 10 valores a direita da string
#Eu teria que fazer uma conta e tal, neste caso nao, nos podemos fazer o seguinte, pegar a quantidade de caracteres que a varaivel Joaquin
#possui atraves de um len e adicionar a quantidade de valores que voce deseja. Neste caso acima mostra isso nos estamos adicionando 10
#asteriscos a direita da String.

print(Minusc.rjust(20, '-'))#A varaivel minusc tem 7 caracteres.
#Neste linha acima nos sabemos que a variavel minusc possui 7 caracteres, entao o metodo vai adicionar mais 13 tracos a direita da
#string ate a string possui um total de vinte caracteres.

print(Joaquin.center(20))
#A variavel Joquin possui uma string de sete caracteres, entao o metodo adicionara 13 espacos em branco tanto na direita quando na esquerda.
#Serao 6 para a direita e 7 para a esquerda porque nos devemos interpretar esta atribuicao como coloca um na direita e depois outro na esquerda
#como e um numero impar os ambos lados nao terao a mesma quantidade de sepacos em branco entao quem comeca ira receber um valor a mais no caso
#o lado esquerdo.

print('Welcome Users!'.center(20, '-'))
#A string possui 14 caracteres, entao serao adicionados 6 espacos em branco, 3 na direita e 3 na esquerda.

print('  Matheus  '.strip())
#O metodo strip() ira remover majoritariamente todos os caracteres de espaco em branco. Neste caso ele ira remover tanto da esquerda quanto da
#direita, e vai me retonar String sem eles.

print('   Seu Joaquin   '.lstrip())
#O metodo lstrip() ira remover majoritariamente todos os caracteres de sepaco em branco do lado Esquerdo. Neste caso ambos os lados tem
#espacos em branco, porem apenas o lado Esquerdo sera removido e retonado sem.

print('   Amoedo   '.rstrip())
#O metodo rstrip() vai mejoritariamente remover todos os caracteres de espaco em branco do lado Direito. Neste caso como apenas o lado Direito
#sera removido a aparecia do retorno estaria mais ou menos assim: '   Amoedo'.

print('********Atencao esta chamada e muito portante preste atencao. Voce e inutil*************************'.strip('*'))
#O metodo strip() com argumento ira remover das extremidade da String o valor do argumento da funcao. Neste caso todos os asteriscos (*) das
#bordas serao excluidas.

print('JoaoMatheusJoaoMatheusJoaoJoao'.strip('Joao'))
#Perceba que o Joao dentro de dois Matheus's nao foi excluido, porque ele nao esta entre as extremidades.

#Passar o argumento 'ampS' a strip() lhe dirá para remover as ocorrências de a, m, p e da letra S maiúscula das extremidades da
#string armazenada em spam.
#A ordem dos caracteres na string passada para strip() não importa: strip('ampS') fará o mesmo que strip('mapS') ou strip('Spam').

import pyperclip#Importanto modulo de terceiros.

print('1o. Paste |', pyperclip.paste())#Exbiindo o meu Ctrl-C.
#Nos primeiramente usamos o prefixo do modulo pyperclip e depois a funcao paste do modulo que cola/exibe o texto que ta no seu clipboard Crtl C
#Obs: Qaundo queremos pegar o que ja esta no nosso Ctrl-C sem usar a funcao Copy() nos nao precissamos usar nada apenas o paste().

pyperclip.copy('Matheus')#Colocando ''Matheus' no meu Ctrl-C.
#Neste funcao a cima eu declaro que meu clipboard ('Ctrl-C') possui o valor Matheus, entao quando eu passar para o 'Paste' sera passado 'Matheus'

print('2o. Paste |', pyperclip.paste())#Vamo exibir 'Matheus' porque nos colocamos no Ctrl-C 'Matheus' na linha anterior.

Leave = input('Press Enter to Leave: ')#Um entrada de dados apenas para finalizar o programa.
