#!python3

#mcb.pyw

#mcb.pyw – Salva e carrega porções de texto no clipboard.

#Usage: py.exe mcb.pyw save <palavra-chave> – Salva clipboard na palavra-chave.
#py.exe mcb.pyw <palavra-chave> - Carrega palavra-chave no clipboard.
#py.exe mcb.pyw list – Carrega todas as palavras-chave no clipboard.
#py.exe mcb.pyw values – Carrega todos os valores de cada palavra-chave no clipboard.
#py.exe mcb.pyw help – Carrega todos os comandos no clipboard.
#mcb == multiclipboard

#TODO:

import shelve, sys, pyperclip, os
#Imports necesarios

os.chdir('C:\\Matheus\\Study\\IT\\Python\\Multiclipboard')

mcb_shelf = shelve.open('mcb')
#Abrimos ou criamos, se existir ele abre, se nao ele cria, aonde o programa esta rodando.

if len(sys.argv) == 1:
    #Caso possui apenas argumento na chamanda do arquivo, ele vai exibir uma mensagem (se tiver no prompt de comando) falando
    #que a gente possui apenas um argumento.
    print('Arquivo: mcb.pyw [Sem argumento!]+')
    #Exibir o que foi escrito e porque esta errado.
    pyperclip.copy("Possui apenas um agurmento. Use 'help' para ver os comandos no seu clipboard!")
    #No caso de usar o Win+r e mostrado que ele esta usando apenas um argumento e sugere usar o help para ver quais sao os
    #comandos disponiveis e quais suas funcionalidades.
    sys.exit()
    #Sai do programa
    
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'save': #SAVE
    #Se possui 3 argumento na chamada do programa e o segundo for 'save' ele vai executar este bloco
    mcb_shelf[sys.argv[2]] = pyperclip.paste()
    #sys.argv[2] == Nomes
    #pyperclip.pasta() == Matheus de Oliveiera Silva, Joao de Almeida

    #Ele vai escrever no arquivo shelve criado no inicio do arquivo, uma "chave" com o valor do terceiro argumento.
    #E vai colocar como valor o seu clipboard (Ctrl-C)
    #Exemplo: mcb.pyw save Nomes
    #Seu Clipboard (Matheus de Oliveiera Silva, Joao de Almeida)
    #Entao no arquivo sera armazenado uma chave com o valor "Nomes" e seus valor sera :Matheus de Oliveiera Silva, Joao de Almeida
    #Entao se eu quiser pegar estes nomes eu uso: mcb.pyw Nomes e vai passar para o meu clipboard (Ctrl-c) estes nomes.

elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete': #DELETE
    #Se o primeiro argumento na chamada do programa for "delete" ele vai executar o bloco de comando abaixo.
    del mcb_shelf[sys.argv[2]]
    #Vai deletar a string dentro do arquivo igual ao segundo argumento.
    
elif len(sys.argv) == 2:
    #Se possui dois argumento ele vai executar este bloco.
    if sys.argv[1].lower() == 'list': #LISTA
        print(str(list(mcb_shelf.keys())))
        #Se o segundo argumento for 'list' executa este bloco de comando.
        pyperclip.copy(str(list(mcb_shelf.keys())))
        #Aqui ele vai copiar para o seu clipboard (ctrl-c) todas as chaves que estao armazenadas no arquivo mcb.dir

    elif sys.argv[1].lower() == 'del_all': #DELETE ALL
        #Se o tiver apenas um argumento e for "del_all" ele vai executar o bloco de comandos abaixo.
        for keys in mcb_shelf:
            #Vai deletar todas as chaves do arquivo mcb_shelf
            del mcb_shelf[keys]
            #Deletar de forma unitaria a cada execucao.
        del_all = open('mcb.dat', 'w')
        #Abri o arquivo em forma de leitura e fecha sem escrever nada, o sobreescrevendo nenhum caractere, ou seja, ele vai ficar sem nenhuma caractere agora
        del_all.close()

    elif sys.argv[1].lower() == 'value': #VALORES 
        print(str(list(mcb_shelf.values())))
        #Se o segundo argumento for 'value' executa este bloco de comando.
        pyperclip.copy(str(list(mcb_shelf.values())))
        #Aqui ele vai copiar para o seu clipboard (ctrl-c) todos os valores que estao armazenados no arquivo mcb.dat

    elif sys.argv[1].lower() == 'help': #HELP
        #Se o segundo argumento for 'help' executa este bloco de comando.
        pyperclip.copy('mcb.pyw – Salva e carrega porções de texto no clipboard.\n\
Usage: py.exe mcb.pyw save <palavra-chave> – Salva clipboard na palavra-chave.\n\
py.exe mcb.pyw <palavra-chave> - Carrega palavra-chave no clipboard.\n\
py.exe mcb.pyw list – Carrega todas as palavras-chave no clipboard.\n\
py.exe mcb.pyw values – Carrega todos os valores de cada palavra-chave no clipboard.\n\
py.exe mcb.pyw help – Carrega todos os comandos no clipboard.')
        print('mcb.pyw – Salva e carrega porções de texto no clipboard.\n\
Usage: py.exe mcb.pyw save <palavra-chave> – Salva clipboard na palavra-chave.\n\
py.exe mcb.pyw <palavra-chave> - Carrega palavra-chave no clipboard.\n\
py.exe mcb.pyw list – Carrega todas as palavras-chave no clipboard.\n\
py.exe mcb.pyw values – Carrega todos os valores de cada palavra-chave no clipboard.\n\
py.exe mcb.pyw help – Carrega todos os comandos no clipboard.')
        #Aqui ele vai copiar para o seu clipboard (ctrl-c) esta string que mostra todas as funcoes e o que elas fazem.

    elif sys.argv[1] in mcb_shelf: #BUSCAR CHAVE EXISTENTE
        #Se o segundo argumento existir em alguma "chave" do arquivo ele vai executar o bloco de comandos abaixo.
        pyperclip.copy(mcb_shelf[sys.argv[1]])
        #O valor da chave de sys.argv[1] vai ser passado para o seu clipboard (ctrl-c)
        
    elif sys.argv[1] not in mcb_shelf: #BUSCAR CHAVE INEXISTENTE.
        print('Esta chave nao existe.')
        #Se tentar nao possui a chave no arquivo shelf ele vai executar o bloco de comando abaixo.
        pyperclip.copy('Esta chave nao existe.')
        #Caso nao exista a chave no segundo argumento em que voce digitou, ele vai passar para o eu clipboard esta mensagem.
        
mcb_shelf.close()
#Fecha o arquivo depois de tudo.