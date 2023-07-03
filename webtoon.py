import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon"
res = requests.get(url)
res.raise_for_status()  # 수정: 괄호 추가

soup = BeautifulSoup(res.text, "lxml")
cartoons = soup.find_all("div", attrs={"class": "text"})

for cartoon in cartoons:  # 수정: 변수명 변경 (cartoons -> cartoon)
    print(cartoon.get_text())
