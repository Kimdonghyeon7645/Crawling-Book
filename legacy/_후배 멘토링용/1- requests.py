import requests

res = requests.get("https://comic.naver.com/webtoon/weekday.nhn")
print(res)
print(type(res))
print(*dir(res), sep='\n')
print(*res.headers.items(), sep='\n')
print(res.ok)
print(res.status_code)
print(res.text)
# dir() : 객체의 필드 리스트 출력
# type() : 객체 타입 출력
