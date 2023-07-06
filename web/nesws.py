from bs4 import BeautifulSoup
import requests

def scr():
    print("[오늘의 날씨]")
    url = "https://news.jtbc.co.kr/"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    new_list = soup.find_all("div", attrs={"class" : "cjs_journal_wrap _item_contents"})
    for index, news in enumerate(new_list):
        title = news.find("div", attrs={"class":"cjs_t"}).get_text().strip()
        link = url + news.find("a")["href"]
        print(title, link)

if __name__ == "__main__":
    scr()
