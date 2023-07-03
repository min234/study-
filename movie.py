from selenium import webdriver
from bs4 import BeautifulSoup
import requests


url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84"
driver = webdriver.Chrome()
driver.get(url)

soup = BeautifulSoup(driver.page_source, "lxml")

images = soup.find_all("div", attrs={"class": "thumb"})


for idx, image in enumerate(images):
        img_tag = image.find("img")
        if img_tag and "src" in img_tag.attrs:
            img_url = img_tag["src"]
            response = requests.get(img_url)
            if response.status_code == 200:
                
                with open(f"movie{idx+1}.jpg", "wb") as f:
                    f.write(response.content)
                if idx >= 4 : #상위 5개 까지만
                    break 
                print(f"Saved image {idx+1}")
            else:
                print(f"Failed to retrieve image {idx+1}")
