import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = webdriver.Chrome()

chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저 창을 띄우지 않고 실행하려면 주석 해제
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--lang=ko_KR")
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")


url = "https://play.google.com/store/movies?hl=ko&gl=US&pli=1"
browser.get(url)


soup = BeautifulSoup(browser.page_source.encode("utf-8"), "lxml", from_encoding="utf-8")

movies = soup.find_all("div",attrs={"class" : "ULeU3b neq64b"})


print(len(movies))

# with open("movie.html","w",encoding="utf-8") as f :
#     f.write(soup.prettify())#문서 이쁘게 정리하는법

