#! python3

#strip_regex

#este programa faz com que nos entramos com um texto e descidimos qual valor nos quremos remover deste testo, por exmeplo
#eu posso remover todos os 'a' deu um texto

import re, pyperclip

def strip_regex(string_text_argv, string_remocao_argv):
    if string_remocao_argv == '':
        remocao_vazia = re.compile(r'(\w)(\s)')
        aa = remocao_vazia.sub(r'\1', string_text_argv)
        return aa
    elif string_remocao_argv != '':
        cc = ''
        for remocao in string_text_argv:
            if remocao == string_remocao_argv:
                remocao = ''
                cc += remocao
            else:
                cc += remocao
        return cc
    
string_text = input('Digite um texto: ')
string_remocao = input('caractere a ser removido (apenas enter para espacos em branco): ')
print(strip_regex(string_text, string_remocao))
    
#Exemplo de texto: mduhasduifohdaafsdfa dfasdf asdfsdafa 



