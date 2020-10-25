#! python3

#outlook_emails_automaticos.py

#O programa deve abrir o hotmail fazer login e enviar emails para o email igual ao primeiro argumento, titulos igual ao
#segundo argumento e a mensagem igual ae terceiro agumento em diante.

#TODO: Importar as bibliotecas necesarias.
#TODO: Armazenar o segundo (email) e terceiro (mensagem) argumento da chamada do programa.

import sys, time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

email_client = sys.argv[1]
subject = sys.argv[2]
messenge = ' '.join(sys.argv[3:])

browser = webdriver.Firefox()

wait = WebDriverWait(browser, 10)

browser.get('https://outlook.live.com/owa/')

browser.find_element_by_partial_link_text('Entrar').click()
time.sleep(3)
browser.find_element_by_id('i0116').send_keys('email')#Coloque o seu email
time.sleep(3)
browser.find_element_by_id('idSIButton9').send_keys(Keys.RETURN)
time.sleep(3)
browser.find_element_by_id('i0118').send_keys('password')#Coloque a sua senha
time.sleep(3)

try:
    browser.find_element_by_id('idChkBx_PWD_KMSI0Pwd').click()
    time.sleep(3)
except:
    print('error')

browser.find_element_by_id('idSIButton9').send_keys(Keys.RETURN)
time.sleep(3)

try:
    browser.find_element_by_id('idSIButton9').click()
    time.sleep(3)
except:
    print('error')

for i in range(10):
    time.sleep(10)
    wait.until(EC.presence_of_element_located((By.ID, 'id__3'))).click()
    time.sleep(10)
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[2]/div/div[2]/div[1]/div/div/div/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div/div[1]/div/div/input').send_keys(email_client)
    browser.find_element_by_class_name('ms-TextField-field').send_keys(subject)
    browser.find_element_by_class_name('_4utP_vaqQ3UQZH0GEBVQe').send_keys(messenge)
    #browser.find_element_by_partial_link_text('Send').click()
    #browser.find_element_by_class_name('ms-Button-flexContainer').click()
    browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[1]/div[3]/div[1]/span/div/div/div/div/div[1]/div[1]/button').click()