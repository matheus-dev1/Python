#! python3

#mad_libs

#Ler arquivo e pertmite o usuario 

print('Write a text similar this: The ADJECTIVE panda walked to the NOUN and then VERB. \
A nearby NOUN was unaffected by these events.\n')
# Write a text similar this: The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events.
#Exemplo de texto para o usuario digitar

print('Cab be ADJECTIVE, NOUN, VERB, ADVERB\n')
#OS tipos de palavras que podem ser colocadas para ser alteradas.

User_text = input('Type your text: ')
#Usuario digitar o texto para ser corrido.

mad_libs = open('text_libs.txt', 'w')
#Abrir o arquivo de texto unico.

print('\n')
#Pula linha

mad_libs.write(User_text)
#Escrevemos o texto do usuario no arquivo para ser alterado mais pra frente.

mad_libs.close()
#Fechar o arquivo em modo de escrita.

mad_libs = open('text_libs.txt', 'r')
#Abrir o mesmo arquivo no modo de leitura.

print('Text to correct: ' + User_text)
#Mostra ao usuario o texto que ele tem que corrigir.

linhas_mad_libs = mad_libs.read()
#Ler todas as paginas e armazenar em uma variavel.

palavras_mad_libs = linhas_mad_libs.split()
#Transfoma a string em uma lista de string para podemos alterar o valor no local certo.

for palavra in range(len(palavras_mad_libs)):
    if palavras_mad_libs[palavra] == 'ADJECTIVE':
        adjective = input('Enter an adjective: ')
        #Type an adjetve
        palavras_mad_libs[palavra] = adjective
    elif palavras_mad_libs[palavra] == 'ADJECTIVE.':
        adjective = input('Enter an adjective: ')
        #Type an adjetve
        palavras_mad_libs[palavra] = adjective + '.'
    #Se em determinada possicao estiver a sttring ADJECTIVE ou ADJECTIVE. ele vai alterar para o ADJECTIVE em que
    #o usuario digitou na variavel ADJECTIVE.
        
    elif palavras_mad_libs[palavra] == 'NOUN':
        noun = input('Enter a noun: ')
        #Type a noun
        palavras_mad_libs[palavra] = noun
    elif palavras_mad_libs[palavra] == 'NOUN.':
        noun = input('Enter a noun: ')
        #Type a noun
        palavras_mad_libs[palavra] = noun + '.'
    #Se em determinada possicao estiver a sttring NOUN ou NOUN. ele vai alterar para o NOUN em que
    #o usuario digitou na variavel NOUN.
        
    elif palavras_mad_libs[palavra] == 'VERB':
        verb = input('Enter a verb: ')
        #Type a verb
        palavras_mad_libs[palavra] = verb
    elif palavras_mad_libs[palavra] == 'VERB.':
        verb = input('Enter a verb: ')
        #Type a verb
        palavras_mad_libs[palavra] = verb + '.'
    #Se em determinada possicao estiver a sttring VERB ou VERB. ele vai alterar para o VERB em que
    #o usuario digitou na variavel VERB.

    elif palavras_mad_libs[palavra] == 'ADVERB':
        adverb = input('Enter a adverb: ')
        #Type a adverb
        palavras_mad_libs[palavra] = adverb
    elif palavras_mad_libs[palavra] == 'ADVERB.':
        adverb = input('Enter a adverb: ')
        #Type a adverb
        palavras_mad_libs[palavra] = adverb + '.'
    #Se em determinada possicao estiver a sttring ADVERB ou ADVERB. ele vai alterar para o ADVERB em que
    #o usuario digitou na variavel ADVERB.
             
palavras_mad_libs_string = ' '.join(palavras_mad_libs)
#Tranforma a lista em uma string e armazena em uma variavel.

print(palavras_mad_libs_string)
#Exibe a string ja alterada.

mad_libs.close()
#Fecha o arquivo em modo de leitura.

mad_libs = open('new_text_libs.txt', 'w')
#Abri outro arquivo em modo de escrita.

mad_libs.write(palavras_mad_libs_string)
#Escreve a strin correta no arquivo.

mad_libs.close()
#Fecha o arquivo.
