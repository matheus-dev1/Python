#!python3

#O progama deve criar 35 provas e 35 cabaritos, correspondente as 35 provas, e cada prova deve conter 50 perguntas, referente
#a cada estado dos estados unidos e cada pergunta deve ter 4 alternativas (A, B, C e D) aonde existe apenas 1 correta.
#No Gabarito possui as 50 questoes com todas as respostas corretas.
#O intuito deste programa e que agente crie uma prova aonde sera usada em uma papel, ma teoria e nao no conputador.

#Provas_aleatorias

import os, random
#Import dos modulos os para manipulacao de paths e random para gerar e gerir valores aleatorios.

Estados_e_Capitais = {'Alabama': 'Montgomery',
'Alasca': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'LittleRock',
'Califórnia': 'Sacramento',
'CarolinadoNorte': 'Raleigh',
'CarolinadoSul': 'Colúmbia',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'DakotadoNorte': 'Bismarck',
'DakotadoSul': 'Pierre',
'Delaware': 'Dover',
'Flórida': 'Tallahassee',
'Geórgia': 'Atlanta',
'Havaí': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Indiana': 'Indianápolis',
'Iowa': 'DesMoines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Luisiana': 'BatonRouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'SaintPaul',
'Mississippi': 'Jackson',
'Missouri': 'JeffersonCity',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada': 'CarsonCity',
'NovaHampshire': 'Concord',
'NovaIorque': 'Albany',
'NovaJérsei':' Trenton',
'NovoMéxico': 'SantaFé',
'Ohio': 'Columbus',
'Oklahoma': 'OklahomaCity',
'Oregon': 'Salem',
'Pensilvânia': 'Harrisburg',
'RhodeIsland': 'Providence',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'SaltLakeCity',
'Vermont': 'Montpelier',
'Virgínia': 'Richmond',
'VirgíniaOcidental': 'Charleston',
'Washington': 'Olympia',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}
#Estados dos estados unidos, sendo estados primeiro, capitais depois.

NumProva = 0
#Este valor ele e simplesmente usado para mostrar qual o numero da prova no cabelhaco.
for Prova in range(1, 36):
#Um looping de 35 vezes, porque a ideia e criar 35 provas e 35 Gabarito.
    NumProva = NumProva + 1
    #NumProva e usado para especificar o numero de cada prova no cabecalho.
    #Exemplo: Quiz sobre as Capitais dos Estados Unidos - Prova 23
    #E assim subsequentea ate chegar ao valor 35.
    Prova = 'Prova - ' + str(Prova) + '.txt'
    #Aqui nos criamos uma string que representa o nome do arquivo de texto referente a prova, a cada ciclo ele adiciona + 1.
    ProvaAluno = open(os.path.join('C:\\Matheus\\Study\\IT\\Python\\Provas', Prova), 'w')
    #Aqui nos abrimos/criamos o arquivo da prova em forma de ESCRETA, e armazenamos sua "Id" em ProvaAluno.
    Prova = 'Gabarito - ' + str(Prova) + '.txt'
    #Aqui usamos a mesma string da Prova, porem para o gabarito.
    GabaritoProva = open(os.path.join('C:\\Matheus\\Study\\IT\\Python\\Provas', Prova), 'w')
    #AQui criamos/abrimos o arquivo do gabarito em forma de ESCRITA, e armazenamos sua "ID" em GabaritoProva.
    ProvaAluno.write('Nome: ' + '\n' + '\n')
    #Nesta parte nos escrevemos no arquivo de texto da prova  a primeira parte do cabecalho. O nome.
    ProvaAluno.write('Data: ' + '\n' + '\n')
    #Na segunda parte nos escrevemos no arquivo de texto da prova. A data.
    ProvaAluno.write('Periodo: ' + '\n' + '\n')
    #Na terceira parte nos escrevemos no arquivo de texto da prova. O periodo.
    ProvaAluno.write('Quiz sobre as Capitais dos Estados Unidos - Prova %s' %NumProva + '\n' + '\n')
    #Na quarta parte do cabecalho nos escrevemoso tipo e o numero da prova.
    #Obs: Usamos o String Formatting, onde nos colocamos na string % + uma letra caracterizada pelo tipo do dado, no caso
    #%s e do tipo string. e por fora da string nos usamos % + mais um valor para representar na string.
    #No nosso caso a genet esta representando o numero da prova no cabecalho.
    Estados = list(Estados_e_Capitais.keys())
    #Primeiro a gente esta pegando apenas as chaves do dicionarios que sao os estados.
    #Nos pegamos apenas os estados porque nos proximo laco for, o que vai escrever cada questao ele segue uma sequencia
    #do 1 ao 50 entao ele vai reto, por isso nos precisamos embaralhar aqui antes para que ele possa seguir livremente
    #do 1 ao 50 sem nenhuma interrupcao pelo simples fato que os estados (chaves) ja estao
    #no tipo de valor dicionario e embaralhados
    random.shuffle(Estados)
    #O metodo shuffle e simple, ele pega uma seria de valores, (PESQUISAR TIPOS DE VALORES, MAS PROVAVELMENTE APENAS DO TIPO LISTA)
    #e ele embaralha os valores, trocando suas possicoes originais.
    #EMBARALHA
    for PerguntaNum in range(50):
        #Aqui nos vamos criar 50 perguntas e as 50 questoes estarao tambem no gabarito.
        #print(Estados[PerguntaNum])
        RespostasCorretas = Estados_e_Capitais[Estados[PerguntaNum]]#E uma unica resposta por looping
        #Vamo comecar com o que ele faz aqui, primeiro temos que lembrar que a variavel "Estados" esta com os valores do tipo
        #lista dos estados do dicionario "Estados_e_Capitais".
        #Depois a gente vai pegar o dicionario "Estados_e_Capitais" e vamo procurar por uma chave por exemplo: Estados[PerguntaNum]
        #(supondo que PerguntaNum esta com o valor de 3).
        #Ele vai me retornar o 3 valor da lista, vamos supor que seja Maryland, entao ele vai passar
        #para "Estados_e_Capitais" (Estados_e_Capitais['Maryland']) e estados e capitais vai achar o valor
        #esta chave que seria Annapolis, entao a respota correta para a terceira
        #pergunta e (3. Qual e a Capital de Maryland? = Annapolis) e Annapolis sera armazenada em "RespostasCorretas".
        
        #Obs: Estados_e_Capitais ainda esta valor do tipo dicionario.
        RespostasErradas = list(Estados_e_Capitais.values())
        #Esta linha sozinha nao faz nada.
        #Ela tranforma o dicionario em lista, pega todos os valores de todas as chaves do dicionario e armazena em RespostasErradas
        del RespostasErradas[RespostasErradas.index(RespostasCorretas)]
        #Agora a gente vai pegar 3 valores do dicionarios que ESTAO ERRADOS.
        #Primeiro a gente pega os valores do dicionario, transformam em lista e armzenamos em RespostasErradas.
        #Segundo nos vamos deletar o valor (Capital) da chave (Estado) correta da lista do primeiro passo, apenas
        #existindo valores incorretos.
        #A gente faz isso pegando o indice da resposta correta e deletando o valor da chave.
        RespostasErradas = random.sample(RespostasErradas, 3)
        #No terceiro passo nos usamos um metodo chamado sample, que ele pega uma string, tranforma em lista e escolhe
        #a quantidade do segundo argumento para dar como retorno, no nosso caso nos pegamos o valor de retorno e armazenamos
        #em RespostasErradas assim finalizando a procura pela resposta correta e 3 alternativas erradas.

        #random.sample(população, k) - (Transforma uma string em uma lista e depois embaralha essa lista.
        #A população que deve ser informada é a string e o k é o número de caracteres da string que se deseja escolher
        #aleatoriamente. Se quiser embaralhar todos os caracteres da string use len().)
        RespostasOpcoes = RespostasErradas + [RespostasCorretas]
        #Respota opcoes e uma concatenacao de listas sendo 3 valores as alternativas erradas e 1 valor a alternativa correta.
        random.shuffle(RespostasOpcoes)
        #Depois usamos o metodo shuffle para embaralhar as alternativas.
        #random.shuffle(Embaralha os elementos de uma lista. | Exemplo: Embaralhar nome de 4 alunos)

        #random.randint(Escolhe aleatoriamente um número inteiro.)
        #random.choice(Escolhe um elemento aleatório de uma sequência. | Exemplo: escolher um nome aleatório entre os alunos.)
        ProvaAluno.write('%s. Qual e a Capital de %s?' % (PerguntaNum + 1, Estados[PerguntaNum]))
        #O primeiro String Formatting e para identificar qual e o numero da pergunta e o segundo e para pegar o numero do looping
        #e retonar o Estado em sua determinada posicao, dependendo de como ele foi embaralhado.
        #Obs: Como estados esta embaralhado o looping 1 pode ser diferente do looping 1 de outra prova.
        ProvaAluno.write('\n')
        #Nos paenas escrevemos uma linha em branco.
        for Alternativas in range(4):
            #Escrever as 4 alternativas de cada questao.
            ProvaAluno.write('   %s. %s\n' % ('ABCD'[Alternativas], RespostasOpcoes[Alternativas]))
            #Nesta linha nos temos uma stirng de quatro valor A, B, C e D e uma for, nos podemos usar
            #indices em strings, entao a gente vai pegar cada indice do valor "ABCD" conforme o valor de "Alternativas"
            #E assim ele vai escrevendo, entao por exemplo se ele tiver no valor 3 vai ser D. Obs: for sempre comeca no 0.
            #E para RespostasOpcoes[Alternativas], ele vai comocar A. qual o valor que tiver no
            #primeiro indice de RespostasOpcoes[Alternativas].
        ProvaAluno.write('\n')
        #Nos paenas escrevemos uma linha em branco.
        GabaritoProva.write('%s. %s\n' % (PerguntaNum + 1, 'ABCD'[RespostasOpcoes.index(RespostasCorretas)]))
        #No hgabarito nos vamos usar o primeiro valor PerguntaNum que e o looping para 5 questoes, entao cada questao
        #ele vai colocar o numero da questao e o indice dentro do valor RespostasOpcoes que contem as 3 erradas 1 correta
        #e vai pegar o indice que corresponde ao valor da resposta correta, usando dentro do argumento
        #index o valor do RespostasCorretas. 
    ProvaAluno.close()
    #No final de tudo nos simplesmente fechamos o arquivo da prova.
    GabaritoProva.close()
    #No final de tudo nos simplesmente fechamos o arquivo do Gabarito.
