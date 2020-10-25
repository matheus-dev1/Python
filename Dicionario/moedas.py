#! python3

#moedas

#O programa mostra qual e a soma de cada tipo de moeda que todas as pessoas juntas posusi. Moedas: Real, Dolar, Bitcoin e Peso

people = {'Matheus': {'Dolar': 323, 'Real': 5443, 'Peso': 24234},
           'Ferreira': {'Peso': 13897, 'Bitcoin': 0.42},
           'Xavier': {'Dolar': 1000, 'Bitcoin': 9, 'Real': 10000}}
#Um dicionario que possui tres chaves, e em valor de cada chave, temos um novo dicionario que poossui mais tres chaves, porem cada
#chave dentro da primeira chave, possui apenas um valor.
#Por exemplo na chave 'Matheus' criamos um dicionario como valor, e neste dicionario temos mais tres chaves, caracterizados por tipos de
#moedas, entao por exemplo real e uma chave que contem um valor dentro que seria o valor da chave.

def Contabilizador(people_def, moeda_def):
    #Uma funcao que recebe, o dicionario people e o tipo de moeda em que ele quer contabilizar.
    Total = 0
    #Inicia a contagem de uma determinada moeda pelo valor de 0
    for pessoa, moeda in people_def.items():
        #Explicando todo o processo para obter os valores, primeiro ele entra na primeira chave do dicionario que no caso e
        #'Matheus' e a variavel pessoa so vai receber
        #outra chave quando, a variavel moeda passar por todas as chaves dentro de 'Matheus' que seriam, Dolar, Real e Peso.
        
        #Ou moeda tambem pode ser entendido como, que ele vai passar por todos os par chave-valor.
        Total += moeda.get(moeda_def, 0)
        #Quando a funcao for chamada, ele vai ter como referencia o tipo de moeda que ele ta buscando.
        #Se for a moeda em que ele ta buscand ele adiciona o valor dentro da chave, se nao ele coloca pra somar 0.
        #Depois de somar tudo ele retornar o total da soma depois de passar por cada chave e seus valores.
    return Total

print('Total da soma de cada moeda de Matheus, Ferreira e Xavier!')
print(' - Dolar: ' + str(Contabilizador(people, 'Dolar')))
print(' - Peso: ' + str(Contabilizador(people, 'Peso')))
print(' - Bitcoin: ' + str(Contabilizador(people, 'Bitcoin')))
print(' - Real: ' + str(Contabilizador(people, 'Real')))
