# -*- coding: utf-8 -*-
import requests
# requests(리퀘스트스, 요청하다)는 웹브라우저가 아닌 파이썬에서 HTTP Request할 수 있게 해주는 모듈

url = "https://www.naver.com"
response = requests.get(url)
# url의 링크로 Get요청을 하고, 요청해서 받은 값을 response(리스판스, 대답)(쫄 것 없이 그냥 변수 이름이다)에 저장
print(response.status_code)
# response(받은 값). status_code(객체) 를 출력하면서 객체 값을 확인 (status_code는 상태코드를 저장),
# 200이면 정상적인 응답을 의미하는 상태코드, 그렇지 못하면 문제 발생!
print(response.text)
# esponse(받은 값), text(객체) 를 출력하면서 객체 값을 확인 (text는 HTML코드를 저장),
# 출력하면 response(받은 값)의 url(요청한 링크) 주소의 HTML 코드가 출력



# *** parameter(파라미터, 매개변수)로 링크 넣어주기
# 위같이 링크를 모두 직접 넣어주는 경우도 있지만, 아래와 파라미터를 이용해서 링크를 적용시킬수 있고 많이 쓰인다.
# params = {'param': 'value'}
# res = requests.get(URL, params=params)
# 괄호 안의 값은 (URL주소)?param=value 가 됨
# ex) URL = "https://www.naver.com"라면 괄호 안의 값은 https://www.naver.com/?para-value


