from selenium import webdriver
import time

options = webdriver.ChromeOptions()

"""
(아 이거 영업비밀인데;;)
셀레니움, 기존 pc로도 잘 켜지는데 왜 굳이 모바일 화면으로 열까?

크게 2가지 이유가 있다. 첫번째는 html 구조가 쉬워 파싱하기 쉽고, 두번째는 보안이 상대적으로 여유롭다.
셀레니움 pc로는 로그인 인증되지 않던게 모바일에서 되는 경우가 있다는 것이다! 

이러한 이유때문에 셀레니움을 모바일 화면으로 열기도 한다.
"""
# mobile_emulation = {"deviceName": "iPhone X"}     # 간단하게 이 한줄로도 모바일 창 설정을 할 수 있음
mobile_emulation = {
    # "deviceMetrics": {"width": 1000, "height": 812, "pixelRatio": 3.0},       # 모바일 창의 높이와 넓이를 정적으로 지정해줄 수 있음
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}
options.add_experimental_option("mobileEmulation", mobile_emulation)

chrome_driver_path = r"C:\Users\user\Documents\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path, options=options)
time.sleep(1)

driver.get('https://google.com')
time.sleep(7)

driver.quit()
