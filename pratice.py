import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

url = "https://www.naver.com/"

driver = webdriver.Chrome()
driver.get(url)

scroll_count = 5  # 스크롤 횟수 설정

for _ in range(scroll_count):
    # 스크롤 동작
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    # 스크롤된 후 페이지 소스 가져오기
    soup = BeautifulSoup(driver.page_source, "lxml")

    div_tag = soup.find("div", attrs={"class": "ContentHeaderSubView-module__news_title___wuetX"})
    a_tags = div_tag.find_all("a")

    for a_tag in a_tags:
        href = a_tag.get_text()
        print(href)

driver.quit()
