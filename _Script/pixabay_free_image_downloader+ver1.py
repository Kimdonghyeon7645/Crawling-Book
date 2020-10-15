# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
"""
저작권없는 이미지 일괄 다운로더, 
원하는 검색어를 입력하면, 그 검색결과 상단의 이미지를 모두 추출하는 프로그램.
사용한 사이트 https://pixabay.com/ (픽사베이, 저작권없는 무료 이미지 사이트)

ver 1
    검색어를 입력했을때 
"""
head_url = "https://pixabay.com/images/search/"