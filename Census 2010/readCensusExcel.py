#! python3

#readCensusExcel.py – Cria uma tabela com a população e o número de setores censitários de cada condado.

#O programa deve ler a planilha censospopdata.xlsx e posteriomente estuturar todos os dados
#e gravar em um arquivo python.

#TODO: 

import openpyxl, pprint
print("Opening Workbook...")

workbook = openpyxl.load_workbook('censuspopdata.xlsx')

mainSheet = workbook.get_sheet_by_name('Population by Census Tract')

dataCountry = {}

print("Reading Rows...")

for row in range(2, mainSheet.max_row + 1):
    #row = Linha
    #Neste looping nos vamos comecar na linha dois pegando de cada da linha da primeiro ate a ultima os
    #itens state, country e qtdpop.
    state = mainSheet["B" + str(row)].value
    county = mainSheet['C' + str(row)].value
    pop = mainSheet['D' + str(row)].value
    #Row e liha entao ele ira passar linha por linha e nos iremos passar por cada celula da linha.
    dataCountry.setdefault(state, {})
    #Se a abreviacao do estado atual, nao existir na lista, sera criado um dicionario com a chave igual
    #ao valor armzenado em "state" com o valor de chave igual um dicionario vazio!
    dataCountry[state].setdefault(county, {'tracts': 0, 'pop': 0})
    #Se o o condado nao existir no dicionario da abreviacao do estado, entao sera criado um valor ao 
    #dicionario "state" a chave com o valor do condado + outro dicionario como valor do condado
    #igual a {'tracts': 0, 'pop': 0}
    dataCountry[state][county]['tracts'] += 1
    #Depois de armazenar e criar o dicionario das abreviacoes dos estados, dos condados e {'tracts': 0, 'pop': 0}
    #nos iremos passar por cada linha, fazendo os incrementos necessarios.
    #Cada linha representa um setor censitário, portanto incrementa o valor de um.
    #Por exemplo a primeira abreviacao de estado ("tracs") tera 12.
    dataCountry[state][county]['pop'] += int(pop)
    #Vamos somar toda a populacao deste condado ("tracts") e vamos armazenar no dicionario no
    #valor da chave "pop".
    #Soma a população desse setor censitário à população do condado.

# Abre um novo arquivo-texto e grava o conteúdo de countyData nesse arquivo.
print('Writing results...')
resultFile = open('census2010.py', 'w')
resultFile.write('allData = ' + pprint.pformat(dataCountry))
#Nos colocamos o "allData = " porque assim isso se torna uma variavel no arquivo census2010.py
#fazendo com que nos podemos importar este arquivo a partir desta variavel e gerenciar
#todo os dados desta deste arquivo.