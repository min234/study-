from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")

# webdriver 설정
servi = Service(executable_path='C:/project/dd/chromedriver.exe')
browser = webdriver.Chrome(service=servi, options=chrome_options)

browser.set_window_size(1920, 1280)  # 최대, 최소 크기

url = 'https://prod.danawa.com/list/?cate=112758&15main_11_02'
browser.get(url)

try:
    element = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))
    )
    element.click()
except:
    print("요소를 찾을 수 없거나 클릭할 수 없습니다.")

target = 5  # 크롤링할 페이지 수
cur_page = 1  # 현재 페이지

while cur_page <= target:
    # bs 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # css 사용 이유: 유연성, 구조 파악, 스타일 정보, 다른 플랫폼 호환, 호환성
    prp_list = soup.select('div.main_prodlist.main_prodlist_list > ul > li')
    # 페이지 번호 출력
    print('****** current page : {}'.format(cur_page), '******')
    print()

    # 정보 추출
    for v in prp_list:
        if not v.find('div', class_="ad_header"):
            print(v.select('p.prod_name > a')[0].text.strip())
            # 스크린샷
            browser.save_screenshot("target_page {}.png".format(cur_page))

    # 현재 페이지 증가
    cur_page += 1

    # 다음 페이지 클릭
    next_page_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="productListArea"]/div[4]/div/div/a[{}]'.format(cur_page + 1)))
    )
    next_page_button.click()

    # 페이지가 로딩되기를 기다림
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'div.main_prodlist.main_prodlist_list > ul > li'))
    )

browser.quit()
