from bs4 import BeautifulSoup
import requests

def create_soup(url):
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scr():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0&tqi=i6RqFlp0JywssUMxn4RssssstBR-342908"
    soup = create_soup(url)

    summary = soup.find("p", attrs={"class": "summary"}).get_text()
    curr_temp = soup.find("div", attrs={"class": "temperature_text"}).get_text()
    min_temp = soup.find("span", attrs={"class": "lowest"}).get_text()
    max_temp = soup.find("span", attrs={"class": "highest"}).get_text()

    print(summary)
    print(curr_temp)
    print(min_temp)
    print(max_temp)

def scrape():
    print("[오늘의 날씨]")
    url = "https://news.naver.com/"
    soup = create_soup(url)
    new_list = soup.find_all("div", attrs={"class" : "cjs_journal_wrap _item_contents"})
    for index, news in enumerate(new_list):
        title = news.find("div", attrs={"class":"cjs_t"}).get_text().strip()
        link = url + news.find("a")["href"]
        print(title, link)

if __name__ == "__main__":
    scr()
    scrape()
 # 아래 코드만 사용하겠다는 의미