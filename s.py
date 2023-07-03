import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()


browser.get("https://www.naver.com/")

#로그인
elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")
elem.click()

#3.id,pw입력

browser.find_element(By.NAME,"id").send_keys("ektmd7676")

browser.find_element(By.NAME,"pw").send_keys("rlaalsdnr7676@")

#4.로그인 클릭
e = browser.find_element(By.CLASS_NAME,"btn_login")
e.click()



while(True):
    	pass

