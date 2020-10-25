#! python3

#Beginners_guide_selenium2.py

#O programa ensina alguns tutoriais basico de Selenium parte 2.

#TODO:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#Com o import desta maneira agente so precisa usar o Keys.METODO
import time
#Import necessarios

browser = webdriver.Firefox()
#Definiro navegador!

browser.get('http://nostarch.com')
#Abrir o navegador
time.sleep(3)
browser.find_element_by_tag_name('html').send_keys(Keys.END)
#Dentro do HTML inteiro da pagina ele aperta o botao END que desce a pagina ate o final
time.sleep(3)
#ESpera 3 segundos, padrao, rlx.
browser.find_element_by_tag_name('html').send_keys(Keys.HOME)
#Depois sobe pra HOME que vai para o inicio da pagina.

#Atributos                                         | Significados
#Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT         | As teclas de direção do teclado.
#Keys.ENTER, Keys.RETURN                           | As teclas ENTER e RETURN.
#Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP | As teclas HOME, END, PAGEDOWN e PAGEUP.
#Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE         | As teclas ESC, BACKSPACE e DELETE.
#Keys.F1, Keys.F2, . . . , Keys.F12                | As teclas de F1 a F12 na parte superior do teclado.
#Keys.TAB                                          | A tecla TAB.

#browser.back()     | Clica no botão Back (Retornar). "Avancar uma pagina pra frente."
#browser.forward()  | Clica no botão Forward (Avançar). "Voltar um pagina pra tras."
#browser.refresh()  | Clica no botão Refresh/Reload (Atualizar/Recarregar).
#browser.quit()     | Clica no botão Close Window (Fechar janela).