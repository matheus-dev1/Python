#! python

#forecast_san_frascisco.py

#O programa pega todas as previcoes do tempo da semana de san franscisco do site https://forecast.weather.gov

#TODO: 

from bs4 import BeautifulSoup
import requests
#Imports necessarios

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168#.X1ULvYvQ9PZ')
#Baixar pagina

soup = BeautifulSoup(page.content, 'html.parser')
#Tranformar em um objeto BeautifulSoup o conteudo da pagina.

seven_day = soup.find(id="seven-day-forecast")
#Aqui nos vamo encontrar o id seven-day-forecast, apenas existe um id com o mesmo nome entao nos achamos o bloco de 
#tags este id. Entoa nos usamos o metodo find porque queremos apenas um id a ser encontrado.

forcast_items = seven_day.find_all(class_="forecast-tombstone")
#Depois buscamos por todos as classes tombstone-container que possui diversas dentro de id="seven-day-forecast"
#E forecast_items recebe uma lista de classes class_="tombstone-container"

for item in forcast_items:
    try:
        period = item.find(class_="period-name").get_text()
        #Pegando o texto da classe de period-name
        short_desc = item.find(class_="short-desc").get_text()
        #Pegando o texto da classe de short-desc
        high_temp = item.find(class_="temp").get_text()
        #Pegando o texto da clsse temp temp-high
        #Importante nos podemos usar partes do nome da classe, por exemplo high_temp tem o nome da classe igual a: temp temp-high
        #Porem no podemos usar apenas temp.
        print(period + ' ' + short_desc + ' ' + high_temp, '\n')
        #Exibimos o perido, descricao e temperatura.
    except Exception as error:
        print()
        #se ocorrer um erro ele exibe o erro.
