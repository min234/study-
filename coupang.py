from selenium import webdriver
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")

items = soup.find_all("li",attrs={"class": re.compile("^search-product")}) 

for item in items : 
    name = item.find("div", attrs={"class":"name"}).get_text() #품명
    price =item.find("strong", attrs={"class":"price-value"}).get_text() #가격
    rate =item.find("em", attrs={"class":"rating"}) 
    rate_cut = item.find("span", attrs={"class": "rating-total-count"})
  
    if rate : 
        rate = rate.get_text()
    else:
       print("<평점 없는 상품 제외>")
       continue

    if rate_cut : 
           rate_cut = rate_cut.get_text()
    else:
        print("<평점 없는 상품 제외>")
        continue


    print(name,price,rate,rate_cut)