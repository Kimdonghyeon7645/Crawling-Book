# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

"""
이슈:
스크롤을 해야 이미지를 가져오는 녀석임 

프로그램설명 : 
unsplash.com 이라는 저작권 없는 이미지 사이트에서
원하는 키워드에 맞는 사진들을 일괄 다운로드 받는 프로그램
"""

head_url = "https://unsplash.com/s/photos/"

keyword = "-".join(input("다운받을 사진들의 키워드를 입력하세요 : ").rstrip().split()) # 키워드 사이의 공백은 하이픈(-)처리
response = requests.get(head_url + keyword)
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

