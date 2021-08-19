import requests
from bs4 import BeautifulSoup

res = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
# print(res.text)
html = BeautifulSoup(res.text, "html.parser")
# print(html)
print(type(html))
print(dir(html))


# # 1.  find()(여러개는 find_all())와   2.  select()(한개는 select_one()) 추가로  3.  get()도 있다.
# find() -> 맨 처음 한개
# find_all() -> 여러개
# select() -> 여러개
# select_one() -> 맨 처음 한개
for i in html.select("#content > ul li a"):
    print(type(i))
    print(i)    # 요소 담아서
    print(i.text)   # .text = 요소가 감싸는 텍스트
    print(i['href'])    # ['속성명'] = 요소의 해당 속성값


res2 = BeautifulSoup(requests.get("https://comic.naver.com/webtoon/list.nhn?titleId=662774&weekday=wed").text, 'html.parser')
print(res2.select_one("#content > div.comicinfo > div.detail > h2").text.strip().split()[0])
