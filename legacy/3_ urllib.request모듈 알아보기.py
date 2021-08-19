# -*- coding: utf-8 -*-
import urllib.request
# urllib(URL + lib(라이브러리)) URL로 작업할 수 있는 모듈을 모은 패키지

url = "https://www.naver.com"
html = urllib.request.urlopen(url)
# html = requests.get(url) 했던 것과 같이, url 에 접속하는 것이다.
source = html.read()
# source = html.text 접속한 파일을 html 소스코드로 source 변수에 저장하는 것이다.

img_url = 'https://encykorea.aks.ac.kr/Contents/GetImage?id=1e3ed9ce-bbb5-439c-9ae6-38ba332a9262&w=600&h=600&square=1'
path = 'C:/PycharmProjects/이미지 크롤링 입문/venv/Scripts/'
img_name = 'test이미지.jpg'
urllib.request.urlretrieve(img_url, path + img_name)
# urllib.request.urlretrieve('다운로드 할 이미지 URL', '저장할 경로(파일명)')
# 하면 간단하게 url(링크)를 이용하여 이미지를 다운로드 할 수 있다.
# url + retrieve(릿리브, 되찾아오다)

# 그외에도 from icrawler.builtin import UrlListCrawler 를 사용해,
# urllist_crawler = UrlListCrawler(downloader_threads=8, storage={'root_dir': 'D:\iCrawler'})
# urllist_crawler.crawl('file_list.txt', max_num=17936)
# 로도 해줄 수 있다는데, 나중에나 해보자 (정보 부족으로 검색 실패)


# 참고
# https://data-make.tistory.com/173
# https://blog.azulpintor.io/entry/Python3-URL%EB%A1%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C
