from selenium import webdriver

url = ""
# 사이트를 방문할 링크

chrome_driver_path = r"C:\Users\user\Documents\Python\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver.get(url) 
driver.implicitly_wait(5)

savedCookies = driver.get_cookies()
print('첫번째 쿠키 : ')
print(savedCookies)
print('\n\n')

driver2 = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver2.get(url)
driver2.delete_all_cookies()
for cookie in savedCookies:
    driver2.add_cookie(cookie)

driver2.get(url)
driver.implicitly_wait(3)
print('두번째 쿠키 : ')
print(driver2.get_cookies())
