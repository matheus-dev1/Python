import census2010

print(census2010.allData["WY"]["Sheridan"])
#Aqui eu vou retornar tudo(pop e tracts) do estado WY na cidade Sheridan

SheridanPop = census2010.allData["WY"]["Sheridan"]["pop"]
#Estou no estado WY, cidade Sheridan e vou retornar a quantidade da populacao.

print(census2010.allData['WV']['Jefferson'])

print('The 2010 population of Sheridan was ' + str(SheridanPop))