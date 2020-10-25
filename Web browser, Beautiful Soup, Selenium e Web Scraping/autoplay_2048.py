#! python3

#autoplay_2048.py

#Joga sozinho o jogo 2048

#TODO:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get('https://play2048.co/')

try:
    browser.find_element_by_partial_link_text('game-message game-over')
except:
    while True:
        time.sleep(1)
        browser.find_element_by_tag_name('html').send_keys(Keys.UP)
        time.sleep(1)
        browser.find_element_by_tag_name('html').send_keys(Keys.RIGHT)
        time.sleep(1)
        browser.find_element_by_tag_name('html').send_keys(Keys.DOWN)
        time.sleep(1)
        browser.find_element_by_tag_name('html').send_keys(Keys.LEFT)