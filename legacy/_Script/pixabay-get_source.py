# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

"""
저작권없는 이미지 일괄 다운로더, 
원하는 검색어를 입력하면, 그 검색결과 상단의 이미지를 모두 추출하는 프로그램.
사용한 사이트 https://pixabay.com/ (픽사베이, 저작권없는 무료 이미지 사이트)
"""

url = "https://pixabay.com/images/search/kroea/?pagi=1"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
"""
크롤링 접근을 막아놓음.
header USer-Agent, Accept-Language 로 우회 불가
time.sleep 로 우회 불가

- 차단 페이지에 Please enable cookies. 가 눈에 띔 (쿠키문제임)
셀레니움 시도... 성공

셀레니움으로 쿠키 추출... 성공
[{'domain': '.pixabay.com', 'expiry': 1585150321, 'httpOnly': False, 'name': '_gat_UA-20223345-1', 'path': '/', 'secure': False, 'value': '1'},
 {'domain': 'pixabay.com', 'expiry': 1616686262, 'httpOnly': False, 'name': 'client_width', 'path': '/', 'secure': False, 'value': '1019'},
 {'domain': '.pixabay.com', 'expiry': 1585236661, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.224625591.1585150262'}, 
 {'domain': '.pixabay.com', 'expiry': 1648222261, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2026316497.1585150262'}, 
 {'domain': 'pixabay.com', 'expiry': 748081150262, 'httpOnly': False, 'name': 'is_human', 'path': '/', 'secure': False, 'value': '1'}, 
 {'domain': 'pixabay.com', 'expiry': 1648222261, 'httpOnly': False, 'name': '_sp_id.aded', 'path': '/', 'secure': False, 'value': 'bcdbae62-a6f4-4a95-9422-c1a314c4a33f.1585150262.1.1585150262.1585150262.4307b378-5e6e-41da-b79a-cde94a119894'}, 
 {'domain': 'pixabay.com', 'httpOnly': False, 'name': 'anonymous_user_id', 'path': '/', 'secure': False, 'value': '27e13d0b-3afb-4d5d-b5cd-d83878ca7c2f'}, 
 {'domain': 'pixabay.com', 'expiry': 1585152061, 'httpOnly': False, 'name': '_sp_ses.aded', 'path': '/', 'secure': False, 'value': '*'}, 
 {'domain': '.pixabay.com', 'expiry': 1587742261.043492, 'httpOnly': True, 'name': '__cfduid', 'path': '/', 'secure': True, 'value': 'd52dc252962a15bd7a10afe73db7db6b51585150262'}
 ]
이게 추출한 쿠키. 근데 써먹기 실패...


"""
# options = webdriver.ChromeOptions()
# # options.add_argument('headless')
# driver = webdriver.Chrome("C:/Users/user/Documents/chromedriver.exe", options=options)
# driver.get(url)
# print(driver.get_cookies())
# time.sleep(3)
# soup = BeautifulSoup(driver.page_source, "html.parser")
# print(soup)
response = requests.get(url, cookies=cookies)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
