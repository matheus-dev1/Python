#! python3

#Expressoes Regulares

#regex

import re

option = input('''Regex + Explained [1]
Regex Groups [2]
Regex Pipe [3]
Regex Pipe com Prefixo [4]
Regex Optional [5]
Regex Pipe 2 [6]
Regex Optional 2 [7]
Regex Option Cellphone [8]
Regex Asterisco [9]
Regex Adicao [10]
Regex Repeticoes especificas [11]
Regex Greedy and Nongreedy [12]
Regex Findall [13]
Regex com Classes de Caracteres [14]
Regex Acento Circunflexo e Sifrao [15]
Regex Caractere Coringa [16]
Regex variaveis de re.compile[17]
Escreva aqui: ''')
#Opcoes para aprensentar cada funcao diferente ou tipo de pesquisa em uma expressao regular diferente.

if option == '1':
    print()
    phone_number_regex = re.compile(r'\d\d \d\d\d\d-\d\d\d\d\d')#Padrao Brasileiro 11 9696-99509
    #re.compile nao faz nada sozinho mas junto com outras funcoes do modulo re, ele consegue buscar expressoes regulares.
    #O re.compile vai basicamente criar um objeto Regex, isso significa que, este padra de caracteres esta sendo buscado
    #e ele tem que passar pelo re.compile para ser entendido como um padrao a ser buscado pelas outras funcoes do modulo re.
    print('Objeto Regex, criado para ser o padrao do programa: '+ str(phone_number_regex) + "\n")
    value = phone_number_regex.search('Meu telfone e 11 9696-99509')
    #A funcao search() simplemente pega o que ta no seu argumento e testa para ver se o padrao passado pelo objeto regex craido em
    #re.compile condiz com alguma parte da string parada no arumento de search().

    #O Metodo search() vai testar o valor que esta em seu argumento se occore alguma semelhanca ao objeto regex criado em re.compile
    #Se possui alguma ocorencia ele vai pegar a primeira e para e armazenar navariavel value, o valor obtido.
    print('''re.Match object [1] (Mostra que foi criado um objeto Match, que significa que foi \
encontrado um valor igual ao regex passado pelo re.compile)

span=(14, 27) [2] (O span tem dois numero o primeiro e aonde comeca a ocorrencia encontra e o segundo numero e aone termina a ocorrencia.)

match='' [3] (Foi o valor encontrado e armazenado na variavel 'Value' ''', end='')
    print(str(value) + ')' + '\n')
    print('Numero encontrado: ' + value.group())
elif option == '2':
    print()
    phone_number_regex2 = re.compile(r'(\(\d{2}\)) (\d{4})-(\d{5})')#Temos que escapar o caractere de \( \) para podemos busca-los.
    #Separando com varios grupos nos conseguimos exibir cada grupo especificamente atravez do metodo group() com o argumento
    #de valor inteiro para representar o grupo que voce quiser.
    value2 = phone_number_regex2.search('Meu telefone e (11) 9696-99509')
    print('Sem argumentos e com os parenteses: ' + value2.group() + "\n")
    print('Com looping for: ')
    for i in range(0, 4):
        print(value2.group(i) + ' [' + str(i) + ']')
    print()
    print('Exibindo todos os grupos: ' + str(value2.groups(0)) + "\n")
    #Transforma em uma Tupla de Strings
    #Obs: So podemos usar o Group() no pularal, ou seja, Groups() se a gente criar um regex com parenteses,
    #ou seja um ou mais grupos.
    ddd, num1, num2 = value2.groups()#Multipla atribuicao
    print('DDD: ' + ddd + '\n1. part num: ' + num1 + '\n2. part num: ' + num2)
    #Exibindo as varaiveis tranferidas pela atriibuicao multipla atraves do metodo groups()
elif option == '3':
    print()
    regex_pipe = re.compile('Matheus|Joao')
    #O simbolo | separa o que deve ser exibido. Basicamente a ocorrencia da string que ocorrer primeiro vai ser exibida.
    #Entao em uma string que Matheus aparece primeirio de pois joao, o objeto Match da string 'Matheus' sera criada e nao de 'Joao'
    value3 = regex_pipe.search('Matheus de Oliveira Silva e Joao de Castro')
    #Exibe semper a primeira ocorrencia do texto.
    print(value3.group())#Exibe Matheus
    value3 = regex_pipe.search('Joao de Castro e Matheus de Oliveira Silva')
    print(value3.group())#Exibe Joao
elif option == '4':
    print()
    regex_pipe_2 = re.compile('Carr(ao|inho|oca|o)')#Aqui a gente vai sempre buscar por 'Carr' e o que tiver depois disso e que tenha
    #Dentro do parenteses por exemplo de iver 'inho' depois de Carr ele ira retonar 'Carr' + 'inho' = 'Carrinho'
    value4 = regex_pipe_2.search('Meu Carrinho da conta.')
    print(value4.group())
    print(value4.group(1))
    value4 = regex_pipe_2.search('Meu Carroca da conta.')
    print(value4.group())
elif option == '5':
    print()
    regex_optional = re.compile(r'Bat(wo)?man')#Se tiver wo ele ira teronar bat + wo + man, se nao apenas bat + man
    #A String wo em parenteses e depois uma interrogacao, faz o seguinte, ele pega essa string e so vai criar um objeto match COM ELA, se
    #ela estiver mas se nao tiver sera criadu m objeto match sem o wo
    value5 = regex_optional.search('The best hero is Batman')
    #objeto Match criado sem o wo, porque ele esta na string do argumento de search()
    print(value5.group())
    value5 = regex_optional.search('The best hero is Batwoman')
    #AQui ele vai exibir wo porque esta na String de argumento de Search()
    print(value5.group())
elif option == '6':
    print()
    regex_pipe_2 = re.compile(r'\d{2}/\d{2}/\d{4}|\d{2}.\d{2}.\d{4}')
    #AS chaves aqui servem para multiplicar a string antecessora. E o simbolo | para dicidir exibir um outro dependendo da ocorrencia
    #que tiver no argumento de search
    value6 = regex_pipe_2.search('04.05.2020')
    #Como aqui tem os ponto depois de cada numero, ele vai criar o objeto com os pontos porque este padcrao TAMBEM existe.
    print(value6.group())
    value6 = regex_pipe_2.search('04/05/2020')
    #Podemos tambem usar o outro padrao, caso no argumento estiver com barras.
    print(value6.group())
elif option == '7':
    print()
    regex_optional_2 = re.compile(r'(https://www.)?[a-z]+.com')#Estas chaves significaque que a gente esta buscando 7 letras do a ao z.
    #E o https e opcinal, entao o objeto match pode ou ser criado se ele tiver ou nao respectivamente.
    value7 = regex_optional_2.search('youtube.com')
    print(value7.group())
    value7 = regex_optional_2.search('https://www.youtube.com')
    print(value7.group())
    value7 = regex_optional_2.search('twitter.com')
    print(value7.group())
    value7 = regex_optional_2.search('https://www.twitter.com')
    print(value7.group())
    site = input('Digite um site: ')
    value7 = regex_optional_2.search(site)
    print(value7.group())
elif option == '8':
    print()
    regex_optional_3 = re.compile(r'(\(\d{2}\))?\ ?\d{4}-\d{5}')#Se nao houver o DDD ele vai apenas exibir o numero.
    value8 = regex_optional_3.search('9696-99509')
    print(value8.group())
    value8 = regex_optional_3.search('(11) 9696-99509')
    print(value8.group())
elif option == '9':
    print()
    regex_asterisco = re.compile(r'k(k*)')#Caso voce queira apenas pegar os kkkkk temos que escrever como esta nesta linha.
    #O primeiro k e obrigatorio ter, e depois nos adicionamos a quantidade igual ao da string passada no argumento de search()
    #Neste caso do simbolo * e indeterminado entao quantos tiver depois do primeiro k, o objeto sera criado indepente da quantidade.
    value9 = regex_asterisco.search('ta trollando certeza kkkkkkkkkkkkkkkkkkkkkkkkk')
    print(value9.group())
    regex_asterisco_2 = re.compile(r'kus(cu)*')
    #Primeiro kus e um padrao obrigatorio para ser criado o objeto regex, e o cu e opcional, entao pode ter UM ou MAIS deles sendo o mais
    #indeterminado a sua quantidade.
    value10 = regex_asterisco_2.search('Eu como kuscucucucucucucucucucu')
    print(value10.group())
    value10a = regex_asterisco_2.search('Eu como kus')
    print(value10a.group())
elif option == '10':
    print()
    regex_adicao = re.compile(r'(k)+')#Como agente tem mais que 1 'k' no argumento de search() entao ele vai nos retonar nos os k's que
    #seguem uma sequencia e nao sao interrompidos.
    #o simbolo de + exige que tenha pelo menos 1 do valor que esta entre parenteses, no caso acima precisa pelo menos ter um k para
    #o objeto regex ser criado.
    value11 = regex_adicao.search('se fodeu kkkkkk')
    print(value11.group())
    
    regex_adicao_1 = re.compile(r'Te(e)+mo')#Depois do segundo 'e' pode vir quantos quiser e so termina quando chega no 'm'.
    #Neste caso precisa pelo menos ter um e depois do pirmiero e obrigatorio, entao podemos passar como argumento Teeeeeeeeeeeemo que o objeto
    #match sera criado desta maneira.
    Teemo = input("'Teemo' com dois ou mais 'e': ")
    value12 = regex_adicao_1.search(Teemo)
    print(value12.group())
    
    value12 = regex_adicao_1.search('Teemao')
    #Me retonar None, porque este padrao nao corresponde ao objeto regex cridao pelo re.compile.
    print(value12)#Vai me retonar none porque possui apenas 1 'e'. E o final na oe igual.
elif option == '11':
    print()
    regex_repeticoes_especificas = re.compile(r'(Teemo){2}')#Nos fazemos igual aos numero na linha 34.
    #Pegamos a palavra em parenteses e multiplicamos a quantidade de vezes da chave ao lado.
    value13 = regex_repeticoes_especificas.search('aphgfsasdafsafa TeemoTeemo')
    print(value13.group())
    
    value14 = regex_repeticoes_especificas.search('Teemo')#Se nao atender ao requisitos tanto, minimos quanto maximo, ele ira retonar None.
    print(value14)

    regex_repeticoes_especificas_1 = re.compile(r'T(e){2,}mo')
    #O minimo e 2 o maximo e indeterminado.
    Teemo = input("Digite a palavra ' Teemo' com dois ou mais 'e': ")
    value15 = regex_repeticoes_especificas_1.search(Teemo)
    print(value15.group())

    regex_repeticoes_especificas_2 = re.compile(r'Salve (Quinto){,5}')
    #A string entre parenteses pode aparecer 1, 2, 3, 4 ou 5 vezes na string de argumento de search()
    #E Salve e opcional entao pode ou nao conter que o objeto Match e criado.
    value16 = regex_repeticoes_especificas_2.search('Salve QuintoQuintoQuintoQuinto')
    print(value16.group())

elif option == '12':
    print()
    #As expresoes regulare do Python sao Greedy, o que quer dizer que as correspondecia sao feitas sempre com o maior valor possivel.
    #A versao Nongreedy faz com que a correpondia da expressao sempre busque a menor string possivel. Usando um ponto de interrogacao depois
    #da chave nos podemos fazer isso.
    regex_greedy = re.compile(r'(k){3,10}')
    #Greedy, ou seja, busca sempre pela maior string.
    value17 = regex_greedy.search('kkkkkkkk')
    print(value17.group())

    regex_nongreedy = re.compile(r'(k){3,10}?')#{n,m}? ou *? ou +?
    #nongreedy
    value18 = regex_nongreedy.search('kkkkkkkkk')
    print(value18.group())
elif option == '13':
    print()
    regex_findall = re.compile(r'\d')#Sem nenhum grupo.
    value19 = regex_findall.findall('214234234')#Ele me retonar um valor de lista
    #O metodo findall() vai criar uma lista e me retornar todos os valores que ocorrem com o padrao regular passado.
    print(value19)

    regex_findall_2 = re.compile(r'(\(\d{2}\))?\ (\d{4})-?(\d{5})')#Correspondeu a expressao Regular.
    #Quando usamos parentes, ou seja, criamos um objeto regex separado por grupos, ele vai criar uma lista de tuplas onde
    #cada tupla possui um valor completo do regex, no nosso caso ele vai ter o numero intero ((11) 9696-99509) e dentro da tupla ele separa
    #cada grupo do regex, entao a tupla teria os 3 grupos que sao tres valores dentro da tupla. ('(11)', '9696', '99509').
    #Cada tupla representa uma correspondência identificada, e seus itens serão as strings correspondentes a cada grupo da regex.
    #Obs: Quando a gente criar por exemplo 3 grupo no regex, porem a gente coloca um ponto de interrogacao e essa ocorencia ocorre sem
    #um dos grupos ele vai criar um valor vazio ex: (9696-99509)
    value20 = regex_findall_2.findall('Meu telefone celular: (11) 9696-99509 + 9696-99509 + 969699509')
    print(value20)

    #\d Qualquer dígito de 0 a 9. Apenas numeros
    #\D Qualquer caractere que não seja um dígito de 0 a 9, ou seja, qualquer coisa que nao seja numeros.
    #\w Qualquer letra, numeros, dígito ou o caractere underscore. (Pense nisso como uma correspondência
    #de caracteres de “palavra”.)
    #Obs: no \w numero como 1, 2, 3 tambem funcionam.
    #\W Qualquer caractere que não seja uma letra, numeros, um dígito ou o caractere underscore, ou seja, apenas caracteres especias.
    #\s Qualquer espaço, tabulação ou caractere de quebra de linha. (Pense nisso como uma correspondência de caracteres de “espaço”.)
    #\S Qualquer caractere que não seja um espaço, uma tabulação ou uma quebra de linha, ou seja, um numero, uma letra, um digito,
    #caracteres especiais e o underscore.
elif option == '14':
    print()
    #Como agente esta usando apenas uma classe de caracteres no objeto regex, cada caractere que corresponder
    #a expressao vai ser in iten da lista.
    #Obs: segue para as linhas abaixo. 
    regex_d = re.compile(r'\d')
    value21 = regex_d.findall('2352134234521345463635463546')
    print(value21)
    print()

    regex_D = re.compile(r'\D')
    value22 = regex_D.findall('MatheusOIVEVE_@`hotmail.com')
    print(value22)
    print()

    regex_w = re.compile(r'\w')
    value23 = regex_w.findall('123qwerQWEWQE!@#$_')
    print(value23)
    print()

    regex_W = re.compile(r'\W')
    value24 = regex_W.findall('a!@$!$    :')
    print(value24)
    print()

    regex_s = re.compile(r'\s')
    value25 = regex_s.findall('                             ')#Vai identificar quantos espacos tem e cada espaco vira um item na lista.
    print(value25)
    print()

    regex_S = re.compile(r'\S')
    value26 = regex_S.findall('~!@@!~#%$?::"{{_+_erweqrweqrAsdfSADWERWEQRWEQRQWERQ52345235234523452354235235278')
    print(value26)
    print()

    regex_classe_caracteres = re.compile(r'\w+\s\w+\s\w+\s\w+')
    value27 = regex_classe_caracteres.findall('Matheus de Oliveira Silva Karina de Oliveira Silva Pedro de Oliveira Silva')
    print(value27)
    print()

    regex_classe_caracteres_2 = re.compile(r'(\w+)(@)(hotmail|yahoo|gmail|bol)(.com)(.br)?')
    value28 = regex_classe_caracteres_2.findall('matheusdeoliveiraferrero@hotmail.com, Kojodosbr@yahoo.com.br, 23523156512345@bol.com.br')
    print(value28)
    print()

    regex_propria_classe_caracteres = re.compile(r'[a]')#[a] e a+ sao quase a mesma coisa, diferenca e que o a+ precisa de no minino 1 'a'
    #e o [a] nao precisa de um minimo e nao tem um maximo.
    value29 = regex_propria_classe_caracteres.findall('Matheus de Oliveira Silva')
    print(value29)
    print()

    regex_propria_classe_caracteres_2 = re.compile(r'[.,]')#Buscar apenas os pontos e virgulas e isso.
    #Crair as nossas proprias classe nos ajuda a criar um padrao que pode ser usado muitas vezes em um program ou para nao ter que
    #ficar colocando varios | que significa 'ou'.
    value30 = regex_propria_classe_caracteres_2.findall('Ola, eu acredito muito na sua experiencia. Mas nos infelizmente naotemos \
    esta oportunidade no momento.')
    print(value30)
    print()

    regex_propria_classe_caracteres_3 = re.compile(r'[aeiouAEIOU]')
    #Criar um objeto regEx para encontrar qualquer letra que seja entre aeiou ou AEIOU.
    value31 = regex_propria_classe_caracteres_3.findall('Todas as nossas oportunidade estao em analise. A unica disponivel voce mao possui \
    os requisitos.')
    print(value31)
    print()

    regex_propria_classe_caracteres_4 = re.compile(r'[^aeiouAEIOU]')#Criar um objeto regex para encontrar qualquer letra que nao seja
    #aeiou ou AEIOU, ou seja, consoantes.
    value32 = regex_propria_classe_caracteres_4.findall('Todas as nossas oportunidade estao em analise. A unica disponivel voce mao possui \
    os requisitos.')
    print(value32)
    print()
elif option == '15':
    print()
    regex_inicio = re.compile(r'^Mouse')
    #O simbolo cincurflexo significa que o argumento passado em search() e percisa ter sua primeira palavra igual a 'Mouse', se nao
    #o metodo retona None.
    value33 = regex_inicio.search('Mouse Gamer Logitech, R$288,99')
    print(value33)
    print('Valor encontrado: ' + str(value33.group()))
    print()
    
    value34 = regex_inicio.search('Por apenas R$288,99 o Mouse Gamer da Logitech')
    #Vai me retonar None, porque a string contem a palavra Mouse, mas nao no inicio como o objeto regex craio em re.compile
    print('A varaivel valor34 foi retornada com o valor: ' + str(value34) + ' == ' + str(value34 == None))
    print()

    regex_fim = re.compile(r'.$')
    value35 = regex_fim.search('Ola, bom dia.')
    print(value35)
    print('Valor encontrado: ' + str(value35.group()))
    print()

    regex_inicio_fim = re.compile(r'^Hb34$')#Ele tem que comecar e terminar com esta palavra, ou seja, apenas ter ela.
    value36 = regex_inicio_fim.search('Hb34')
    print(value36)
    print()

    #A diferenca entre o metodo search e findall e a quantidade de valor que ele abstrai, enquanto o serach apenas a primeira ocorrencia
    #o metodo findall vai retonar todas as ocorrencais em forma de lista, e quando temos grupos no regex, ele me retonar tuplas dentro de
    #listas
    regex_inicio_fim_2 = re.compile(r'#225')
    value37 = regex_inicio_fim_2.findall('O marcador que nos mais usamos e o #225 que se trada de uma marcacao baseado em pornto \
    e facilita muito a nossa utilizacao dos quadro. Entao aplicamos o #225 com a adicao do red_line e temos uma borna Dragon.')
    print(value37)
    print()
elif option == '16':
    print()
    regex_coringa = re.compile(r'Bo.')
    #Ele vai aceitar como uma ocorrecia apenas mais uma letra depois de Bo e pode ser qualquer letra porem apenas uma.
    #oBS: Mas nao pode ser uma quebra de linha.
    value38 = regex_coringa.findall('Bom dia, Boa Tarde, Boa noite')
    print(value38)
    print()

    regex_coringa_2 = re.compile(r'Nome:(.*) Sobrenome:(.*) Idade:(.*) Endereco:(.*) Bairro:(.*)')
    value39 = regex_coringa_2.findall('Nome: Matheus Sobrenome:Oliveira Idade:21 anos Endereco:Rua Tiradentes, 1837 Bairro:Santa Terezinha')
    #Neste caso o (.*) so irai parar quando eles chegarem no outro valor por exemplo eu posso digitar o quando eu quiser em Nome
    #Se na proxima linha for o Sobrenome, ele para de contar o anterior.
    print(value39)
    print()
    
    regex_coringa_3 = re.compile(r'.*\?')
    #O findall() e muito util quando a gente quer achar varias informacoes, em pedacionhos ,quando a gente quer uma unica informacao
    #ou uma unica grande informacao usamos o search().
    value40 = regex_coringa_3.search('-Ola, tudo bem? -Eu estou bem. -E voce? -Tambem!')
    #Neste caso vamos usar o search porque nos queremos o retono de apenasum valo completo.
    #Que consiste em, uma frase completa aonde ele vai captar todos os caracteres ate o ultimo simbolo de interroacao.
    print(value40.group())
    print()

    regex_coringa_4 = re.compile(r'-.*?\!')
    #Neste tambem vamos uar o search porque nos queremos apenas um resultado e nao uma serie de resultados.
    #E o retorno esperado para esta string seria apenas o -Ola, tudo bem? porque nos estamo usando nongreedy e quando ocorrer
    #o primeiro interrogacao ele para de abstrair caracteres.
    value41 = regex_coringa_4.search('-Ola, tudo bem? -Eu estou bem! -E voce!')
    print(value41.group())
    print()

    regex_coringa_5 = re.compile(r'.*', re.DOTALL)
    #re.compile sem o re.DOTALL nao entende quebra de linha, porem comolando re.DOTALL como segundo argumento dentro de re.compile
    #ele compreende a quebra de linha e apenas isso, ela nao faz parte do padrao, mas apenas faz que com o seu padrao entenda o que
    #e uma quebra de linha.
    
    #O caractere . normalmente corresponde a qualquer caractere, exceto o caractere de quebra de linha.
    #Se re.DOTALL for passado como segundo argumento de re.compile(), o ponto também corresponderá aos caracteres
    #de quebra de linha.
    value42 = regex_coringa_5.search('Em tempos de crise, Medite. \nEsta pratica e uma mudanca interna que liberta o seu strees mental.')
    print(value42.group())
    print()
elif option == '17':
    print()
    regex_no_sensitive_case = re.compile(r'Meditacao', re.IGNORECASE)
    #O segundo argumento em re.compile o re.IGNORECASE vai ignorar todas as diferencas entre letras maiusculas e minusucas, fazendo com que
    #se meu objeto regex estiver com letras maiusculas e eu escrever com letras minusculas em search ele vai me retonar o valor
    #como foir escrito, em letras minusculas, mas ainda continua sendo o valor que nos buscamos.
    print(regex_no_sensitive_case.search('A pratica da meditacao pode nao ser facil e nem trazer beneficios no curto prazo \
    mas vai te dar uma paz de espirito incrivel. Se voce quiser e claro.').group())
    #Podemos usar o group no proprio metodo search()

    regex_sub = re.compile(r'\*')
    #Aonde tiver um asterisoc tem que mudar para a string importnate.
    #Obs: se nao tiver nenhuma ocorremcia ele retonar a string sem nenhuma alteracao.
    value43 = regex_sub.sub('Important', 'Black Cleaver(*), The Blade of the Ruined Kingdom (), Berserker Boots(*)')
    print(value43)
    print()

    regex_sub_2 = re.compile(r'(O)(A)', re.IGNORECASE)
    #Obs: Tanto o argumento de re.compile, como o primeiro argumento de sub, devem ter o r (string pura)
    value44 = regex_sub_2.sub(r'0','O erro e a duvida sempre serao uma companheira, quando o medo esta no meio desta amizade.')
    print(value44)
    print()

    regex_sub_3 = re.compile(r'(\w*)a')
    value45 = regex_sub_3.sub(r'\1 4','O erro e a duvida sempre serao uma companheira, quando o medo esta no meio desta amizade.')
    print(value45)
    print()

    regex_sub_4 = re.compile(r'(\d{2})/(\d{2})/(\d{4})') 
    value46 = regex_sub_4.sub(r'\1.\2.\3','Este codigo foi escrito em: 14/06/2020')
    print(value46)
    print()
    regex_verbose = re.compile(r'''
    (\d{2}|\(\d{2}\))\ ?    #DDD, sendo possivel com barras ou sem barras, mas numero e sempre necessario.
    (\d{4})                 #Primeiros 4 digitos do de um telefone celular.
    (-|\||\/)?              #Traco ou barra invertida ou barra normal.
    (\d{5})                 #Os ultimos 5 numeros.
    ''', re.VERBOSE)        #Os espacos em bracno que nos damos ate chegar nos comentarios tambem sao ignorados.
    #Colosando re.VERBOSE no segundo argumento do re.compile nos conseguimos criar multiplas strins para criar um regex.
    #Isso facilita a visualizacao e podemos comentar cada linha.
    value47 = regex_verbose.findall('(11) 969699509, 11 9696-99509, 11 969699509')
    print(value47)
    print()
    
    regex_variaveis = re.compile(r'''
    (.*)
    '''
    ,re.VERBOSE|    #Permite criar um objeto regex com uma string de multilinhas.
    re.IGNORECASE|  #Ignora caracteres Maiscuslos e minusculos.
    re.DOTALL)      #Ignora quebra de linha
    value48 = regex_variaveis.search('A arte da meditacao e a busca pela paz. \nA busca pela paz e a busca pela liberdade.\
    \nA liberdade e tudo o que voce precisa.')
    print(value48.group())
