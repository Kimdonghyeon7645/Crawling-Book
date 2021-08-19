import requests
from bs4 import BeautifulSoup

path = "C:/Users/user/Downloads/"
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/76.0.3809.146 Whale/2.6.89.9 Safari/537.36',
           'Referer' : "https://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=208&weekday=wed"}
res = requests.get("https://comic.naver.com/webtoon/detail.nhn?titleId=662774&no=208&weekday=wed")
# print(res.text)
html = BeautifulSoup(res.text, "html.parser")
for img in html.select("#comic_view_area > div.wt_viewer img"):
    img_res = requests.get(img['src'], headers=headers)
    img_name = img['src'].split('_')[-1]
    with open(path + img_name, "wb") as f:
        f.write(img_res.content)

