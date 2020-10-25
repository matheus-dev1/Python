#! python3

#Beginners_guide_selenium.py

#O programa ensina alguns tutoriais basico de Selenium

#TODO:

from selenium import webdriver
#Modulo para abrir o browser e acesso ao seus metodos.
from selenium.webdriver.support.ui import WebDriverWait
#Funcao WebDriverWait para podermos criar uma especie de timer.
from selenium.webdriver.support import expected_conditions as EC
#Determina as conticoes do timer.
from selenium.webdriver.common.by import By
#Especifica uma ID em expected_conditions.
from selenium.webdriver.common.keys import Keys
#Teclas.
import time
#Somo obrigados a importar desta maneira.

browser = webdriver.Firefox()
#Define como o navegador Firefox.

wait = WebDriverWait(browser, 10)
#Colocamos um timer de 10 segundo ate carregar toda a pagina.

print(type(browser))
#Exibe o tipo da classe desta variavel.

browser.get('http://inventwithpython.com')
#Abre o navegador nesta pagina.
#Obs: Cada vez que nos alteramos de site precisamos usar o browser.get() para que nos conseguimos usar as funcoes e 
#identificar tags e elementos da pagina mudada.
try:
    Element = browser.find_element_by_class_name('jumbotron')
    #Aqui nos achamos um elemento atraves do valor da classe.
    print('Found <%s> element with that class name!' %(Element.tag_name))
    #Tag.name e o metodo que extrai o elemento da classe "jumbotron"
    #<a href="#automate" class="btn btn-primary">More Info </a>
except:
    print("Was not able find an element with that name.")
    #Caso nao encontra uma classe com o nome "jumbotron"

try:
    Link_element = browser.find_element_by_link_text('More Info')
    #btn btn-primary
    Link_element.click()
    #Depois de encontrar o elemento de forma percisa nos podemos usar o metodo click() que simula um click do computador.
    print("Tha button was be clicked!")
    #Exibe que o botao foi clicado
except:
    print("Link element doesn't finded.")
    #Caso ocorra algum erro.

print("Aguarde um momento para abrir o Yahoo...")
#Exibindo mensamgem para aguardar o Yahoo abrir.
time.sleep(3)
#Espera 3 segundos
print("Abrindo Yahoo Login!")
#Exibe a mensagem que o esta entrando na pagina de logging.

try:
    browser.get('https://mail.yahoo.com')
    #Abre o navegador na pagina do Yahoo
    time.sleep(5)
    #Timer
    browser.find_element_by_xpath("/html/body/div[2]/div[1]/a").click()
    #Encontramos o elemento do butao usando o metodo de encontrar ele pelo xpath
    #Simula o botao do click referente a pagina para fazer login.

    #Caso no elemento que voce esta procurando voce pode pegar o link do elemento e abrir outro browser.get()
    #Usando o metodo: .get_attribute('href') ou qualquer outro que retile o link em que queira.
    time.sleep(5)
    #Timer
    browser.find_element_by_id('login-username').send_keys('email')
    #Buscamos o ID de Login de user o elemento (a caixa de input de login)
    #E tambem nos pegamos o elemento do input de login e usamos o medoto send_keys() para que podemos enviar qualquer texto
    #para o input do elemento de "Email_element_input".
    time.sleep(5)
    #Timer
    browser.find_element_by_id('login-signin').send_keys(Keys.RETURN)
    #Aqui nos pegamos o elemento responsavel pelo butao para ir para a pagina de colocar a senha.
    #Aqui nos simulamos o click para ir a pagina de colocar a senha.

    #print(browser.current_url)
    #Exibir a pagina atual
    time.sleep(5)
    #Timer
    browser.find_element_by_id("login-passwd").send_keys("password")
    #Colocamos a senha do dentro do elemento id da senha.
    time.sleep(5)
    #Timer
    wait.until(EC.presence_of_element_located((By.ID, 'login-passwd'))).send_keys(Keys.RETURN)
    #Esperamos a pagina carregar e inserir os caracteres e em seguida apertamos enter no botao de login.

    #browser.quit()
    #Fecha o navegador.

    #OBSERVACAO DO BLOCO TRY: NOS NAO PRECISAMO PEGAR O VALOR DE RETORNO E USAR UMA FUNCAO A PARTIR DELA
    #NOS PODEMOS POR EXEMPLO PEGAR O RESULTADO DE find_element_by_xpath("/html/body/div[2]/div[1]/a") 
    #E JA PEGAR O RETORNO E USAR EM .CLICK()
except Exception as error:
    print(error)
    #Caso houver um erro.

#Nome do Método                                     | Objeto WebElement/lista retornados
#browser.find_element_by_class_name(nome)           | Elementos que utilizam a classe CSS nome.
#browser.find_elements_by_class_name(nome)          |
 
#browser.find_element_by_css_selector(seletor)      | Elementos que correspondem ao seletor CSS.
#browser.find_elements_by_css_selector(seletor)     | 

#browser.find_element_by_id(id)                     | Elementos com um valor de atributo id correspondente.
#browser.find_elements_by_id(id)                    | 

#browser.find_element_by_link_text(texto)           | Elementos <a> que correspondem totalmente ao texto especificado.
#browser.find_elements_by_link_text(texto)          |

#browser.find_element_by_partial_link_text(texto)   | Elementos <a> que contêm o texto especificado.
#browser.find_elements_by_partial_link_text(texto)  | 

#browser.find_element_by_name(nome)                 | Elementos com um valor de atributo nome correspondente.
#browser.find_elements_by_name(nome)                |

#find_element_by_xpath(xpath)                       | Busca um elemento a partir de um xpath. Exemplo: /html/body/div[2]/div[1]/a

#browser.find_element_by_tag_name(nome)             | Elementos com uma tag nome correspondente (sem diferenciar letras maiúsculas 
#                                                   | de minúsculas; um elemento <a> corresponde a 'a' e a 'A').

#Atributo ou método  | Descrição
#tag_name            | O nome da tag, por exemplo, 'a' para um elemento <a>.
#get_attribute(nome) | O valor do atributo nome do elemento.
#text                | O texto do elemento, por exemplo, 'hello' em <span>hello</span>.
#clear()             | Para campos de texto ou elementos correspondentes à área de texto, limpa o texto digitado.
#is_displayed()      | Retorna True se o elemento estiver visível; caso contrário, retorna False.
#is_enabled()        | Para elementos de entrada, retorna True se o elemento estiver habilitado; caso contrário, retorna False.
#is_selected()       | Para elementos relacionados a caixas de seleção ou botões de rádio, retorna True se o elemento
#                    | estiver selecionado; caso contrário, retorna False.
#location            | Um dicionário com chaves 'x' e 'y' para a posição do elemento na página.