from selenium import webdriver

"""
웹 사이트 테스트 프레임워크이자 라이브러리 (다양한 언어 지원) 
web driver(=가상의 브라우저 프로그램)을 활용해 동적인 크롤링을 할 수 있다.
웹 사이트 테스트란 용도처럼 웹의 모든 동작을 프로그램에서 실행가능, 느리지만 강력하다.  
"""
with webdriver.Chrome("chromedriver.exe") as driver:    # .Chrome() : 크롬드라이버(exe)를 실행하고 그 객체를 반환한다.
    import time

    time.sleep(100)
    # driver.get("https://github.com/")   # .get(url) : 넘겨준 url 로 크롬드라이버가 접속한다.
    # print(driver.page_source)       # .page_source : 크롬드라이버의 현재 페이지 소스(html)을 반환한다.
