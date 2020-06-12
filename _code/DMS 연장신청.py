# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep

choice = {
    '가온실': 1,
    '나온실': 2,
    '다온실': 3,
    '라온실': 4,
    '2층 여자 독서실': 5,
    '3층 학교측 독서실': 6,
    '3층 기숙사측 독서실': 7,
    '4층 학교측 독서실': 8,
    '4층 기숙사측 독서실': 9,
    '5층 열린 교실': 10,
    '3층 소파': 11,
}
check = input('연장을 신청하시겠습니까? (거부시 신청을 취소) [y/n] : ').rstrip()
print(choice)
room = int(input('신청할 장소의 번호를 입력하세요 (ex> 가온실이면 1입력) : '))
time = int(input('신청할 시간을 입력하세요 (11시면 0, 12시면 1을 입력) : '))
target = 'https://www.dsm-dms.com/'
options = webdriver.ChromeOptions()
# options.add_argument('--start-fullscreen')
options.add_argument('headless')
browser = webdriver.Chrome("C:/Users/user/Documents/chromedriver.exe", options=options)
browser.get(target)
sleep(1)

# 로그인 수행
nav_path = '//*[@id="meal"]/div/header/nav/'
browser.find_element_by_xpath(nav_path + 'button').click()
sleep(1)
form_path = '//*[@id="root"]/div[1]/div/div[2]/div[1]/'
browser.find_element_by_xpath(form_path + 'input[1]').send_keys('kkddhh7645')
browser.find_element_by_xpath(form_path + 'input[2]').send_keys('kkddhh77887788')
browser.find_element_by_xpath(form_path + 'button').click()
sleep(1)
try:
    at = browser.switch_to.alert
    at.accept()
except Exception as e:
    print(e)
sleep(1)

# 로그인 완료후, 연장 신청 페이지로 이동
browser.find_element_by_xpath(nav_path + 'span[1]').click()
sleep(1)
browser.find_element_by_xpath('//*[@id="apply"]/div/div[2]/a[1]/button').click()
sleep(1)

# 연장신청 수행
check_path = '//*[@id="root"]/div/div[2]/div/div[2]/div/div[2]/'
browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[1]/div[2]/div[' + str(room) + ']').click()
browser.find_element_by_xpath(check_path + 'div[1]/div/table/tr[1]/td[2]').click()
if time:
    browser.find_element_by_xpath('//*[@id="root"]/div/div[2]/div/div[2]/div/div[1]/ul/li[2]').click()
if check in ['y', 'Y', 'Yes', 'yes']:   # 연장 신청
    browser.find_element_by_xpath(check_path + 'div[2]/div[2]').click()
else:   # 연장 취소
    browser.find_element_by_xpath(check_path + 'div[2]/div[1]').click()
sleep(1)
try:
    at = browser.switch_to.alert
    at.accept()
except Exception as e:
    print(e)
sleep(5)
browser.close()
