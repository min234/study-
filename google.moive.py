import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

browser = webdriver.Chrome()


url = "https://play.google.com/store/movies?hl=ko&gl=kr"
browser.get(url)

soup = BeautifulSoup(browser.page_source, "lxml")


movies = soup.find_all("div",attrs={"class" : "VfPpkd-EScbFb-JIbuQc UVEnyf"})


#print(len(movies))

#with open("movie.html","w",encoding="utf-8") as f :
     #f.write(soup.prettify())#문서 이쁘게 정리하는법

for movie in movies : 
    title = movie.find("div", attrs = {"class" :"Epkrse"}).get_text()
    print(title)

    link = movie.find('a',attrs={"class": "Si6A0c ZD8Cqc"})["href"]

    print(f"제목 :{title}")
    print(f"링크 :", "https://play.google.com" + link )

    browser.quit()