import requests
# -*- coding: utf-8 -*-  / 한글 인코딩 주석

url = '' # 실제 이미지 링크 주소
referer_url = "" # 이미지를 가져온 사이트 주소
path = 'C:/Users/user/Pictures/Saved Pictures/'
img_name = 'test.png'

"""
크롤링을 하다보면 함부로 이미지를 다운받을 수 없게, referer(리퍼러, 사이트 경로의 흔적)을 체크하는 경우가 있다.
추가로 user-agent 에서 브라우저인지 봇인지 판단하는 경우가 있는데, 이를 대처하기 위해서 둘의 설정을 변경해준다.
이미지 정보를 못가져오는 상황에서 이 두 값을 변경해준다면, 막힘없이 이미지를 가져오는 것을 볼 수 있다.
(이외의 크롤링 방지법에 대한 대처법은 다음에 설명)
"""
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/76.0.3809.146 Whale/2.6.89.9 Safari/537.36',
           'Referer' : referer_url
           # 이 Referer가 다운받을 때 어떤 링크를 거쳐왔는지 나타냄, 매우 중요!!
           }
r = requests.get(url, headers=headers)
with open(img_name,"wb") as f:
    f.write(r.content)

