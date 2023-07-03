import csv
from selenium import webdriver
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0"

filename = "시가 총액 1-200.csv"
f = open(filename,"w",encoding="utf-8-sig",newline="")
writer =csv.writer(f)

title ="N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
writer.writerow(title)

for page in range(1, 2):

    driver = webdriver.Chrome()
    driver.get(url)

    soup = BeautifulSoup(driver.page_source, "lxml")

    

    data = soup.find("table", attrs={"class": "type_2"}).find("tbody").find_all("tr")

    for datas in data:
        columns = datas.find_all("td")
        if len(columns) <= 1 :
            continue
        d = [column.get_text().strip() for column in columns]
        #print(d)

        writer.writerow(d)

    driver.quit()
