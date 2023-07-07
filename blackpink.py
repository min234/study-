import time
from selenium import webdriver

url = 'https://blackpinkhanoi2023.com/?lang=en'
target_time = '15:00:00'  # 오후 3시를 나타내는 시간
chrome_driver_path = 'C:/Program Files/chromedriver_win32 (1)/chromedriver.exe'  # Chrome 드라이버의 경로

# 특정 시간까지 대기하는 함수
def wait_until(target_time):
    current_time = time.strftime('%H:%M:%S', time.localtime())
    while current_time < target_time:
        time.sleep(1)
        current_time = time.strftime('%H:%M:%S', time.localtime())

# Chrome 드라이버 및 Selenium 버전 호환성 확인
chrome_version = '현재 사용 중인 Chrome 브라우저의 버전'
selenium_version = '사용 중인 Selenium 버전'
compatible_driver_version = '호환되는 Chrome 드라이버 버전'

# Chrome 드라이버의 버전이 호환되는지 확인
if chrome_version != compatible_driver_version:
    print("Chrome 드라이버와 호환되는 버전을 다운로드하여 설치하세요.")

# Chrome 드라이버 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 창을 열지 않고 백그라운드에서 실행

# Chrome 드라이버 실행
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Chrome 브라우저로 웹 페이지 접속
driver.get(url)

# 특정 시간까지 대기
wait_until(target_time)

# 여기에 원하는 작업을 수행합니다.

# 무한 대기
while True:
    time.sleep(10)
