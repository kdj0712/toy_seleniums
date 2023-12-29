# * 웹 크롤링 동작
from selenium import webdriver

# - chrome browser 열기
browser = webdriver.Chrome()

# - 주소 입력
browser.get("https://www.oliveyoung.co.kr/store/goods/getGoodsDetail.do?goodsNo=A000000184922&dispCatNo=1000001001200040001&t_page=%EC%B9%B4%ED%85%8C%EA%B3%A0%EB%A6%AC%EA%B4%80&t_click=%EB%B2%A0%EC%9D%B4%EC%8A%A4/%ED%83%91%EC%BD%94%ED%8A%B8_%EC%A0%84%EC%B2%B4__%EC%83%81%ED%92%88%EC%83%81%EC%84%B8&t_number=1")

# - 가능 여부에 대한 OK 받음
# - html 파일 받음(and 확인)
html = browser.page_source
# print(html)

# - 정보 획득
from selenium.webdriver.common.by import By

# reviewInfo > a
browser.find_element(by=By.CSS_SELECTOR, value="#reviewInfo > a").click()
import time
time.sleep(3)
list = browser.find_elements(by=By.CSS_SELECTOR, value="#gdasList > li")

# browser.save_screenshot('./formats.png')

# 브라우저 종료
browser.quit()

# *웹 크롤링 동작
# -(install browser)
# -set up driver
# - vrowser(Chrome) 열기
# -주소 입력 후 Enter
# -가능 여부에 대한 ok받음
# -html 파일 받음(and 확인)
# -정보획득
# -browser닫기

