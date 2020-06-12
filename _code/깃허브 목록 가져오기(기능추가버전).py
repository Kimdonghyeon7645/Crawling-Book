# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

a = '['
b = ']('
c = ')'
filter_str = '.'
head = 'https://github.com/'
url = input("추출할 깃허브의 url을 입력하세요 : ").strip()

if input("특정 제목의 링크만 가져오시겠습니까? (Y/N) : ") in ['Y', 'y', 'yes']:
    filter_str = input("어떤 값을 포함하는 링크를 가져올지, 그 값을 입력하세요 : ")
if input("출력되는 형식을 변경하시겠습니까? (Y/N) : ") in ['Y', 'y', 'yes']:
    a, b, c = input("출력되는 형식을 입력하세요, 제목과 링크는 각각 $으로 치환해서 입력하세요 \n (예시: [제목](링크) => [$]($) : ").rstrip().split('$')
soup = BeautifulSoup(requests.get(url).text, 'html.parser')
table = soup.select('.files tbody')[-1]
for link in table.select('tr td.content a'):
    if filter_str in link.text:
        print(a + str(link.text) + b + head + link['href'] + c)
