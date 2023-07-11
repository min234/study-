import time
from selenium import webdriver
import selenium
import platform

url = 'https://blackpinkhanoi2023.com/?lang=en'
target_time = '15:00:00'  # 오후 3시를 나타내는 시간
chrome_driver_path = 'C:/project/dd/chromedriver.exe'


# 특정 시간까지 대기하는 함수
def wait_until(target_time):
    current_time = time.strftime('%H:%M:%S', time.localtime())
    while current_time < target_time:
        time.sleep(1)
        current_time = time.strftime('%H:%M:%S', time.localtime())


# Chrome 드라이버 실행
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')  # 창을 열지 않고 백그라운드에서 실행

# Chrome 드라이버 실행
service = webdriver.chrome.service.Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Chrome 브라우저로 웹 페이지 접속
driver.get(url)

# 특정 시간까지 대기
wait_until(target_time)

# 여기에 원하는 작업을 수행합니다.

# 무한 대기
while True:
    time.sleep(10)
