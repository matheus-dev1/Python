#1 python3

#previsao_do_tempo.py

#O programa retora a minina e maxima de hoje, amanha e depois de amanha do site https://www.climatempo.com.br/

#TODO:

import requests, bs4, sys, re
#imports necessarios

if len(sys.argv) < 2:
    print('O programa possui apenas um argumento em sua chamada. Tente novamente.')

elif len(sys.argv) == 2:
    main_url = sys.argv[1]
    object_response_requests_get = requests.get(main_url)
    print('Downloading... %s' %main_url)
    try:
        object_response_requests_get.raise_for_status()
        object_response_soup = bs4.BeautifulSoup(object_response_requests_get.text, 'html.parser')
        weather_days = object_response_soup.find_all(class_="_margin-l-20")#_margin-l-20
        for item in weather_days:
            try:
                day = item.find(class_="_block _margin-b-5 -bold -dark-blue").get_text()
                weather = item.find(class_="_block _margin-b-5 -gray").get_text()
                print(day + ' - ' + weather, '\n')
            except Exception as error:
                a = 0
    except Exception as error:
        a = 0
else:
    print('A chamda do programa possui argumentos demais! Tente novamente.')