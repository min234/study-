from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=769209"

# Chrome 드라이버 경로 설정
webdriver_path = "/path/to/chromedriver"

# Chrome 옵션 설정
chrome_options = Options()
chrome_options.add_argument("--headless")  # 백그라운드 실행 옵션
chrome_options.add_argument("--no-sandbox")

# Chrome 드라이버 서비스 설정
service = Service(webdriver_path)

# Chrome 드라이버 초기화
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get(url)

# 페이지가 완전히 로드될 때까지 대기
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "EpisodeListList__meta_info--Cgquz")))

# 페이지 소스 가져오기
soup = BeautifulSoup(driver.page_source, "lxml")

# 데이터 크롤링
divs = soup.find_all("div", class_="EpisodeListList__meta_info--Cgquz")
total_sum = 0
span_count = 0
for div in divs:
    span = div.find("span", class_="text")
    span_value = float(span.get_text())
    total_sum += span_value
    span_count += 1
    print(span_value)


    # 전체 합계 출력
 
print("전체 평균:" , total_sum/(span_count))
print("전체 합계:", total_sum)
     
# 드라이버 종료
driver.quit()
