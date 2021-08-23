import requests

"""
파이썬 HTTP 통신 라이브러리
메소드로 request 를 보내고, 반환값으로 response 객체를 받는다.
정적 크롤링에서 주로 활용되며, 간단하고 빠르다.  
"""
response = requests.get("https://github.com/")     # .get(url) : 메소드의 인자로 요청보낼 url 을 넘겨준다.
print(response.text)    # .test : 응답받은 본문 내용을 보여준다.
print(response.status_code, response.url)   # 응답받은 객체에는 다양한 속성이 있으니 경우에 맞게 잘 활용하면 된다.
