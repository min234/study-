import time

from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True 
options.add_argument("window-size=1920x1080")


browser = webdriver.Chrome(options=options)

url = "https://play.google.com/store/movies/top?hl=ko&gl=kr"
browser.get(url)

# 스크롤 내리기
# 모니터(해상도) 높이인 1080 위치 스크롤 내리기
# browser.execute_script("window.scrollTo(0,1080)") # 1920 x 1080

# browser.execute_script("window.scrollTo(0,2080)") # 1920 x 1080
# 화면 가장 아래로 스크롤 하기
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 1920 x 1080

prev_height = browser.execute_script("return document.body.scrollHeight")

interval = 2

while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)") # 1920 x 1080
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print('스크롤완료')
browser.get_screenshot_as_file("google_movie.png")