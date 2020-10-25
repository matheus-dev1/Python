import census2010

print(census2010.allData["WY"]["Sheridan"])

SheridanPop = census2010.allData["WY"]["Sheridan"]["pop"]

print('The 2010 population of Sheridan was ' + str(SheridanPop))