from selenium import webdriver
from bs4 import BeautifulSoup
import time


def filter_tag():
    """ 총 검색 기록에서 level1, python3 필터 추가 """
    time.sleep(1)
    driver.find_element_by_xpath("""//*[@id="collapseFilterLevel"]/li[1]/label""").click()  # level1 필터 클릭
    driver.find_element_by_xpath("""//*[@id="collapseFilterLanguage"]/li[9]/label""").click()   # python3 필터 클릭
    time.sleep(2)


def get_pages():
    """ 페이지 읽어오기 """
    return driver.find_elements_by_xpath("""//*[@id="tab_all_challenges"]/section/div/div[2]/div[2]/div[2]/nav/ul/li""")


def get_questions():
    """ html 텍스트를 받아서, 원하는 질문 링크를 리스트로 반환 """
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    question_list.extend([a_tag['href'] for a_tag in
                          soup.select("#tab_all_challenges > section > div > div.challenge__algorithms--index.col-md-8 "
                                      "> div.algorithm-list > div.row > div > div > a")])


def get_all_questions():
    """ 모든 페이지의 질문 링크를 반환 """
    question_list.append(get_questions())
    page_li = get_pages()
    max_page = int(page_li[-2].text)

    for page in range(2, max_page+1):
        print(f"{page} 페이지 크롤링... ", end='\t')
        for ele in page_li:
            if str(page) == ele.text:
                ele.click()
                get_questions()
                break
        page_li = get_pages()
        print("완료")


if __name__ == '__main__':
    header_url = "https://programmers.co.kr/"
    url = "https://programmers.co.kr/learn/challenges?tab=all_challenges"   # 프로그래머스 알고리즘 url
    question_list = []

    driver = webdriver.Chrome(r"C:\Users\user\Documents\chromedriver.exe")
    driver.get(url)
    filter_tag()
    question_list.append(get_all_questions())

    print(question_list)
    driver.close()
