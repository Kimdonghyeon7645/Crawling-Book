# -*- coding: utf-8 -*-
from selenium import webdriver
import time

url1 = 'https://www.youtube.com/?gl=KR'
url2 = 'https://www.youtube.com/channel/UCI8HW08rOSlvweOjJ9Gp2Ng'


""" 아래는 기본적인 셀레니움 웹드라이버로 유튜브 탭을 여는 코드다. """
# driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
# driver.get(url1)
# time.sleep(5)
# driver.close()


""" 아래 코드는 드라이버를 두개 열어서 각각 하나의 탭을 여는 코드고, """
# driver1 = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
# driver1.get(url1)
# print(driver1.window_handles)
# driver1.close()
# driver2 = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
# driver2.get(url2)
# print(driver2.window_handles)
# driver2.close()


""" 아래 코드는 드라이버의 탭을 하나로 유지하면서 갈아치우는 코드다. """
# driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
# driver.get(url1)
# print(driver.window_handles)
# driver.get(url2)
# print(driver.window_handles)
# driver.close()


""" 
그럼 어떻게 하면, 하나의 드라이버에서 두개의 탭을 열고 닫을 수 있을까?
찾아보니 자바스크립트 명령어를 사용해서 새탭을 여는 방법이 있었다.
자세하게는 .execute_script() 라는 함수를 사용해서, 그러한 자바스크립트 코드를 여기서 실행시키는 것이다. 
<참고> js 명령어 : http://blog.daum.net/anywiz/55 , http://blog.daum.net/7179bb/3522625
"""
driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
driver.get(url1)
print(driver.window_handles)
# driver.execute_script("window.open('https://www.youtube.com/channel/UCI8HW08rOSlvweOjJ9Gp2Ng')")
# 아래처럼 새창을 불러올 링크를 변수로 포맷팅해줬다.
driver.execute_script(f"window.open('{url2}')")
print(driver.window_handles)
time.sleep(6)
"""
.window_handles 로 현재 드라이버에서 있는 창들을 리스트로 반환시킬수 있다.
그러면 반환된 리스트 목록을 가지고 뭘 하느냐...
.switch_to.window() 함수로 활성화 된 창을 전환시킬수 있다.
함수의 인자값으로 리스트로 반환된 창 요소를 이때 사용하면 된다.
"""
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.switch_to.window(driver.window_handles[-1])
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)
driver.quit()
"""
이렇게 자유롭게 활성창을 와리가리 할수 있다. 게다가 코드로 해서 자동으로 말이다.
그외에도 셀레니움에서 지원하는 함수는 꽤 많다. 사실 너무 많다.
자세한건 셀레니움 문서 번역 파일을 참고하자
"""

# 참고