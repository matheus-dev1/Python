#! python3

#dictionary_and_birthday

#O programa cria um dicionario com nome de tres amigos com a suas datas de aniversario como par chave-valor em seguida solicita
#que o usuario procure um nome dentro do
#do dicionario onde contem os nome do seus amigos e depois mostra um mensagem dependendo do que voce digitou que contia ou
#nao o nome, e depois solicita ao usuario que
#atualize a data de nascimento do nome do amigo em que ele digitou.

birthday_friends = {'ferreira': 'December 23', 'xavier': 'May 17', 'knightmaster300': 'August 02'}

while True:
    birthday_choose = input('Type a friend`s name (Press Enter to Leave): ')
    if birthday_choose == '':
        break
    if birthday_choose in birthday_friends:#A funcao in pode ser entendi como 'se tiver em' e Ele esta procurando a chave dentro do dicionario.
        print(birthday_friends[birthday_choose] + ' is the birthday of ' + birthday_choose)
    else:#Se nao possui ele executa a clausula do else, e que faz com que a agente adiciona uma data para o nome em que a gente digitou.
        print('This name is not finded ' + birthday_choose)
        birthday_choose_date = input('What is their birthday? ')
        birthday_friends[birthday_choose] = birthday_choose_date
        #Com esta linha assim o que nos fazemos, primero a gente sabe que o nome(chave) nao existe, entao sabendo disso
        #a gente adiciona no dicionario a chave(birthday_choose) e o valor(birthday_choose_date)
        print('Birthday database updated!')
