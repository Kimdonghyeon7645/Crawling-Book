"""
개발시간 30분내외, 동생이 볼 웹툰 이미지 일괄 저장하는 프로그램 제작
"""
import requests
from bs4 import BeautifulSoup
import os

path = "C:/Users/user/Downloads/"
first_url = input("다운로드할 웹툰의 첫화 링크를 입력하세요 : ").rstrip()
folder_name = input("폴더 이름을 입력하세요(웹툰 이름) : ")
head_url = first_url[:-13]
tale_url = first_url[-12:]
last_page = int(input("어느 화까지 다운로드 할 건지 숫자로 입력하세요 : "))
if os.path.isdir(path + folder_name + '/') is False:
    os.mkdir(path + folder_name + '/')
path = path + folder_name + '/'

for now_page in range(1, last_page+1):
    now_page_url = head_url + str(now_page) + tale_url
    response = requests.get(now_page_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.select("div.wt_viewer img")
    num = 1
    for image in images:
        image_name = f'{now_page}화_{num:03}.' + image.get("src").split('.')[-1]
        r = requests.get(image.get("src"), headers={'Referer': now_page_url})
        with open((path + image_name), "wb") as f:
            f.write(r.content)
        num += 1
    print(now_page, "화 다운로드 완료!", sep='')