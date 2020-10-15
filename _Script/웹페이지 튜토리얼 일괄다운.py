# _*_ coding:utf8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep

path = r'C:/Users/user/Downloads/'
head = 'https://poiemaweb.com/'
soup = BeautifulSoup(requests.get(head).text, 'html.parser')
print('='*10 + "\nhtml 파일만 일괄 다운: 1 \ncss 파일 다운: 2 \nhtml 파일 + css \n적용 일괄 다운: 3 \n링크 목록 보기 : 4 \n"
               "링크 목록만 html 파일 다운로드 : 5 \n" + '='*10)
md = int(input("선택할 작업의 번호를 입력하세요 : "))

if md == 1:
    for i in soup.select('li.toc-month a'):
        title = str(i.text).replace('/', ',')
        print(title + ' 다운로드')
        with open(path + title + '.html', 'wb') as f:
            f.write(requests.get(head + i['href']).content)

elif md == 2:
    i = soup.select('li.toc-month a')[0]
    title = str(i.text).replace('/', ',')
    print(title + ' 다운로드')
    css_urls = BeautifulSoup(requests.get(head[:-1] + i['href']).content, 'html.parser')
    for cs in css_urls.select('head link')[1:]:
        css_file = head[:-1] + cs['href']
        with open(path + css_file.split('/')[-1].split('?')[0], 'wb') as f:
            f.write(requests.get(css_file).content)
        print(css_file + ' 다운로드')

elif md == 3:
    for i in soup.select('li.toc-month a'):
        title = str(i.text).replace('/', ',').replace('?', '')
        print(title + ' 다운로드')
        with open(path + title + '.html', 'w', encoding="utf-8") as f:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            browser = webdriver.Chrome("C:/Users/user/Documents/chromedriver.exe", options=options)
            browser.get(head + i['href'])
            sleep(5)
            source = BeautifulSoup(browser.page_source, 'html.parser')
            for h in source.select('link')[1:]:
                h['href'] = './' + str(h['href']).split('/')[-1].split('?')[0]
            f.write(str(source))

elif md == 4:
    for i in soup.select('li.toc-month a'):
        print(i)

elif md == 5:
    print("a 태그 값들을 입력하세요 (입력받은 값 리스트가 뜨지 않는다면 엔터!) : \n")
    li = []
    while True:
        a = input()
        if a: li.append(a)
        else: break
    print("입력받은 값 : ", li)
    for i in li:
        title_text = i.split('>')[-2].split('<')[0].replace('/', ',').replace('?', '')
        title_num = i.split('>')[-3].split('<')[0]
        print(title_num + '-' + title_text + ' 다운로드')
        with open(path + title_num + '-' + title_text + '.html', 'w', encoding="utf-8") as f:
            options = webdriver.ChromeOptions()
            options.add_argument('headless')
            browser = webdriver.Chrome("C:/Users/user/Documents/chromedriver.exe", options=options)
            browser.get(head + i.split('"')[1])
            sleep(5)
            source = BeautifulSoup(browser.page_source, 'html.parser')
            for h in source.select('link')[1:]:
                h['href'] = './' + str(h['href']).split('/')[-1].split('?')[0]
            f.write(str(source))
    browser.close()

else:
    print("제대로 선택하셨나요?\n현재 입력한 값 :", md)
