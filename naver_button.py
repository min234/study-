from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


service1 = Service(executable_path='C:/project/dd/chromedriver.exe')

driver = webdriver.Chrome(service = service1)

url = 'http://naver.com'

driver.get(url)
tex = '야구'

driver.find_element('xpath','//*[@id="query"]').send_keys(tex)


driver.find_element('xpath','//*[@id="sform"]/fieldset/button').click()

while driver : 
    True