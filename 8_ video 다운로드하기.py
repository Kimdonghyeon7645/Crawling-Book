import requests
from bs4 import BeautifulSoup

post_url = '' # 영상 or 이미지가 있는 사이트 주소

post_html = requests.get(post_url).text
post_soup = BeautifulSoup(post_html, 'html.parser')
try:
    img_url = "https:" + post_soup.select("div.post a")[0].get('href')
except IndexError:
    img_url = "https:"+ post_soup.select("div.post source")[0].get('src')
img_name = 'test.' + img_url.split('.')[3]
r = requests.get(img_url, headers={'Referer': post_url})
with open(img_name, "wb") as f:
    f.write(r.content)

print(img_name, " 다운로드 완료")

"""
여기서의 코드는 실험했던 페이지에서만 적용되므로, 
실제 원하는 페이지에서 멀티미디어파일을 다운받으려면, select()부분을 수정하시길 바랍니다.
"""
