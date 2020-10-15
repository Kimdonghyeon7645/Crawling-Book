# -*- coding : utf-8 -*-
import requests
from bs4 import BeautifulSoup

head = 'https://github.com/'
url = input("추출할 깃허브의 url을 입력하세요 : ").strip()
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table = soup.select('.files tbody')[-1]
for link in table.select('tr td.content a'):
    print(link.text, head + link['href'])
