# -*- coding: utf-8 -*-
# (여기서 부터는 이제 Requests 와 BS를 이용한 크롤링이 안될때 쓰는 크롤링이다.
# 속도가 매우 느리고 Requests 보다 좋진 않아도, Requests 가 못가지고 오는 html 외부 데이터를 가져올 수 있다.)

# Web Driver는 브라우저가 제공하는 API()로, 코드로 사용자가 브라우저를 다룰수 있게 해준다.
# 사용가능한 브라우저로는, Firefox, Chrome, IE, Opera, PhantomJs 가 있다.
# 크롬 웹 브라우저는 https://sites.google.com/a/chromium.org/chromedriver/downloads 에서 다운받을 수 있다.
# 자신이 깔린 크롬 버전을 확인해서 그에 맞게, 컴퓨터의 운영체제에 맞게 다운받는다(윈도우 64bit도 32bit를 다운받으면 된다.)
from selenium import webdriver
import time
# selenium(셀레니움)은 파이썬에서 webdriver를 사용할 수 있는 라이브러리로, 앞으로 requests 를 못쓰는 상황에서 요긴하게 쓸 놈이다.

#     웹브라우저 숨기기 : 웹브라우저를 실행할 때의 창이 안뜨게 headless모드로 들어가는 것이다.
options = webdriver.ChromeOptions()  # 크롬의 옵션 객체를 생성
options.add_argument('headless') # headless 모드로 설정
options.add_argument("--disable-gpu") # gpu를 사용 안하도록 설정
options.add_argument("lang=ko_KR") # 한국어로 실행되게 설정
#그리고 webdriver.Chrome(경로, 옵션)에서 옵션부분에 chrome_options=(옵션 객체) 와 같이 해준다.

chrome_driver_path = r"C:\Users\user\Documents\chromedriver.exe"
# r + 웹드라이버가 있는 경로 + chromedriver.exe 해서 경로값을 담아준다. (변수 이름 chromedriver 같이 하면 에러난다)
driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
# webdriver.(웹드라이버 브라우저)("(경로)") : 로 해서 웹 드라이버를 연결한다.
driver.implicitly_wait(3)
# 값을 읽어오는데 전달인자(숫자)만큼의 초를 기다려준다.(암묵적 웹자원 로드 기다림) 여러번 반복할 것이면 time.sleep()함수를 사용하자.
url = 'https://google.com'
driver.get(url)
# 특정 url(링크)로 브라우저를 킨다. (철자 조심)
html = driver.page_source
# 이제 .page_source를 사용해서 선택된 elements(요소들)의 페이지 html소스를 가져올 수 있다. 나머진 bs로 파싱하자
print(html)

# find_element_by_name('...’) # 페이지의 단일 element중 name값으로 접근
# find_element_by_id('HTML_id’) # id값으로 접근
# find_element_by_xpath ("//(태그명)[@(속성명)='(속성값)']") # xpath값으로 접근
# find_element_by_css_selector(‘...’) # css selector로 접근
# find_element_by_class_name('...’) # class 이름으로 접근
# find_element_by_tag_name('...’) # tag name으로 접근
# 과 같이 selenium에서도 BS처럼 원하는 값을 파싱 할 수도 있고,
# .send_keys('...') # 값 입력
# .click() # 요소 클릭
# 으로 원하는 값에 작업을 할 수 있다.

#     iFrames (html속 외부 html 참조) 값 접근하기
iframes = driver.find_elements_by_css_selector('iframe')
# 이렇게 하여 iframe의 이름들을 저장하고,
# driver.switch_to_default_content  # 상위 프레임으로 전환
# driver.switch_to_frame('프레임이름') # 특정 프레임으로 전환
# 등으로 웹브라우저(driver)를 와리가리 할 수 있다.

time.sleep(3)
# time.sleep() 를 쓸 때는 import time 을 잊지말자.
driver.close()
# 이제 브라우저를 닫을 수 있다.
driver.quit()
# 이 함수는 브라우저를 종료시키는 함순데, 솔직히 탭이 1개라면 .close()나 .quit()나 브라우저가 종료된다.


# 참고
# 웹크롤링의 3종류 : https://cceeddcc.tistory.com/96?category=786970
# 왜 selenium(셀레니움)을 쓸까? : http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221188260422&parentCategoryNo=&categoryNo=&viewDate=&isShowPopularPosts=false&from=postView
# 웹브라우저란 : https://yumere.tistory.com/75
# 셀레니움 함수 : https://01073144993.tistory.com/155
# selenium(셀레니움) 함수 표 정리 : https://cceeddcc.tistory.com/98
# iframes : http://blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221253004219&parentCategoryNo=&categoryNo=35&viewDate=&isShowPopularPosts=false&from=postList