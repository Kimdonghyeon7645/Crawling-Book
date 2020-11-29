from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import os


def filter_tag(level: int):
    """ 총 검색 기록에서 level1, python3 필터 추가 """
    print("검색 필터 적용중...", end="\t")
    time.sleep(2)
    driver.find_element_by_xpath(f"""//*[@id="collapseFilterLevel"]/li[{level}]/label""").click()  # level 필터 클릭
    driver.find_element_by_xpath("""//*[@id="collapseFilterLanguage"]/li[9]/label""").click()  # python3 필터 클릭
    print("완료")
    time.sleep(3)


def get_pages():
    """ 페이지 읽어오기 """
    return driver.find_elements_by_xpath("""//*[@id="tab_all_challenges"]/section/div/div[2]/div[2]/div[2]/nav/ul/li""")


def get_questions_url():
    """ html 텍스트를 받아서, 원하는 질문 링크를 리스트로 반환 """
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    question_list.extend([a_tag['href'] for a_tag in
                          soup.select("#tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 "
                                      "> div.algorithm-list > div.row > div > div > a") if a_tag['href']])


def get_all_questions_url():
    """ 모든 페이지의 질문 링크를 반환 """
    print(f"첫 페이지 크롤링... ", end='\t')
    get_questions_url()
    page_li = get_pages()
    max_page = int(page_li[-2].text)
    print("완료")

    for page in range(2, max_page + 1):
        print(f"{page} 페이지 크롤링... ", end='\t')
        for ele in page_li:
            if str(page) == ele.text:
                ele.click()
                time.sleep(1)
                get_questions_url()
                break
        page_li = get_pages()
        print("완료")


def get_question_content(q_url: str):
    html = BeautifulSoup(requests.get(q_url).text, 'html.parser')
    title = html.select_one("#tab > li").text.split('\n')[1].strip().replace('?', '')
    if check_solved:

        return
    with open(PATH + title + ".md", "wt", encoding="utf-8") as f:
        f.write("프로그래머스 문제 바로가기 : " + q_url + "\n")
        f.write(str(html.select_one("#tour2")))
    print(f"문제 '{title}' 다운로드 완료")


def get_all_questions_content():
    count = 0
    for q in question_list:
        get_question_content(header_url + q)
        count += 1
    print(f"총 {count}건의 문제가 파일로 저장되었습니다. 프로그램을 정상 종료합니다...")


def get_solved_questions_title() -> tuple:
    return tuple(i.split('(')[0].split('.')[0].rstrip()
                 for i in os.listdir(r"C:\Users\user\Documents\알고리즘\프로그래머스\프로그래머스 Level " + str(level))
                 if i.split('.')[-1] == 'py')


if __name__ == '__main__':
    # 변수 초기화
    header_url = "https://programmers.co.kr/"
    url = "https://programmers.co.kr/learn/challenges?tab=all_challenges"
    PATH = "C:/Users/user/Downloads/알고리즘_문제/"
    level = 2
    mode = 1
    check_solved = True
    question_list = []
    check_li = tuple()

    # 변수 설정
    if mode is 1:
        PATH = input("다운로드될 파일들이 저장될 경로를 입력하세요 : ")
        level = int(input("저장할 레벨을 입력하세요 : "))
        check_solved = (input("이미 푼 문제는 제외하고 다운받을까요? (y/n) : ") in ['1', 'y', 'Y', 'yes', 'Yes', "YES"])

    if check_solved:
        check_li = get_solved_questions_title()
        print("이미 푼 문제 목록 : ", check_li)

    # 셀레니움 크롬 드라이버 실행
    option = webdriver.ChromeOptions()
    # option.add_argument('headless')
    driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe", options=option)
    driver.get(url)

    # 함수 순서대로 실행
    filter_tag(level=level)
    get_all_questions_url()
    get_all_questions_content(True)

    # 셀레니움 종료
    driver.close()

