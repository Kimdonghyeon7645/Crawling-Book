# -*- coding: utf-8 -*-
from selenium import webdriver
import time

head_url = 'https://pixabay.com/images/search/korea/?pagi='
urls = []
htmls = []
for i in range(1,31):
    urls.append(head_url + str(i) + '.html')
''' urls == 1~ 20 페이지의 링크가 담겨있음 '''

# for url in urls:
#     driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
#     driver.get(url)
#     time.sleep(8)
#     print(url)
#     htmls.append(driver.page_source)
#     driver.close()

""" 위코드로 돌리면 얼마지않아서 멈춘다.
selenium.common.exceptions.WebDriverException: 
Message: Service C:\\Users\\user\\Documents\\chromedriver.exe unexpectedly exited. Status code was: 3221225794
라는 구글링으로도 안나오는 괘상한 오류로 셀레니움을 다룰때 엄청 고생했고 삽질했는데, 어떻게 하면 좋을까? 
"""

# driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
# for url in urls:
#     driver.get(url)
#     time.sleep(8)
#     print(url)
#     htmls.append(driver.page_source)
#     driver.close()

"""
바로 윗 행의 driver.close() 코드를 추가하면 두번째에 에러가 뜬다.
원인은 열려있던 유일한 탭을 .close()로 닫아버리면서 드라이버가 종료됬는데, 그상황에서 .get()을 사용해서 였다.
따라서 그부분을 반복문 이후로 미루고 코드를 실행하니 감격스럽게도 30개의 링크가 모두 적용된다!
아래는 거기에 headless 모드를 추가한 최종 버전이다.!
"""
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe", options=options)
for url in urls:
    driver.get(url)
    time.sleep(8)
    print(url)
    htmls.append(driver.page_source)

driver.close()
for html in htmls:
    print(htmls.index(html), "번째 html 코드 : ", html)

"""
드디어 찾았다. 천지신명님 만세!
드디어 셀레니움에서 불가능할 것 같았던 난제를 해결할 수 있게 되었다!
2020. 01. 22.
"""
