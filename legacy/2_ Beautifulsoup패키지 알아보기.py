# -*- coding: utf-8 -*-
# (한글 사용시 오류 안나게 인코딩 해주는 코드)
from bs4 import BeautifulSoup
# BeautifulSoup(아름다운 수프?)는 HTML, XML 파일에서 원하는 데이터를 Parsing(파싱)할 수 있는 라이브러리다.
# (B와 S 대문자로 써줘야 함!)
# from bs4 import BeautifulSoup  =  BeautifulSoup 라이브러리에서 bs4(BeautifulSoup4)만 골라서 import

# Parsing = 구문분석이라고 하며, 일련의 문자열을 의미있는 token(어휘 분석 단위)로 분해, 데이터 빼내는 프로그램
# Parser = parsing(파싱)을 하는 processor(프로세서, 가공하는 기계)로 Parser(파서)가 parsing(파싱)을 함

with open("예시.html") as fp:
    # with은 파일 open시, 영역을 벗어나면 자동 close()해주고, 여기서 html 파일을 fp로 치환(as) 해서 open()함
    soup = BeautifulSoup(fp, 'html.parser')
    # 이렇게 파싱을 할 파서를 호출할 수 있다. Beautiful(마크업 파일, 'html.parser')구조
    # 그외에도 lxml HTML parser, lxml XML parser, html5lib 등의 파서를 beautifulsoup에서 사용 가능

# html 파일 안에서 내가 원하는 부분만 선택하는 함수는 여러가지가 있다.
# 1.  find()(여러개는 find_all())와   2.  select()(한개는 select_one()) 추가로  3.  get()도 있다.

# 1.  find(), find_all() 함수
    all_divs = soup.find_all("div")
    # find_all()함수 = 해당 조건에 맞는 모든 태그들을 추출
    print("모든 div 태그 :", all_divs, sep="\n") # 출력 결과 <div>...</div>에 속하는 태그 출력 (리스트)

    first_div = soup.find("div")
    #find()함수 = 해당 조건에 맞는 하나의(중복시 맨 처음의)태그를 추출
    print("첫번째 div 태그 :", first_div, sep="\n") # 출력 결과 <div>...</div> 맨처음 태그 출력

    ex_id_divs = soup.find('div',{'id':'ex_id'})
    #태그 * 속성으로 추출 = 첫번째 인자로 태그('div')를, 두번째 인자로 속성:값('id':'ex_id')를 넣어줌
    #find('태그명',{'속성명':'값' ...}), find_all('태그명',{'속성명':'값' ...}) 과 같은 형식 (두 함수 모두 가능)
    #find('태그명', '속성명'='값' ...}), find_all('태그명', '속성명'='값' ...}) 과 같은 형식도 가능
    print("id가 ex_id인 div 태그 :", ex_id_divs, sep='\n') # <div>태그 중 id 속성이 ex_id 인 태그 출력

    all_ps_in_ex_id_divs = ex_id_divs.find_all("p")
    # 이미 find(), find_all()로 가져온 부분 중에서도 다시 find(), find_all()로 원하는 값을 추출 가능
    print("id가 ex_id인 div 태그중에서 p태그 :", all_ps_in_ex_id_divs, sep="\n")
    # <div>태그 중 id 속성이 ex_id 인 태그 중 <p> 태그 출력

    print("\n\nselect()함수 이용\n")
# 2.  select(), select_one() 함수
    print("모든 div 태그 :", soup.select('div'), sep="\n") # .select('태그명')
    #find_all()함수 같이 div 태그들을 추출 (여기선 바로 출력)
    print("모든 body > div > p 태그 :", soup.select('body > div > p'), sep="\n")  # .select('상위태그명 > ... > 하위태그명')
    # 직계 자식 태그를 들어가는 기호 > 를 사용해서 그부분에 속하는 태그를 추출
    print("모든 body ... p 태그 :", soup.select('body  p'), sep="\n")  # .select('상위태그명 '하위태그명')
    # 과 같이하면 바로 아래 자식이 아니여도 상관없음, 자손 태그도 들어갈 수 있음

    # 클래스와 id는 각각 . 과 # 을 앞에 붙임   # 단독으로 쓰일수도 있지만 태그옆에 붙기도 하고 > 도 가능하다.
    # .select('.클래스명') = 클래스명을 가지는 태그 추출
    # .select('#id명') = id명을 가지는 태그 추출
    # .select('태그명[속성명 = 속성값]') = 그외 속성들은 이렇게 지정 가능하다.
    # ex) soup.select('a[href = http://test1]')

    #이제 이런 값을 select()는 복수 그룹형태로 가져오기에 그중 몇번째 자료를 가져오고 싶으면
    # select('가져올것')[0] 과 같이 하면 첫번째 자료형을 가지고 올 수 있다. (인덱스 번호)


# 3.  get() 함수
    # soup.get('속성명') : soup 에 담겨진 속성명의 값을 추출
    # soup.name : soup 에 담겨진 태그명을 가리킴    ex) div
    # soup['속성명'] : soup 에 담겨진 속성명의 값을 가리킴    ex) ex_id

    # find().children , find().parent , find_parent(), find_parents()   로 써먹을 수도 있다!


#   예제.html 파일 (참고)'태그명',{'속성명':'값' ...}
# <!DOCTYPE html>
# <html>
# 	<head>
# 		<title>Page title</title>
# 	</head>
# 	<body>
#     	<div>
#             <p>a</p>
#             <p>b</p>
#             <p>c</p>
#         </div>
#         <div class="ex_class">
#             <p>d</p>
#             <p>e</p>
#             <p>f</p>
#         </div>
#         <div id="ex_id">
#             <p>g</p>
#             <p>h</p>
#             <p>i</p>
#         </div>
# 		<h1>This is a heading</h1>
# 		<p>This is a paragraph.</p>
# 		<p>This is another paragraph.</p>
# 	</body>
# </html>

#참고 자료 출처:
# https://twpower.github.io/84-how-to-use-beautiful-soup
# https://brownbears.tistory.com/414
# https://systemtrade.tistory.com/347?category=593045
# https://m.blog.naver.com/PostView.nhn?blogId=kiddwannabe&logNo=221177292446&proxyReferer=https%3A%2F%2Fwww.google.com%2F