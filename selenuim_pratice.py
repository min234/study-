from bs4 import BeautifulSoup
import requests
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from lxml import etree

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 브라우저 창 숨기기
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-suage')
service = Service(executable_path='C:/project/dd/chromedriver.exe')
wd = webdriver.Chrome(service=service, options=chrome_options)

url = 'http://suanlab.com/'
wd.get(url)

soup = BeautifulSoup(wd.page_source, "lxml")
label_tags = soup.find_all('label')  # 모든 label 태그 찾기

for label in label_tags:
    print(label.get_text())

#css select 이용한  크롤링 
s = soup.select('#wrapper > section > div > div > div > div > div > label')

for label2 in s :
    print(label2.get_text())

#toggle부모 태그의 속성에도 있을 경우 , 부모태그 기준 한번 지정 후 사용
toggle_class = soup.select('#wrapper > section > div > div > div > div > div ')

for label3 in toggle_class : 
    print(label3.get_text())

# css slector 중 xpath 사용 할 경우
response = requests.get(url)
html = response.text
tree = etree.HTML(html)

toggle_class2 = tree('xpath','//*[@id="wrapper"]/section/div/div/div/div/div')

for label4 in toggle_class2 : 
    print(label4.text())

## webdriver.common.by 사용 시 
from selenium.webdriver.common.by import By


for label6 in wd.find_element(By.CLASS_NAME,'label') :
    print(label6.text)

for label6 in wd.find_element(By.CSS_SELECTOR,'l#wrapper > section > div > div > div > div > div ') :
    print(label6.text)

wd.quit()

