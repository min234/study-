from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless') #브라우저 없애는거
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-suage')

wd = webdriver.Chrome('C:/Program Files/chromedriver_win32 (1)/chromedriver.exe',options=chrome_options)

print(type(wd))

url = 'http://suanlab.com/'
wd.get(url)

label_tags = wd.find_elements_by_tag_name('label') ## list 얻기

